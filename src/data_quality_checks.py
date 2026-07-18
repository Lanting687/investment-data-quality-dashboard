import os
import pandas as pd

input_file = "data/investment_data_quality_tableau_dataset.xlsx"
output_file = "output/generated_exceptions.xlsx"

securities = pd.read_excel(
    input_file,
    sheet_name="Securities"
)

output_columns = [
    "Security_ID",
    "Ticker",
    "Security_Name",
    "Exception_Type",
    "Exception_Description",
    "Severity",
    "Status",
]


# Rule 1: Missing ISIN
missing_isin = securities[securities["ISIN"].isna()].copy()

missing_isin["Exception_Type"] = "Missing ISIN"
missing_isin["Exception_Description"] = "ISIN is missing"
missing_isin["Severity"] = "Medium"
missing_isin["Status"] = "Open"

missing_isin_exceptions = missing_isin[output_columns]


# Rule 2: Missing Currency
missing_currency = securities[
    securities["Currency"].isna()
].copy()

missing_currency["Exception_Type"] = "Missing Currency"
missing_currency["Exception_Description"] = "Currency is missing"
missing_currency["Severity"] = "High"
missing_currency["Status"] = "Open"

missing_currency_exceptions = missing_currency[output_columns]


# Rule 3: Missing Credit Rating
missing_rating = securities[
    securities["Credit_Rating"].isna()
].copy()

missing_rating["Exception_Type"] = "Missing Rating"
missing_rating["Exception_Description"] = "Credit rating is missing"
missing_rating["Severity"] = "Medium"
missing_rating["Status"] = "Open"

missing_rating_exceptions = missing_rating[output_columns]


# Rule 4: Missing Sector
missing_sector = securities[
    securities["Sector"].isna()
].copy()

missing_sector["Exception_Type"] = "Missing Sector"
missing_sector["Exception_Description"] = "Sector is missing"
missing_sector["Severity"] = "Medium"
missing_sector["Status"] = "Open"

missing_sector_exceptions = missing_sector[output_columns]


# Combine all exceptions
exceptions = pd.concat(
    [
        missing_isin_exceptions,
        missing_currency_exceptions,
        missing_rating_exceptions,
        missing_sector_exceptions,
    ],
    ignore_index=True
)

os.makedirs("output", exist_ok=True)

exceptions.to_excel(
    output_file,
    index=False
)

print(f"Generated {len(exceptions)} exceptions.")
print()
print(exceptions["Exception_Type"].value_counts())
print()
print(f"Saved to: {output_file}")
