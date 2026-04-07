#!/usr/bin/env python3
"""
update_sponsor_blog_mentions.py

Scans every blog post in /pages/blog/ for mentions of each sponsor and
automatically adds missing entries to the "Menciones en nuestro blog"
section of the corresponding /pages/patrocinios/*.md file.

Idempotent: safe to run multiple times. Entries are matched by URL so
duplicates are never created.

Usage:
    python scripts/update_sponsor_blog_mentions.py              # update all
    python scripts/update_sponsor_blog_mentions.py --dry-run    # preview only
    python scripts/update_sponsor_blog_mentions.py --sponsor huggingface
"""

import argparse
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).parent.parent
BLOG_DIR = ROOT / "pages" / "blog"
PATROCINIOS_DIR = ROOT / "pages" / "patrocinios"
BLOG_BASE_URL = "https://somosnlp.org/blog"

# ---------------------------------------------------------------------------
# Sponsor → search-keyword mapping
#
# Each keyword is matched as a whole word (case-insensitive, word boundaries).
# Add the new sponsor slug and its keywords whenever a new patrocinios page
# is created. Leave out sponsors that have no distinctive keyword yet.
# ---------------------------------------------------------------------------
SPONSOR_KEYWORDS: dict[str, list[str]] = {
    "agilmentor":           ["AgilMentor"],
    "argilla":              ["Argilla"],
    "bsc":                  ["BSC", "Barcelona Supercomputing"],
    "calamoycran":          ["CÁLAMO", "Cálamo", "Calamo"],
    "divertles":            ["DiverTLes"],
    "ging-upm":             ["GING"],
    "hitz":                 ["HiTZ"],
    "huggingface":          ["Hugging Face", "HuggingFace"],
    "iic":                  ["Instituto de Ingeniería del Conocimiento", r"\bIIC\b"],
    "iimas_unam":           ["IIMAS"],
    "ilenia":               ["ILENIA"],
    "impulse-ai":           ["ImpulseAI", "Impulse AI"],
    "latinx-in-ai":         ["LatinX in AI", "LatinX in NLP"],
    "lenguaje-natural-ai":  ["LenguajeNaturalAI", "LenguajeNatural"],
    "monsterapi":           ["MonsterAPI"],
    "narrativa":            ["Narrativa"],
    "nlp-spain":            ["NLP Spain"],
    "nova":                 [r"\bNova\b"],
    "omdena-mx":            ["Omdena"],
    "platzi":               ["Platzi"],
    "q-blocks":             ["Q Blocks", "QBlocks"],
    "saturdays-ai":         ["SaturdaysAI", "Saturdays AI"],
    "sepln":                ["SEPLN"],
    "software-themis":      ["Software Themis"],
    "spain-ai":             ["Spain AI"],
    "wtn":                  ["WomenTech"],
    # Sponsors with no distinctive keyword yet — add when blog posts appear:
    # "aaaimx":             ["AAAIMX"],
    # "ai-the-new-sexy":    ["AI the New Sexy"],
    # "aitinkerers":        ["AI Tinkerers"],
    # "big-onion":          ["Big Onion"],
    # "datagenero":         ["DataGénero"],
    # "gli-unam":           ["Ingeniería Lingüística"],
    # "ibidat":             ["IBiDat"],
    # "imfd":               ["IMFD", "Milenio Fundamentos"],
    # "mcd-unison":         ["MCD UNISON"],
    # "meaning-cloud":      ["MeaningCloud", "Meaning Cloud"],
    # "mujeres-tech":       ["Mujeres Tech"],
    # "nlp-webinars-mx":    ["NLP Webinars"],
    # "piango-solutions":   ["Piango"],
    # "uned-nlp":           ["UNED NLP"],
    # "unl":                ["Universidad Nacional de Loja"],
    # "upr":                ["UPR", "Puerto Rico"],
    # "yamato":             ["Yamato"],
}

# Files in patrocinios/ to skip entirely (template, etc.)
SKIP_FILES = {"0-plantilla.md"}

SECTION_HEADER = "## Menciones en nuestro blog"


# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (fields_dict, body) from a markdown file with YAML front-matter."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            v = val.strip()
            # Strip surrounding quotes only when the value is fully quoted.
            if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
                v = v[1:-1]
            fields[key.strip()] = v
    return fields, text[end + 5:]


# ---------------------------------------------------------------------------
# Keyword matching
# ---------------------------------------------------------------------------

def mentions_sponsor(text: str, keywords: list[str]) -> bool:
    """Return True if *text* contains any of *keywords* (whole-word, case-SENSITIVE).

    Case-sensitive matching avoids false positives where Spanish common words
    share spelling with sponsor names (e.g. "narrativa" vs company "Narrativa").
    All sponsor names are proper nouns with distinctive capitalisation.
    """
    for kw in keywords:
        # Keywords that start with \b are already regex patterns; escape the rest.
        pattern = kw if kw.startswith(r"\b") else r"\b" + re.escape(kw) + r"\b"
        if re.search(pattern, text):  # intentionally case-sensitive
            return True
    return False


# ---------------------------------------------------------------------------
# Sponsor-page helpers
# ---------------------------------------------------------------------------

