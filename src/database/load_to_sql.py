import pandas as pd
from database.database_connection import get_engine
from sqlalchemy import text
from utils.logger import Logger





def run(empresa, company_id):

    Logger.info(f"Carregando dados da {empresa} no SQL Server...")

   

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

    with engine.begin() as conn:

        conn.execute(
         text(
              "DELETE FROM job_skills WHERE company_id = :company_id"
         ),
         {"company_id": company_id}
    )

        conn.execute(
         text(
             "DELETE FROM jobs WHERE company_id = :company_id"
         ),
          {"company_id": company_id}
    )

    

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

    Logger.success(f"{len(jobs)} vagas carregadas.")
    Logger.success(f"{len(skills)} skills carregadas.")
    Logger.success("Dados enviados com sucesso!")

    return jobs, skills


if __name__ == "__main__":
    run("qca")