from sqlalchemy import text

def run_sql_file(engine, file_path):
    with open(file_path, 'r') as file:
        sql = file.read()

    with engine.connect() as conn:
        for statement in sql.split(';'):
            if statement.strip():
                conn.execute(text(statement))