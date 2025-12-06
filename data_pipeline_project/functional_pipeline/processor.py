import pandas as pd
def handle_missing(df, strategy='fill', fill_value=0, columns=None):
    """
    Handle missing values in a DataFrame.

    - strategy: 'fill' (default) or 'drop'.
    - fill_value: scalar value, or a dict mapping column->fill_value.
    - columns: optional list of columns to target for filling.

    Behavior:
    - 'fill' preserves all rows and fills NA values.
    - 'drop' removes any rows with NA (same as ``dropna()``).
    """
    out = df.copy()
    if strategy == 'fill':
        # If user provided a list of columns, only fill those
        if columns is not None:
            if isinstance(fill_value, dict):
                for col in columns:
                    if col in out.columns:
                        val = fill_value.get(col, fill_value.get('__default__', 0))
                        out[col] = out[col].fillna(val)
            else:
                # scalar fill for specified columns
                cols = [c for c in columns if c in out.columns]
                out[cols] = out[cols].fillna(fill_value)
        else:
            # No columns specified: fill across entire DataFrame
            if isinstance(fill_value, dict):
                out = out.fillna(value=fill_value)
            else:
                out = out.fillna(fill_value)
    elif strategy == 'drop':
        out = out.dropna()
    return out

def standardize_date(df, column='transaction_date', fmt=None):
    """
    Convert a date column to datetime. Optional formatting.
    """
    out = df.copy()
    if column in out.columns:
        out[column] = pd.to_datetime(out[column], errors='coerce')
        if fmt is not None:
            out[column] = out[column].dt.strftime(fmt)
    return out

def standardize_numbers(df, columns, decimals=2):
    """
    Ensure numeric columns are numeric and rounded to specified decimals.
    """
    out = df.copy()
    for col in columns:
        if col in out.columns:
            out[col] = pd.to_numeric(out[col], errors='coerce').round(decimals)
    return out
