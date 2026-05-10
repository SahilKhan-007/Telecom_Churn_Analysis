-- Customer Segmentation
SELECT 
    customerID,
    CLV,
    NTILE(4) OVER (ORDER BY CLV DESC) AS segment
FROM customers;


-- High-Risk Customers
SELECT 
    customerID,
    CLV,
    MonthlyCharges,
    Contract,
    PaymentMethod
FROM customers
WHERE Churn = 'Yes'
AND CLV > (
    SELECT AVG(CLV) FROM customers
)
ORDER BY CLV DESC;