import csv
import sys
from pathlib import Path

RENAME = {
    "¿Cuál es tu nombre en Discord? Por ejemplo: somosnlp#0000. Invitación para unirte: https://discord.com/invite/my8w7JUxZR": "Discord (ES)",
    "Qual é o seu nome no Discord? Por exemplo: somosnlp#0000. Convite para entrar: https://discord.com/invite/my8w7JUxZR": "Discord (PT)",
    "Which is your Discord username? Invite: https://discord.com/invite/my8w7JUxZR": "Discord (EN)",
    "¿Cuál es tu nombre en el Hub de Hugging Face? Invitación: https://hf.co/organizations/somosnlp-hackathon-2026/share/DNcqoZrtSmEkyLLOiSYTQCzkcrquceDoVY": "Hugging Face (ES)",
    "Qual é o seu nome no Hub do HuggingFace? Convite: https://hf.co/organizations/somosnlp-hackathon-2026/share/DNcqoZrtSmEkyLLOiSYTQCzkcrquceDoVY": "Hugging Face (PT)",
    "Which is your Hugging Face username? Invite: https://huggingface.co/organizations/somosnlp-hackathon-2026/share/DNcqoZrtSmEkyLLOiSYTQCzkcrquceDoVY": "Hugging Face (EN)",
    "Me gustaría ayudar a difundir la iniciativa compartiendo el contenido que  me facilitéis": "Ayudar (ES)",
    "Gostaria de ajudar a divulgar a iniciativa compartilhando o conteúdo que vocês me fornecerem": "Ayudar (PT)",
    "I would like to help give visibility to the hackathon": "Ayudar (EN)",
    "Me gustaría ayudar a organizar el hackathon": "Visibilidad (ES)",
    "I would like to support the organization of the hackathon": "Visibilidad (EN)",
    "Gostaria de ajudar a organizar o hackathon": "Visibilidad (PT)",
}

KEEP = ["Order #", "Ticket Type", "Attendee #", *RENAME.keys()]

args = [a for a in sys.argv[1:] if a != "--filter"]
filter_yes = "--filter" in sys.argv

src = Path(args[0])
dst = src.with_name(src.stem + "_clean.csv")

FILTER_COLS = [k for k, v in RENAME.items() if v.startswith(("Ayudar", "Visibilidad"))]

def is_yes(v: str) -> bool:
    return "sí" in v.lower() or "sim" in v.lower() or "yes" in v.lower()

with src.open() as f_in, dst.open("w", newline="") as f_out:
    reader = csv.DictReader(f_in)
    writer = csv.DictWriter(f_out, fieldnames=[RENAME.get(c, c) for c in KEEP])
    writer.writeheader()
    for row in reader:
        if filter_yes and not any(is_yes(row[c]) for c in FILTER_COLS):
            continue
        writer.writerow({RENAME.get(c, c): row[c] for c in KEEP})

print(f"wrote {dst}")
