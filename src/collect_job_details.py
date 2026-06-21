import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
from bs4 import BeautifulSoup

url = "https://qca.gupy.io/job/eyJqb2JJZCI6MTE1MTczMjIsInNvdXJjZSI6Imd1cHlfcG9ydGFsIn0=?jobBoardSource=gupy_portal"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

next_data = soup.find("script", {"id": "__NEXT_DATA__"})

print("NEXT_DATA encontrado:", next_data is not None)

data = json.loads(next_data.string)
print(data["props"]["pageProps"].keys())

job = data["props"]["pageProps"]["job"]

vaga = {
    "id": job.get("id"),
    "cargo": job.get("name"),
    "cidade": job.get("addressCity"),
    "estado": job.get("addressState"),
    "tipo_trabalho": job.get("workplaceType"),
    "tipo_vaga": job.get("jobType"),
    "data_publicacao": job.get("publishedAt"),
    "empresa": job.get("company", {}).get("subdomain")
}

print(job["company"])

df = pd.DataFrame([vaga])

df.to_csv(
    "data/raw/jobs_raw.csv",
    index=False,
    encoding="utf-8-sig"
)

descricao_html = job["description"]

descricao_limpa = BeautifulSoup(
    descricao_html,
    "html.parser"
).get_text(" ", strip=True)

print("\nRESPONSIBILITIES:\n")
print(job["responsibilities"])

print("\nPREREQUISITES:\n")
print(job["prerequisites"])