from datetime import datetime

def handle_missing(rows, strategy='fill', fill_value='0'):
    out = []
    for r in rows:
        new_r = r.copy()
        for k, v in new_r.items():
            if v is None or v == '':
                if strategy == 'fill':
                    new_r[k] = str(fill_value)
                elif strategy == 'drop':
                    new_r = None
                    break
        if new_r is not None:
            out.append(new_r)
    return out

def standardize_date(rows, column='Date', fmt='%Y-%m-%d'):
    for r in rows:
        try:
            # parse then format back to string (mutation allowed in imperative)
            d = datetime.fromisoformat(r[column])
            r[column] = d.strftime(fmt)
        except Exception:
            # try other parsing
            try:
                d = datetime.strptime(r[column], '%Y-%m-%d')
                r[column] = d.strftime(fmt)
            except Exception:
                r[column] = ''
    return rows

def standardize_numbers(rows, columns, decimals=2):
    for r in rows:
        for col in columns:
            try:
                val = float(r.get(col, '') or 0.0)
                r[col] = str(round(val, decimals))
            except Exception:
                r[col] = str(0.0)
    return rows
