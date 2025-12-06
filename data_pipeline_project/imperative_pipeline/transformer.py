from collections import defaultdict

def filter_rows(rows, column, threshold):
    out = []
    for r in rows:
        try:
            if float(r.get(column, 0)) > threshold:
                out.append(r)
        except Exception:
            pass
    return out

def compute_column(rows, new_col, col1, col2, op='diff'):
    for r in rows:
        try:
            a = float(r.get(col1, 0))
            b = float(r.get(col2, 0))
            if op == 'diff':
                r[new_col] = str(a - b)
            elif op == 'ratio':
                r[new_col] = str(a / b if b != 0 else 0)
        except Exception:
            r[new_col] = '0'
    return rows

def aggregate_sum(rows, group_col, agg_col):
    agg = defaultdict(float)
    for r in rows:
        key = r.get(group_col, 'Unknown')
        try:
            agg[key] += float(r.get(agg_col, 0))
        except Exception:
            pass
    out = []
    for k, v in agg.items():
        out.append({group_col: k, agg_col: str(v)})
    return out
