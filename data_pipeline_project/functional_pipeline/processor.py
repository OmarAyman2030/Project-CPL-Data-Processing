import pandas as pd

def handle_missing(df, strategy='fill', fill_value=0):
    out = df.copy()
    if strategy == 'fill':
        out = out.fillna(fill_value)
    elif strategy == 'drop':
        out = out.dropna()
    return out

def standardize_date(df, column='Date', fmt=None):
    out = df.copy()
    if column in out.columns:
        out[column] = pd.to_datetime(out[column], errors='coerce')
        if fmt is not None:
            out[column] = out[column].dt.strftime(fmt)
    return out

def standardize_numbers(df, columns, decimals=2):
    out = df.copy()
    for col in columns:
        if col in out.columns:
            out[col] = pd.to_numeric(out[col], errors='coerce').round(decimals)
    return out
