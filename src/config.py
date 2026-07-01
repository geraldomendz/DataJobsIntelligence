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
    }
]