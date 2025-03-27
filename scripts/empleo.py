"""Script to update job offers in the SomosNLP job board.

This script processes a CSV file containing job offers from a Google Form and generates
a TypeScript file (ofertas.ts) with the current valid job offers. The script handles:
- Date parsing and formatting
- Job offer validation (filtering out expired offers)
- Unique job name generation
- Data cleaning and formatting

The CSV file should contain the following columns:
- Marca temporal: Timestamp of form submission (DD/MM/YYYY HH:MM:SS)
- Ocupación: Job title/role
- Palabras clave: Keywords related to the job
- Tipo de contrato: Contract type
- Nombre de la empresa o instituto de investigación: Company/organization name
- Tamaño de la empresa o instituto de investigación: Company size
- Localización: Job location
- Fecha límite para enviar solicitudes: Application deadline (DD/MM/YYYY)
- Enlace a la descripción completa de la oferta: Link to full job description

The script considers a job offer valid if:
- It has a future deadline date, or
- It was published less than 3 months ago (if no deadline specified)
"""

import json
import os
import re
from datetime import datetime

import pandas as pd


def clean_text(text):
    """Clean text by removing special characters and converting to lowercase.

    Args:
        text (str): The text to clean.

    Returns:
        str: The cleaned text with:
            - All characters converted to lowercase
            - Special characters removed
            - Multiple spaces replaced with single underscore
            - Leading/trailing whitespace removed
    """
    # Remove special characters and convert to lowercase
    clean = text.lower()
    clean = re.sub(r"[^a-z0-9\s]", "", clean)
    # Replace multiple spaces with single underscore
    clean = re.sub(r"\s+", "_", clean.strip())
    return clean


def create_job_name(company, occupation, index):
    """Create a unique job name from company and occupation.

    Args:
        company (str): Company/organization name.
        occupation (str): Job title/role.
        index (int): Counter to make the name unique in case of duplicates.

    Returns:
        str: A unique job name that:
            - Combines company name and first 3 words of occupation
            - Is shortened to max 50 characters
            - Has an index suffix if it's a duplicate
            - Contains only lowercase letters, numbers and underscores
    """
    # Clean company name
    company_clean = clean_text(company)

    # Clean and shorten occupation (take first 3 words)
    occupation_clean = clean_text(occupation)
    occupation_words = occupation_clean.split("_")[:3]
    occupation_short = "_".join(occupation_words)

    # Combine company and occupation
    job_name = f"{company_clean}_{occupation_short}"

    # Shorten if too long (max 50 chars)
    if len(job_name) > 50:
        job_name = job_name[:50]

    # Add index if this is a duplicate
    if index > 0:
        job_name = f"{job_name}_{index}"

    return job_name


def parse_date(date_str):
    """Parse a date string and return a datetime object.

    Handles multiple date formats:
    - DD/MM/YYYY
    - DD/MM/YY
    - DD/MM/YYYY HH:MM:SS (Google Forms timestamp)

    Args:
        date_str (str): The date string to parse.

    Returns:
        datetime or None: The parsed datetime object, or None if parsing fails.
    """
    if pd.isna(date_str):
        return None

    try:
        # Try to parse date in DD/MM/YYYY format
        return datetime.strptime(date_str.strip(), "%d/%m/%Y")
    except (ValueError, AttributeError):
        try:
            # Try to parse date in DD/MM/YY format
            return datetime.strptime(date_str.strip(), "%d/%m/%y")
        except (ValueError, AttributeError):
            try:
                # Try to parse Google Forms timestamp format
                return datetime.strptime(date_str.strip(), "%d/%m/%Y %H:%M:%S")
            except (ValueError, AttributeError):
                return None


def format_date(date):
    """Format a datetime object to YYYY/MM/DD string.

    Args:
        date (datetime): The datetime object to format.

    Returns:
        str: The formatted date string in YYYY/MM/DD format, or empty string if date is None.
    """
    return date.strftime("%Y/%m/%d") if date else ""


def is_offer_valid(pub_date, deadline_date):
    """Check if a job offer is still valid based on its dates.

    An offer is considered valid if:
    - It has a future deadline date, or
    - It was published less than 3 months ago (if no deadline specified)

    Args:
        pub_date (datetime): Publication date of the offer.
        deadline_date (datetime): Application deadline date.

    Returns:
        bool: True if the offer is still valid, False otherwise.
    """
    today = datetime.now()

    # If there's a deadline date, use it
    if deadline_date:
        return deadline_date >= today

    # If no deadline, consider offers valid for 3 months from publication
    if pub_date:
        return (today - pub_date).days <= 90

    return False


