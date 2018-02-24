import csv
import json
from datetime import datetime


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
        )
        for row in reader:
            for loader in (load_gdax_row, load_coinbase_row):
                try:
                    yield loader(row)
                except Exception as e:
                    continue


def load_gdax_row(r):
    return {
        "product": r["product"].split("-")[0],
        "event": r["side"],
        "timestamp": r["created at"],
        "size": r["size"],
        "price": r["price"],
        "fee": r["fee"],
        "source_record": r,
    }


def load_coinbase_row(r):
    return {
        "product": r["Currency"],
        "event": r["side"],
        "timestamp": r["created at"],
        "size": r["size"],
        "price": r["price"],
        "fee": r["fee"],
        "source_record": r,
    }
