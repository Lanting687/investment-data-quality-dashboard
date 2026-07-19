import pandas as pd

from . import config


# Rule 1: Missing ISIN
def missing_isin(securities):
    # Flags any security without an ISIN identifier.
    return securities[securities["ISIN"].isna()].copy()


# Rule 2: Missing Currency
def missing_currency(securities):
    # Flags any security without a settlement currency.
    return securities[
        securities["Currency"].isna()
    ].copy()


# Rule 3: Missing Credit Rating
def missing_credit_rating(securities):
    # Flags any security without a credit rating.
    return securities[
        securities["Credit_Rating"].isna()
    ].copy()


# Rule 4: Missing Sector
def missing_sector(securities):
    # Government bonds and derivatives are legitimately sector-less,
    # so they're excluded from this check rather than flagged.
    return securities[
        ~securities["Asset_Class"].isin(config.SECTOR_OPTIONAL_ASSET_CLASSES)
        & securities["Sector"].isna()
    ].copy()


# Rule 5: Stale record (last updated date older than 90 days)
def stale_records(securities):
    # Records with no update date at all are skipped here (not "stale"),
    # not flagged by this rule.
    today = pd.Timestamp.today().normalize()

    return securities[
        securities["Last_Updated_Date"].notna()
        & (
            today - securities["Last_Updated_Date"]
        ).dt.days.gt(config.STALE_THRESHOLD_DAYS)
    ].copy()


# Rule 6: Duplicate Record (same ISIN shared by more than one security)
def duplicate_isin(securities):
    # keep=False marks every row that shares its ISIN with another row,
    # not just the second occurrence onward.
    return securities[
        securities["ISIN"].notna()
        & securities["ISIN"].duplicated(keep=False)
    ].copy()
