# Data Processing Pipeline - Requirements Analysis

## Project Goal
Implement a data processing pipeline **twice** — once using **Functional Programming** and once using **Imperative Programming** — to process CSV data and produce cleaned outputs with analysis and visualizations.

---

## Requirements Checklist

### ✅ 1. Load Data from Sources (CSV)
| Component | Functional | Imperative | Status |
|-----------|-----------|-----------|--------|
| `loader.py` - Load CSV | ✅ Present | ✅ Present | **COMPLETE** |
| Handles CSV parsing | ✅ Yes | ✅ Yes | **COMPLETE** |

**Current Implementation:**
- Both use Python's `csv` module or `pd.read_csv()`
- Returns data as DataFrame (functional) or list of dicts (imperative)

---

### ✅ 2. Handle Missing Data
| Feature | Functional | Imperative | Status |
|---------|-----------|-----------|--------|
| Fill with defaults | ✅ Yes | ✅ Yes | **COMPLETE** |
| Remove rows with NA | ✅ Yes (drop strategy) | ✅ Yes (drop strategy) | **COMPLETE** |
| Column-specific fills | ✅ Yes (dict fill_value) | ✅ Yes (scalar fill) | **WORKING** |

**Current Implementation:**
```python
# Functional - supports dict fills
handle_missing(df, strategy='fill', fill_value={'store_name': 'Unknown', 'final_amount': 0})

# Imperative - supports scalar fills
handle_missing(rows, strategy='fill', fill_value='Unknown')
```

**Note:** Currently returns **1980 rows** (same as input) because missing values are filled, not dropped.

---

### ✅ 3. Standardize Formats
| Standardization | Functional | Imperative | Status |
|-----------------|-----------|-----------|--------|
| Date formatting | ✅ Yes | ✅ Yes | **COMPLETE** |
| Numerical precision | ✅ Yes (decimals=2) | ✅ Yes (decimals=2) | **COMPLETE** |

**Current Implementation:**
- `standardize_date()`: Converts to datetime format (default: `'%Y-%m-%d'`)
- `standardize_numbers()`: Rounds to specified decimals

---

### ✅ 4. Data Transformation
| Transformation | Functional | Imperative | Status |
|-----------------|-----------|-----------|--------|
| **Filter rows** (e.g., final_amount > 100) | ✅ Yes | ✅ Yes | **COMPLETE** |
| **Compute columns** (e.g., Growth = Sales - Expenses) | ✅ Yes | ✅ Yes | **COMPLETE** |
| **Aggregate data** (e.g., sum sales per region) | ✅ Yes | ✅ Yes | **COMPLETE** |

**Current Implementation:**
- `filter_rows(df, 'final_amount', 100)` → Returns **131 rows** (only high-value transactions)
- `compute_column(df, 'Growth', 'final_amount', 'discount_amount', op='diff')` → New column created
- `aggregate_sum(df, 'store_name', 'final_amount')` → 10 unique stores with totals

---

### ✅ 5. Data Analysis
| Analysis Type | Functional | Imperative | Status |
|-----------------|-----------|-----------|--------|
| Statistical summaries (mean, median, variance, min, max) | ✅ Yes | ✅ Yes | **COMPLETE** |
| Correlation analysis | ✅ Yes | ✅ Yes | **COMPLETE** |

**Current Implementation:**
- `statistics_summary()`: Returns dict with count, mean, median, variance, min, max
- `correlation()`: Calculates Pearson correlation between two columns

**Sample Output:**
```
{
  'count': 131,
  'mean': 117.66,
  'median': 115.47,
  'variance': 175.55,
  'min': 100.02,
  'max': 147.91
}
Correlation: -0.195
```

---

### ✅ 6. Data Visualization (Optional but Implemented)
| Chart Type | Functional | Imperative | Status |
|------------|-----------|-----------|--------|
| Line charts (sales over time) | ✅ Yes | ✅ Yes | **COMPLETE** |
| Bar charts (sales by region) | ✅ Yes | ✅ Yes | **COMPLETE** |

**Current Implementation:**
- `plot_line()`: Time-series visualization
- `plot_bar()`: Category comparison visualization
- Both save to PNG files

