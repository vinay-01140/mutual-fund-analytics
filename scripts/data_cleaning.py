import pandas as pd
import os

raw_path = "data/raw"
processed_path = "data/processed"

# NAV HISTORY

nav = pd.read_csv(
    os.path.join(raw_path,
    "02_nav_history.csv")
)

nav["date"] = pd.to_datetime(
    nav["date"]
)

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav = nav.drop_duplicates()

nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

nav = nav[nav["nav"] > 0]

nav.to_csv(
    os.path.join(
        processed_path,
        "02_nav_history_cleaned.csv"
    ),
    index=False
)

print("NAV cleaned")

# INVESTOR TRANSACTIONS

txn = pd.read_csv(
    os.path.join(
        raw_path,
        "08_investor_transactions.csv"
    )
)

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
    .str.title()
)

txn = txn[
    txn["amount_inr"] > 0
]

print(
    txn["kyc_status"].unique()
)

txn.to_csv(
    os.path.join(
        processed_path,
        "08_investor_transactions_cleaned.csv"
    ),
    index=False
)

print("Transactions cleaned")

# SCHEME PERFORMANCE

perf = pd.read_csv(
    os.path.join(
        raw_path,
        "07_scheme_performance.csv"
    )
)

returns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in returns:

    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

anomalies = perf[
    (perf["expense_ratio_pct"] < 0.1)
    |
    (perf["expense_ratio_pct"] > 2.5)
]

anomalies.to_csv(
    os.path.join(
        processed_path,
        "performance_anomalies.csv"
    ),
    index=False
)

perf.to_csv(
    os.path.join(
        processed_path,
        "07_scheme_performance_cleaned.csv"
    ),
    index=False
)

print("Performance cleaned")
other_files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in other_files:

    df = pd.read_csv(f"data/raw/{file}")

    df = df.drop_duplicates()

    df = df.dropna(how="all")

    output_name = file.replace(
        ".csv",
        "_cleaned.csv"
    )

    df.to_csv(
        f"data/processed/{output_name}",
        index=False
    )

    print(output_name, "cleaned")