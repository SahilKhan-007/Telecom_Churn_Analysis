from sqlalchemy import create_engine
from urllib.parse import quote_plus
import os
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    try:
        user = os.getenv("DB_USER")
        password = quote_plus(os.getenv("DB_PASSWORD"))  
        host = os.getenv("DB_HOST")
        database = os.getenv("DB_NAME")

        engine = create_engine(
            f"mysql+pymysql://{user}:{password}@{host}/{database}"
        )

        print("SQLAlchemy engine created")
        return engine

    except Exception as e:
        print(f" Error: {e}")
        return None