"""Script to update talks and speaker profiles for the SomosNLP Hackathon 2024.

Before running the script:
- add ponencias.csv to scripts/data
- add columns "Status" (="Aceptada")
- update the constants at the beginning of the script
- if the talk is already planned, add columns "Cartel" and "YouTube"

This script processes a CSV file ("ponencias.csv") containing talk submissions from a Google Form and:
1. Creates/updates talk files in pages/hackathon-2024/
2. Creates/updates speaker profiles in pages/comunidad/

The script handles:
- Talk file creation with proper formatting
- Speaker profile management
- File naming and content formatting
- Metadata processing
"""

import locale
import logging
import os
import re
from datetime import datetime

import pandas as pd
import yaml

# Constants
EVENT_NAME = "Hackathon SomosNLP"
EVENT_YEAR = "2025"
EVENT_DIR = "hackathon"
DEFAULT_POSTER = "https://somosnlp.github.io/assets/logo_somosnlp.png"
DEFAULT_YOUTUBE = "https://www.youtube.com/@SomosNLP"
COMMUNITY_PHOTOS_BASE_URL = "https://somosnlp.github.io/assets/images/comunidad"
FILE_PATH = "ponencias.csv"


# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Set locale to Spanish
try:
    locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
except locale.Error:
    try:
        locale.setlocale(locale.LC_TIME, "es_ES")
    except locale.Error:
        logging.warning("Could not set Spanish locale, dates will be in English")


def clean_filename(text):
    """Convert text to a valid filename.

    Args:
        text (str): Text to convert to filename.

    Returns:
        str: A valid filename with:
            - Only lowercase letters, numbers, underscores and hyphens
            - Accents removed
            - Spaces replaced with underscores
            - Original hyphens preserved
    """
    # Remove accents
    text = text.lower()
    text = re.sub(r"[áàäâ]", "a", text)
    text = re.sub(r"[éèëê]", "e", text)
    text = re.sub(r"[íìïî]", "i", text)
    text = re.sub(r"[óòöô]", "o", text)
    text = re.sub(r"[úùüû]", "u", text)
    text = re.sub(r"[ñ]", "n", text)

    # Replace special characters (except hyphens) and spaces with underscore
    text = re.sub(r"[^a-z0-9\s\-]", "", text)
    text = re.sub(r"\s+", "_", text.strip())
    return text


def clean_field(value):
    """Clean a field value, replacing NaN with empty string."""
    return "" if pd.isna(value) else str(value).strip()


def format_learning_points(points_str):
    """Format the learning points string into a bullet list.

    Args:
        points_str (str): String containing learning points, possibly with newlines.

    Returns:
        str: Formatted bullet points for markdown.
    """
    if pd.isna(points_str):
        return ""

    # Split by newlines, question marks, or periods and clean
    points = []
    raw_points = re.split(r"[?\n.]", points_str)
    for p in raw_points:
        p = p.strip()
        if p and not p.isspace():
            # Add question mark back if it was a question
            if points_str.find(p + "?") != -1:
                p += "?"
            points.append(p)

    # Format as markdown bullet points
    return "\n".join(f"- {point}" for point in points)


