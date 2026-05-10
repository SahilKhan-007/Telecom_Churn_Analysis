import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    
    # 1. Strip column names
    df.columns = df.columns.str.strip()

    # 2. Fix TotalCharges (critical step)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # 3. Handle missing values
    df = df.dropna(subset=['TotalCharges'])

    # 4. Convert categorical columns
    categorical_cols = df.select_dtypes(include='object').columns
    for col in categorical_cols:
        df[col] = df[col].astype('category')

    # 5. Convert SeniorCitizen to category
    df['SeniorCitizen'] = df['SeniorCitizen'].astype('category')

    return df