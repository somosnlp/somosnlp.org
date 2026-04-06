"""Script to update event pages and speaker profiles for SomosNLP Hackathon.

Set CSV_FILE_PATH (relative to scripts/data/) as the only variable to configure.
Year and file type (ponencias / mentorias) are derived from the filename automatically.

Supported filename patterns:
    ponencias-YYYY.csv  →  creates talk pages in pages/hackathon-YYYY/
    mentorias-YYYY.csv  →  creates mentoria pages in pages/hackathon-YYYY/

Also updates pages/eventos/index.vue: inserts or refreshes the hackathon-YYYY grid
for any accepted entry that has a valid local poster image in the Cartel column.

Usage:
    python ponencias.py                      # uses CSV_FILE_PATH constant below
    python ponencias.py ponencias-2025.csv   # override via CLI argument
"""

import logging
import os
import re
import sys
from datetime import datetime

import pandas as pd
import yaml

# ─── CONFIGURE ──────────────────────────────────────────────────────────────
# Path to CSV file, relative to scripts/data/. Can also pass as a CLI argument.
CSV_FILE_PATH = "ponencias-2025.csv"
# ────────────────────────────────────────────────────────────────────────────

EVENT_NAME = "Hackathon SomosNLP"
DEFAULT_POSTER = "/images/patrocinios/somosnlp.png"
DEFAULT_YOUTUBE = "https://www.youtube.com/@SomosNLP"
YEAR_PLAYLISTS = {
    "2022": "https://www.youtube.com/playlist?list=PLTA-KAy8nxaAbVZ2lVcycHnJ2qEDip7hG",
    "2023": "https://www.youtube.com/playlist?list=PLTA-KAy8nxaCDc0IJpLac-3csiAepV546",
    "2024": "https://www.youtube.com/playlist?list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J",
    "2025": "https://www.youtube.com/playlist?list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6",
}
COMMUNITY_PHOTOS_BASE_URL = "/images/comunidad"
GITHUB_ASSETS_BASE = "https://somosnlp.github.io/assets"

# Column name candidates per file type (tried in order; first match wins).
COLUMNS = {
    "ponencias": {
        "name": ["Nombre"],
        "occupation": ["Ocupación"],
        "title": ["Título del evento"],
        "description": ["Descripción del evento"],
        "learning_points": [
            "¿Qué aprenderán las personas que asistan a tu evento? Escribe 3-5 puntos clave."
        ],
        "bio": ["Breve biografía"],
        "website": ["Página web"],
        "twitter": ["Twitter"],
        "linkedin": ["LinkedIn"],
        "photo": ["Foto de perfil"],
        "level": ["Nivel técnico"],
        "topic": ["¿Cuál es la temática?"],
        "cartel": ["Cartel"],
        "youtube": ["YouTube"],
        "fecha": ["Fecha"],
    },
    "mentorias": {
        "name": ["Nombre completo", "Nombre"],
        "occupation": ["Ocupación y afiliación", "Ocupación"],
        "title": [],  # synthesized as "Mentoría con {name}"
        # 2025: "Descripción de la mentoría"
        # 2023: very long question starting with "¿Cuál es tu especialidad?"
        "description": ["Descripción de la mentoría", "¿Cuál es tu especialidad?"],
        "learning_points": [],
        "bio": ["Breve biografía"],
        "website": ["Página web"],
        "twitter": ["Twitter"],
        "linkedin": ["LinkedIn"],
        "photo": ["Foto de perfil"],
        "level": [],
        "topic": ["Formato de mentoría", "Tipo de mentoring"],
        "cartel": ["Cartel"],
        "youtube": ["YouTube"],
        "fecha": ["Fecha"],
    },
}

# Canonical frontmatter key order for speaker profiles
SPEAKER_FM_KEYS = [
    "title",
    "description",
    "cover",
    "website",
    "twitter",
    "linkedin",
    "github",
    "huggingface",
    "community",
]

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# ─── Filename helpers ────────────────────────────────────────────────────────


