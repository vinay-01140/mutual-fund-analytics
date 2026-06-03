import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

tables = [
    "dim_fund",
    "dim_date",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum"
]

for table in tables:

    query = f"SELECT COUNT(*) as rows FROM {table}"

    count = pd.read_sql(
        query,
        engine
    )

    print(table)
    print(count)
    print("-" * 40)