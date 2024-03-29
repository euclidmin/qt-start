import argparse
import pandas as pd

from PySide2.QtCore import QDateTime, QTimeZone

def transform_date(utc, timezone=None):
    utc_fmt = "yyyy-MM-ddTHH:mm:ss.zzzZ"
    new_date = QDateTime().fromString(utc, utc_fmt)
    if timezone:
        new_date.setTimeZone(timezone)

    return new_date

def read_data(fname):
    df = pd.read_csv(fname)
    df = df.drop(df[df.mag<0].index)
    magnitudes = df["mag"]
    timezone = QTimeZone(b"Europe/Berlin")
    times = df["time"].apply(lambda x: transform_date(x, timezone))
    return times, magnitudes

# def read_data(fname):
#     return pd.read_csv(fname)

if __name__ == "__main__":
    options = argparse.ArgumentParser()
    options.add_argument("-f", "--file", type=str, required=True)
    args = options.parse_args()
    data = read_data(args.file)
    print(data)


