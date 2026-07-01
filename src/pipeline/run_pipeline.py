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


def main():

   

    total_empresas = 0
    total_vagas = 0

    pipeline_timer = Timer()

    print("=" * 60)
    print("         DATA JOBS INTELLIGENCE")
    print("=" * 60)

    load_companies(COMPANIES)

    for company in COMPANIES:

        company_timer = Timer()

        empresa = company["name"]
        url = company["url"]

        print(f"\n{'=' * 60}")
        print(f"PROCESSANDO: {empresa.upper()}")
        print(f"{'=' * 60}")
        

        print("\n[1/5] Coletando vagas...")
        jobs = collect_jobs(empresa, url)

        if jobs.empty:
            print(f"⚠ {empresa.upper()} não possui vagas abertas. Pulando...\n")
            continue

        print("\n[2/5] Coletando detalhes...")
        collect_job_details(empresa, url)
        
        print("\n[3/5] Mesclando dados...")
        merge_jobs(empresa)
        
        
        print("\n[4/5] Extraindo skills...")
        extract_skills(empresa)
        
        print("\n[5/5] Enviando para SQL Server...")
        jobs, skills = load_to_sql(empresa, company["id"])

        total_vagas += len(jobs)
        total_empresas += 1
        
        print(f"\n✔ {empresa.upper()} finalizada em {company_timer}.")
        

    print("\nGerando ranking geral de skills...")
    analyze_skills()
    
    

    print("\n" + "=" * 60)
    print("PIPELINE FINALIZADA COM SUCESSO!")
    print("=" * 60)

    print(f"Empresas processadas : {total_empresas}")
    print(f"Total de vagas       : {total_vagas}")
    print(f"Tempo total          : {pipeline_timer}")
    


if __name__ == "__main__":
    main()