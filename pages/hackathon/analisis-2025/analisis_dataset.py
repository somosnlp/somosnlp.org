#!/usr/bin/env python3
"""
Análisis del dataset de preferencias culturales - Hackathon SomosNLP 2025
=========================================================================
Script principal que realiza todos los análisis y genera las visualizaciones.
"""

import json
import re
import os
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# ─── Configuración ─────────────────────────────────────────────────────────
INPUT_PATH = "/mnt/user-data/uploads/dataset_2025.json"
OUT_DIR = Path("/home/claude/analisis")
GRAF_DIR = OUT_DIR / "graficas"
GRAF_DIR.mkdir(parents=True, exist_ok=True)

COLORS = [
    "#2563EB", "#DC2626", "#16A34A", "#D97706", "#7C3AED",
    "#0891B2", "#DB2777", "#65A30D", "#EA580C",
]

# ─── 1. Carga y aplanamiento ──────────────────────────────────────────────

def cargar_dataset(path: str) -> list[dict]:
    """Carga el JSON agrupado por país y lo aplana en una lista de registros."""
    with open(path, encoding="utf-8") as f:
        raw = json.load(f)
    registros = []
    for pais, items in raw.items():
        for item in items:
            item["pais"] = pais
            registros.append(item)
    return registros


# ─── 2. Categorización cultural ──────────────────────────────────────────

# Taxonomía basada en BLEnD, CVQA, WVS y la guía de anotación
CATEGORIAS_KEYWORDS = {
    "Gastronomía y alimentación": [
        "comida", "comer", "cocina", "receta", "plato", "ingrediente",
        "tortilla", "arepa", "empanada", "asado", "ceviche", "taco",
        "bebida", "almuerzo", "cena", "desayuno", "gastronomía",
        "culinari", "sazón", "guiso", "postre", "dulce", "pan ",
        "café", "mate", "chicha", "cerveza", "trago", "tomar",
        "restaurante", "mercado", "feria", "cocinero", "chef",
        "manjar", "tereré", "chipa", "sopa", "mole", "tamale",
        "lechón", "frijol", "arroz", "maíz", "plátano",
    ],
    "Lenguaje y expresiones": [
        "expresión", "modismo", "refrán", "dicho", "jerga", "argot",
        "slang", "coloquial", "significa", "decir", "palabra",
        "vocabulario", "dialecto", "habla", "lunfardo", "voseo",
        "tuteo", "usted", "lenguaje", "frase", "término",
        "significa la palabra", "qué quiere decir", "cómo se dice",
        "chilenismo", "mexicanismo", "colombianismo", "cubanismo",
        "modismo", "acento", "hablar", "insulto", "piropo",
        "grosería", "vulgar", "eufemismo",
    ],
    "Normas sociales y convivencia": [
        "norma", "educación", "cortesía", "saludo", "despedida",
        "protocolo", "etiqueta", "costumbre", "comportamiento",
        "transporte público", "fila", "cola", "vecino", "convivencia",
        "urbanidad", "respeto", "puntualidad", "propina",
        "interacción", "confianza", "amabilidad", "hospitalidad",
        "visita", "invitado", "anfitrión", "quedar", "reunión",
        "espacio personal", "beso", "abrazo", "apretón",
    ],
    "Tradiciones y celebraciones": [
        "tradición", "fiesta", "celebración", "festiv", "carnaval",
        "navidad", "año nuevo", "semana santa", "día de muertos",
        "feriado", "ritual", "ceremonia", "procesión", "danza",
        "baile", "folklor", "patronal", "quinceañera", "boda",
        "bautizo", "velorio", "funeral", "santo", "virgen",
        "romería", "sanfermín", "fallas", "tomatina",
    ],
    "Historia y política": [
        "histori", "independencia", "revolución", "colonia",
        "presidente", "gobierno", "política", "partido", "elección",
        "constitución", "dictadura", "democracia", "guerr",
        "conflicto", "paz", "tratado", "conquista", "virreinato",
        "república", "estado", "ley", "derecho", "legisl",
    ],
    "Identidad y valores": [
        "identidad", "nacional", "patriotismo", "orgullo",
        "idiosincrasia", "cosmovisión", "mentalidad", "valor",
        "moral", "ética", "religión", "iglesia", "fe", "creencia",
        "familia", "género", "machismo", "feminismo", "diversidad",
        "inclusión", "discriminación", "racismo", "clasismo",
        "indígena", "afrodescendiente", "mestizo", "criollo",
    ],
    "Educación y trabajo": [
        "escuela", "universidad", "educación", "profesor", "maestro",
        "clase", "examen", "carrera", "título", "beca",
        "trabajo", "empleo", "oficio", "sueldo", "salario",
        "empresa", "negocio", "emprendimiento", "economía",
        "informal", "migración", "remesa",
    ],
    "Geografía y medio ambiente": [
        "ciudad", "pueblo", "barrio", "región", "provincia",
        "departamento", "estado", "sierra", "costa", "selva",
        "montaña", "río", "playa", "isla", "volcán", "valle",
        "clima", "terremoto", "huracán", "inundación",
        "biodiversidad", "parque", "reserva", "naturaleza",
    ],
    "Arte y entretenimiento": [
        "música", "canción", "cantante", "artista", "pintor",
        "escritor", "poeta", "novela", "libro", "película",
        "cine", "teatro", "televisión", "serie", "telenovela",
        "deporte", "fútbol", "béisbol", "boxeo", "juego",
        "cumbia", "salsa", "reguetón", "reggaeton", "tango",
        "mariachi", "vallenato", "bolero", "son", "punto",
    ],
    "Vida cotidiana": [
        "día a día", "cotidian", "rutina", "hogar", "casa",
        "barrio", "calle", "transporte", "bus", "metro",
        "taxi", "colectivo", "compra", "tienda", "bodega",
        "farmacia", "hospital", "médico", "salud", "enfermedad",
        "seguridad", "delincuencia", "robo", "violencia",
    ],
}


