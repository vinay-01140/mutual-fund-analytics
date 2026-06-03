-- 1. Top 5 Funds by AUM
SELECT *
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV Per Month
SELECT strftime('%Y-%m', nav_date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- 3. SIP Transactions Count
SELECT COUNT(*) AS sip_count
FROM fact_transactions
WHERE transaction_type='Sip';

-- 4. Transactions by State
SELECT state,
COUNT(*) AS transactions
FROM fact_transactions
GROUP BY state
ORDER BY transactions DESC;

-- 5. Funds with Expense Ratio < 1%
SELECT amfi_code,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Top Fund Houses by AUM
SELECT fund_house,
SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC;

-- 7. Highest 1-Year Returns
SELECT amfi_code,
return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 10;

-- 8. Highest Sharpe Ratio Funds
SELECT amfi_code,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

-- 9. Transaction Type Distribution
SELECT transaction_type,
COUNT(*) AS total
FROM fact_transactions
GROUP BY transaction_type;

-- 10. Risk Category Distribution
SELECT risk_category,
COUNT(*) AS total_funds
FROM dim_fund
GROUP BY risk_category;