def clean_filename(text):
    """Convert text to a lowercase underscore-separated filename slug."""
    text = text.lower()
    for pattern, repl in [
        (r"[áàäâ]", "a"),
        (r"[éèëê]", "e"),
        (r"[íìïî]", "i"),
        (r"[óòöô]", "o"),
        (r"[úùüû]", "u"),
        (r"[ñ]", "n"),
    ]:
        text = re.sub(pattern, repl, text)
    text = re.sub(r"[^a-z0-9\s\-]", "", text)
    text = re.sub(r"[\s\-]+", "_", text.strip())
    return text


def format_speaker_filename(name):
    """Convert a full name to a hyphen-separated filename slug."""
    return "-".join(clean_filename(part) for part in name.strip().split())


# ─── Field helpers ───────────────────────────────────────────────────────────


def get_field(row, candidates, default=""):
    """Return the first non-empty value found among the column name candidates.

    First tries exact column name matches, then falls back to prefix matching
    to handle long column names (e.g. 2023 mentorias CSV where the description
    column name is the full question text starting with "¿Cuál es tu especialidad?").
    """
    for col in candidates:
        if col in row.index:
            val = row[col]
            if not pd.isna(val):
                return str(val).strip()
    # Prefix fallback: match any column whose name starts with a candidate
    for col in candidates:
        for actual_col in row.index:
            if str(actual_col).startswith(col):
                val = row[actual_col]
                if not pd.isna(val):
                    return str(val).strip()
    return default


def normalize_row(row, file_type):
    """Return a dict of standard field names mapped to their values for this row."""
    cols = COLUMNS.get(file_type, COLUMNS["ponencias"])
    fields = {key: get_field(row, candidates) for key, candidates in cols.items()}
    # Synthesize title for mentorias (and any row where title column is absent)
    if not fields.get("title"):
        fields["title"] = f"Mentoría con {fields['name']}"
    return fields


# ─── URL / photo helpers ─────────────────────────────────────────────────────


def format_cartel_url(url):
    """Return a usable local path for a cartel (poster) image.

    - Local path (/…)          → returned as-is
    - GitHub-hosted assets URL → converted to local /images/… path
    - Google Drive / empty     → DEFAULT_POSTER
    """
    if not url or pd.isna(url):
        return DEFAULT_POSTER
    url = str(url).strip()
    if url.startswith("/"):
        return url
    if url.startswith(GITHUB_ASSETS_BASE):
        return url[len(GITHUB_ASSETS_BASE) :]
    return DEFAULT_POSTER


def format_video_url(url):
    """Convert a YouTube URL to embed format; return DEFAULT_YOUTUBE if invalid."""
    if not url or pd.isna(url):
        return DEFAULT_YOUTUBE
    patterns = [
        r"(?:youtube\.com/watch\?v=|youtu\.be/)([^&\n?]+)",
        r"youtube\.com/embed/([^&\n?]+)",
    ]
    for pattern in patterns:
        match = re.search(pattern, str(url))
        if match:
            return f"https://www.youtube.com/embed/{match.group(1)}"
    return str(url)


def get_community_photo_url(name):
    """Return the expected community photo URL for a speaker."""
    return f"{COMMUNITY_PHOTOS_BASE_URL}/{clean_filename(name)}.png"


def format_photo_url(url, is_speaker=False, speaker_name=None):
    """Return a photo URL suitable for a speaker profile."""
    if not url or pd.isna(url):
        return (
            get_community_photo_url(speaker_name)
            if (is_speaker and speaker_name)
            else DEFAULT_POSTER
        )
    url = str(url).strip()
    if url.startswith("/"):
        return url
    if url.startswith(GITHUB_ASSETS_BASE):
        return url[len(GITHUB_ASSETS_BASE) :]
    if is_speaker and speaker_name:
        return get_community_photo_url(speaker_name)
    return DEFAULT_POSTER


# ─── Content helpers ─────────────────────────────────────────────────────────


