import sys
from pathlib import Path

# Adiciona a pasta src ao PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parents[1]))

from config import COMPANIES

from scraping.collect_jobs import run as collect_jobs
from scraping.collect_job_details import run as collect_job_details

from processing.merge_jobs import run as merge_jobs
from processing.extract_skills import run as extract_skills
from processing.analyze_skills import run as analyze_skills

from database.load_to_sql import run as load_to_sql
from database.load_companies import run as load_companies

from utils.timer import Timer
from utils.logger import Logger


def main():

    total_empresas = 0
    total_vagas = 0

    pipeline_timer = Timer()

    Logger.separator()
    print("         DATA JOBS INTELLIGENCE")
    Logger.separator()

    load_companies(COMPANIES)

    for company in COMPANIES:

        company_timer = Timer()

        empresa = company["name"]
        url = company["url"]

        Logger.company(empresa)

        Logger.step(1, 5, "Coletando vagas")
        jobs = collect_jobs(empresa, url)

        if jobs.empty:
            Logger.warning(
                f"{empresa.upper()} não possui vagas abertas. Pulando..."
            )
            continue

        Logger.step(2, 5, "Coletando detalhes")
        collect_job_details(empresa, url)

        Logger.step(3, 5, "Mesclando dados")
        merge_jobs(empresa)

        Logger.step(4, 5, "Extraindo skills")
        extract_skills(empresa)

        Logger.step(5, 5, "Enviando para SQL Server")
        jobs, skills = load_to_sql(empresa, company["id"])

        total_empresas += 1
        total_vagas += len(jobs)

        Logger.finish_company(
            empresa,
            company_timer
        )

    Logger.info("Gerando ranking geral de skills...")
    analyze_skills()

    Logger.pipeline_finish(
        total_empresas,
        total_vagas,
        pipeline_timer
    )


if __name__ == "__main__":
    main()