def format_video_url(url):
    """Convert YouTube URL to embed format.

    Args:
        url (str): YouTube video URL.

    Returns:
        str: YouTube embed URL or default channel URL if invalid/empty.
    """
    if not url or pd.isna(url):
        return DEFAULT_YOUTUBE

    # Extract video ID from various YouTube URL formats
    patterns = [
        r"(?:youtube\.com/watch\?v=|youtu\.be/)([^&\n?]+)",
        r"youtube\.com/embed/([^&\n?]+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return f"https://www.youtube.com/embed/{match.group(1)}"

    return url  # Return original if no pattern matches


def get_community_photo_url(name):
    """Generate the URL for a community member's photo.

    Args:
        name (str): Name of the community member.

    Returns:
        str: URL to their photo in the community assets directory.
    """
    filename = clean_filename(name)  # Reuse our filename cleaning function
    return f"{COMMUNITY_PHOTOS_BASE_URL}/{filename}.png"


def format_photo_url(url, is_speaker=False, speaker_name=None):
    """Format photo URL, using appropriate default for the context.

    Args:
        url (str): Photo URL, possibly from Google Drive.
        is_speaker (bool): Whether this is for a speaker profile.
        speaker_name (str, optional): Name of the speaker if is_speaker is True.

    Returns:
        str: Direct photo URL:
            - Community photo URL if it's a speaker
            - Original URL if it's from somosnlp.github.io
            - Default logo for other cases
    """
    if not url or pd.isna(url):
        return (
            get_community_photo_url(speaker_name)
            if is_speaker and speaker_name
            else DEFAULT_POSTER
        )

    # Use original URL if it's from somosnlp.github.io
    if "somosnlp.github.io" in url:
        return url

    # For speakers, always use their community photo
    if is_speaker and speaker_name:
        return get_community_photo_url(speaker_name)

    # Use default logo for Google Drive URLs or other cases
    return DEFAULT_POSTER


def parse_frontmatter(content):
    """Parse YAML frontmatter from markdown content.

    Args:
        content (str): Markdown content with YAML frontmatter.

    Returns:
        tuple: (dict of frontmatter, rest of content)
    """
    if not content or not content.startswith("---\n"):
        return {}, content

    parts = content.split("---\n", 2)
    if len(parts) < 3:
        return {}, content

    try:
        frontmatter = yaml.safe_load(parts[1])
        return frontmatter, parts[2]
    except yaml.YAMLError:
        return {}, content


def format_date(date):
    """Format a date in Spanish.

    Args:
        date (datetime): Date to format.

    Returns:
        str: Date formatted as 'dd de month de yyyy' in Spanish.
    """
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

    # Format date
    eng_date = date.strftime("%d de %B de %Y")

    # Replace month name with Spanish version
    for eng, esp in months.items():
        if eng in eng_date:
            return eng_date.replace(eng, esp)

    return eng_date


def create_talk_content(row):
    """Create the content for a talk markdown file.

    Args:
        row (pandas.Series): Row from the CSV containing talk data.

    Returns:
        str: Formatted markdown content for the talk file.
    """
    # Clean all fields
    title = clean_field(row["Título del evento"])
    description = clean_field(row["Descripción del evento"])
    learning_points = format_learning_points(
        row[
            "¿Qué aprenderán las personas que asistan a tu evento? Escribe 3-5 puntos clave."
        ]
    )
    speaker_name = clean_field(row["Nombre"])
    speaker_bio = clean_field(row["Breve biografía"])
    speaker_occupation = clean_field(row["Ocupación"])
    website = clean_field(row["Página web"])
    twitter = clean_field(row["Twitter"])
    linkedin = clean_field(row["LinkedIn"])

    # Handle missing or empty Cartel and YouTube columns
    try:
        poster = format_photo_url(clean_field(row.get("Cartel", "")))
    except (KeyError, AttributeError):
        poster = DEFAULT_POSTER

    try:
        video = format_video_url(clean_field(row.get("YouTube", "")))
    except (KeyError, AttributeError):
        video = DEFAULT_YOUTUBE

    tema = clean_field(row["¿Cuál es la temática?"])
    nivel = clean_field(row["Nivel técnico"])

    # Format the content
    content = f"""---
title: "{title}"
date: 2024-03-26T18:00:00.000+01:00
time:
duration: 30 mins
cover: {poster}
author: {speaker_name}
twitter: {twitter}
linkedin: {linkedin}
website: {website}
bio: {speaker_bio}
---

<EventSummary
    description="{description}"
    poster="{poster}"
    video="{video}"
    tema="{tema}"
    nivel="{nivel}"
    name="{speaker_name}"
    website="{website}"
    twitter="{twitter}"
    linkedin="{linkedin}"
    bio="{speaker_bio}"
/>

## ¿Qué vas a aprender al asistir a esta charla?

{learning_points}

## Enlaces útiles

## Charlas relacionadas
"""
    return content


def create_speaker_content(row, existing_content=None):
    """Create or update content for a speaker profile markdown file.

    Args:
        row (pandas.Series): Row from the CSV containing speaker data.
        existing_content (str, optional): Existing content of the speaker file.

    Returns:
        str: Formatted markdown content for the speaker profile.
    """
    # Clean all fields
    name = clean_field(row["Nombre"])
    occupation = clean_field(row["Ocupación"])
    bio = clean_field(row["Breve biografía"])
    website = clean_field(row["Página web"])
    twitter = clean_field(row["Twitter"])
    linkedin = clean_field(row["LinkedIn"])
    photo = format_photo_url(
        clean_field(row["Foto de perfil"]), is_speaker=True, speaker_name=name
    )
    talk_title = clean_field(row["Título del evento"])
    description = clean_field(row["Descripción del evento"])

    # Handle missing or empty Cartel and YouTube columns
    try:
        poster = format_photo_url(clean_field(row.get("Cartel", "")))
    except (KeyError, AttributeError):
        poster = DEFAULT_POSTER

    try:
        video = format_video_url(clean_field(row.get("YouTube", "")))
    except (KeyError, AttributeError):
        video = DEFAULT_YOUTUBE

    # Format talk title with hackathon name
    talk_title_with_hackathon = f"{talk_title} | {EVENT_NAME} {EVENT_YEAR}"

    if existing_content:
        # Parse existing content
        frontmatter, content = parse_frontmatter(existing_content)

        # Find the Ponencias section
        sections = content.split("\n## ")
        ponencias_idx = -1
        for i, section in enumerate(sections):
            if section.startswith("Ponencias"):
                ponencias_idx = i
                break

        if ponencias_idx == -1:
            # No Ponencias section found, add it before Biografía
            for i, section in enumerate(sections):
                if section.startswith("Biografía"):
                    sections.insert(
                        i,
                        f'Ponencias\n\n- {talk_title_with_hackathon}\n\n<EventSummary\n    description="{description}"\n    poster="{poster}"\n    video="{video}"\n/>\n',
                    )
                    break
        else:
            # Check if talk already exists by looking for the exact talk title
            ponencias = sections[ponencias_idx]
            if f"- {talk_title}" not in ponencias:
                # Add new talk to Ponencias section
                sections[ponencias_idx] = (
                    f'Ponencias\n{ponencias.split("Ponencias", 1)[1].strip()}\n\n- {talk_title_with_hackathon}\n\n<EventSummary\n    description="{description}"\n    poster="{poster}"\n    video="{video}"\n/>\n'
                )
            else:
                # Update existing talk to include hackathon name
                lines = ponencias.split("\n")
                for i, line in enumerate(lines):
                    if line.startswith(f"- {talk_title}"):
                        lines[i] = f"- {talk_title_with_hackathon}"
                sections[ponencias_idx] = "\n".join(lines)

        # Create ordered frontmatter
        ordered_frontmatter = {
            "title": name,
            "description": occupation,
            # Never update cover if there's an existing file
            "cover": frontmatter.get("cover", ""),
            "website": website,
            "twitter": twitter,
            "linkedin": linkedin,
            "github": frontmatter.get("github", ""),
            "huggingface": frontmatter.get("huggingface", ""),
            "community": frontmatter.get("community", f"Ponente {EVENT_YEAR}"),
        }

        # Reconstruct the file
        content = (
            "---\n"
            + yaml.dump(ordered_frontmatter, allow_unicode=True, sort_keys=False)
            + "---\n\n"
            + "\n## ".join(sections)
        )

        return content

    # Create new content with ordered fields
    content = f"""---
title: {name}
description: {occupation}
cover: {photo}
website: {website}
twitter: {twitter}
linkedin: {linkedin}
github: ""
huggingface: ""
community: Ponente {EVENT_YEAR}
---

## Ponencias

- {talk_title_with_hackathon}

<EventSummary
    description="{description}"
    poster="{poster}"
    video="{video}"
/>

## Biografía

{bio}

*Última actualización: {format_date(datetime.now())}*
"""
    return content


def format_speaker_filename(name):
    """Format a speaker name into a valid filename.

    Args:
        name (str): Full name of the speaker.

    Returns:
        str: A filename with:
            - All name parts separated by hyphens
            - Accents removed
            - Only lowercase letters
            - No special characters
    """
    # Split the name into parts and clean each part
    parts = [clean_filename(part) for part in name.strip().split()]

    # Join all parts with hyphens
    return "-".join(parts)


def update_talks_and_speakers():
    """Update talk and speaker files from the CSV data.

    Only processes events where Status is 'Aceptada'.
    """
    # Get the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Read the CSV file
    csv_path = os.path.join(script_dir, "data", FILE_PATH)
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        logging.error(f"CSV file not found: {csv_path}")
        return
    except pd.errors.EmptyDataError:
        logging.error(f"CSV file is empty: {csv_path}")
        return

    # Remove empty rows
    df = df.dropna(how="all")

    # Filter only accepted events
    df = df[df["Status"] == "Aceptada"]
    if len(df) == 0:
        logging.warning("No accepted events found in the CSV")
        return

    # Track processed files to handle duplicates
    processed_talks = set()

    # Process each row
    for _, row in df.iterrows():
        # Skip if essential fields are empty
        if pd.isna(row["Título del evento"]) or pd.isna(row["Nombre"]):
            logging.warning(
                f"Skipping row with missing title or name: {row['Título del evento']} - {row['Nombre']}"
            )
            continue

        try:
            # Create talk filename
            talk_filename = f"{clean_filename(row['Título del evento'])}.md"

            # Skip if we've already processed this talk
            if talk_filename in processed_talks:
                logging.warning(f"Duplicate talk found, skipping: {talk_filename}")
                continue

            processed_talks.add(talk_filename)

            talk_path = os.path.join(
                script_dir, "..", "pages", EVENT_DIR, talk_filename
            )

            # Create speaker filename with surname-names format
            speaker_filename = f"{format_speaker_filename(row['Nombre'])}.md"
            speaker_path = os.path.join(
                script_dir, "..", "pages", "comunidad", speaker_filename
            )

            # Create talk file
            talk_content = create_talk_content(row)
            with open(talk_path, "w", encoding="utf-8") as f:
                f.write(talk_content)
            logging.info(f"Created/updated talk file: {talk_filename}")

            # Update speaker file
            existing_content = None
            if os.path.exists(speaker_path):
                with open(speaker_path, "r", encoding="utf-8") as f:
                    existing_content = f.read()

            speaker_content = create_speaker_content(row, existing_content)
            with open(speaker_path, "w", encoding="utf-8") as f:
                f.write(speaker_content)
            logging.info(f"Created/updated speaker profile: {speaker_filename}")

        except Exception as e:
            logging.error(
                f"Error processing row: {row['Título del evento']} - {str(e)}"
            )


if __name__ == "__main__":
    update_talks_and_speakers()
