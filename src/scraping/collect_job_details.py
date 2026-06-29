import base64
import json
import re

import pandas as pd
import requests
from bs4 import BeautifulSoup


def clean_html(text):
    return BeautifulSoup(
        text or "",
        "html.parser"
    ).get_text(" ", strip=True)


def run(empresa):

    print(f"Coletando detalhes das vagas da {empresa}...")

    df = pd.read_csv(
        f"data/raw/{empresa}_jobs.csv"
    )

    results = []

    for _, row in df.iterrows():

        job_id = row["id"]

        try:

            payload = {
                "jobId": int(job_id),
                "source": "gupy_portal"
            }

            encoded = base64.b64encode(
                json.dumps(
                    payload,
                    separators=(",", ":")
                ).encode()
            ).decode()

            url = (
                f"https://{empresa}.gupy.io/job/"
                f"{encoded}?jobBoardSource=gupy_portal"
            )

            print(f"Coletando vaga {job_id}...")

            response = requests.get(
                url,
                timeout=20
            )

            response.raise_for_status()

            match = re.search(
                r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',
                response.text
            )

            if not match:
                print(f"⚠ Não foi possível ler a vaga {job_id}")
                continue

            data = json.loads(match.group(1))

            job = data["props"]["pageProps"]["job"]

            results.append({
                "id": job.get("id"),
                "titulo": job.get("name"),
                "data_publicacao": job.get("publishedAt"),
                "descricao": clean_html(job.get("description")),
                "responsabilidades": clean_html(job.get("responsibilities")),
                "prerequisitos": clean_html(job.get("prerequisites"))
            })

        except Exception as e:
            print(f"Erro na vaga {job_id}: {e}")

    details_df = pd.DataFrame(results)

    output_file = (
        f"data/processed/{empresa}_jobs_details.csv"
    )

    details_df.to_csv(
        output_file,
        index=False,
        encoding="utf-8-sig"
    )

    print("\n======================")
    print("COLETA FINALIZADA")
    print("======================")
    print(f"Empresa: {empresa}")
    print(f"Vagas coletadas: {len(details_df)}")
    print(f"Arquivo salvo: {output_file}")

    return details_df


if __name__ == "__main__":
    run("qca")