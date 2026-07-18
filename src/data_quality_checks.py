import os
import pandas as pd

input_file = "data/investment_data_quality_tableau_dataset.xlsx"

output_file = "output/generated_exceptions.xlsx"

securities = pd.read_excel(input_file, sheet_name="Securities")

missing_isin = securities[securities["ISIN"].isna()].copy()

missing_isin["Exception_Type"] = "Missing ISIN"
missing_isin["Exception_Description"] = "ISIN is missing"
missing_isin["Severity"] = "Medium"
missing_isin["Status"] = "Open"

exceptions = missing_isin[["Security_ID","Ticker", "Security_Name", "Exception_Type", "Exception_Description", "Severity", "Status",]]

os.makedirs("output", exist_ok=True)

exceptions.to_excel(output_file, index=False)

print(f"Generated {len(exceptions)} exceptions.")
print(f"Saved to: {output_file}")







