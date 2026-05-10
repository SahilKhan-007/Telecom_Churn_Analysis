from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.feature_engineering import add_features
from src.export import export_data
from src.db_connection import get_engine   
from src.run_queries import run_sql_file


def main():

    print("Starting Pipeline...\n")

    # Load
    df = load_data('data/raw/telco_churn.csv')

    # Clean
    df = clean_data(df)

    # Feature Engineering
    df = add_features(df)

    # -------------------------
    # CONNECT TO DATABASE
    # -------------------------
    engine = get_engine()

    # -------------------------
    # EXPORT (CSV + Excel + MySQL)
    # -------------------------
    export_data(
        df,
        'data/processed/cleaned_data.csv',
        'data/processed/cleaned_data.xlsx',
        engine  
    )

    print("\nPipeline Completed Successfully!")

if __name__ == "__main__":
    main()



