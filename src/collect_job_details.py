import pandas as pd
import base64
import json
import requests
import re
from bs4 import BeautifulSoup

# =====================================
# LER CSV
# =====================================

df = pd.read_csv("data/raw/qca_jobs.csv")

# pegar primeira vaga para teste
job_id = df.iloc[0]["id"]

# =====================================
# GERAR URL DA GUPY
# =====================================

payload = {
    "jobId": int(job_id),
    "source": "gupy_portal"
}

encoded = base64.b64encode(
    json.dumps(payload, separators=(',', ':')).encode()
).decode()

url = f"https://qca.gupy.io/job/{encoded}?jobBoardSource=gupy_portal"

print(f"\nAcessando vaga {job_id}")
print(url)

# =====================================
# ACESSAR PÁGINA
# =====================================

response = requests.get(url)

print("\nStatus:", response.status_code)

# =====================================
# EXTRAIR __NEXT_DATA__
# =====================================

match = re.search(
    r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',
    response.text
)

print("NEXT_DATA encontrado:", match is not None)

if not match:
    raise Exception("NEXT_DATA não encontrado")

# =====================================
# CONVERTER JSON
# =====================================

data = json.loads(match.group(1))

job = data["props"]["pageProps"]["job"]

# =====================================
# LIMPAR HTML
# =====================================

descricao = BeautifulSoup(
    job.get("description", ""),
    "html.parser"
).get_text(" ", strip=True)

responsabilidades = BeautifulSoup(
    job.get("responsibilities", ""),
    "html.parser"
).get_text(" ", strip=True)

prerequisitos = BeautifulSoup(
    job.get("prerequisites", ""),
    "html.parser"
).get_text(" ", strip=True)

# =====================================
# EXIBIR RESULTADOS
# =====================================

print("\n" + "=" * 80)
print("NOME DA VAGA")
print("=" * 80)

print(job.get("name"))

print("\n" + "=" * 80)
print("PUBLICADA EM")
print("=" * 80)

print(job.get("publishedAt"))

print("\n" + "=" * 80)
print("DESCRIÇÃO")
print("=" * 80)

print(descricao[:1000])

print("\n" + "=" * 80)
print("RESPONSABILIDADES")
print("=" * 80)

print(responsabilidades[:1000])

print("\n" + "=" * 80)
print("PRÉ-REQUISITOS")
print("=" * 80)

print(prerequisitos[:1000])

from utils import generate_gupy_url

print(
    generate_gupy_url(11517322)
)