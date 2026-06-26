from sqlalchemy import create_engine

SERVER = "localhost"
DATABASE = "DataJobsIntelligence"

connection_string = (
    f"mssql+pyodbc://@{SERVER}/{DATABASE}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(connection_string)

print("Conexão realizada com sucesso!")