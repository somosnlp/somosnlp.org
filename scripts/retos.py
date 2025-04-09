import csv
import os
from datetime import datetime


def format_date_range(date_str):
    if not date_str:
        return ""

    # Dictionary for month translations
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

    try:
        # Split the date range
        if "→" in date_str:
            dates = date_str.split("→")
        else:
            # Handle single date
            date = datetime.strptime(date_str.strip(), "%B %d, %Y")
            return f"{date.day} de {months[date.strftime('%B')]}"

        if len(dates) != 2:
            return date_str

        # Process start date
        start_date = dates[0].strip()
        if "(" in start_date:  # Handle dates with time
            start_date = start_date.split("(")[0].strip()
        start = datetime.strptime(start_date, "%B %d, %Y")

        # Process end date
        end_date = dates[1].strip()
        if "(" in end_date:  # Handle dates with time
            end_date = end_date.split("(")[0].strip()
        end = datetime.strptime(end_date, "%B %d, %Y")

        # Format in Spanish
        return f"{start.day} de {months[start.strftime('%B')]} - {end.day} de {months[end.strftime('%B')]}"
    except:
        return date_str


def format_list(text):
    if not text:
        return ""
    # Fix common line break issues
    text = text.replace("co-", "co")  # Remove hyphen from co-autoría
    items = [item.strip() for item in text.split("-") if item.strip()]
    return "\n".join(f"- {item}" for item in items)


def get_value(row, key):
    # Try both with and without BOM
    return row.get(key, row.get("\ufeff" + key, ""))


def format_challenge_content(reto):
    content = []

    # Basic info outside toggle
    content.extend(
        [
            f"### {get_value(reto, 'Evento')}",
            "",
            f"{get_value(reto, 'Descripción')}",
            "",
        ]
    )

    # Format dates and points in one line
    date_str = format_date_range(get_value(reto, "Fechas"))
    points_str = get_value(reto, "Puntos máx")
    if date_str or points_str:
        info_parts = []
        if date_str:
            info_parts.append(date_str)
        if points_str:
            info_parts.append(f"máx {points_str} ptos")
        content.extend(
            [
                f"*{' | '.join(info_parts)}*",
                "",
            ]
        )

    if get_value(reto, "Espacio de anotación"):
        content.extend(
            [f"¡Participa ya! {get_value(reto, 'Espacio de anotación')}", ""]
        )

    # Toggle content
    toggle_content = []

    if get_value(reto, "Guías y material de apoyo"):
        toggle_content.extend(
            [
                "Guías y material de apoyo:",
                format_list(get_value(reto, "Guías y material de apoyo")),
                "",
            ]
        )

    if get_value(reto, "Incentivos"):
        toggle_content.extend(
            ["Incentivos:", format_list(get_value(reto, "Incentivos")), ""]
        )

    patrocinios = []
    if get_value(reto, "Patrocinios"):
        patrocinios.extend(format_list(get_value(reto, "Patrocinios")).split("\n"))
    if get_value(reto, "Equipo"):
        patrocinios.append(f"- El equipo: {get_value(reto, 'Equipo')}")

    if patrocinios:
        toggle_content.extend(["Muchísimas gracias a:", "\n".join(patrocinios), ""])

    # Add toggle if there's content
    if toggle_content:
        content.extend(
            [
                "<details>",
                "<summary>Más información</summary>",
                "",
                *toggle_content,
                "</details>",
                "",
            ]
        )

    return content


def generate_retos_md():
    # Read the CSV file
    retos = []
    try:
        with open("scripts/data/retos.csv", "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            retos = list(reader)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    # Generate the markdown content
    content = []

    # Add the frontmatter
    content.extend(
        [
            "---",
            'title: "Retos #HackathonSomosNLP 2025"',
            "description: Vamos a impulsar la creación de modelos de lenguaje alineados con la cultura de los países de LATAM y la Península Ibérica.",
            "lang: es",
            "cover: https://somosnlp.github.io/assets/images/eventos/250401_hackathon_sinfecha.jpg",
            "---",
            "",
            "## Mini retos",
            "",
        ]
    )

    # Process mini retos
    mini_retos = [r for r in retos if get_value(r, "Tipo de evento") == "Mini reto"]
    for reto in mini_retos:
        content.extend(format_challenge_content(reto))

    # Add Reto principal section
    content.extend(["## Reto principal", ""])

    # Process retos principales
    retos_principales = [
        r for r in retos if get_value(r, "Tipo de evento") == "Reto principal"
    ]
    for reto in retos_principales:
        content.extend(format_challenge_content(reto))

    # Add Eventos section
    content.extend(["## Eventos", ""])

    # Process charlas
    charlas = [r for r in retos if get_value(r, "Tipo de evento") == "Charla"]
    for charla in charlas:
        content.extend(
            [
                f"#### {get_value(charla, 'Evento')}",
                "",
                (
                    f"{get_value(charla, 'Descripción')}"
                    if get_value(charla, "Descripción")
                    else ""
                ),
                "",
                "",
            ]
        )

    # Write the content to the file
    try:
        with open("pages/hackathon/retos.md", "w", encoding="utf-8") as f:
            f.write("\n".join([line for line in content if line is not None]))
        print("Successfully generated retos.md")
    except Exception as e:
        print(f"Error writing markdown file: {e}")


if __name__ == "__main__":
    generate_retos_md()