def format_learning_points(points_str):
    """Format a string of learning points into a markdown bullet list.

    Handles: newline-separated, inline numbered "1. X 2. Y", or question-separated.
    """
    if not points_str:
        return ""

    # Newline-separated (most common)
    lines = [p.strip() for p in points_str.split("\n") if p.strip()]
    if len(lines) > 1:
        strip_num = lambda l: re.sub(r"^\d+[.)\s]+", "", l)
        return "\n".join(f"- {strip_num(line)}" for line in lines)

    # Inline numbered list: "1. xxx 2. xxx"
    numbered = re.split(r"\s*\d+\.\s+", points_str.strip())
    numbered = [p.strip().rstrip(".") for p in numbered if p.strip()]
    if len(numbered) > 1:
        return "\n".join(f"- {p}" for p in numbered)

    # Fallback: split on "?" only
    points = [p.strip() + "?" for p in re.split(r"\?", points_str) if p.strip()]
    return "\n".join(f"- {p}" for p in points)


def format_date(date):
    """Format a datetime as 'dd de mes de yyyy' in Spanish."""
    months = {
        "January": "enero",
        "February": "febrero",
        "March": "marzo",
        "April": "abril",
        "May": "mayo",
        "June": "junio",
        "July": "julio",
        "August": "agosto",
        "September": "septiembre",
        "October": "octubre",
        "November": "noviembre",
        "December": "diciembre",
    }
    text = date.strftime("%d de %B de %Y")
    for en, es in months.items():
        text = text.replace(en, es)
    return text


def parse_frontmatter(content):
    """Parse YAML frontmatter from markdown content; return (dict, body_str)."""
    if not content or not content.startswith("---\n"):
        return {}, content
    parts = content.split("---\n", 2)
    if len(parts) < 3:
        return {}, content
    try:
        fm = yaml.safe_load(parts[1]) or {}
        return fm, parts[2]
    except yaml.YAMLError:
        return {}, content


# ─── Talk / mentoria page generator ──────────────────────────────────────────


def _sanitize_for_frontmatter(text):
    """Prepare a text field for safe embedding as a YAML double-quoted scalar.

    - Collapses newlines/blank-lines (bare newlines inside double-quoted YAML
      strings are allowed, but blank lines end the YAML document).
    - Escapes internal double-quotes so the string delimiter is not broken.
    """
    if not text:
        return ""
    text = " ".join(text.split())  # collapse all whitespace and newlines
    text = text.replace('"', '\\"')  # escape embedded double-quotes
    return text


def create_talk_content(fields, year):
    """Return markdown content for a talk or mentoria event page."""
    poster = format_cartel_url(fields["cartel"])
    video = format_video_url(fields["youtube"])
    learning_points = format_learning_points(fields["learning_points"])
    bio_fm = _sanitize_for_frontmatter(fields["bio"])

    content = (
        f"---\n"
        f'title: "{fields["title"]}"\n'
        f"date: {year}-01-01T00:00:00.000+00:00\n"
        f"time:\n"
        f"duration: 30 mins\n"
        f"cover: {poster}\n"
        f'author: {fields["name"]}\n'
        f'twitter: {fields["twitter"]}\n'
        f'linkedin: {fields["linkedin"]}\n'
        f'website: {fields["website"]}\n'
        f'bio: "{bio_fm}"\n'
        f"---\n\n"
        f"<EventSummary\n"
        f'    description="{fields["description"]}"\n'
        f'    poster="{poster}"\n'
        f'    video="{video}"\n'
        f'    tema="{fields["topic"]}"\n'
        f'    nivel="{fields["level"]}"\n'
        f'    name="{fields["name"]}"\n'
        f'    website="{fields["website"]}"\n'
        f'    twitter="{fields["twitter"]}"\n'
        f'    linkedin="{fields["linkedin"]}"\n'
        f'    bio="{fields["bio"]}"\n'
        f"/>\n"
    )
    if learning_points:
        content += (
            f"\n## ¿Qué vas a aprender al asistir a esta charla?\n\n{learning_points}\n"
        )
    content += "\n## Enlaces útiles\n\n## Charlas relacionadas\n"
    return content


# ─── Speaker profile generator ───────────────────────────────────────────────


def _build_event_entry(fields, event_name):
    """Return the markdown block for one event entry in a speaker's Ponencias section."""
    poster = format_cartel_url(fields["cartel"])
    video = format_video_url(fields["youtube"])
    return (
        f'- {fields["title"]} | {event_name}\n\n'
        f"<EventSummary\n"
        f'    description="{fields["description"]}"\n'
        f'    poster="{poster}"\n'
        f'    video="{video}"\n'
        f"/>"
    )


