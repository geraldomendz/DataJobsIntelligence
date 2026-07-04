from pathlib import Path

# ================================
# DIRETÓRIOS
# ================================

ROOT_DIR = Path(__file__).resolve().parent.parent

RAW_DATA = ROOT_DIR / "data" / "raw"
PROCESSED_DATA = ROOT_DIR / "data" / "processed"

# ================================
# EMPRESAS
# ================================

COMPANIES = [
    {
        "id": 1,
        "name": "qca",
        "url": "https://qca.gupy.io/"
    },
    {
        "id": 2,
        "name": "grupoboticario",
        "url": "https://grupoboticario.gupy.io/"
    },
     {
        "id": 3,
        "name": "itau",
        "url": "https://vemproitau.gupy.io/"
    },
    
    {
        "id": 4,
        "name": "raizen",
        "url": "https://genteraizen.gupy.io/"
    },
    {
        "id": 5,
        "name": "vivo",
        "url": "https://vivo.gupy.io/"
    },
     {
        "id": 6,
        "name": "ambev",
        "url": "https://ambev.gupy.io/"
    },
     {
        "id": 7,
        "name": "localiza",
        "url": "https://localiza.gupy.io/"
    },
     {
        "id": 8,
        "name": "porto",
        "url": "https://porto.gupy.io/"
    },
     {
        "id": 9,
        "name": "minsait",
        "url": "https://minsait.gupy.io/"
    },
     {
        "id": 10,
        "name": "globalhitss",
        "url": "https://globalhitss.gupy.io/"
    }

]