def categorizar_prompt(texto: str) -> str:
    """Asigna una categoría cultural al prompt basándose en palabras clave."""
    texto_lower = texto.lower()
    scores: dict[str, int] = {}
    for cat, keywords in CATEGORIAS_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw in texto_lower)
        if score > 0:
            scores[cat] = score
    if not scores:
        return "Otro / Sin categoría clara"
    return max(scores, key=scores.get)


# ─── 3. Métricas de calidad ──────────────────────────────────────────────

def evaluar_calidad_prompt(registro: dict) -> dict:
    """Evalúa la calidad de un prompt individual según la guía de anotación."""
    prompt = registro["user_message"]
    system = registro["system_message"]
    flags = {}

    # ¿Tiene system prompt con rol/país?
    flags["tiene_system_prompt"] = len(system.strip()) > 10
    flags["system_menciona_pais"] = bool(re.search(
        r"(España|Chile|México|Colombia|Perú|Ecuador|Paraguay|Nicaragua|Cuba"
        r"|Argentina|Venezuela|Bolivia|Uruguay|Honduras|Guatemala|"
        r"panam|dominican|costarric|salvadoreñ|español|chilen|mexican"
        r"|colombian|peruan|ecuatorian|paraguayo|nicarag|cuban)",
        system, re.IGNORECASE
    ))

    # ¿Es trivial (saludo sin contenido)?
    flags["es_trivial"] = bool(re.match(
        r"^(hola|hey|buenos días|buenas tardes|qué tal|hi|hello|"
        r"como estás|cómo estás|hola que tal|hola como va)[!?.\s]*$",
        prompt.strip(), re.IGNORECASE
    ))

    # Longitud del prompt
    prompt_len = len(prompt.strip())
    flags["longitud_prompt"] = prompt_len
    flags["prompt_muy_corto"] = prompt_len < 20
    flags["prompt_largo"] = prompt_len > 200

    # ¿Tiene anclaje cultural explícito?
    flags["mencion_cultural"] = bool(re.search(
        r"(cultura|tradición|costumbre|típic|local|region|país|nacion"
        r"|pueblo|comunidad|folklor|patrimonio|ancestral|autócton"
        r"|España|Chile|México|Colombia|Perú|Ecuador|Paraguay|Cuba|Nicaragua"
        r"|Bogotá|Lima|Quito|Santiago|Madrid|CDMX|Asunción|Habana|Managua)",
        prompt, re.IGNORECASE
    ))

    # ¿Es neutral (no incluye juicios fuertes)?
    flags["posible_sesgo"] = bool(re.search(
        r"(mejor|peor|superior|inferior|odio|asco|todos son|"
        r"siempre son|nunca son|los \w+ son)",
        prompt, re.IGNORECASE
    ))

    # ¿El prompt es una pregunta o instrucción, no un chat vacío?
    flags["es_pregunta_o_instruccion"] = bool(re.search(
        r"(\?|cuál|cómo|qué|dónde|por qué|explica|describe|imagina"
        r"|recomienda|cuenta|dime|háblame|ayúdame)",
        prompt, re.IGNORECASE
    ))

    return flags


