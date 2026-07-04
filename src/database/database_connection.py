from sqlalchemy import create_engine
from utils.logger import Logger

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
    Logger.success("Conexão realizada com sucesso!")