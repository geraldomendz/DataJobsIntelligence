import pandas as pd

# =====================================
# CONFIGURAÇÃO
# =====================================

EMPRESA = "qca"

# exemplos:
# EMPRESA = "qca"
# EMPRESA = "grupoboticario"

# =====================================
# LEITURA DOS DADOS
# =====================================

jobs = pd.read_csv(
    f"data/raw/{EMPRESA}_jobs.csv"
)

details = pd.read_csv(
    f"data/processed/{EMPRESA}_jobs_details.csv"
)

# =====================================
# MERGE
# =====================================

merged = jobs.merge(
    details.drop(columns=["titulo"]),
    on="id",
    how="inner"
)

# =====================================
# SALVAR
# =====================================

output_file = (
    f"data/processed/{EMPRESA}_jobs_enriched.csv"
)

merged.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

print()
print("Arquivo criado:")
print(output_file)

print()
print("Shape:")
print(merged.shape)

print()
print(merged.head())