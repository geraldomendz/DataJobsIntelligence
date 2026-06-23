import pandas as pd

df = pd.read_csv(
    "data/processed/qca_jobs_enriched.csv"
)



skills_map = {
    "Excel": [
        "excel"
    ],

    "SQL": [
        "sql",
        "mysql",
        "postgresql",
        "sql server"
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
    ]
}

results = []

for _, row in df.iterrows():

    texto = " ".join([
        str(row.get("descricao", "")),
        str(row.get("responsabilidades", "")),
        str(row.get("prerequisitos", ""))
    ]).lower()

    for skill, keywords in skills_map.items():

        encontrou = any(
            keyword in texto
            for keyword in keywords
        )

        if encontrou:

            results.append({
                "job_id": row["id"],
                "titulo": row["titulo"],
                "skill": skill
            })

skills_df = pd.DataFrame(results)

skills_df.to_csv(
    "data/processed/job_skills.csv",
    index=False,
    encoding="utf-8-sig"
)

print(skills_df.head())
print()
print("Total registros:", len(skills_df))

print(skills_df["skill"].value_counts())