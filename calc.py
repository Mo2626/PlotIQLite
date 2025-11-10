# calc.py

import pandas as pd


def merge_data(df_grund: pd.DataFrame,
               df_geo: pd.DataFrame,
               df_wirt: pd.DataFrame) -> pd.DataFrame:
    """
    Führt die drei Tabellen über die Spalte 'projekt' zusammen.
    Ergebnis: ein DataFrame mit allen Infos pro Projekt.
    """
    df = df_grund.merge(df_geo, on="projekt", how="left")
    df = df.merge(df_wirt, on="projekt", how="left")
    return df


def calculate_kpis(df: pd.DataFrame) -> pd.DataFrame:
    """
    Berechnet die wichtigsten KPIs für die Machbarkeits-/Wirtschaftlichkeitsprüfung.
    Erwartete Spalten:
    - grundstuecksflaeche_m2
    - gfz_zulaessig
    - baukosten_chf_m2
    - miete_chf_m2_a
    - leerstand_prozent
    - betriebskosten_chf_m2_a
    - cap_rate_prozent
    """

    # 1) zulässige BGF nach GFZ
    df["zul_bgf_m2"] = df["gfz_zulaessig"] * df["grundstuecksflaeche_m2"]

    # 2) Investition (ganz grob)
    df["investition_chf"] = df["zul_bgf_m2"] * df["baukosten_chf_m2"]

    # 3) Ertrag (Miete)
    df["ertrag_chf_a"] = (
        df["zul_bgf_m2"]
        * df["miete_chf_m2_a"]
        * (1 - df["leerstand_prozent"] / 100)
    )

    # 4) Betriebskosten pro Jahr
    df["betriebskosten_chf_a"] = (
        df["zul_bgf_m2"] * df["betriebskosten_chf_m2_a"]
    )

    # 5) NOI
    df["noi_chf_a"] = df["ertrag_chf_a"] - df["betriebskosten_chf_a"]

    # 6) Rendite
    df["bruttorendite_prozent"] = (
        df["noi_chf_a"] / df["investition_chf"]
    ) * 100

    # 7) Kapitalisierungswert
    df["cap_value_chf"] = df["noi_chf_a"] / (df["cap_rate_prozent"] / 100)

    return df


if __name__ == "__main__":
    from data_loader import load_data
    df_grund, df_geo, df_wirt = load_data()
    df_all = merge_data(df_grund, df_geo, df_wirt)
    df_all = calculate_kpis(df_all)
    print(df_all.head())


