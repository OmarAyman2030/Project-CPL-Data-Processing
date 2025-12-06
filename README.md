# Data Processing Pipeline Project

This project contains two implementations of the same data-processing pipeline using **Python**:

1. **Functional paradigm** (`functional_pipeline/`): Uses pandas and pure-style functions (no in-place mutation).
2. **Imperative paradigm** (`imperative_pipeline/`): Uses built-in `csv` and lists/dicts with explicit loops and mutations.

## How to run

Requirements (for functional version):
- Python 3.8+
- pandas, matplotlib

Install requirements (optional):
```
pip install pandas matplotlib
```

Run functional version:
```
cd functional_pipeline
python main.py
```

Run imperative version (no extra packages required):
```
cd imperative_pipeline
python main.py
```

## What each pipeline does

- Loads `../data.csv`
- Handles missing values (fill or drop)
- Standardizes date and numeric formats
- Computes a `Growth = Sales - Expenses` column
- Filters rows where `Sales > 1000`
- Aggregates total sales per `Region`
- Produces summary statistics and correlation
- Saves cleaned CSV and aggregation CSV to `output/` folders

## Files included
- `data.csv` : sample dataset
- `functional_pipeline/` : pandas-based functional implementation
- `imperative_pipeline/` : csv + loops imperative implementation

You can modify `data.csv` and re-run both pipelines to test different cases.
