import re

import pandas as pd

from utils.logger import Logger

from tqdm import tqdm


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


def run(empresa):

    Logger.info(f"Extraindo skills da {empresa}...")

    df = pd.read_csv(
        f"data/processed/{empresa}_jobs_enriched.csv"
    )

    results = []


    for _, row in tqdm(
        df.iterrows(),
        total=len(df),
        desc=f"{empresa.upper()}",
        unit="vaga"
    ):

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
                    "empresa": empresa,
                    "job_id": row["id"],
                    "titulo": row["titulo"],
                    "skill": skill
                })

    skills_df = pd.DataFrame(results)

    output_file = (
        f"data/processed/{empresa}_skills.csv"
    )

    skills_df.to_csv(
        output_file,
        index=False,
        encoding="utf-8-sig"
    )

    Logger.success(f"{len(skills_df)} skills encontradas.")
    Logger.info(f"Arquivo salvo em {output_file}")

    return skills_df


if __name__ == "__main__":
    run("qca")