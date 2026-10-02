import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# CUSTOMER RETENTION & CHURN ANALYSIS
# FUTURE INTERNS - TASK 2
# ============================================

# 1. Load the CSV file
df = pd.read_csv("customer_churn.csv")

print("Dataset loaded successfully!")
print("Number of customers:", len(df))

# ============================================
# 2. CLEAN THE DATA
# ============================================

# Remove duplicate rows
df = df.drop_duplicates()

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Replace missing TotalCharges with 0
df["TotalCharges"] = df["TotalCharges"].fillna(0)

print("\nData cleaning completed.")

# ============================================
# 3. OVERALL CHURN ANALYSIS
# ============================================

total_customers = len(df)

churned = (df["Churn"] == "Yes").sum()
retained = (df["Churn"] == "No").sum()

churn_rate = churned / total_customers * 100
retention_rate = retained / total_customers * 100

print("\n========== CHURN ANALYSIS ==========")

print("Total Customers:", total_customers)
print("Churned Customers:", churned)
print("Retained Customers:", retained)

print("Churn Rate:", round(churn_rate, 2), "%")
print("Retention Rate:", round(retention_rate, 2), "%")

# ============================================
# 4. CUSTOMER LIFETIME
# ============================================

average_tenure = df["tenure"].mean()

churned_tenure = df[
    df["Churn"] == "Yes"
]["tenure"].mean()

retained_tenure = df[
    df["Churn"] == "No"
]["tenure"].mean()

print("\n========== CUSTOMER LIFETIME ==========")

print(
    "Average Tenure:",
    round(average_tenure, 2),
    "months"
)

print(
    "Average Tenure of Churned Customers:",
    round(churned_tenure, 2),
    "months"
)

print(
    "Average Tenure of Retained Customers:",
    round(retained_tenure, 2),
    "months"
)

# ============================================
# 5. CHURN BY CONTRACT
# ============================================

contract_table = pd.crosstab(
    df["Contract"],
    df["Churn"]
)

print("\n========== CHURN BY CONTRACT ==========")
print(contract_table)

# Calculate churn percentage by contract
contract_rate = pd.crosstab(
    df["Contract"],
    df["Churn"],
    normalize="index"
) * 100

print("\nChurn Percentage by Contract:")
print(contract_rate.round(2))

# ============================================
# 6. CHURN BY INTERNET SERVICE
# ============================================

internet_table = pd.crosstab(
    df["InternetService"],
    df["Churn"]
)

print("\n========== CHURN BY INTERNET SERVICE ==========")
print(internet_table)

# ============================================
# 7. CHURN BY PAYMENT METHOD
# ============================================

payment_table = pd.crosstab(
    df["PaymentMethod"],
    df["Churn"]
)

print("\n========== CHURN BY PAYMENT METHOD ==========")
print(payment_table)

# ============================================
# 8. MONTHLY CHARGES
# ============================================

churned_charge = df[
    df["Churn"] == "Yes"
]["MonthlyCharges"].mean()

retained_charge = df[
    df["Churn"] == "No"
]["MonthlyCharges"].mean()

print("\n========== MONTHLY CHARGES ==========")

print(
    "Average Monthly Charges - Churned:",
    round(churned_charge, 2)
)

print(
    "Average Monthly Charges - Retained:",
    round(retained_charge, 2)
)

# ============================================
# 9. CHART 1 - CHURN DISTRIBUTION
# ============================================

churn_count = df["Churn"].value_counts()

plt.figure(figsize=(6, 4))

plt.bar(
    churn_count.index,
    churn_count.values
)

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

# ============================================
# 10. CHART 2 - CHURN BY CONTRACT
# ============================================

contract_table.plot(
    kind="bar",
    figsize=(7, 5)
)

plt.title("Customer Churn by Contract")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ============================================
# 11. CHART 3 - CHURN BY INTERNET SERVICE
# ============================================

internet_table.plot(
    kind="bar",
    figsize=(7, 5)
)

plt.title("Customer Churn by Internet Service")
plt.xlabel("Internet Service")
plt.ylabel("Number of Customers")

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ============================================
# 12. CHART 4 - TENURE OF CHURNED CUSTOMERS
# ============================================

plt.figure(figsize=(7, 5))

plt.hist(
    df[df["Churn"] == "Yes"]["tenure"],
    bins=20
)

plt.title("Tenure of Churned Customers")
plt.xlabel("Tenure (Months)")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

# ============================================
# 13. CHART 5 - MONTHLY CHARGES OF CHURNED
# ============================================

plt.figure(figsize=(7, 5))

plt.hist(
    df[df["Churn"] == "Yes"]["MonthlyCharges"],
    bins=20
)

plt.title("Monthly Charges of Churned Customers")
plt.xlabel("Monthly Charges")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

# ============================================
# 14. BUSINESS INSIGHTS
# ============================================

print("\n========== BUSINESS INSIGHTS ==========")

print(
    "1. The overall customer churn rate is",
    round(churn_rate, 2),
    "%."
)

print(
    "2. The overall customer retention rate is",
    round(retention_rate, 2),
    "%."
)

print(
    "3. Churned customers have an average tenure of",
    round(churned_tenure, 2),
    "months."
)

print(
    "4. Retained customers have an average tenure of",
    round(retained_tenure, 2),
    "months."
)

print(
    "5. Contract type is an important factor to analyze "
    "for customer retention."
)

print(
    "6. Internet service type shows differences in "
    "customer churn behaviour."
)

print(
    "7. Payment method can be analyzed to identify "
    "customer groups with higher churn."
)

print(
    "8. Customers with shorter tenure should receive "
    "early retention support."
)

print(
    "9. Monthly charges should be monitored because "
    "pricing may influence customer churn."
)

print(
    "10. The company can use these findings to design "
    "targeted customer retention strategies."
)

# ============================================
# 15. SAVE CLEANED DATA
# ============================================

df.to_csv(
    "cleaned_customer_churn.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")

print("\n========== ANALYSIS COMPLETED ==========")