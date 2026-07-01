import json

import pandas as pd
import requests
from bs4 import BeautifulSoup


def run(empresa, url):

    print(f"\nColetando vagas da {empresa}...")

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    next_data = soup.find(
        "script",
        {"id": "__NEXT_DATA__"}
    )

    data = json.loads(next_data.string)

    jobs = data["props"]["pageProps"]["jobs"]

    dados = []

    for job in jobs:

        dados.append({
            "id": job.get("id"),
            "titulo": job.get("title"),
            "tipo_vaga": job.get("type"),
            "departamento": job.get("department"),
            "cidade": job.get("workplace", {})
                         .get("address", {})
                         .get("city"),
            "estado": job.get("workplace", {})
                         .get("address", {})
                         .get("state"),
            "modalidade": job.get("workplace", {})
                             .get("workplaceType")
        })

    df = pd.DataFrame(dados)

    if df.empty:
        print("⚠ Nenhuma vaga encontrada.")
        return df

    output_file = f"data/raw/{empresa}_jobs.csv"

    df.to_csv(
        output_file,
        index=False,
        encoding="utf-8-sig"
    )

    print(f"✔ {len(df)} vagas coletadas.")
    print(f"✔ Arquivo salvo em {output_file}")

    return df


if __name__ == "__main__":

    run(
    empresa="grupoboticario",
    url="https://grupoboticario.gupy.io/"
)