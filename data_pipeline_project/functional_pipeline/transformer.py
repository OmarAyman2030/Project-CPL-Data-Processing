import pandas as pd

def filter_rows(df, column, threshold):
    if column not in df.columns:
        return df.copy()
    return df[df[column] > threshold].copy()

def compute_column(df, new_col, col1, col2, op='diff'):
    out = df.copy()
    if col1 not in out.columns or col2 not in out.columns:
        out[new_col] = None
        return out

    if op == 'diff':
        out[new_col] = out[col1] - out[col2]
    elif op == 'ratio':
        out[new_col] = out[col1] / out[col2].replace(0, pd.NA)
    return out

def aggregate_sum(df, group_col, agg_col):
    """
    Aggregate the sum of agg_col grouped by group_col.
    """
    if group_col not in df.columns or agg_col not in df.columns:
        return pd.DataFrame(columns=[group_col, agg_col])
    return df.groupby(group_col)[agg_col].sum().reset_index()
