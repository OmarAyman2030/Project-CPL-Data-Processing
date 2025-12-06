from pathlib import Path
from loader import load_csv
import processor as proc
import transformer as trans
import analyzer as an
import output as outp
import visualizer as viz

BASE = Path(__file__).resolve().parent
DATA = BASE.parent / 'grocery_chain_data.csv'
OUT = BASE / 'output'
OUT.mkdir(exist_ok=True)

def run_imperative_pipeline():
    rows = load_csv(DATA)
    rows = proc.handle_missing(rows, strategy='fill', fill_value='Unknown')
    rows = proc.standardize_date(rows, 'transaction_date')
    rows = proc.standardize_numbers(rows, ['final_amount','discount_amount'], decimals=2)

    rows = trans.compute_column(rows, 'Growth', 'final_amount', 'discount_amount', op='diff')
    rows = trans.filter_rows(rows, 'final_amount', 100)
    region_sales = trans.aggregate_sum(rows, 'store_name', 'final_amount')

    stats = an.statistics_summary(rows, 'final_amount')
    corr = an.correlation(rows, 'final_amount', 'discount_amount')

    cleaned_path = OUT / 'imperative_clean.csv'
    region_path = OUT / 'imperative_region_sales.csv'
    outp.save_csv_rows(cleaned_path, rows)
    outp.save_csv_rows(region_path, region_sales, fieldnames=['store_name','final_amount'])

    viz.plot_line(rows, 'transaction_date', 'final_amount', save_path=str(OUT / 'imperative_sales_line.png'))
    viz.plot_bar(region_sales, 'store_name', 'final_amount', save_path=str(OUT / 'imperative_region_bar.png'))
    
    print('--- Imperative Pipeline Summary ---')
    print('Records after filter (final_amount>100):', len(rows))
    print('Statistics (Sales):', stats)
    print('Correlation final_amount vs discount_amount:', corr)
    print('Saved:', cleaned_path, region_path)

if __name__ == '__main__':
    run_imperative_pipeline()
