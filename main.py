# main.py

from data_loader import load_data
from calc import merge_data, calculate_kpis
from check_rules import check_building_rules


def main():
    # 1. Daten einlesen
    df_grund, df_geo, df_wirt = load_data()

    # 2. zusammenführen
    df_all = merge_data(df_grund, df_geo, df_wirt)

    # 3. wirtschaftliche KPIs berechnen
    df_all = calculate_kpis(df_all)

    # 4. baurechtlich/geometrische Regeln prüfen
    df_all = check_building_rules(df_all)

    # 5. Ergebnis anzeigen (erstmal in der Konsole)
    print(df_all[[
        "projekt",
        "zul_bgf_m2",
        "geplante_bgf_m2",
        "rule_bgf_ok",
        "gebaeudehoehe_m",
        "max_hoehe_m",
        "rule_hoehe_ok",
        "geplante_geschosse",
        "geschosse_max",
        "rule_geschosse_ok",
        "rules_all_ok",
        "bruttorendite_prozent",
        "cap_value_chf"
    ]])


if __name__ == "__main__":
    main()
