import pandas as pd


def run(empresa):

    print(f"\nMesclando dados da {empresa}...")

    jobs = pd.read_csv(
        f"data/raw/{empresa}_jobs.csv"
    )

    details = pd.read_csv(
        f"data/processed/{empresa}_jobs_details.csv"
    )

    merged = jobs.merge(
        details.drop(columns=["titulo"]),
        on="id",
        how="inner"
    )

    output_file = (
        f"data/processed/{empresa}_jobs_enriched.csv"
    )

    merged.to_csv(
        output_file,
        index=False,
        encoding="utf-8-sig"
    )

    print(f"✔ Arquivo criado: {output_file}")
    print(f"✔ Total de vagas: {len(merged)}")

    return merged


if __name__ == "__main__":

    run("grupoboticario")