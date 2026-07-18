import os

from . import config


def write_exceptions(exceptions, output_file=config.OUTPUT_FILE):
    os.makedirs("output", exist_ok=True)

    exceptions.to_excel(
        output_file,
        index=False
    )


def print_summary(exceptions, output_file=config.OUTPUT_FILE):
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