def format_job_object(row):
    """Convert a row from the CSV into a job object with the correct format.

    Args:
        row (pandas.Series): A row from the CSV containing job offer data.

    Returns:
        dict: A dictionary with the job offer data formatted for TypeScript output:
            - Empty fields are represented as empty strings
            - Dates are formatted as YYYY/MM/DD
            - All text fields are stripped of leading/trailing whitespace
    """

    def clean_field(value):
        """Clean a field value, replacing NaN with empty string."""
        return "" if pd.isna(value) else str(value).strip()

    # Parse dates
    pub_date = parse_date(row["Marca temporal"])
    deadline_date = parse_date(row["Fecha límite para enviar solicitudes"])

    # Format dates for display
    pub_date_str = format_date(pub_date)
    deadline_date_str = format_date(deadline_date)

    # Combine dates in required format
    date_str = pub_date_str
    if deadline_date_str:
        date_str += f" ({deadline_date_str})"

    return {
        "ocupación": clean_field(
            row[
                "Ocupación\n\ne.g.: NLP Engineer, Data Scientist, Lingüista Computacional"
            ]
        ),
        "palabras clave": clean_field(
            row[
                "Palabras clave\n\ne.g.: traducción, textos bioclínicos, legal, educación, investigación, LLM, audio... \n\nNo es necesario especificar términos genéricos como NLP o ML ni palabras ya incluidas en la ocupación."
            ]
        ),
        "contrato": clean_field(row["Tipo de contrato"]),
        "entidad": clean_field(
            row["Nombre de la empresa o instituto de investigación"]
        ),
        "nº trabajadores/as": clean_field(
            row["Tamaño de la empresa o instituto de investigación"]
        ),
        "localización": clean_field(
            row[
                "Localización\n\ne.g.: Presencial Madrid, Híbrido Barcelona, Remoto 100%"
            ]
        ),
        "fecha publicación (fecha límite)": date_str,
        "más": clean_field(row["Enlace a la descripción completa de la oferta"]),
    }


def update_ofertas_ts():
    """Update the ofertas.ts file with current valid job offers.

    This function:
    1. Reads job offers from the CSV file
    2. Filters out expired offers
    3. Creates unique names for each job
    4. Formats the data for TypeScript
    5. Writes the updated content to ofertas.ts

    The output file includes:
    - A constant for each job offer with its data
    - The column names for the job board
    - An array of all current job offers
    """
    # Get the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Read the CSV file from the scripts directory
    csv_path = os.path.join(script_dir, "data", "empleo.csv")
    df = pd.read_csv(csv_path)

    # Remove empty rows (where all values are NaN)
    df = df.dropna(how="all")

    # Track job name occurrences
    job_name_counts = {}

    # Convert each row to a job object
    jobs = []
    for _, row in df.iterrows():
        company = row["Nombre de la empresa o instituto de investigación"]
        occupation = row[
            "Ocupación\n\ne.g.: NLP Engineer, Data Scientist, Lingüista Computacional"
        ]

        # Skip rows where essential fields are empty
        if pd.isna(company) or pd.isna(occupation):
            continue

        # Parse dates to check validity
        pub_date = parse_date(row["Marca temporal"])
        deadline_date = parse_date(row["Fecha límite para enviar solicitudes"])

        # Skip expired offers
        if not is_offer_valid(pub_date, deadline_date):
            continue

        # Create base job name
        base_job_name = create_job_name(company, occupation, 0)

        # Get count for this job name and increment
        count = job_name_counts.get(base_job_name, -1) + 1
        job_name_counts[base_job_name] = count

        # Create final job name with count if needed
        job_name = create_job_name(company, occupation, count)

        job_obj = format_job_object(row)
        jobs.append((job_name, job_obj))

    # Generate the TypeScript file content
    ts_content = """// Para añadir una nueva oferta, crea una constante con la información correspondiente y añádela a la lista `ofertas` al final del archivo.

"""

    # Add job objects
    for job_name, job_obj in jobs:
        ts_content += f"const {job_name} = {json.dumps(job_obj, indent=4, ensure_ascii=False)}\n\n"

    # Add columns and exports
    ts_content += """export const columnas = ['ocupación', 'contrato', 'entidad', 'nº trabajadores/as', 'localización', 'fecha publicación (fecha límite)', 'más']

export const ofertas = [
"""

    # Add job names to the ofertas array
    ts_content += ",\n".join(f"    {job_name}" for job_name, _ in jobs)
    ts_content += "\n]\n"

    # Write the updated content to ofertas.ts (relative to script directory)
    output_path = os.path.join(script_dir, "..", "pages", "empleo", "ofertas.ts")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ts_content)


if __name__ == "__main__":
    update_ofertas_ts()
