import pandas as pd

# Load raw data
sales = pd.read_csv("../raw_data/sales.csv")
expenses = pd.read_csv("../raw_data/expenses.csv")
tax_rates = pd.read_csv("../raw_data/tax_rates.csv")

# Merge sales with tax rates
sales_tax = pd.merge(sales, tax_rates, on="region", how="left")

# Tax calculations
sales_tax["tax_amount"] = sales_tax["revenue"] * sales_tax["tax_rate"]
sales_tax["net_revenue"] = sales_tax["revenue"] - sales_tax["tax_amount"]

# Merge with expenses
final_df = pd.merge(sales_tax, expenses, on="region", how="left")

# Profit calculation
final_df["profit"] = final_df["net_revenue"] - final_df["expense_amount"]

# Data quality check
assert final_df.isnull().sum().sum() == 0

# Save final output
final_df.to_csv("../output/final_tax_report.csv", index=False)

print("✅ Tax Automation Pipeline Executed Successfully")
