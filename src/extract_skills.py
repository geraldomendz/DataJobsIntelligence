import pandas as pd
import re

# =====================================
# CONFIGURAÇÃO
# =====================================

EMPRESA = "grupoboticario"

# =====================================
# LEITURA
# =====================================

df = pd.read_csv(
    f"data/processed/{EMPRESA}_jobs_enriched.csv"
)

# =====================================
# MAPA DE SKILLS
# =====================================

skills_map = {

    "Excel": [
        "excel"
    ],

    "SQL": [
        "sql",
        "mysql",
        "postgresql",
        "sql server",
        "oracle",
        "bigquery",
        "banco de dados"
    ],

    "Python": [
        "python"
    ],

    "Power BI": [
        "power bi",
        "powerbi"
    ],

    "API": [
        "api",
        "apis"
    ],

    "Jira": [
        "jira"
    ],

    "Trello": [
        "trello"
    ],

    "Notion": [
        "notion"
    ],

    "AWS": [
        "aws",
        "amazon web services"
    ],

    "Azure": [
        "azure",
        "microsoft azure"
    ],

    "Databricks": [
        "databricks"
    ],

    "Spark": [
        "spark",
        "apache spark"
    ],

    "Git": [
        "git",
        "github"
    ],

    "Docker": [
        "docker"
    ],

    "ETL": [
        "etl"
    ],

    "Tableau": [
        "tableau"
    ]
}

results = []

# =====================================
# EXTRAÇÃO
# =====================================

for _, row in df.iterrows():

    texto = " ".join([
        str(row.get("descricao", "")),
        str(row.get("responsabilidades", "")),
        str(row.get("prerequisitos", ""))
    ]).lower()

    for skill, keywords in skills_map.items():

        encontrou = any(
            re.search(
                rf"\b{re.escape(keyword.lower())}\b",
                texto
            )
            for keyword in keywords
        )

        if encontrou:

            results.append({
                "empresa": EMPRESA,
                "job_id": row["id"],
                "titulo": row["titulo"],
                "skill": skill
            })

# =====================================
# SALVAR
# =====================================

skills_df = pd.DataFrame(results)

output_file = (
    f"data/processed/{EMPRESA}_skills.csv"
)

skills_df.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

print(skills_df.head())

print()
print("Total registros:", len(skills_df))

print()
print(skills_df["skill"].value_counts())

print()
print(f"Arquivo salvo: {output_file}")