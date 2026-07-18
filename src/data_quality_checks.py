import os
import pandas as pd

input_file = "data/investment_data_quality_tableau_dataset.xlsx"
output_file = "output/generated_exceptions.xlsx"

securities = pd.read_excel(
    input_file,
    sheet_name="Securities"
)

securities["Last_Updated_Date"] = pd.to_datetime(securities["Last_Updated_Date"], errors="coerce")

output_columns = [
    "Security_ID",
    "Ticker",
    "Security_Name",
    "Last_Updated_Date",
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

# Rule 5: Stale record (last updated date older than 90 days)

today = pd.Timestamp.today().normalize()
stale_threshold_days = 90

stale_records = securities[
    securities["Last_Updated_Date"].notna()
    & (
        today - securities["Last_Updated_Date"]
    ).dt.days.gt(stale_threshold_days)
].copy()

stale_records["Exception_Type"] = "Stale Record"
stale_records["Exception_Description"] = (
    "Record has not been updated for more than 90 days"
)
stale_records["Severity"] = "Medium"
stale_records["Status"] = "Open"

stale_record_exceptions = stale_records[output_columns]

# Combine all exceptions
exceptions = pd.concat(
    [
        missing_isin_exceptions,
        missing_currency_exceptions,
        missing_rating_exceptions,
        missing_sector_exceptions,
        stale_record_exceptions,
    ],
    ignore_index=True
)

os.makedirs("output", exist_ok=True)

exceptions.to_excel(
    output_file,
    index=False
)

print(f"Generated {len(exceptions)} exception records.")

total_unique_securities = exceptions["Security_ID"].nunique()

print(f"Total unique securities with exceptions: {total_unique_securities}")

print("\nUnique securities by exception type:")
print(
    exceptions.groupby("Exception_Type")["Security_ID"]
    .nunique()
    .sort_values(ascending=False)
)

print()
print(f"Saved to: {output_file}")



