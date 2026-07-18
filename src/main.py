from .data_loader import load_securities
from .exception_builder import build_exceptions
from .report_writer import write_exceptions, print_summary


def main():
    securities = load_securities()
    exceptions = build_exceptions(securities)

    write_exceptions(exceptions)
    print_summary(exceptions)


if __name__ == "__main__":
    main()