def calcular_score_calidad(flags: dict) -> float:
    """Puntúa un registro de 0 a 1 según criterios de calidad."""
    score = 0.0
    if flags["tiene_system_prompt"]:
        score += 0.15
    if flags["system_menciona_pais"]:
        score += 0.15
    if not flags["es_trivial"]:
        score += 0.20
    if flags["mencion_cultural"]:
        score += 0.20
    if flags["es_pregunta_o_instruccion"]:
        score += 0.15
    if not flags["posible_sesgo"]:
        score += 0.05
    if not flags["prompt_muy_corto"]:
        score += 0.10
    return round(score, 2)


# ─── 4. Análisis estadístico ─────────────────────────────────────────────

def analisis_por_pais(registros: list[dict]) -> dict:
    counter = Counter(r["pais"] for r in registros)
    return dict(counter.most_common())


def analisis_por_modelo(registros: list[dict]) -> dict:
    wins = Counter()
    losses = Counter()
    for r in registros:
        if not r["tie"] and not r["both_bad"]:
            wins[r["accepted_model"]] += 1
            losses[r["rejected_model"]] += 1
    all_models = sorted(set(wins) | set(losses))
    result = {}
    for m in all_models:
        total = wins[m] + losses[m]
        result[m] = {
            "victorias": wins[m],
            "derrotas": losses[m],
            "total_apariciones": total,
            "win_rate": round(wins[m] / total, 3) if total else 0,
        }
    return result


def analisis_por_usuario(registros: list[dict]) -> dict:
    user_data = defaultdict(lambda: {"n_prompts": 0, "paises": set(), "ties": 0, "both_bad": 0})
    for r in registros:
        u = r["username"]
        user_data[u]["n_prompts"] += 1
        user_data[u]["paises"].add(r["pais"])
        if r["tie"]:
            user_data[u]["ties"] += 1
        if r["both_bad"]:
            user_data[u]["both_bad"] += 1
    # Convert sets to lists for JSON
    return {u: {**d, "paises": sorted(d["paises"])} for u, d in user_data.items()}


def analisis_por_longitud(registros: list[dict]) -> dict:
    prompt_lens = [len(r["user_message"]) for r in registros]
    accepted_lens = [len(r["accepted_response"]) for r in registros]
    rejected_lens = [len(r["rejected_response"]) for r in registros]
    def stats(vals):
        arr = np.array(vals)
        return {
            "media": round(float(arr.mean()), 1),
            "mediana": round(float(np.median(arr)), 1),
            "min": int(arr.min()),
            "max": int(arr.max()),
            "std": round(float(arr.std()), 1),
            "p25": round(float(np.percentile(arr, 25)), 1),
            "p75": round(float(np.percentile(arr, 75)), 1),
        }
    return {
        "prompts": stats(prompt_lens),
        "respuestas_aceptadas": stats(accepted_lens),
        "respuestas_rechazadas": stats(rejected_lens),
    }


def analisis_categorias(registros: list[dict]) -> dict:
    cat_counts = Counter(r["categoria"] for r in registros)
    cat_por_pais = defaultdict(Counter)
    for r in registros:
        cat_por_pais[r["pais"]][r["categoria"]] += 1
    return {
        "totales": dict(cat_counts.most_common()),
        "por_pais": {p: dict(c.most_common()) for p, c in cat_por_pais.items()},
    }


