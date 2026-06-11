import pandas as pd

scheme = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

def recommend_funds(risk_level):

    filtered = scheme[
        scheme["risk_grade"].str.lower() == risk_level.lower()
    ]

    recommendations = filtered.sort_values(
        "sharpe_ratio",
        ascending=False
    ).head(3)

    return recommendations[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct"
        ]
    ]

print("Available Risk Grades:")
print(scheme["risk_grade"].unique())

risk = input(
    "\nEnter Risk Appetite (Low/Moderate/High): "
)

result = recommend_funds(risk)

print("\nTop 3 Recommended Funds")
print(result)