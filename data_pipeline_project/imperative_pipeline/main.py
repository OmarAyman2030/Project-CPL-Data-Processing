from pathlib import Path
from loader import load_csv
import processor as proc
import transformer as trans
import analyzer as an
import output as outp
import visualizer as viz

BASE = Path(__file__).resolve().parent
DATA = BASE.parent / 'data.csv'
OUT = BASE / 'output'
OUT.mkdir(exist_ok=True)

def run_imperative_pipeline():
    rows = load_csv(DATA)
    rows = proc.handle_missing(rows, strategy='fill', fill_value='0')
    rows = proc.standardize_date(rows, 'Date')
    rows = proc.standardize_numbers(rows, ['Sales','Expenses'], decimals=2)

    rows = trans.compute_column(rows, 'Growth', 'Sales', 'Expenses', op='diff')
    rows = trans.filter_rows(rows, 'Sales', 1000)
    region_sales = trans.aggregate_sum(rows, 'Region', 'Sales')

    stats = an.statistics_summary(rows, 'Sales')
    corr = an.correlation(rows, 'Sales', 'Expenses')

    cleaned_path = OUT / 'imperative_clean.csv'
    region_path = OUT / 'imperative_region_sales.csv'
    outp.save_csv_rows(cleaned_path, rows)
    outp.save_csv_rows(region_path, region_sales, fieldnames=['Region','Sales'])

    viz.plot_line(rows, 'Date', 'Sales', save_path=str(OUT / 'imperative_sales_line.png'))
    viz.plot_bar(region_sales, 'Region', 'Sales', save_path=str(OUT / 'imperative_region_bar.png'))
    
    print('--- Imperative Pipeline Summary ---')
    print('Records after filter (Sales>1000):', len(rows))
    print('Statistics (Sales):', stats)
    print('Correlation Sales vs Expenses:', corr)
    print('Saved:', cleaned_path, region_path)

if __name__ == '__main__':
    run_imperative_pipeline()
