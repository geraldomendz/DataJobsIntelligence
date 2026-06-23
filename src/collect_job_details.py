import pandas as pd
import base64
import json
import requests
import re
from bs4 import BeautifulSoup


def clean_html(text):
    return BeautifulSoup(
        text or "",
        "html.parser"
    ).get_text(" ", strip=True)

# =====================================
# LER CSV
# =====================================

df = pd.read_csv("data/raw/qca_jobs.csv")

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
                separators=(',', ':')
            ).encode()
        ).decode()

        url = (
            f"https://qca.gupy.io/job/"
            f"{encoded}?jobBoardSource=gupy_portal"
        )

        print(f"Coletando {job_id}...")

        response = requests.get(url, timeout=20)

        match = re.search(
            r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',
            response.text
        )

        if not match:
            print(f"Erro na vaga {job_id}")
            continue

        data = json.loads(match.group(1))

        job = data["props"]["pageProps"]["job"]

        results.append({
            "id": job.get("id"),
            "titulo": job.get("name"),
            "data_publicacao": job.get("publishedAt"),
            "descricao": clean_html(
                job.get("description", "")
            ),
            "responsabilidades": clean_html(
                job.get("responsibilities", "")
            ),
            "prerequisitos": clean_html(
                job.get("prerequisites", "")
            )
        })

    except Exception as e:
        print(f"Erro {job_id}: {e}")




details_df = pd.DataFrame(results)

details_df.to_csv(
    "data/processed/qca_jobs_details.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\n======================")
print("COLETA FINALIZADA")
print("======================")
print(f"Vagas coletadas: {len(details_df)}")