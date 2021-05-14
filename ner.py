import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import os
from PIL import Image


desired_width = 620
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 3)
pd.set_option('display.max_rows', 500)

df = pd.read_csv('dzien_ziemi_ner.csv', delimiter=',', usecols=["ner_products", "ner_postprocess_brands", "ner_postprocess_products"])

products = df['ner_products']
post_brands = df['ner_postprocess_brands']
post_products = df['ner_postprocess_products'].dropna()

def ner_wordcloud1(text=post_products):
    currdir = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    mask = np.array(Image.open(os.path.join(currdir, 'mask.png')))
    stopwords = set(STOPWORDS)
    stopwords.add('RT')
    stopwords.add('ner_postprocess_products')
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
    stopwords.add('dtype')
    stopwords.add('object')
    stopwords.add('kluczowe')
    wc = WordCloud(background_color='white',
                   mask=mask,
                   max_words=200,
                   min_font_size=10,
                   stopwords=stopwords)
    wc.generate(str(text))
    wc.to_file(os.path.join(currdir, 'postproduct.png'))
    return