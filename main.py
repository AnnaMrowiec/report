# created on 2021-04-16 at 12:45 by Anna Mrowiec

from line_chart import graph1, graph2, graph3, graph4, graph5
from bar_chart import bar1, bar2, bar3, bar4
from wordcloud_chart import wordcloud1, wordcloud2, wordcloud3
from pie_chart import share, gender
from author_chart import interactivity, influenceScore, appearance_frequency
from hashtag import hashtag, count_hashtag
import time


'''
CHART1 - ROZKŁAD WZMIANEK W CZASIE
CHART2 - ROZKŁAD ZASIĘGU WZMIANEK W CZASIE
CHART3 - ROZKŁAD WZMIANEK W CZASIE WG ŹRÓDEŁ
CHART4 - ROZKŁAD WZMIANEK W CZASIE WG PŁCI AUTORA
CHART5 - PROCENTOWY UDZIAŁ PŁCI W LICZBIE WZMIANEK
BAR1 - NAJPOPULARNIEJSZE ŹRÓDŁA
BAR2 - PROCENTOWY UDZIAŁ ŹRÓDŁA W LICZBIE WZMIANEK
BAR3 - PROCENTOWY UDZIAŁ SENTYMENTU WZMIANEK PER ŹRÓDŁO
BAR4 - PROCENTOWY UDZIAŁ SENTYMENTU POZYTYWNEGO I NEGATYWNEGO PER ŹRÓDŁO
WORDCLOUD1 - CHMURA WYKORZYSTANYCH SŁÓW KLUCZOWYCH
WORDCLOUD2 - CHMURA SŁÓW Z WYPOWIEDZI O POZYTYWNYM SENTYMENCIE
WORDCLOUD3 - CHMURA SŁÓW Z WYPOWIEDZI O NEGATYWNYM SENTYMENCIE
SHARE - UDZIAŁ PROCENTOWY TEMATÓW W ŁĄCZNEJ LICZBIE WZMIANEK
GENDER - UDZIAŁ PROCENTOWY PŁCI W ŁĄCZNEJ LICZBIE WZMIANEK
INTERACTIVITY - INTERACTIVITY INDEX LICZONY, JAK W SOTRENDERZE: REAKCJA = 1; KOMENTARZ = 4; UDOSTĘPNIENIE = 16
INFLUENCESCORE - 10 AUTORÓW O NAJWYŻSZYM WSKAŹNIKU INFLUENCESCORE Z PLIKU ŹRÓDŁOWEGO
APPEARANCE_FREQUENCY - CZĘSTOTLIWOŚĆ WYSTĘPOWANIA KOMENTARZY PRZYPISANA DO KONKRETNEGO AUTORA 
HASHTAG- UDZIAŁ WZMIANEK MARKI/SŁÓW KLUCZOWYCH WE WSZYSTKICH WZMIANKACH
'''
start = time.time()

# print('Wykresy liniowe: ', graph1(), graph2(), graph3(), graph4(), graph5())
# print('Wykresy słupkowe: ', bar1(), bar2(), bar3(), bar4())
# print('Chmury słów kluczowych: ', wordcloud1(), wordcloud2(), wordcloud3())
# print('Wykresy kołowe: ', share(), gender())
# print('Autorzy: ', interactivity(), influenceScore(), appearance_frequency())
print('Analiza hashtagów: ', hashtag(), count_hashtag())


end = time.time()
print(round(end-start))

