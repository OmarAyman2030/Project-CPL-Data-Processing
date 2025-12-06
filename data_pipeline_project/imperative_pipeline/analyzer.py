import math

def statistics_summary(rows, column):
    vals = []
    for r in rows:
        try:
            vals.append(float(r.get(column, 0)))
        except Exception:
            pass
    if not vals:
        return {}
    n = len(vals)
    mean = sum(vals)/n
    sorted_vals = sorted(vals)
    median = sorted_vals[n//2] if n%2==1 else (sorted_vals[n//2 -1] + sorted_vals[n//2])/2
    variance = sum((x-mean)**2 for x in vals)/n
    return {
        'count': n,
        'mean': mean,
        'median': median,
        'variance': variance,
        'min': min(vals),
        'max': max(vals)
    }

def correlation(rows, col1, col2):
    pairs = []
    for r in rows:
        try:
            a = float(r.get(col1, ''))
            b = float(r.get(col2, ''))
            pairs.append((a,b))
        except Exception:
            pass
    n = len(pairs)
    if n < 2:
        return None
    sum_x = sum(p[0] for p in pairs)
    sum_y = sum(p[1] for p in pairs)
    mean_x = sum_x / n
    mean_y = sum_y / n
    num = sum((p[0]-mean_x)*(p[1]-mean_y) for p in pairs)
    den_x = math.sqrt(sum((p[0]-mean_x)**2 for p in pairs))
    den_y = math.sqrt(sum((p[1]-mean_y)**2 for p in pairs))
    if den_x * den_y == 0:
        return None
    return num / (den_x * den_y)
