import os
from sqlalchemy import create_engine, text

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST', 'localhost')
db_port = os.getenv('DB_PORT', '5432')
db_name = os.getenv('DB_NAME')

if not all([db_user, db_password, db_name]):
    raise ValueError("Missing required environment variables: DB_USER, DB_PASSWORD, DB_NAME")

connection_string = f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection_string)

with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM penguins LIMIT 5"))
    for row in result:
        print(row)