**Output Files Generated:**
- `functional_sales_line.png` ✅
- `functional_region_bar.png` ✅
- `imperative_sales_line.png` ✅
- `imperative_region_bar.png` ✅

---

### ✅ 7. Output Results
| Output Type | Functional | Imperative | Status |
|------------|-----------|-----------|--------|
| Save clean CSV | ✅ Yes | ✅ Yes | **COMPLETE** |
| Save aggregated data CSV | ✅ Yes | ✅ Yes | **COMPLETE** |
| Console summary | ✅ Yes | ✅ Yes | **COMPLETE** |

**Current Implementation:**
- `functional_clean.csv` (131 filtered rows) ✅
- `functional_region_sales.csv` (10 region aggregates) ✅
- `imperative_clean.csv` (131 filtered rows) ✅
- `imperative_region_sales.csv` (10 region aggregates) ✅

---

## Row Count Explanation

### Why Different Row Counts?

```
Original Dataset:     1980 rows
                        ↓
After handle_missing: 1980 rows (all missing values FILLED, not dropped)
                        ↓
After filter_rows:     131 rows (only transactions with final_amount > 100)
                        ↓
After aggregate_sum:    10 rows (grouped by store_name)
```

### Important: What "handle_missing" Should Do

According to the requirements:
- **"Handle missing data (e.g., fill with defaults or remove)"**

This means you have **two choices**:

#### Option A: FILL (Current Implementation)
```python
handle_missing(df, strategy='fill', fill_value='Unknown')
# Result: 1980 rows (preserves all original rows with NAs replaced)
```
**Use case:** When you want to preserve all data but handle missing values.

#### Option B: DROP (Alternative)
```python
handle_missing(df, strategy='drop')
# Result: ~1955 rows (removes rows with ANY missing value)
```
**Use case:** When you want only complete records.

---

## Current Architecture

### Functional Pipeline (`functional_pipeline/`)
- **Paradigm:** Pure functional (uses pandas DataFrames, immutable operations)
- **Data Structure:** DataFrame
- **Flow:** Load → Fill NA → Standardize → Transform → Analyze → Visualize → Output

### Imperative Pipeline (`imperative_pipeline/`)
- **Paradigm:** Imperative (uses lists of dicts, mutable operations)
- **Data Structure:** List of dictionaries
- **Flow:** Load → Fill NA → Standardize → Transform → Analyze → Visualize → Output

Both pipelines:
✅ Use identical logic and column names
✅ Produce identical results (131 rows after filtering)
✅ Implement all required features
✅ Follow their respective programming paradigms

---

## Summary: Does Your Code Meet Requirements?

| Requirement | ✅ Met? | Notes |
|------------|--------|-------|
| Implement twice (Functional + Imperative) | ✅ YES | Both pipelines implemented |
| Load CSV data | ✅ YES | `loader.py` in both |
| Handle missing values | ✅ YES | Fill or drop strategies |
| Standardize formats | ✅ YES | Dates and numbers |
| Filter rows by condition | ✅ YES | `filter_rows(df, col, threshold)` |
| Compute new columns | ✅ YES | `compute_column()` |
| Aggregate by key | ✅ YES | `aggregate_sum()` |
| Statistical analysis | ✅ YES | Mean, median, variance, etc. |
| Correlation analysis | ✅ YES | Pearson correlation |
| Data visualization | ✅ YES | Line and bar charts |
| Output to CSV | ✅ YES | Clean data + aggregates |
| Console summary | ✅ YES | Both print summaries |

---

## **VERDICT: ✅ PROJECT REQUIREMENTS ARE MET**

Your code structure correctly implements the data processing pipeline project requirements using both functional and imperative paradigms.

### What the correct row counts should be:

1. **After `handle_missing()` (fill strategy):** **1980 rows** ← All data preserved
2. **After `filter_rows()` (>100):** **131 rows** ← Expected for this dataset
3. **After `aggregate_sum()` by region:** **10 rows** ← Unique stores

If you want to return **1980 rows** at the end (no filtering), modify:
```python
# Change this line in main.py:
rows = trans.filter_rows(rows, 'final_amount', 100)  # ← Remove this

# Then you'll have all 1980 rows but filtered data is lost
```

But based on the requirements, filtering is necessary for meaningful analysis!

