import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

url = "https://grupoboticario.gupy.io/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

next_data = soup.find("script", {"id": "__NEXT_DATA__"})

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

print(jobs[0].keys())

df.to_csv(
    "data/raw/grupoboticario_jobs.csv",
    index=False,
    encoding="utf-8-sig"
)

print(f"\n{len(df)} vagas salvas!")