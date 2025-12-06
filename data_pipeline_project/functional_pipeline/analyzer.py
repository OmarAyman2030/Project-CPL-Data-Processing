import numpy as np

def statistics_summary(df, column):
    col = df[column].dropna().astype(float)
    return {
        'count': int(col.count()),
        'mean': float(col.mean()),
        'median': float(col.median()),
        'variance': float(col.var(ddof=0)) if col.count()>0 else None,
        'min': float(col.min()) if col.count()>0 else None,
        'max': float(col.max()) if col.count()>0 else None
    }

def correlation(df, col1, col2):
    s1 = df[col1].astype(float).dropna()
    s2 = df[col2].astype(float).dropna()
    # align on index intersection
    joined = df[[col1, col2]].dropna().astype(float)
    if len(joined) < 2:
        return None
    return float(joined[col1].corr(joined[col2]))
