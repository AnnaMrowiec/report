import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import os
from PIL import Image

desired_width = 620
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 44)
df = pd.read_csv('CSV/source.csv', usecols=["Tresc wypowiedzi", "Sentyment", 'Slowa kluczowe'], delimiter=';', low_memory=False, encoding='latin-1')

text = df['Tresc wypowiedzi']
keywords = df['Slowa kluczowe']
negative = df.loc[df['Sentyment'] == 'NEGATIVE']
negative_text = negative['Tresc wypowiedzi']
positive = df.loc[df['Sentyment'] == 'POSITIVE']
positive_text = positive['Tresc wypowiedzi']


'''
Wordclouds 1-3 are based on source.csv which is the main csv downloaded from the Source.
Wordcloud 1 represents most often used keywords in this projects.
Wordcloud 2 and 3 represent positive and negative words from all mentions represented.
Stopwords must include words such as 'się', 'na', and other often mentioned connotations.
'''

def wordcloud1(text=keywords):
    currdir = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    mask = np.array(Image.open(os.path.join(currdir, 'mask.png')))
    stopwords = set(STOPWORDS)
    stopwords.add('RT')
    stopwords.add('sie')
    stopwords.add('w')
    stopwords.add('we')
    stopwords.add('za')
    stopwords.add('sa')
    stopwords.add('Length')
    stopwords.add('NaN')
    stopwords.add('Name')
    stopwords.add('Slowa')
    stopwords.add('z')
    stopwords.add('i')
    stopwords.add('Weglarczyk')
    stopwords.add('dtype')
    stopwords.add('object')
    stopwords.add('kluczowe')
    wc = WordCloud(background_color='white',
                   mask=mask,
                   max_words=200,
                   min_font_size=10,
                   stopwords=stopwords).generate(str(text))
    wc.to_file(os.path.join(currdir, 'charts/wc_keywords.png'))
    return

def wordcloud2(text=positive_text):
    currdir = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    mask = np.array(Image.open(os.path.join(currdir, 'mask.png')))
    stopwords = set(STOPWORDS)
    stopwords.add('RT')
    stopwords.add('sie')
    stopwords.add('w')
    stopwords.add('we')
    stopwords.add('za')
    stopwords.add('sa')
    stopwords.add('z')
    stopwords.add('i')
    stopwords.add('ale')
    stopwords.add('jest')
    stopwords.add('b')
    stopwords.add('na')
    stopwords.add('nie')
    stopwords.add('ja')
    stopwords.add('dtype')
    stopwords.add('kluczowe')
    stopwords.add('name')
    stopwords.add('tresc')
    stopwords.add('ze')
    stopwords.add('jak')
    stopwords.add('co')
    stopwords.add('od')
    stopwords.add('ty')
    stopwords.add('pl')
    stopwords.add('Length')
    stopwords.add('b')
    stopwords.add('byl')
    stopwords.add('dzien')
    stopwords.add('którym')
    stopwords.add('TeryAsic1')
    stopwords.add('robertpi9')
    stopwords.add('object')
    stopwords.add('o')
    stopwords.add('report')
    stopwords.add('P00lskiKarlista')
    stopwords.add('moje')
    stopwords.add('tym')
    stopwords.add('tylu')
    stopwords.add('temu')
    stopwords.add('te')
    stopwords.add('Jacek01522794')
    stopwords.add('temu')
    stopwords.add('ta')
    stopwords.add('dobra')
    stopwords.add('LukasKampa')
    stopwords.add('fi')
    stopwords.add('Dariusz')
    stopwords.add('Kondrat')
    stopwords.add('annam')
    stopwords.add('zeby')
    stopwords.add('NocnaZ')
    stopwords.add('po')
    stopwords.add('mysl')
    stopwords.add('dobry')
    stopwords.add('sobie')
    stopwords.add('ksiazka')
    stopwords.add('wiecej')
    stopwords.add('Zadanie')
    stopwords.add('moze')
    stopwords.add('dobry')
    stopwords.add('podziekowalam')
    stopwords.add('Artur')
    stopwords.add('Michalak')
    stopwords.add('marudz')
    stopwords.add('polska')
    stopwords.add('podsumowanie')
    stopwords.add('refera')
    stopwords.add('weeke')
    stopwords.add('informa')
    stopwords.add('kupic')
    stopwords.add('osobisci')
    stopwords.add('pytanie')
    stopwords.add('zazwyczaj')
    stopwords.add('taniego')
    stopwords.add('radzicie')
    stopwords.add('stresem')
    stopwords.add('zaufana')
    stopwords.add('zyczliw')
    stopwords.add('cyklu')
    stopwords.add('DZIALA')
    stopwords.add('szybkie')
    stopwords.add('szybko')
    stopwords.add('wczorajszym')
    stopwords.add('rozmowa')
    stopwords.add('wypowiedzi')
    wc = WordCloud(background_color='white',
                   colormap='Greens',
                   mask=mask,
                   max_words=200,
                   min_font_size=10,
                   stopwords=stopwords,
                   random_state=100).generate(str(text))
    wc.to_file(os.path.join(currdir, 'charts/wc_positive.png'))
    return

def wordcloud3(text=negative_text):
    currdir = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    mask = np.array(Image.open(os.path.join(currdir, 'mask.png')))
    stopwords = set(STOPWORDS)
    stopwords.add('RT')
    stopwords.add('sie')
    stopwords.add('w')
    stopwords.add('we')
    stopwords.add('za')
    stopwords.add('sa')
    stopwords.add('z')
    stopwords.add('i')
    stopwords.add('na')
    stopwords.add('ja')
    stopwords.add('dtype')
    stopwords.add('kluczowe')
    stopwords.add('name')
    stopwords.add('tresc')
    stopwords.add('zin')
    stopwords.add('ze')
    stopwords.add('jak')
    stopwords.add('co')
    stopwords.add('od')
    stopwords.add('ty')
    stopwords.add('ale')
    stopwords.add('nie')
    stopwords.add('tak')
    stopwords.add('go')
    stopwords.add('pl')
    stopwords.add('Length')
    stopwords.add('b')
    stopwords.add('byl')
    stopwords.add('dzien')
    stopwords.add('którym')
    stopwords.add('TeryAsic1')
    stopwords.add('robertpi9')
    stopwords.add('object')
    stopwords.add('o')
    stopwords.add('report')
    stopwords.add('P00lskiKarlista')
    stopwords.add('moje')
    stopwords.add('tym')
    stopwords.add('tylu')
    stopwords.add('temu')
    stopwords.add('Krzysztof')
    stopwords.add('Znajac')
    stopwords.add('klucz')
    stopwords.add('nas')
    stopwords.add('Swiercz')
    stopwords.add('bedzie')
    stopwords.add('Mówienie')
    stopwords.add('slyszalam')
    stopwords.add('posiadanie')
    stopwords.add('Kilka')
    stopwords.add('wypowiedzi')
    stopwords.add('tygodni')
    stopwords.add('prezydentpl')
    stopwords.add('znowu')
    stopwords.add('slowo')
    stopwords.add('napisal')
    stopwords.add('dobrze')
    stopwords.add('Pan')
    stopwords.add('skoncza')
    stopwords.add('dzikie')
    stopwords.add('zapasy')
    stopwords.add('rozsmieszaj')
    wc = WordCloud(background_color='white',
                   colormap='Oranges',
                   mask=mask,
                   max_words=200,
                   min_font_size=10,
                   stopwords=stopwords).generate(str(text))
    wc.to_file(os.path.join(currdir, 'charts/wc_negative.png'))
    return