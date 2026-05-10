# Customer Retention & Revenue Leakage Analysis (Telecom Churn)

## 📌 Project Overview

This project focuses on analyzing customer churn and revenue leakage in a telecom subscription business. The objective is to identify key churn drivers, understand revenue impact, segment high-value customers, and provide actionable retention strategies using data analytics and business intelligence techniques.

The project follows an end-to-end analytics workflow using:

- Python for data cleaning and feature engineering  
- MySQL for business-driven SQL analysis  
- Power BI for interactive dashboarding  
- Excel for quick validation and pivot analysis  

---

## 🎯 Business Problem

Subscription-based businesses often face customer churn, which directly impacts revenue and growth.

This project aims to answer:

- Why are customers churning?  
- Which customers are most valuable?  
- How much revenue is being lost?  
- What actions can reduce churn?  

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|--------|
| Python (Pandas, NumPy) | Data cleaning & feature engineering |
| MySQL | SQL analysis & business queries |
| Power BI | Dashboard & storytelling |
| VS Code | Development environment |

---

## 🔄 Pipeline Flow

Raw CSV Data  
→ Python Data Cleaning  
→ Feature Engineering  
→ Export Cleaned Data  
→ Load into MySQL  
→ SQL Business Analysis  
→ Power BI Dashboard  
→ Insights & Recommendations  

---

## ⚙️ Data Preparation (Python)

### ✔ Tasks Performed

- Handled missing values  
- Fixed incorrect data types  
- Standardized categorical values  
- Removed inconsistencies  

### ✔ Feature Engineering

- **Customer Lifetime Value (CLV)**  
  CLV = MonthlyCharges × Tenure  

- **Tenure Groups**
  - 0–6 months  
  - 6–12 months  
  - 12–24 months  
  - 24+ months  

- Revenue proxy using Monthly Charges  

---

## 🧮 SQL Analysis

Business-driven SQL queries were used for insights:

### ✔ Churn Analysis
- Churn by contract type  
- Churn by payment method  
- Churn by tenure group  

### ✔ Revenue Analysis
- Revenue from churned customers  
- Total revenue loss estimation  
- Top revenue-generating customers  

### ✔ Customer Segmentation
- High-value customer identification  
- High-risk customer analysis  
- Ranking using window functions  

---

## 📊 Power BI Dashboard

The dashboard includes:

- KPI overview  
- Churn driver analysis  
- Revenue impact visualization  
- Customer segmentation insights  
- Business recommendations  

---

## 🔍 Key Insights

- Monthly contracts show the highest churn rate  
- Early-tenure customers are more likely to churn  
- Electronic check users have higher churn probability  
- High-value customers contribute most revenue but are at risk  

---

## 💡 Recommendations

- Promote long-term contracts with incentives  
- Improve onboarding experience for new users  
- Encourage automatic payment methods  
- Focus retention on high-value customers  
- Run targeted churn prevention campaigns  

---

## 📚 Learning Outcomes

- End-to-end data pipeline development  
- Business-focused SQL analysis  
- Dashboard storytelling using Power BI  
- Translating data into actionable business insights  
- Real-world analytics workflow design  

---

## 📈 Future Improvements

- Predictive churn modeling using Machine Learning  
- Real-time dashboard integration  
- Automated reporting pipeline  
- Advanced customer segmentation models  

---

## ⚠️ Disclaimer

This project is created strictly for **educational and learning purposes only**.

All data used is assumed to be from publicly available or simulated telecom datasets and is used solely for analytical practice.

- No personal or sensitive customer data is used  
- The project is not intended for commercial use  
- All insights are for demonstration and learning purposes only  
- Any resemblance to real business data is purely coincidental  

---

## 🏁 Conclusion

This project demonstrates an end-to-end analytics workflow focused on solving a real-world business problem using data.

It combines **Python, SQL, and Power BI** to transform raw telecom customer data into actionable insights for customer retention and revenue optimization.