def _update_ponencias_section(body, event_entry, event_name, bio=""):
    """Insert or update the event entry in the ## Ponencias section of the profile body.

    - If an entry with the exact same title+event already exists → replace it (idempotent).
    - If no entry with this exact title exists → append (handles multiple events same year).
    - If no Ponencias section exists → create it (before ## Biografía if present).
    """
    # Match on the exact list-item line (e.g. "- Talk Title | Hackathon SomosNLP 2025")
    # so that two different talks from the same year can coexist.
    entry_title_line = event_entry.split("\n")[0]  # "- Title | event_name"
    entry_pattern = re.compile(
        re.escape(entry_title_line) + r"\n\n<EventSummary[\s\S]*?/>",
        re.MULTILINE,
    )

    ponencias_match = re.search(r"(?m)^## Ponencias[ \t]*\n", body)

    if not ponencias_match:
        # No Ponencias section at all – create one
        ponencias_block = f"## Ponencias\n\n{event_entry}\n\n"
        first_section = re.search(r"(?m)^## ", body)
        if first_section:
            return (
                body[: first_section.start()]
                + ponencias_block
                + body[first_section.start() :]
            )
        # Body has no sections at all: append Ponencias (+ Biografía if body was empty)
        result = (
            (body.rstrip("\n") + "\n\n" + ponencias_block)
            if body.strip()
            else ponencias_block
        )
        if bio and "## Biografía" not in body:
            result += f"## Biografía\n\n{bio}\n\n*Última actualización: {format_date(datetime.now())}*\n"
        return result

    ponencias_start = ponencias_match.end()
    next_section = re.search(r"(?m)^## ", body[ponencias_start:])
    ponencias_end = (
        ponencias_start + next_section.start() if next_section else len(body)
    )
    ponencias_body = body[ponencias_start:ponencias_end]

    existing_entry = entry_pattern.search(ponencias_body)

    if existing_entry:
        # Replace existing entry (same event, possibly updated poster/video)
        new_ponencias = (
            ponencias_body[: existing_entry.start()]
            + event_entry
            + ponencias_body[existing_entry.end() :]
        )
    else:
        # Append new entry for this event
        new_ponencias = ponencias_body.rstrip("\n") + f"\n\n{event_entry}\n"

    return body[:ponencias_start] + new_ponencias + body[ponencias_end:]


def create_speaker_content(fields, year, event_name, existing_content=None):
    """Create or update a speaker/mentor profile page.

    For new files: creates a full profile with Ponencias and Biografía sections.
    For existing files:
      - Updates social links and occupation (may have changed in CSV).
      - Preserves manually-set fields: title, cover, github, huggingface, community.
      - Inserts or updates the event entry in ## Ponencias (never duplicates).
      - Leaves ## Biografía and any other sections untouched.
    """
    name = fields["name"]
    occupation = fields["occupation"]
    bio = fields["bio"]
    photo = format_photo_url(fields["photo"], is_speaker=True, speaker_name=name)
    event_entry = _build_event_entry(fields, event_name)

    # ── New file ──────────────────────────────────────────────────────────────
    if not existing_content:
        fm_lines = (
            f"title: {name}\n"
            f"description: {occupation}\n"
            f"cover: {photo}\n"
            f"website: {fields['website']}\n"
            f"twitter: {fields['twitter']}\n"
            f"linkedin: {fields['linkedin']}\n"
            f'github: ""\n'
            f'huggingface: ""\n'
            f"community: Ponente {year}\n"
        )
        return (
            f"---\n{fm_lines}---\n\n"
            f"## Ponencias\n\n{event_entry}\n\n"
            f"## Biografía\n\n{bio}\n\n"
            f"*Última actualización: {format_date(datetime.now())}*\n"
        )

    # ── Existing file ─────────────────────────────────────────────────────────
    fm, body = parse_frontmatter(existing_content)

    # Update fields that should reflect the latest CSV data
    fm["description"] = occupation
    fm["website"] = fields["website"]
    fm["twitter"] = fields["twitter"]
    fm["linkedin"] = fields["linkedin"]
    # Preserve manually-set fields; only set defaults when missing
    if not fm.get("title"):
        fm["title"] = name
    if not fm.get("cover"):
        fm["cover"] = photo
    for key in ("github", "huggingface"):
        if key not in fm:
            fm[key] = ""
    if "community" not in fm:
        fm["community"] = f"Ponente {year}"

    ordered_fm = {k: fm.get(k, "") for k in SPEAKER_FM_KEYS}
    # Preserve any extra keys the user may have added
    for k, v in fm.items():
        if k not in ordered_fm:
            ordered_fm[k] = v

    fm_block = (
        "---\n" + yaml.dump(ordered_fm, allow_unicode=True, sort_keys=False) + "---\n"
    )

    updated_body = _update_ponencias_section(body, event_entry, event_name, bio)
    return fm_block + updated_body


