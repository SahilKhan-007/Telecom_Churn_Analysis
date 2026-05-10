import pandas as pd

def export_data(df, csv_path, excel_path, engine=None):
    
    # Export CSV
    df.to_csv(csv_path, index=False)

    # Export Excel
    df.to_excel(excel_path, index=False)

    # Export to MySQL (only if engine is provided)
    if engine:
        df.to_sql('customers', con=engine, if_exists='replace', index=False)