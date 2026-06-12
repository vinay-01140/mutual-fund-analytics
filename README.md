# Mutual Fund Analytics Capstone Project

## Overview

This project is an end-to-end Mutual Fund Analytics solution developed as part of the Bluestock Capstone Program. The objective is to analyze mutual fund performance, investor behavior, portfolio composition, and industry trends using data analytics, financial metrics, and interactive dashboards.

The project covers the complete analytics lifecycle, including data ingestion, cleaning, exploratory data analysis (EDA), performance analytics, advanced risk analysis, database management, and Power BI dashboard development.


## Project Objectives

* Build a complete ETL pipeline for mutual fund datasets.
* Clean and standardize data from multiple sources.
* Perform exploratory data analysis (EDA).
* Analyze mutual fund performance using financial metrics.
* Study investor demographics and transaction behavior.
* Develop advanced analytics models for risk and portfolio evaluation.
* Create interactive Power BI dashboards.
* Generate actionable insights from mutual fund data.


## Technology Stack

### Programming & Analytics

* Python
* Pandas
* NumPy
* Matplotlib

### Database

* SQLite

### Visualization

* Power BI

### Development Tools

* Jupyter Notebook
* VS Code
* Git & GitHub


## Project Structure

```text
MUTUAL-FUND-ANALYTICS/

├── charts/
│   ├── age_group_distribution.png
│   ├── aum_growth.png
│   ├── category_heatmap.png
│   ├── equity_vs_debt_folio.png
│   ├── folio_growth.png
│   ├── nav_trend.png
│   ├── sector_allocation.png
│   ├── sip_monthly_trend.png
│   └── state_distribution.png
│
├── dashboard/
│   ├── bluestock_mf_dashboard.pbix
│   └── bluestock_mf_dashboard.pdf
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── 06_monte_carlo_simulation.ipynb
│
├── reports/
│   ├── data_dictionary.md
│   └── day1_data_quality.md
│
├── screenshots/
│   ├── Page1_IndustryOverview.png
│   ├── Page2_FundPerformance.png
│   ├── Page3_InvestorAnalytics.png
│   └── Page4_SIPMarketTrends.png
│
├── scripts/
│   ├── data_ingestion.py
│   ├── data_cleaning.py
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   └── verify_counts.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── Advanced_Analytics.ipynb
├── recommender.py
├── amfi_validation.py
├── fund_master_analysis.py
├── requirements.txt
├── rolling_sharpe_chart.png
├── var_cvar_report.csv
└── README.md
```


## Datasets Used

The project uses multiple datasets covering different aspects of the mutual fund ecosystem.

1. Fund Master Dataset
2. NAV History Dataset
3. AUM by Fund House Dataset
4. Monthly SIP Inflows Dataset
5. Category Inflows Dataset
6. Industry Folio Count Dataset
7. Scheme Performance Dataset
8. Investor Transactions Dataset
9. Portfolio Holdings Dataset
10. Benchmark Indices Dataset


## ETL Pipeline

The project follows a structured ETL process.

### Extract

* Loaded raw CSV datasets.
* Validated dataset structure and AMFI codes.

### Transform

* Removed duplicate records.
* Handled missing values.
* Standardized date formats.
* Renamed columns for consistency.
* Validated data types.
* Created derived analytical datasets.

### Load

* Stored cleaned datasets in processed CSV files.
* Loaded data into SQLite for validation and analysis.

### Pipeline Flow

Raw Data

↓

Data Cleaning & Validation

↓

Processed Data

↓

SQLite Database

↓

EDA & Analytics

↓

Dashboard & Reports


## Exploratory Data Analysis

The EDA phase focused on understanding industry growth, investor participation, and fund performance.

### Visualizations Created

* Daily NAV Trend
* Top 10 Funds by NAV
* AUM Growth Analysis
* Monthly SIP Inflow Trend
* SIP YoY Growth Analysis
* Category Inflow Heatmap
* Age Group Distribution
* Gender Distribution
* State-wise Distribution
* Equity vs Debt Analysis
* T30 vs B30 Analysis
* Folio Growth Trend
* NAV Correlation Matrix
* Sector Allocation Analysis

### Key Findings

* Most schemes exhibited a consistent upward NAV trend.
* SBI Mutual Fund maintained the highest AUM.
* Monthly SIP inflows reached approximately ₹31,000 Crore.
* Investors aged 25–40 represented the largest investor segment.
* Liquid Funds attracted the highest category inflows.
* Equity-oriented funds dominated investor participation.

## Performance Analytics

Several performance metrics were implemented to evaluate mutual fund schemes.

### Metrics Calculated

* Daily Returns
* CAGR
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* Tracking Error
* Fund Scorecard

### Key Findings

* Multiple funds generated strong long-term CAGR values.
* Funds 100033 and 101206 achieved Sharpe Ratios above 1.
* Several schemes produced positive Alpha values.
* Drawdown analysis highlighted varying levels of downside risk.
* Fund 119598 achieved the highest composite score.


## Advanced Analytics

### Historical VaR & CVaR

Calculated downside risk using daily return distributions at a 95% confidence level.

### Rolling 90-Day Sharpe Ratio

Evaluated changes in risk-adjusted performance over time.

### Investor Cohort Analysis

Grouped investors based on first transaction year and analyzed investment behavior.

### SIP Continuity Analysis

Identified investors at risk of discontinuing SIP investments.

### Fund Recommendation System

Created a simple rule-based recommender that suggests top funds based on investor risk appetite.

### Sector HHI Concentration Analysis

Measured portfolio concentration using the Herfindahl-Hirschman Index (HHI).


## Bonus Challenge Completed

### B3 – Monte Carlo Simulation

Implemented a Monte Carlo Simulation model to project future NAV growth over a five-year horizon.

Features:

* 100 simulation paths
* Volatility-based forecasting
* Scenario analysis
* Long-term NAV projection

The simulation demonstrates how uncertainty and market volatility can impact future mutual fund performance.


## Power BI Dashboard

The dashboard contains four interactive pages.

### Page 1 – Industry Overview

* Industry Folios
* SIP Inflows
* Industry AUM Trend
* AUM by AMC

### Page 2 – Fund Performance

* Return vs Risk Analysis
* Fund Scorecard
* NAV vs Benchmark

### Page 3 – Investor Analytics

* State-wise Investments
* Transaction Trends
* Investment Type Distribution
* Age Group Analysis

### Page 4 – SIP & Market Trends

* SIP Inflow Trend
* Nifty 50 Trend
* Category Inflow Heatmap
* Top Categories by Net Inflow


## Future Improvements

Potential future enhancements include:

* Real-time NAV integration
* Automated ETL scheduling
* Streamlit web application
* Machine Learning based recommendations
* Cloud deployment
* Live dashboard refresh


## Conclusion

This project demonstrates the practical application of data engineering, financial analytics, and business intelligence techniques in the mutual fund industry. Through ETL pipelines, performance analytics, advanced risk analysis, and interactive dashboards, the project provides meaningful insights into fund performance, investor behavior, and market trends.


## Author

Viyyapu Vinay
mail: viyyapuvinay939@gmail.com
