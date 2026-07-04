import base64
import json
import re

import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from utils.logger import Logger


def clean_html(text):
    return BeautifulSoup(
        text or "",
        "html.parser"
    ).get_text(" ", strip=True)


def run(empresa, base_url):


    df = pd.read_csv(
        f"data/raw/{empresa}_jobs.csv"
    )
    
    Logger.info(f"Coletando detalhes das vagas da {empresa}...")
    Logger.info(f"{len(df)} vagas encontradas.")
    

    results = []

    erros = 0

    for _, row in tqdm(
        df.iterrows(),
        total=len(df),
        desc=f"{empresa.upper()}",
        unit="vaga"
    ):

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

            base_url = base_url.rstrip("/")

            url = (
                f"{base_url}/job/"
                f"{encoded}?jobBoardSource=gupy_portal"
            )

            

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
                erros += 1
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

        except Exception:
            erros += 1
            Logger.error(f"Vaga {job_id}: {e}")

    details_df = pd.DataFrame(results)

    output_file = (
        f"data/processed/{empresa}_jobs_details.csv"
    )

    details_df.to_csv(
        output_file,
        index=False,
        encoding="utf-8-sig"
    )
    
    Logger.success(f"{len(details_df)} detalhes coletados.")

    if erros > 0:
        Logger.warning(f"{erros} vagas não puderam ser processadas.")

    Logger.info(f"Arquivo salvo em {output_file}")
    

    return details_df


if __name__ == "__main__":
    run("qca")