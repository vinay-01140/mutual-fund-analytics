import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

Path("data/db").mkdir(parents=True, exist_ok=True)

engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

# DIM FUND

fund = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

dim_fund = fund[
    [
        "amfi_code",
        "fund_house",
        "scheme_name",
        "category",
        "sub_category",
        "risk_category"
    ]
]

dim_fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

# DIM DATE

nav = pd.read_csv(
    "data/processed/02_nav_history_cleaned.csv"
)

nav["date"] = pd.to_datetime(
    nav["date"]
)

dim_date = pd.DataFrame()

dim_date["full_date"] = (
    nav["date"]
    .drop_duplicates()
    .sort_values()
)

dim_date["date_key"] = (
    dim_date["full_date"]
    .dt.strftime("%Y%m%d")
    .astype(int)
)

dim_date["year"] = dim_date["full_date"].dt.year
dim_date["quarter"] = dim_date["full_date"].dt.quarter
dim_date["month"] = dim_date["full_date"].dt.month
dim_date["day"] = dim_date["full_date"].dt.day

dim_date = dim_date[
    [
        "date_key",
        "full_date",
        "year",
        "quarter",
        "month",
        "day"
    ]
]

dim_date.to_sql(
    "dim_date",
    engine,
    if_exists="replace",
    index=False
)

# FACT NAV

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

# FACT TRANSACTIONS

txn = pd.read_csv(
    "data/processed/08_investor_transactions_cleaned.csv"
)

txn.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)
# FACT PERFORMANCE

perf = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

# FACT AUM

aum = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("Database Loaded Successfully")