#!/usr/bin/env bash

# Skrypt automatyzujący potok danych w środowisku Unix/Linux

echo "===> 1. Tworzenie struktur katalogów..."
mkdir -p data

echo "===> 2. Uruchamianie kontenera bazy danych (Docker)..."
docker compose up -d

echo "===> 3. Czekanie na uruchomienie MS SQL Server (15 sek)..."
sleep 15

echo "===> 4. Pobieranie danych źródłowych (Unix curl)..."
# Przykładowe publiczne dane CSV
curl -s "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv" -o ./data/raw_data.csv

if [ -f "./data/raw_data.csv" ]; then
    echo "[OK] Plik pobrany pomyślnie."
else
    echo "[ERROR] Błąd pobierania pliku!"
    exit 1
fi

echo "===> 5. Uruchamianie przetworzenia i ładowania danych w Pythonie..."
python3 load_data.py

echo "===> 6. Podsumowanie pliku w terminalu (Unix head/wc)..."
echo "Liczba wierszy w pobranym pliku:"
wc -l ./data/raw_data.csv

echo "===> Pipeline zakończony sukcesem!"