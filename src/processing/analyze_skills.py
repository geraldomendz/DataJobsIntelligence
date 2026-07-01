import pandas as pd

from config import COMPANIES


def run():


    dataframes = []

    for company in COMPANIES:

        empresa = company["name"]

        arquivo = (
            f"data/processed/{empresa}_skills.csv"
        )

        df = pd.read_csv(arquivo)

        dataframes.append(df)

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

    output_file = (
        "data/processed/skill_ranking.csv"
    )

    ranking.to_csv(
        output_file,
        index=False,
        encoding="utf-8-sig"
    )

    print(f"✔ Ranking gerado com {len(ranking)} skills.")
    print(f"✔ Arquivo salvo em {output_file}")

    return ranking


if __name__ == "__main__":
    run()