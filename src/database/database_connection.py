from sqlalchemy import create_engine

SERVER = "localhost"
DATABASE = "DataJobsIntelligence"

connection_string = (
    f"mssql+pyodbc://@{SERVER}/{DATABASE}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)


def get_engine():
    return create_engine(connection_string)


if __name__ == "__main__":
    engine = get_engine()
    print("Conexão realizada com sucesso!")