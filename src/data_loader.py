import pandas as pd

from . import config


def load_securities(input_file=config.INPUT_FILE, sheet_name=config.SHEET_NAME):
    securities = pd.read_excel(
        input_file,
        sheet_name=sheet_name
    )

    securities["Last_Updated_Date"] = pd.to_datetime(
        securities["Last_Updated_Date"], errors="coerce"
    )

    return securities
