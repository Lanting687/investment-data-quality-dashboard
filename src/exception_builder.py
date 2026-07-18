import pandas as pd

from . import config
from . import validation_rules as rules


def _to_exceptions(df, exception_type, exception_description, severity):
    df = df.copy()

    df["Exception_Type"] = exception_type
    df["Exception_Description"] = exception_description
    df["Severity"] = severity
    df["Status"] = "Open"

    return df[config.OUTPUT_COLUMNS]


def build_exceptions(securities):
    missing_isin_exceptions = _to_exceptions(
        rules.missing_isin(securities),
        "Missing ISIN",
        "ISIN is missing",
        "Medium",
    )

    missing_currency_exceptions = _to_exceptions(
        rules.missing_currency(securities),
        "Missing Currency",
        "Currency is missing",
        "High",
    )

    missing_rating_exceptions = _to_exceptions(
        rules.missing_credit_rating(securities),
        "Missing Rating",
        "Credit rating is missing",
        "Medium",
    )

    missing_sector_exceptions = _to_exceptions(
        rules.missing_sector(securities),
        "Missing Sector",
        "Sector is missing for an asset class that requires sector classification",
        "Medium",
    )

    stale_record_exceptions = _to_exceptions(
        rules.stale_records(securities),
        "Stale Record",
        "Record has not been updated for more than 90 days",
        "Medium",
    )

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

    return exceptions
