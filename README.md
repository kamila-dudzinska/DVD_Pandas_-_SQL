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

Output: Plik Excel z zakładkami (zaktualizowany 08.11.2026)


Aktualizacja (07.11.2026) To był mój pierwszy projekt ETL łączący SQL z Pythonem, dlatego zdecydowałam się tylko na dwie poprawki:

* bezpieczeństwo danych – dane logowania do bazy są w pliku .env (zmienne środowiskowe), a nie w kodzie
* poprawność danych – zapytanie SQL łączy płatności z filmami przez wypożyczenia (rental), dzięki czemu nie powstaje iloczyn kartezjański i płatności się nie powielają (łączny przychód ok. 61 tys. zamiast 2,1 mln).


Konfiguracja ze zmiennymi środowiskowymi w celu zachowania bezpieczeństwa:
![konfiguracja](images/congfig.png)


Funkcje:

![Segmentacja klientów](images/client_segment.png)



![przychód wg lokacji](images/function1.png)



Główny skrypt analizy:
![main](images/main.png)

Główny skrypt analizy: - zapis wyników:
![main](images/main2.png)


<hr style="border:3px solid #AEC6CF;">

###  Kontakt:


[![Kamila Dudzińska](https://img.shields.io/badge/Kamila%20Dudzińska-ff69b4?style=for-the-badge)](mailto:kamila.dudzinska@onet.pl)
[![Email](https://img.shields.io/badge/Email-555555?style=for-the-badge)](mailto:kamila.dudzinska@onet.pl)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge)](https://www.linkedin.com/flagship-web/in/kamila-dudzi%C5%84ska-856bb31b8/)





