from sqlalchemy import create_engine
from utils.logger import Logger
from dotenv import load_dotenv
import os

load_dotenv()

SERVER = os.getenv("DB_SERVER")
DATABASE = os.getenv("DB_DATABASE")
DRIVER = os.getenv("DB_DRIVER")

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