from pathlib import Path
import pandas as pd

from loader import load_csv
import processor as proc
import transformer as trans
import analyzer as an
import visualizer as viz

BASE = Path(__file__).resolve().parent
DATA = BASE.parent / 'grocery_chain_data.csv'
OUT = BASE / 'output'
OUT.mkdir(exist_ok=True)

def run_functional_pipeline():
    # Load
    df = load_csv(DATA)

    # --- FIXED COLUMN NAMES BASED ON YOUR DATASET ---
    SALES_COL = "final_amount"      
    EXPENSES_COL = "discount_amount"  
    DATE_COL = "transaction_date"
    REGION_COL = "store_name"
    # Functional transformations
    # Fill missing store_name with 'Unknown' and numeric columns with 0
    df1 = proc.handle_missing(df, strategy='fill', fill_value={'store_name': 'Unknown', 'final_amount': 0, 'discount_amount': 0})
    df2 = proc.standardize_date(df1, DATE_COL)
    df3 = proc.standardize_numbers(df2, [SALES_COL, EXPENSES_COL], decimals=2)

    # Transformations
    df4 = trans.compute_column(df3, 'Growth', SALES_COL, EXPENSES_COL, op='diff')
    df5 = trans.filter_rows(df4, SALES_COL, 100)  
    region_sales = trans.aggregate_sum(df5, REGION_COL, SALES_COL)

    # Analysis
    stats = an.statistics_summary(df5, SALES_COL)
    corr = an.correlation(df5, SALES_COL, EXPENSES_COL)

    # Output
    cleaned_path = OUT / 'functional_clean.csv'
    region_path = OUT / 'functional_region_sales.csv'
    df5.to_csv(cleaned_path, index=False)
    region_sales.to_csv(region_path, index=False)

    # Visualization
    try:
        viz.plot_line(
            df5.sort_values(DATE_COL),
            DATE_COL,
            SALES_COL,
            save_path=str(OUT / "functional_sales_line.png")
        )
        viz.plot_bar(
            region_sales,
            REGION_COL,
            SALES_COL,
            save_path=str(OUT / "functional_region_bar.png")
        )
    except Exception as e:
        print("Visualization skipped:", e)

    # Console summary
    print("\n--- Functional Pipeline Summary ---")
    print(f"Records after filter ({SALES_COL} > 100):", len(df5))
    print("Statistics (Sales):", stats)
    print("Correlation Sales vs Expenses:", corr)
    print("Saved:", cleaned_path, region_path)

if __name__ == '__main__':
    run_functional_pipeline()
