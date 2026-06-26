import pandas as pd
from sqlalchemy import create_engine

# =====================================
# CONFIGURAÇÃO
# =====================================

EMPRESA = "grupoboticario"

# qca -> company_id = 1
# grupoboticario -> company_id = 2

company_ids = {
    "qca": 1,
    "grupoboticario": 2
}

company_id = company_ids[EMPRESA]

# =====================================
# CONEXÃO
# =====================================

SERVER = "localhost"
DATABASE = "DataJobsIntelligence"

engine = create_engine(
    f"mssql+pyodbc://@{SERVER}/{DATABASE}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

# =====================================
# LER ARQUIVOS
# =====================================

jobs = pd.read_csv(
    f"data/processed/{EMPRESA}_jobs_enriched.csv"
)

skills = pd.read_csv(
    f"data/processed/{EMPRESA}_skills.csv"
)

# =====================================
# ADICIONAR COMPANY_ID
# =====================================

jobs["company_id"] = company_id
skills["company_id"] = company_id

# =====================================
# REORDENAR COLUNAS
# =====================================

jobs = jobs[
    [
        "id",
        "company_id",
        "titulo",
        "tipo_vaga",
        "departamento",
        "cidade",
        "estado",
        "modalidade",
        "data_publicacao",
        "descricao",
        "responsabilidades",
        "prerequisitos"
    ]
]

skills = skills[
    [
        "job_id",
        "company_id",
        "skill"
    ]
]

# =====================================
# ENVIAR PARA SQL SERVER
# =====================================

jobs.to_sql(
    "jobs",
    engine,
    if_exists="append",
    index=False
)

skills.to_sql(
    "job_skills",
    engine,
    if_exists="append",
    index=False
)

print("Dados enviados com sucesso!")