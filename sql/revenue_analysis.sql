-- Revenue Loss Analysis
SELECT 
    SUM(MonthlyCharges) AS total_revenue,
    SUM(CASE WHEN Churn = 'Yes' THEN MonthlyCharges ELSE 0 END) AS churned_revenue,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN MonthlyCharges ELSE 0 END) * 100.0 
        / SUM(MonthlyCharges),
        2
    ) AS revenue_loss_percentage
FROM customers;


-- Top Customers by CLV
SELECT *
FROM (
    SELECT 
        customerID,
        CLV,
        RANK() OVER (ORDER BY CLV DESC) AS rank_clv
    FROM customers
) ranked
WHERE rank_clv <= 10;