def analisis_ties_bothbad(registros: list[dict]) -> dict:
    total = len(registros)
    ties = sum(1 for r in registros if r["tie"])
    both_bad = sum(1 for r in registros if r["both_bad"])
    clear_pref = sum(1 for r in registros if not r["tie"] and not r["both_bad"])

    por_pais = defaultdict(lambda: {"total": 0, "tie": 0, "both_bad": 0, "clear": 0})
    for r in registros:
        p = r["pais"]
        por_pais[p]["total"] += 1
        if r["both_bad"]:
            por_pais[p]["both_bad"] += 1
        elif r["tie"]:
            por_pais[p]["tie"] += 1
        else:
            por_pais[p]["clear"] += 1

    return {
        "global": {"total": total, "ties": ties, "both_bad": both_bad, "clear_pref": clear_pref,
                    "pct_ties": round(ties/total*100, 1), "pct_both_bad": round(both_bad/total*100, 1)},
        "por_pais": dict(por_pais),
    }


def analisis_calidad(registros: list[dict]) -> dict:
    scores = [r["calidad_score"] for r in registros]
    triviales = sum(1 for r in registros if r["calidad_flags"]["es_trivial"])
    sin_cultural = sum(1 for r in registros if not r["calidad_flags"]["mencion_cultural"])
    sin_system = sum(1 for r in registros if not r["calidad_flags"]["tiene_system_prompt"])

    scores_pais = defaultdict(list)
    for r in registros:
        scores_pais[r["pais"]].append(r["calidad_score"])

    return {
        "score_medio_global": round(np.mean(scores), 3),
        "score_mediano_global": round(float(np.median(scores)), 3),
        "prompts_triviales": triviales,
        "prompts_sin_anclaje_cultural": sin_cultural,
        "prompts_sin_system_prompt": sin_system,
        "pct_triviales": round(triviales / len(registros) * 100, 1),
        "score_por_pais": {
            p: round(np.mean(s), 3) for p, s in scores_pais.items()
        },
    }


# ─── 5. Visualizaciones ──────────────────────────────────────────────────

def plot_bar(data: dict, title: str, xlabel: str, ylabel: str, filename: str,
             horizontal: bool = False, color_idx: int = 0):
    fig, ax = plt.subplots(figsize=(10, max(5, len(data) * 0.5)))
    labels = list(data.keys())
    values = list(data.values())
    color = COLORS[color_idx % len(COLORS)]

    if horizontal:
        bars = ax.barh(labels, values, color=color, edgecolor="white")
        ax.set_xlabel(ylabel)
        ax.set_ylabel(xlabel)
        for bar, v in zip(bars, values):
            ax.text(bar.get_width() + max(values)*0.01, bar.get_y() + bar.get_height()/2,
                    str(v), va="center", fontsize=9)
    else:
        bars = ax.bar(labels, values, color=color, edgecolor="white")
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        plt.xticks(rotation=45, ha="right")
        for bar, v in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(values)*0.01,
                    str(v), ha="center", fontsize=9)

    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig(GRAF_DIR / filename, dpi=150)
    plt.close()


def plot_modelo_winrate(model_stats: dict, filename: str):
    fig, ax = plt.subplots(figsize=(10, 5))
    models = list(model_stats.keys())
    short_names = [m.split("-")[0].capitalize() if len(m) > 20 else m for m in models]
    wins = [model_stats[m]["victorias"] for m in models]
    losses = [model_stats[m]["derrotas"] for m in models]

    x = np.arange(len(models))
    w = 0.35
    ax.bar(x - w/2, wins, w, label="Victorias", color="#16A34A", edgecolor="white")
    ax.bar(x + w/2, losses, w, label="Derrotas", color="#DC2626", edgecolor="white")
    ax.set_xticks(x)
    ax.set_xticklabels(short_names, rotation=30, ha="right", fontsize=9)
    ax.set_ylabel("Número de comparaciones")
    ax.set_title("Victorias vs Derrotas por modelo", fontsize=13, fontweight="bold")
    ax.legend()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig(GRAF_DIR / filename, dpi=150)
    plt.close()


