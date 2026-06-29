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


def main():

    print("=" * 60)
    print("         DATA JOBS INTELLIGENCE")
    print("=" * 60)

    for company in COMPANIES:

        empresa = company["name"]
        url = company["url"]

        print(f"\n{'=' * 60}")
        print(f"PROCESSANDO: {empresa.upper()}")
        print(f"{'=' * 60}")

        collect_jobs(empresa, url)
        collect_job_details(empresa)
        merge_jobs(empresa)
        extract_skills(empresa)
        load_to_sql(empresa)

    

    analyze_skills()

    print("\n" + "=" * 60)
    print("PIPELINE FINALIZADA COM SUCESSO!")
    print("=" * 60)


if __name__ == "__main__":
    main()