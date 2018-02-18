import csv
import json


def base_load_transactions(*args):
    for csv_file in args:
        try:
            yield from load_csv_file(csv_file)
        except Exception as e:
            raise


def load_csv_file(csv_file):

    with open(csv_file, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(
            (row for row in csvfile if not row.startswith("#"))
        )  #,
        #field_names)
        for row in reader:
            yield row


def load_gdax_csv(csv_file):
    pass


def load_coinbase_csv(csv_file):
    pass
