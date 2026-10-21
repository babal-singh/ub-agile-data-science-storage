import pandas as pd


def add_pickup_day(trips: pd.DataFrame) -> pd.DataFrame:
    trips = trips.copy()
    trips["pickup_day"] = trips["tpep_pickup_datetime"].dt.strftime("%Y-%m-%d")
    return trips


def tip_percentage(trips: pd.DataFrame) -> pd.Series:
    valid_fare = trips["fare_amount"].where(trips["fare_amount"] > 0)
    return trips["tip_amount"] * 100 / valid_fare
