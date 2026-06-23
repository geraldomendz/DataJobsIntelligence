import pandas as pd

jobs = pd.read_csv("data/raw/qca_jobs.csv")

details = pd.read_csv(
    "data/processed/qca_jobs_details.csv"
)

merged = jobs.merge(
    details.drop(columns=["titulo"]),
    on="id",
    how="inner"
)

merged.to_csv(
    "data/processed/qca_jobs_enriched.csv",
    index=False
)

print(merged.shape)