# ─── eventos/index.vue update ────────────────────────────────────────────────


def _find_div_end(content, start):
    """Return the index just after the </div> that closes the <div> opened at *start*."""
    depth = 0
    i = start
    while i < len(content):
        if content[i : i + 4] == "<div":
            depth += 1
            i += 4
        elif content[i : i + 6] == "</div>":
            depth -= 1
            if depth == 0:
                return i + 6
            i += 6
        else:
            i += 1
    return -1


def _is_valid_cartel(url):
    """Return True if url is a local events image suitable for eventos/index.vue."""
    return bool(url) and url.startswith("/") and url != DEFAULT_POSTER


def find_speaker_image(name, year, project_root):
    """Find a local event poster image by matching speaker name parts against filenames.

    Image files follow YYMMDD_name_parts.ext; all image stem words must be a
    subset of the speaker name words (after cleaning).
    Returns a path like '/images/eventos/250415_alfonso_amayuelas.png' or None.
    """
    images_dir = os.path.join(project_root, "public", "images", "eventos")
    year_prefix = str(year)[-2:]
    try:
        candidates = sorted(
            [
                f
                for f in os.listdir(images_dir)
                if f.startswith(year_prefix)
                and f.lower().endswith((".png", ".jpg", ".jpeg"))
            ]
        )
    except FileNotFoundError:
        return None
    name_parts = set(clean_filename(name).split("_"))
    for img_file in candidates:
        stem = re.sub(r"^\d{6}_", "", os.path.splitext(img_file)[0])
        img_parts = set(stem.split("_"))
        if img_parts and img_parts.issubset(name_parts):
            return f"/images/eventos/{img_file}"
    return None


def _generate_grid_entries(data, year, file_type, project_root=None):
    """Yield indented <a><img /></a> HTML strings for all accepted entries.

    Image priority: CSV cartel → auto-detected filesystem image → DEFAULT_POSTER.
    Link: event page → CSV youtube → year playlist.
    """
    event_dir = f"hackathon-{year}"
    playlist = YEAR_PLAYLISTS.get(str(year), DEFAULT_YOUTUBE)

    for _, row in data.iterrows():
        fields = normalize_row(row, file_type)

        # ── Poster image ──────────────────────────────────────────────────────
        cartel = format_cartel_url(fields["cartel"])
        if not _is_valid_cartel(cartel) and project_root:
            cartel = find_speaker_image(fields["name"], year, project_root) or ""
        if not _is_valid_cartel(cartel):
            cartel = DEFAULT_POSTER

        # ── Slug and alt text ─────────────────────────────────────────────────
        slug = clean_filename(fields["title"])  # works for both types
        alt = (
            f"Mentoría de {fields['name']}"
            if file_type == "mentorias"
            else f"Charla de {fields['name']}"
        )

        # ── href: event page → CSV youtube → year playlist ────────────────────
        youtube = fields.get("youtube", "") or ""
        fallback = youtube if (youtube and youtube != DEFAULT_YOUTUBE) else playlist
        href = f"/{event_dir}/{slug}" if slug else fallback

        yield (
            f'                    <a href="{href}" target="_blank">\n'
            f'                        <img alt="{alt}" width="650" height="365"\n'
            f'                            src="{cartel}" />\n'
            f"                    </a>"
        )


