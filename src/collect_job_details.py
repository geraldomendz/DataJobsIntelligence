import pandas as pd
import base64
import json
import requests
import re
from bs4 import BeautifulSoup

# =====================================
# CONFIGURAÇÃO
# =====================================

EMPRESA = "qca"

# exemplos:
# EMPRESA = "qca"
# EMPRESA = "grupoboticario"

# =====================================
# FUNÇÃO LIMPEZA HTML
# =====================================

def clean_html(text):
    return BeautifulSoup(
        text or "",
        "html.parser"
    ).get_text(" ", strip=True)

# =====================================
# LER CSV
# =====================================

df = pd.read_csv(
    f"data/raw/{EMPRESA}_jobs.csv"
)

results = []

# =====================================
# LOOP DAS VAGAS
# =====================================

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
            f"https://{EMPRESA}.gupy.io/job/"
            f"{encoded}?jobBoardSource=gupy_portal"
        )

        print(f"Coletando {job_id}...")

        response = requests.get(
            url,
            timeout=20
        )

        match = re.search(
            r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',
            response.text
        )

        if not match:
            print(f"Erro na vaga {job_id}")
            continue

        data = json.loads(
            match.group(1)
        )

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

# =====================================
# SALVAR CSV
# =====================================

details_df = pd.DataFrame(results)

output_file = (
    f"data/processed/{EMPRESA}_jobs_details.csv"
)

details_df.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

print("\n======================")
print("COLETA FINALIZADA")
print("======================")
print(f"Vagas coletadas: {len(details_df)}")
print(f"Arquivo: {output_file}")