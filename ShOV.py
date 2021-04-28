import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud_graph import WordCloud, STOPWORDS
from matplotlib.colors import to_rgba, get_named_colors_mapping
import os
from PIL import Image

desired_width = 620
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 44)
df = pd.read_csv('source.csv', usecols=["Rodzaj wzmianki", "Autor", "Tresc wypowiedzi", "Data stworzenia", "Domena", "Sentyment", "Grupa domen", "Link do wypowiedzi", "Slowa kluczowe", "Plec", "comments", "followers", "influenceScore"], delimiter=';', low_memory=False, encoding='latin-1')


source = df['Grupa domen']
gender = df['Plec']
date = df['Data stworzenia']
text = df['Tresc wypowiedzi']
keywords = df['Slowa kluczowe'].dropna()
sentiment = df['Sentyment']
author = df['Autor']

pd.set_option('display.max_rows', df.shape[0] + 1)
df['Tresc wypowiedzi'] = df['Tresc wypowiedzi'].astype(str)

all_mentions = df['Tresc wypowiedzi'].count()

carb = df[df['Tresc wypowiedzi'].str.contains("wegiel")].count()
green_peace = df[df['Tresc wypowiedzi'].str.contains("greenpeace")].count()

carb_mentions = carb['Tresc wypowiedzi']
green_peace_mentions = green_peace['Tresc wypowiedzi']

ShOv_carb = round((carb_mentions/all_mentions)*100, 2)
ShOv_greenpeace = round((green_peace_mentions/all_mentions)*100, 2)

print(ShOv_greenpeace, ShOv_carb)