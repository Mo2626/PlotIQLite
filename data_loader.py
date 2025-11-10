# data_loader.py

import pandas as pd
from config import DATA_PATHS


def load_data():
    """Liest alle Excels ein und gibt drei DataFrames zurück."""
    df_grund = pd.read_excel(DATA_PATHS["grundstuecke"])
    df_geo = pd.read_excel(DATA_PATHS["geometrie"])
    df_wirt = pd.read_excel(DATA_PATHS["wirtschaft"])
    return df_grund, df_geo, df_wirt


if __name__ == "__main__":
    # einfacher Testlauf
    df_grund, df_geo, df_wirt = load_data()

    print("Grundstücksdaten:")
    print(df_grund.head(), "\n")

    print("Geometriedaten:")
    print(df_geo.head(), "\n")

    print("Wirtschaftsdaten:")
    print(df_wirt.head(), "\n")
