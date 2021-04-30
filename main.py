# created on 2021-04-16 at 12:45 by Anna Mrowiec

from line_chart import graph1, graph2, graph3, graph4, graph5
from bar_chart import bar1, bar2, bar3
from wordcloud_graph import wordcloud1, wordcloud2, wordcloud3
from pie_chart import pie1
from share_voice import share_of_voice
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
WORDCLOUD1 - CHMURA WYKORZYSTANYCH SŁÓW KLUCZOWYCH
WORDCLOUD2 - CHMURA SŁÓW Z WYPOWIEDZI O POZYTYWNYM SENTYMENCIE
WORDCLOUD3 - CHMURA SŁÓW Z WYPOWIEDZI O NEGATYWNYM SENTYMENCIE
PIE1 - UDZIAŁ PROCENTOWY TEMATÓW W ŁĄCZNEJ LICZBIE WZMIANEK
SHARE_OF_VOICE - UDZIAŁ WZMIANEK MARKI WE WSZYSTKICH WZMIANKACH
'''
start = time.time()

print(graph1(), graph2(), graph3(), graph4(), graph5())
print(bar1(), bar2(), bar3())
print(wordcloud1(), wordcloud2(), wordcloud3())
print(pie1())
print(share_of_voice())

end = time.time()
print(round(end-start))

