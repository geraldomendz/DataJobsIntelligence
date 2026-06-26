import pandas as pd

# ============================
# LER ARQUIVOS
# ============================

qca = pd.read_csv(
    "data/processed/qca_skills.csv"
)

boticario = pd.read_csv(
    "data/processed/grupoboticario_skills.csv"
)

# ============================
# UNIR
# ============================

skills = pd.concat(
    [qca, boticario],
    ignore_index=True
)

# ============================
# RANKING GERAL
# ============================

ranking = (
    skills["skill"]
    .value_counts()
    .reset_index()
)

ranking.columns = [
    "skill",
    "quantidade"
]

print("\nTOP SKILLS\n")
print(ranking)

# ============================
# SALVAR
# ============================

ranking.to_csv(
    "data/processed/skill_ranking.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nArquivo salvo!")