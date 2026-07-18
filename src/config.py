INPUT_FILE = "data/investment_data_quality_tableau_dataset.xlsx"
OUTPUT_FILE = "output/generated_exceptions.xlsx"
SHEET_NAME = "Securities"

OUTPUT_COLUMNS = [
    "Security_ID",
    "Ticker",
    "Security_Name",
    "Last_Updated_Date",
    "Exception_Type",
    "Exception_Description",
    "Severity",
    "Status",
]

SECTOR_OPTIONAL_ASSET_CLASSES = [
    "Government Bond",
    "Derivative",
]

STALE_THRESHOLD_DAYS = 90
