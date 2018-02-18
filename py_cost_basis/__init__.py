"""
"""


def compute():
    """Entry point for the application script"""

    import sys
    import argparse
    import json
    from functools import partial

    import argcomplete

    from py_cost_basis.cost_basis_tools import cost_basis

    description = "Cost Basis calculations"
    parser = argparse.ArgumentParser(usage=None, description=description)

    parser.add_argument(
        "-m",
        "--cost-basis-method",
        type=str,
        choices=[
            "average",
            "LIFO",
            "FIFO",
            "HCFO",
            "LCFO",
        ],
        default="average",
        help=("method to use when computing cost basis.")
    )

    parser.add_argument(
        "-i",
        "--input-files",
        type=str,
        nargs="*",
        help=("any number of files containing transactions.")
    )

    parser.add_argument("-o", "--output-file", type=str)

    argcomplete.autocomplete(parser)
    args = parser.parse_args()

    return cost_basis("sells", "buys", args.cost_basis_method)


def ingest():
    """Entry point for the application script"""

    import sys
    import argparse
    import json
    from functools import partial

    import argcomplete

    from py_cost_basis.data_ingest_tools import base_load_transactions

    description = "ingest data from various sources"
    parser = argparse.ArgumentParser(usage=None, description=description)

    parser.add_argument(
        "-i",
        "--input-files",
        type=str,
        nargs="*",
        help=("any number of files containing transactions.")
    )

    parser.add_argument("-o", "--output-directory", type=str)

    argcomplete.autocomplete(parser)
    args = parser.parse_args()

    for t in base_load_transactions(*args.input_files):
        print(json.dumps(t))

    return None


def dedup():
    """Entry point for the application script"""

    import sys
    import argparse
    import json
    from functools import partial

    import argcomplete

    description = "dedup transactions"
    parser = argparse.ArgumentParser(usage=None, description=description)

    parser.add_argument(
        "-i",
        "--input-files",
        type=str,
        nargs="*",
        help=("any number of files containing transactions.")
    )

    parser.add_argument("-o", "--output-file", type=str)

    argcomplete.autocomplete(parser)
    args = parser.parse_args()
