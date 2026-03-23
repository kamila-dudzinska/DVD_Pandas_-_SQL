# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 19:27:31 2026

@author: Kamila Dudzińska
"""


# serce projektu <3

# import modułów
import pandas as pd
import numpy as np
from sqlalchemy import text


# przychód w zależnoci od lokacji 
def revenue_by_location(df):
    
    '''Oblicza przychód w podziale na kraj'''
    
    #przychów w podziale na kraj
    result = df.groupby(['country'], as_index=False)['amount'].sum()
    
    #łączny przychód
    total_revenue = result['amount'].sum()
    
    #udział procentowy
    result['percentage_share']  = (result['amount']/total_revenue) * 100
    
    #zaokrąglamy round()
    result['percentage_share']  = result['percentage_share'].round(2)

    #top n krajów 
    result = result.sort_values(by='amount', ascending = False).reset_index(drop=True)

    return result


#segmentacja klientów na podstawie przychodów i aktywnosci
def active_customers_by_location(df):
    
    '''
    Funkcja pozwala na segmentację klientów na podstawie lokalizacji według kraju.
    
    '''
    
    return(
        df[df['active'] ==  True]
        .groupby('country')['customer_id']
        .nunique()    
        .reset_index(name='active_custmer_num')                                  #tylko unikalne wartosci
        .sort_values(by='active_custmer_num', ascending = False))                
        
       
# segmentacja klientów po kwantylach (równych częsciach)        
def customer_segments(df):
    
    '''
    Funkcja pozwala na segmentację klientów na równe częsci kwantyle według przychodów (revenue)
    
    '''
    
    customer_revenue = df.groupby('customer_id')['amount'].sum()
    
    #funkcja q dzieli zbiór na równe częsci (kwantyle) po liczbie klientów
    segments = pd.cut(customer_revenue,
                       bins=3, 
                       labels=['low', 'medium', 'high'],
                       duplicates = 'drop')    
        
    return segments


# dodanie segmentów do df
def add_segments(df):
    
    '''
    Funkcja dodaje segmenty do Data Frame.
    
    '''
    
    segments = customer_segments(df)
    
    df['segment'] = df['customer_id'].map(segments)
    
    return df


# przychody wg segmentacji klientów na 'low', 'medium', 'high
def revenue_by_segment(df):
    
    '''
    Funkcja pozwala pokazanie przychodów według segmentów.
    
    '''
    
    return(
        df.groupby('segment')['amount'].sum().sort_values(ascending=False).reset_index(name='revenue_by_segment'))
 

# kraje, które generują najwieksze przychody w okreslonym segmencie
def top_country_by_segment(df):
    
    '''
    Funkcja pozwala pokazanie kraje z największymi przychodami (revenue) według segmentów
    
    '''
    
    #tworzymy segmenty z try-except aby wykluczyć błedne wartoci możliwe przy qcut*
    dane = df[['amount', 'country', 'customer_id']].copy().reset_index(drop=True)
    try:
        segments = pd.qcut(dane['amount'], 
                           q=3, labels=['Low', 'Medium', 'High'], 
                           duplicates='drop')
    except ValueError:
        segments = pd.cut(dane['amount'], 
                          bins=3, 
                          labels=['Low', 'Medium', 'High'])

    #przypisanie segmentów
    dane['segment'] = segments.values


    # observed=True - zabezpiecza przed błędami pamięci przy dużych danych
    #unikalni klienci w podziale na kraj
    counts = dane.groupby(['segment', 'country'], 
                          observed=True)['customer_id'].nunique().reset_index()

    #top kliencie dla segmentó
    counts = counts.sort_values(by=['segment', 'customer_id'], ascending=[True, False])


    wynik = counts.drop_duplicates(subset=['segment'], keep='first')

    return wynik.drop_duplicates('segment')


  
# aktywnoSć vs segment
def segment_by_activity(df):
    
    '''
    Funkcja pozwala pokazanie aktywnoci klientów względem segmentów
    
    '''
    
    return (
        df.groupby(['segment', 'active'])['customer_id']
        .nunique()
        .reset_index()
        )    

    
# liczba klientów w poszczególnych segmentach

def customer_number(df):
    
    '''
    Funkcja pozwala na przedstawienie ilosci klientów w poszczególnych segmentach.

    '''
    
    return(
        df[['customer_id', 'segment']]
        .drop_duplicates()
        .groupby('segment')
        .count()
        .reset_index()
        .rename(columns={'customer_id':'number_of_customers'})
        )    


# udział procentowy poszczególnych segmentów
def segments_share_per(df):
    
    '''
    Funkcja pozwala na przedstawienie procentowych udziałów klientów w poszczególnych segmentach.

    '''
    
    counts = (
        df[['customer_id', 'segment']]
        .drop_duplicates()
        .groupby('segment')
        .count()
        )
    
    total = counts['customer_id'].sum()
    
    counts['percentage'] = (counts['customer_id']/total)*100
    counts['percentage'] = counts['percentage'].round(2)
    
    return counts
    
   
# najbardziej popularne języki
def language2(engine):
    
    '''
    Funkcja zlicza liczbę filmów w okrelonym języku.

    '''
    
    query_languages = """
            SELECT
                l.name,
                COUNT(f.film_id) AS ile_filmów
            FROM language l
            LEFT JOIN
                film AS f ON l.language_id = f.language_id
            GROUP BY
                l.name
            ORDER BY 
                ile_filmów DESC
            LIMIT 100000
    """
    with engine.connect() as cur:
        result = cur.execute(text(query_languages))
        
    for i, j in result:
         print(f" Język:  {i} liczba: {j}")

    return result.fetchall()