def plot_categorias_stacked(cat_pais: dict, filename: str):
    all_cats = sorted({c for pais_cats in cat_pais.values() for c in pais_cats})
    paises = sorted(cat_pais.keys())

    fig, ax = plt.subplots(figsize=(14, 7))
    x = np.arange(len(paises))
    bottom = np.zeros(len(paises))
    for i, cat in enumerate(all_cats):
        vals = [cat_pais[p].get(cat, 0) for p in paises]
        color = COLORS[i % len(COLORS)]
        ax.bar(x, vals, bottom=bottom, label=cat[:25], color=color, edgecolor="white", linewidth=0.3)
        bottom += np.array(vals)

    ax.set_xticks(x)
    ax.set_xticklabels(paises, rotation=45, ha="right")
    ax.set_ylabel("Número de prompts")
    ax.set_title("Distribución de categorías culturales por país", fontsize=13, fontweight="bold")
    ax.legend(bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig(GRAF_DIR / filename, dpi=150)
    plt.close()


def plot_calidad_pais(scores_pais: dict, filename: str):
    fig, ax = plt.subplots(figsize=(10, 5))
    paises = sorted(scores_pais.keys())
    vals = [scores_pais[p] for p in paises]
    bars = ax.bar(paises, vals, color=COLORS[:len(paises)], edgecolor="white")
    for bar, v in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
                f"{v:.2f}", ha="center", fontsize=9)
    ax.set_ylabel("Score medio de calidad (0-1)")
    ax.set_title("Calidad media de los prompts por país", fontsize=13, fontweight="bold")
    ax.set_ylim(0, 1)
    ax.axhline(y=0.5, color="gray", linestyle="--", alpha=0.5, label="Umbral mínimo recomendado")
    ax.legend()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(GRAF_DIR / filename, dpi=150)
    plt.close()


def plot_longitud_histograma(registros: list[dict], filename: str):
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    campos = [
        ("user_message", "Longitud de prompts", "#2563EB"),
        ("accepted_response", "Longitud respuestas aceptadas", "#16A34A"),
        ("rejected_response", "Longitud respuestas rechazadas", "#DC2626"),
    ]
    for ax, (campo, titulo, color) in zip(axes, campos):
        lens = [len(r[campo]) for r in registros]
        ax.hist(lens, bins=50, color=color, alpha=0.8, edgecolor="white")
        ax.set_title(titulo, fontsize=11, fontweight="bold")
        ax.set_xlabel("Caracteres")
        ax.set_ylabel("Frecuencia")
        ax.axvline(np.median(lens), color="black", linestyle="--", alpha=0.5, label=f"Mediana: {int(np.median(lens))}")
        ax.legend(fontsize=8)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig(GRAF_DIR / filename, dpi=150)
    plt.close()


def plot_tie_bothbad(tb: dict, filename: str):
    fig, ax = plt.subplots(figsize=(10, 5))
    paises = sorted(tb["por_pais"].keys())
    x = np.arange(len(paises))
    w = 0.25
    clear = [tb["por_pais"][p]["clear"] for p in paises]
    ties = [tb["por_pais"][p]["tie"] for p in paises]
    bb = [tb["por_pais"][p]["both_bad"] for p in paises]
    ax.bar(x - w, clear, w, label="Preferencia clara", color="#16A34A", edgecolor="white")
    ax.bar(x, ties, w, label="Empate", color="#D97706", edgecolor="white")
    ax.bar(x + w, bb, w, label="Ambas malas", color="#DC2626", edgecolor="white")
    ax.set_xticks(x)
    ax.set_xticklabels(paises, rotation=45, ha="right")
    ax.set_ylabel("Número de prompts")
    ax.set_title("Tipo de veredicto por país", fontsize=13, fontweight="bold")
    ax.legend()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig(GRAF_DIR / filename, dpi=150)
    plt.close()


def plot_usuarios_top(user_data: dict, filename: str):
    sorted_users = sorted(user_data.items(), key=lambda x: x[1]["n_prompts"], reverse=True)[:15]
    fig, ax = plt.subplots(figsize=(10, 6))
    names = [u[:25] for u, _ in sorted_users]
    vals = [d["n_prompts"] for _, d in sorted_users]
    ax.barh(names[::-1], vals[::-1], color="#7C3AED", edgecolor="white")
    ax.set_xlabel("Número de prompts")
    ax.set_title("Top 15 usuarios por número de contribuciones", fontsize=13, fontweight="bold")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig(GRAF_DIR / filename, dpi=150)
    plt.close()


