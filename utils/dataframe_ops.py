import pandas as pd

def list_of_states(df: pd.DataFrame):
    states = df['state'].sort_values().unique()
    return states.tolist()

def list_of_dist(df: pd.DataFrame, state: str):
    return df[df['state']==state]['district'].sort_values().unique().tolist()

def get_rain(df: pd.DataFrame, district: str, state: str, month: str):
    return df.query(f'state == "{state}" & district == "{district}"')[month].tolist()[0]