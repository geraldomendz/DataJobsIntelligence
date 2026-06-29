import pandas as pd
from database.database_connection import get_engine


company_ids = {
    "qca": 1,
    "grupoboticario": 2
}


def run(empresa):

    print(f"\nCarregando dados da {empresa} no SQL Server...")

    company_id = company_ids[empresa]

    engine = get_engine()


    jobs = pd.read_csv(
        f"data/processed/{empresa}_jobs_enriched.csv"
    )

    skills = pd.read_csv(
        f"data/processed/{empresa}_skills.csv"
    )

    jobs["company_id"] = company_id
    skills["company_id"] = company_id

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

    print(f"✔ {len(jobs)} vagas carregadas.")
    print(f"✔ {len(skills)} skills carregadas.")
    print("✔ Dados enviados com sucesso!")

    return jobs, skills


if __name__ == "__main__":
    run("qca")