# ─── 6. Ejecución principal ──────────────────────────────────────────────

def main():
    print("Cargando dataset...")
    registros = cargar_dataset(INPUT_PATH)
    print(f"Total de registros: {len(registros)}")

    # Categorización
    print("Categorizando prompts...")
    for r in registros:
        r["categoria"] = categorizar_prompt(r["user_message"])

    # Calidad
    print("Evaluando calidad...")
    for r in registros:
        r["calidad_flags"] = evaluar_calidad_prompt(r)
        r["calidad_score"] = calcular_score_calidad(r["calidad_flags"])

    # Análisis
    print("Ejecutando análisis...")
    resultados = {
        "resumen_general": {
            "total_registros": len(registros),
            "paises": len(set(r["pais"] for r in registros)),
            "usuarios_unicos": len(set(r["username"] for r in registros)),
            "modelos": sorted(set(r["accepted_model"] for r in registros) |
                              set(r["rejected_model"] for r in registros)),
        },
        "por_pais": analisis_por_pais(registros),
        "por_modelo": analisis_por_modelo(registros),
        "por_usuario": analisis_por_usuario(registros),
        "por_longitud": analisis_por_longitud(registros),
        "categorias": analisis_categorias(registros),
        "ties_bothbad": analisis_ties_bothbad(registros),
        "calidad": analisis_calidad(registros),
    }

    # Guardar resultados de análisis
    with open(OUT_DIR / "resultados_analisis.json", "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)

    # Guardar dataset anotado
    print("Guardando dataset anotado...")
    dataset_anotado = {}
    for r in registros:
        pais = r["pais"]
        if pais not in dataset_anotado:
            dataset_anotado[pais] = []
        entry = {
            "system_message": r["system_message"],
            "user_message": r["user_message"],
            "accepted_response": r["accepted_response"],
            "accepted_model": r["accepted_model"],
            "rejected_response": r["rejected_response"],
            "rejected_model": r["rejected_model"],
            "username": r["username"],
            "tie": r["tie"],
            "both_bad": r["both_bad"],
            "categoria": r["categoria"],
            "calidad_score": r["calidad_score"],
        }
        dataset_anotado[pais].append(entry)

    with open(OUT_DIR / "dataset_2025_anotado.json", "w", encoding="utf-8") as f:
        json.dump(dataset_anotado, f, ensure_ascii=False, indent=2)

    # Gráficas
    print("Generando gráficas...")
    plot_bar(resultados["por_pais"], "Distribución de prompts por país",
             "País", "Número de prompts", "01_prompts_por_pais.png", color_idx=0)

    plot_modelo_winrate(resultados["por_modelo"], "02_modelos_winrate.png")

    plot_categorias_stacked(resultados["categorias"]["por_pais"],
                           "03_categorias_por_pais.png")

    plot_bar(resultados["categorias"]["totales"],
             "Distribución de categorías culturales (global)",
             "Categoría", "Número de prompts", "04_categorias_global.png",
             horizontal=True, color_idx=3)

    plot_calidad_pais(resultados["calidad"]["score_por_pais"],
                      "05_calidad_por_pais.png")

    plot_longitud_histograma(registros, "06_longitudes.png")

    plot_tie_bothbad(resultados["ties_bothbad"], "07_ties_bothbad.png")

    plot_usuarios_top(resultados["por_usuario"], "08_top_usuarios.png")

    # Win-rate bar chart
    wr_data = {m: resultados["por_modelo"][m]["win_rate"]
               for m in sorted(resultados["por_modelo"])}
    plot_bar(wr_data, "Win-rate por modelo (excl. empates y ambas malas)",
             "Modelo", "Win-rate", "09_winrate.png", color_idx=2)

    print(f"Análisis completo. Resultados en {OUT_DIR}")
    return registros, resultados


if __name__ == "__main__":
    registros, resultados = main()
