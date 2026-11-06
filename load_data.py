import os
import pandas as pd
from sqlalchemy import create_engine

# Ścieżka do pobranego pliku w środowisku Unix
CSV_PATH = "./data/raw_data.csv"

def process_and_load():
    if not os.path.exists(CSV_PATH):
        print(f"[ERROR] Plik {CSV_PATH} nie istnieje!")
        return

    print("[INFO] Wczytywanie danych z pliku CSV...")
    df = pd.read_csv(CSV_PATH)

    # Prosta transformacja ETL (czyszczenie)
    df.dropna(inplace=True)
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

    # Połączenie z kontenerem MS SQL Server w Dockerze
    conn_str = "mssql+pyodbc://sa:YourStrongPassword123!@localhost:1433/master?driver=ODBC+Driver+17+for+SQL+Server"
    
    # Alternatywa gdy jest uzywany prostszy sterownik:
    # conn_str = "mssql+pymssql://sa:YourStrongPassword123!@localhost:1433/master"

    print("[INFO] Łączenie z bazą MS SQL w Dockerze...")
    engine = create_engine(conn_str)

    print("[INFO] Zapisywanie danych do bazy...")
    df.to_sql('stg_ecommerce_events', con=engine, if_exists='replace', index=False)
    print("[SUCCESS] Dane pomyślnie załadowane do bazy danych!")

if __name__ == "__main__":
    process_and_load()