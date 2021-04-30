import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import os
from PIL import Image

desired_width = 620
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 44)
df = pd.read_csv('source.csv', usecols=["Tresc wypowiedzi", "Sentyment", 'Slowa kluczowe'], delimiter=';', low_memory=False, encoding='latin-1')

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
                   stopwords=stopwords)
    wc.generate(str(text))
    wc.to_file(os.path.join(currdir, 'wc_keywords.png'))
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
    wc = WordCloud(background_color='white',
                   colormap='Greens',
                   mask=mask,
                   max_words=200,
                   min_font_size=10,
                   stopwords=stopwords)
    wc.generate(str(text))
    wc.to_file(os.path.join(currdir, 'wc_positive.png'))
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
    wc = WordCloud(background_color='white',
                   colormap='Oranges',
                   mask=mask,
                   max_words=200,
                   min_font_size=10,
                   stopwords=stopwords)
    wc.generate(str(text))
    wc.to_file(os.path.join(currdir, 'wc_negative.png'))
    return