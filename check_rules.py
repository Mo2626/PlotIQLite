# check_rules.py

import pandas as pd

def check_building_rules(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prüft einfache baurechtliche/geometrische Regeln auf Basis der gemergten Daten.
    1) Geschossprüfung 
    2) Höhenprüfung
    3) BGF-Prüfung
    Fügt dem DataFrame entsprechende Spalten hinzu.
    
    """

    # 1) BGF-Prüfung
    # True = ok, False = überschritten
    df["rule_bgf_ok"] = df["geplante_bgf_m2"] <= df["zul_bgf_m2"]

    # 2) Höhen-Prüfung (nur prüfen, wenn beide Werte vorhanden sind)
    df["rule_hoehe_ok"] = df["gebaeudehoehe_m"] <= df["max_hoehe_m"]

    # 3) Geschoss-Prüfung
    df["rule_geschosse_ok"] = df["geplante_geschosse"] <= df["geschosse_max"]

    # 4) Gesamtergebnis: alle Regeln erfüllt?
    df["rules_all_ok"] = (
        df["rule_bgf_ok"]
        & df["rule_hoehe_ok"]
        & df["rule_geschosse_ok"]
    )
    return df


if __name__ == "__main__":
    print("check_rules: nur als Modul gedacht.")