def _build_grid_block(marker_key, entries_html):
    """Return the full HTML block (with sentinel markers) for a file_type-YYYY section."""
    begin = f"<!-- BEGIN:{marker_key} -->"
    end = f"<!-- END:{marker_key} -->"
    return (
        f"{begin}\n"
        f'            <div class="mx-auto my-8 text-center">\n'
        f'                <div class="grid grid-cols-2 gap-8 my-1">\n'
        f"{entries_html}\n"
        f"                </div>\n"
        f"            </div>\n"
        f"            {end}"
    )


def update_eventos_index(vue_path, year, file_type, data, project_root=None):
    """Insert or refresh the file_type-YYYY grid in pages/eventos/index.vue.

    Each file_type (ponencias/mentorias) gets its own sentinel markers so that
    running multiple CSVs for the same year doesn't overwrite each other.

    Strategy (in priority order):
        1. Typed markers exist (BEGIN:{file_type}-{year}) → replace content between them.
        2. h3 exists → insert new block after the last existing END:*-{year} marker,
           or right after the h3 line if none exist yet.
        3. Neither → insert new <h3> + block before the first older hackathon section.
    """
    entries = list(_generate_grid_entries(data, year, file_type, project_root))
    if not entries:
        logging.info(
            "No entries for %s/%s – skipping eventos/index.vue", file_type, year
        )
        return

    entries_html = "\n\n".join(entries)
    marker_key = f"{file_type}-{year}"
    grid_block = _build_grid_block(marker_key, entries_html)
    begin_marker = f"<!-- BEGIN:{marker_key} -->"
    end_marker = f"<!-- END:{marker_key} -->"
    h3_tag = f'<h3 id="hackathon-{year}">'

    with open(vue_path, "r", encoding="utf-8") as f:
        content = f.read()

    # ── Migrate old generic hackathon-YYYY markers (one-time cleanup) ─────────
    old_begin = f"<!-- BEGIN:hackathon-{year} -->"
    old_end = f"<!-- END:hackathon-{year} -->"
    if old_begin in content:
        old_pattern = re.escape(old_begin) + r".*?" + re.escape(old_end)
        content = re.sub(old_pattern, "", content, flags=re.DOTALL)
        logging.info(
            "Removed old generic hackathon-%s markers (migrating to typed markers)",
            year,
        )

    # ── Case 1: typed markers exist → replace ────────────────────────────────
    if begin_marker in content:
        pattern = re.escape(begin_marker) + r".*?" + re.escape(end_marker)
        new_content = re.sub(pattern, grid_block, content, flags=re.DOTALL)
        logging.info("Updated eventos/index.vue – replaced %s markers", marker_key)

    # ── Case 2: h3 exists → insert after last END:*-{year} or after h3 line ──
    elif h3_tag in content:
        any_end_re = re.compile(r"<!-- END:[\w]+-" + re.escape(str(year)) + r" -->")
        last_end = None
        for m in any_end_re.finditer(content):
            last_end = m

        if last_end:
            ins = last_end.end()
            new_content = (
                content[:ins] + "\n\n            " + grid_block + content[ins:]
            )
        else:
            h3_pos = content.find(h3_tag)
            h3_line_end = content.find("\n", h3_pos) + 1
            new_content = (
                content[:h3_line_end]
                + "            "
                + grid_block
                + "\n"
                + content[h3_line_end:]
            )
        logging.info(
            "Updated eventos/index.vue – inserted %s block under h3", marker_key
        )

    # ── Case 3: no section for this year yet ─────────────────────────────────
    else:
        h3_section = (
            f"{h3_tag}{{{{ t('events.sections.hackathon-{year}') }}}}</h3>\n"
            f"            {grid_block}\n\n            "
        )
        match = re.search(r'<h3 id="hackathon-(\d{4})">', content)
        if match and int(match.group(1)) < int(year):
            new_content = (
                content[: match.start()] + h3_section + content[match.start() :]
            )
            logging.info("Inserted new hackathon-%s section in eventos/index.vue", year)
        else:
            logging.warning(
                "Could not find an insertion point for hackathon-%s in eventos/index.vue. "
                "Add a '<h3 id=\"hackathon-%s\">' marker manually and re-run.",
                year,
                year,
            )
            return

    with open(vue_path, "w", encoding="utf-8") as f:
        f.write(new_content)


