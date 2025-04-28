import csv
import re
from pathlib import Path


def clean_text(text):
    """Clean text by removing all extra whitespace, newlines, and normalizing spaces."""
    # Replace newlines with spaces and normalize all whitespace
    return " ".join(text.replace("\n", " ").split())


def format_occupation(occupation):
    """Format occupation by making the workplace (after @) bold."""
    # Split the occupation by @ and format each workplace in bold
    parts = occupation.split("@")
    if len(parts) == 1:
        return occupation

    formatted_parts = []
    formatted_parts.append(parts[0].strip())

    for part in parts[1:]:
        # Split by common separators to handle multiple positions/workplaces
        subparts = re.split(r"[,|/]", part)
        formatted_subparts = []

        for subpart in subparts:
            # Clean and format each workplace
            workplace = subpart.strip()
            if workplace:
                formatted_subparts.append(f"\\textbf{{{workplace}}}")

        # Rejoin with the original separators found in the text
        formatted_part = ""
        original_separators = re.findall(r"[,|/]", part)
        for i, formatted_subpart in enumerate(formatted_subparts):
            formatted_part += formatted_subpart
            if i < len(original_separators):
                formatted_part += f" {original_separators[i]} "

        formatted_parts.append(formatted_part)

    return " @ ".join(formatted_parts)


def get_year_from_filename(file_path):
    """Extract year from filename ponencias-YYYY.csv."""
    return int(file_path.stem.split("-")[1])


def process_csv_file(file_path, year):
    """Process a single CSV file and return list of LaTeX items."""
    latex_items = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            # Check if this file has a Status column
            has_status = "Status" in reader.fieldnames if reader.fieldnames else False
            required_fields = ["Título del evento", "Nombre", "Ocupación"]

            for row in reader:
                try:
                    # Skip rows missing required fields
                    if not all(key in row and row[key] for key in required_fields):
                        continue

                    # For files with Status column, only include accepted talks
                    if has_status and row["Status"] != "Aceptada":
                        continue

                    # Clean the text fields
                    title = clean_text(row["Título del evento"])
                    name = clean_text(row["Nombre"])
                    occupation = clean_text(row["Ocupación"])

                    # Format the occupation with bold workplaces
                    formatted_occupation = format_occupation(occupation)

                    # Format the item
                    item = f"\\item \\textit{{{title}}}, {name}, {formatted_occupation}, {year}"
                    latex_items.append(item)
                except KeyError as e:
                    print(f"Warning: Missing field {e} in file {file_path}")
                    continue
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return []

    return latex_items


def generate_latex_list():
    # Get the path to the data directory
    script_dir = Path(__file__).parent
    data_dir = script_dir / "data"

    # Find all ponencias-*.csv files and sort them by year in descending order
    csv_files = sorted(
        data_dir.glob("ponencias-*.csv"), key=get_year_from_filename, reverse=True
    )

    if not csv_files:
        raise FileNotFoundError("No ponencias-*.csv files found in data directory")

    print(f"Found {len(csv_files)} files to process:")
    for f in csv_files:
        print(f"  - {f.name}")

    all_items = []

    # Process each file
    for csv_file in csv_files:
        year = get_year_from_filename(csv_file)
        print(f"\nProcessing {csv_file.name}...")
        items = process_csv_file(csv_file, year)
        print(f"Found {len(items)} talks")
        all_items.extend(items)

    if not all_items:
        raise ValueError("No valid items found in any of the CSV files")

    # Generate the complete LaTeX itemize environment with consistent indentation
    latex_output = "\\begin{itemize}\n"
    latex_output += "\n".join(f"    {item}" for item in all_items)
    latex_output += "\n\\end{itemize}"

    return latex_output


def save_latex_output(content):
    """Save the LaTeX content to a file in the data/latex directory."""
    script_dir = Path(__file__).parent
    output_dir = script_dir / "latex"

    # Create the output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "ponencias.tex"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)

    return output_file


if __name__ == "__main__":
    try:
        latex_content = generate_latex_list()
        output_file = save_latex_output(latex_content)
        print(f"\nLaTeX content has been saved to: {output_file}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
