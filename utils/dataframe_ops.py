import pandas as pd
from .npk_calc import N_value, P_value, K_value

def list_of_states(df: pd.DataFrame):
    states = df['state'].sort_values().unique()
    return states.tolist()

def list_of_dist(df: pd.DataFrame, state: str):
    return df[df['state']==state]['district'].sort_values().unique().tolist()

def get_rain(df: pd.DataFrame, district: str, state: str, month: str):
    return df.query(f'state == "{state}" & district == "{district}"')[month].tolist()[0]

def get_composition(df: pd.DataFrame, district: str, state: str):
    n = df.query(f'state == "{state}" & district == "{district}"')['N'].tolist()[0]
    p = df.query(f'state == "{state}" & district == "{district}"')['P'].tolist()[0]
    k = df.query(f'state == "{state}" & district == "{district}"')['K'].tolist()[0]
    return N_value(n), P_value(p), K_value(k)