# ─── Main processing ─────────────────────────────────────────────────────────


def update_talks_and_speakers(csv_filename):
    """Process the CSV and update event pages, speaker profiles, and eventos/index.vue."""
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Derive file type and year from filename (e.g. "ponencias-2025.csv")
    stem = os.path.splitext(csv_filename)[0]
    parts = stem.split("-")
    file_type = parts[0]  # "ponencias" or "mentorias"
    year = parts[-1]  # "2025"
    event_dir = f"hackathon-{year}"
    full_event_name = f"{EVENT_NAME} {year}"

    if file_type not in COLUMNS:
        logging.warning(
            "Unknown file type '%s' (expected 'ponencias' or 'mentorias'). "
            "Falling back to ponencias column mapping.",
            file_type,
        )
        file_type = "ponencias"

    csv_path = os.path.join(script_dir, "data", csv_filename)
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        logging.error("CSV file not found: %s", csv_path)
        return
    except pd.errors.EmptyDataError:
        logging.error("CSV file is empty: %s", csv_path)
        return

    df = df.dropna(how="all")

    # Filter to accepted entries (some older CSVs may not have a Status column)
    if "Status" in df.columns:
        df = df[df["Status"] == "Aceptada"]
        if len(df) == 0:
            logging.warning("No accepted entries found in %s", csv_filename)
            return
    else:
        logging.warning("No 'Status' column – processing all rows in %s", csv_filename)

    name_candidates = COLUMNS[file_type]["name"]
    processed_slugs: set = set()

    for _, row in df.iterrows():
        name = get_field(row, name_candidates)
        if not name:
            logging.warning("Skipping row with missing name")
            continue

        fields = normalize_row(row, file_type)

        try:
            talk_slug = clean_filename(fields["title"])
            talk_filename = f"{talk_slug}.md"
            speaker_file = f"{format_speaker_filename(name)}.md"

            if talk_slug in processed_slugs:
                logging.warning("Duplicate entry – skipping: %s", talk_filename)
                continue
            processed_slugs.add(talk_slug)

            talk_path = os.path.join(
                script_dir, "..", "pages", event_dir, talk_filename
            )
            speaker_path = os.path.join(
                script_dir, "..", "pages", "comunidad", speaker_file
            )

            # ── Event page (always overwrite – canonical source is the CSV) ──
            with open(talk_path, "w", encoding="utf-8") as f:
                f.write(create_talk_content(fields, year))
            logging.info("Created/updated: %s/%s", event_dir, talk_filename)

            # ── Speaker profile (idempotent merge) ───────────────────────────
            existing = None
            if os.path.exists(speaker_path):
                with open(speaker_path, "r", encoding="utf-8") as f:
                    existing = f.read()
            with open(speaker_path, "w", encoding="utf-8") as f:
                f.write(create_speaker_content(fields, year, full_event_name, existing))
            logging.info("Created/updated speaker: %s", speaker_file)

        except Exception as e:
            logging.error("Error processing '%s': %s", fields.get("title", name), e)

    # ── eventos/index.vue ────────────────────────────────────────────────────
    # Only auto-manage the grid for 2024+; older years have manually curated
    # entries with custom images that should not be overwritten by the script.
    vue_path = os.path.join(script_dir, "..", "pages", "eventos", "index.vue")
    project_root = os.path.normpath(os.path.join(script_dir, ".."))
    if int(year) < 2024:
        logging.info(
            "Skipping eventos/index.vue update for %s (manually curated)", year
        )
    elif os.path.exists(vue_path):
        update_eventos_index(vue_path, year, file_type, df, project_root)
    else:
        logging.warning("eventos/index.vue not found at %s", vue_path)


if __name__ == "__main__":
    csv_file = sys.argv[1] if len(sys.argv) > 1 else CSV_FILE_PATH
    update_talks_and_speakers(csv_file)
