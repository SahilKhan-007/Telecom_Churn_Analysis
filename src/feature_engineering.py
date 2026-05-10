import pandas as pd

def add_features(df: pd.DataFrame) -> pd.DataFrame:

    # CLV Proxy
    df['CLV'] = df['MonthlyCharges'] * df['tenure']

    # Tenure Groups
    def tenure_group(t):
        if t <= 12:
            return '0-12 Months'
        elif t <= 24:
            return '12-24 Months'
        elif t <= 48:
            return '24-48 Months'
        else:
            return '48+ Months'

    df['TenureGroup'] = df['tenure'].apply(tenure_group)

    # Revenue Proxy
    df['Revenue'] = df['MonthlyCharges']

    return df