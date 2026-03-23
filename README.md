# DVD_Pandas_SQL

Autor: Kamila Dudzińska 

Automatyczny system pobierający dane z bazy danych PostgreSQL, wykonujący analizę danych i przygotowujący raport podsumowujacy w excelu.

Program:
*  łaczy się z bazą danych dvd_rental z postgres SQL
*  za pomocą zoptymalizowanych kwerend pobierane są dane
*  w pliku df anaysis znajdują się funkcje z dokładnym opisem, które posłużą do analizy danych
*  w main wykonywana jest analiza danych wraz z podsumowaniem
*  na koniec generowany jest plik excel z wieloma zakładkami, w którym uzyskamy odpowiednio zagregowne/policzone/przedstawione dane 

Technologie: 
*  Języki: Python, SQL
*  biblioteki: pandas, SQLAlchemy, Openpyxl, aata_loader, dotenv, psycopg2-binary
*  baza danych: PostgreSQL

Struktura projektu:
src/
* config.py           # Konfiguracja bazy i zmiennych środowiskowych
* sql_query.py        # Zapytanie SQL
* analysis.py         # logika analizy i funkcje z docstringami
* main.py             # Główny skrypt sterujący

Output: Plik Excel z zakładkami

Przykładowy kod:
<img width="588" height="572" alt="image" src="https://github.com/user-attachments/assets/43a0f8f3-9229-4248-9ab8-7d3b74a0c101" />

Konfiguracja ze zmiennymi środowiskowymi w celu zachowania bezpieczeństwa:
<img width="756" height="330" alt="image" src="https://github.com/user-attachments/assets/7468caf6-5f21-43bb-9fbf-c0a8ed5d9fb1" />

Przykładowe wyniki w IDE:
<img width="431" height="152" alt="image" src="https://github.com/user-attachments/assets/7548a7b1-3f3b-4696-b983-a21700cbebc6" />
<img width="598" height="152" alt="image" src="https://github.com/user-attachments/assets/79a6105a-d22e-4539-90ea-2cee9c47e86a" />