def existing_blog_urls(sponsor_text: str) -> set[str]:
    """Return all somosnlp.org/blog/… URLs already present in the file."""
    return set(re.findall(r"https://somosnlp\.org/blog/[^\s)\"']+", sponsor_text))


def find_insertion_point(text: str) -> int:
    """
    Return the character index where a new blog-mentions section should be
    inserted.  Priority:
      1. Before the LAST '<div class="flex justify-center">' (the logo div)
      2. Before '*Última actualización:' line
      3. End of file (stripped of trailing whitespace)
    """
    divs = list(re.finditer(r"\n<div class=\"flex justify-center\">", text))
    if divs:
        return divs[-1].start()
    ts = re.search(r"\n\*Última actualización:", text)
    if ts:
        return ts.start()
    return len(text.rstrip())


def build_entry(slug: str, title: str, author: str) -> str:
    """Format a single bullet-list entry for the blog-mentions section."""
    url = f"{BLOG_BASE_URL}/{slug}"
    if author:
        return f"- [{title}]({url}), {author}"
    return f"- [{title}]({url})"


def update_sponsor_file(
    path: Path,
    new_entries: list[str],
    dry_run: bool,
) -> bool:
    """
    Append *new_entries* to the blog-mentions section of *path*.
    Creates the section if it doesn't exist yet.
    Returns True when the file was (or would be) changed.
    """
    text = path.read_text(encoding="utf-8")

    if SECTION_HEADER in text:
        # ---- Section already exists: append inside it ----
        idx = text.index(SECTION_HEADER) + len(SECTION_HEADER)
        # End of section = first line that opens a new heading or HTML block
        tail = text[idx:]
        end_match = re.search(r"\n(?=##|<div|\*Última)", tail)
        section_end = idx + (end_match.start() if end_match else len(tail))

        new_text = (
            text[:section_end].rstrip("\n")
            + "\n"
            + "\n".join(new_entries)
            + "\n"
            + text[section_end:]
        )
    else:
        # ---- Create a new section at the insertion point ----
        insert_at = find_insertion_point(text)
        block = (
            "\n\n"
            + SECTION_HEADER
            + "\n\n"
            + "\n".join(new_entries)
            + "\n"
        )
        new_text = text[:insert_at] + block + text[insert_at:]

    if new_text == text:
        return False
    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def load_blog_posts() -> list[dict]:
    """
    Return metadata for every blog post (skipping language-variant duplicates
    such as *.en.md or *.pt.md so each slug is processed only once).
    """
    posts = []
    for path in sorted(BLOG_DIR.glob("*.md")):
        # Skip language variants – the main (es) version is sufficient.
        if re.search(r"\.(en|pt|es)\.md$", path.name):
            continue
        raw = path.read_text(encoding="utf-8")
        fm, _ = parse_frontmatter(raw)
        posts.append(
            {
                "path": path,
                "slug": path.stem,
                "title": fm.get("title", path.stem).strip('"'),
                "author": fm.get("author", "").strip(),
                "text": raw,  # search the full file including front-matter
            }
        )
    return posts


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sync blog post mentions into patrocinios/ sponsor pages."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned changes without modifying any files.",
    )
    parser.add_argument(
        "--sponsor",
        metavar="SLUG",
        help="Only process the sponsor with this slug (e.g. huggingface).",
    )
    args = parser.parse_args()

    # 1. Load blog posts
    blog_posts = load_blog_posts()
    print(f"Loaded {len(blog_posts)} blog posts.\n")

    # 2. Resolve sponsor files to process
    sponsor_paths = sorted(PATROCINIOS_DIR.glob("*.md"))
    if args.sponsor:
        sponsor_paths = [p for p in sponsor_paths if p.stem == args.sponsor]
        if not sponsor_paths:
            sys.exit(f"ERROR: no sponsor file found for '{args.sponsor}'")

    prefix = "[DRY RUN] " if args.dry_run else ""
    total_updated = 0
    total_added = 0

    # 3. Process each sponsor
    for sponsor_path in sponsor_paths:
        if sponsor_path.name in SKIP_FILES:
            continue

        keywords = SPONSOR_KEYWORDS.get(sponsor_path.stem)
        if not keywords:
            continue  # No keywords configured for this sponsor yet

        sponsor_text = sponsor_path.read_text(encoding="utf-8")
        already_indexed = existing_blog_urls(sponsor_text)

        new_entries: list[str] = []
        for post in blog_posts:
            post_url = f"{BLOG_BASE_URL}/{post['slug']}"
            if post_url in already_indexed:
                continue  # Already present in the file
            if mentions_sponsor(post["text"], keywords):
                entry = build_entry(post["slug"], post["title"], post["author"])
                new_entries.append(entry)
                print(f"{prefix}{sponsor_path.name}: + \"{post['title']}\"")
                total_added += 1

        if new_entries:
            modified = update_sponsor_file(sponsor_path, new_entries, args.dry_run)
            if modified:
                total_updated += 1

    action = "Would update" if args.dry_run else "Updated"
    print(f"\n{action} {total_updated} sponsor page(s), {total_added} new mention(s) added.")


if __name__ == "__main__":
    main()
