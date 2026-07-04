import os

import pandas as pd

from config import COMPANIES
from utils.logger import Logger


def run():

    dataframes = []

    for company in COMPANIES:

        empresa = company["name"]

        arquivo = f"data/processed/{empresa}_skills.csv"

        if not os.path.exists(arquivo):
            Logger.warning(f"Arquivo não encontrado: {arquivo}")
            continue

        df = pd.read_csv(arquivo)

        if df.empty:
            continue

        dataframes.append(df)

    if not dataframes:
        Logger.warning("Nenhuma skill encontrada.")
        return pd.DataFrame()

    skills = pd.concat(
        dataframes,
        ignore_index=True
    )

    ranking = (
        skills["skill"]
        .value_counts()
        .reset_index()
    )

    ranking.columns = [
        "skill",
        "quantidade"
    ]

    output_file = "data/processed/skill_ranking.csv"

    ranking.to_csv(
        output_file,
        index=False,
        encoding="utf-8-sig"
    )

    Logger.success(f"Ranking gerado com {len(ranking)} skills.")
    Logger.info(f"Arquivo salvo em {output_file}")

    return ranking


if __name__ == "__main__":
    run()