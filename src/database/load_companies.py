import pandas as pd

from database.database_connection import get_engine


def run(companies):

    print("\nSincronizando empresas...")

    engine = get_engine()

    df = pd.DataFrame(companies)[["id", "name"]]

    df = df.rename(
        columns={
            "name": "nome"
        }
    )

    empresas_sql = pd.read_sql(
        "SELECT id FROM companies",
        engine
    )

    df = df[
        ~df["id"].isin(empresas_sql["id"])
    ]

    if len(df) == 0:
        print("✔ Empresas já cadastradas.")
        return

    df.to_sql(
        "companies",
        engine,
        if_exists="append",
        index=False
    )

    print(f"✔ {len(df)} empresas adicionadas.")