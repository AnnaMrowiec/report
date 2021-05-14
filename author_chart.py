import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

desired_width = 620
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 44)
pd.set_option('display.max_rows', 100)

def interactivity():
    df = pd.read_csv('CSV/source.csv', usecols=["Autor", "Tresc wypowiedzi", "Data stworzenia", "Domena", "Slowa kluczowe", "comments", "followers"], delimiter=';', low_memory=False, encoding='latin-1')
    fb = pd.read_csv('CSV/source.csv', delimiter=';', usecols=['Autor', 'comments', 'shares', 'wow', 'love', 'like', 'haha', 'sad', 'angry', 'thankful'], low_memory=False, encoding='latin-1')
    tt = pd.read_csv('CSV/source.csv', delimiter=';', usecols=['Autor', 'comments', 'retweet', 'followers'], low_memory=False, encoding='latin-1')

    author = df['Autor']

    '''
    Caltulating InI:
    Reactions = 1
    Comments = 4
    Shares = 16
    '''

    #  CALCULATING INI FOR FACEBOOK

    reactions_fb = fb['wow'] + fb['love'] + fb['like'] + fb['haha'] + fb['sad'] + fb['angry'] + fb['thankful']
    comments_fb = fb['comments']*4
    shares_fb = fb['shares']*16
    fb['InI_FB'] = reactions_fb + comments_fb + shares_fb
    InI_Author_FB = pd.concat([author, fb["InI_FB"]], axis=1)
    InI_Author_FB = InI_Author_FB.dropna().sort_values('InI_FB', ascending=False).head(10)

    font1 = {'family': 'serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}

    interactivity = InI_Author_FB['InI_FB']
    labels = InI_Author_FB['Autor']
    x = np.arange(len(labels))
    width = 0.8

    fig, ax = plt.subplots()
    ax.bar(x, interactivity, width, color=('#ee8e3b'))  # color orange

    ax.set_xticks(np.arange(len(x)))
    ax.set_xticklabels(['TVN24', 'OKO.Press', 'PolsatNews', 'ONET', 'tvp.info', 'IUSTITIA', 'MKS', 'Lidl PL', 'Planszowe Newsy', "Nauka"], rotation=45, ha='right')
    ax.set_title('Najbardziej aktywni autorzy', fontdict=font1)
    ax.set_ylabel('Interactivity Index', fontdict=font2)
    plt.subplots_adjust(bottom=0.25)

    plt.savefig('charts/ini.png')
    plt.clf()
    return

def influenceScore():
    # FUNCTION FOR THE AUTHOR WITH THE HIGHEST INFLUENCESCORE
    df = pd.read_csv('CSV/source.csv', usecols=["Autor", "influenceScore"], delimiter=';', low_memory=False, encoding='latin-1')

    author = df[['Autor', 'influenceScore']]
    best_author = author.dropna().sort_values('influenceScore', ascending=False).head(10)

    font1 = {'family': 'serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}

    influScore = best_author['influenceScore']
    labels = best_author['Autor']
    x = np.arange(len(labels))
    width = 0.8

    fig, ax = plt.subplots()
    ax.bar(x, influScore, width, color=('#ee8e3b'))  # color orange

    ax.set_xticks(np.arange(len(x)))
    ax.set_xticklabels(labels=['Karolina Gawot', 'OKO.Press', 'TVN24', 'Onet', 'tvp.info', 'PolsatNews', '@tvp_info', '@Piechociński', '@OnetWiadomosci', '@Piechociński'], rotation=45, ha='right')
    ax.set_title('Najlepsi autorzy', fontdict=font1)
    ax.set_ylabel('Influence Score', fontdict=font2)
    plt.subplots_adjust(bottom=0.25)

    plt.savefig('charts/influence.png')
    plt.clf()
    return


def appearance_frequency():
    # FUNCTION FOR THE MOST FREQUENT COMMENTING AUTHOR
    df = pd.read_csv('CSV/source.csv', usecols=["Autor", "influenceScore"], delimiter=';', low_memory=False, encoding='latin-1')
    author = df['Autor']
    freq = author.value_counts().head(10)
    freq = pd.DataFrame(freq)
    freq.reset_index(inplace=True)
    ap = freq.rename(columns={'index': 'Autor',
                            'Autor': 'Appearance'})

    font1 = {'family': 'serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}

    appearance = ap['Appearance']
    labels = ap['Autor']
    x = np.arange(len(labels))
    width = 0.8

    fig, ax = plt.subplots()
    ax.bar(x, appearance, width, color=('#ee8e3b'))  # color orange

    ax.set_xticks(np.arange(len(x)))
    ax.set_xticklabels(labels=labels, rotation=45, ha='right')
    ax.set_title('Najczęściej komentujący autorzy', fontdict=font1)
    ax.set_ylabel('Suma komentarzy', fontdict=font2)
    plt.subplots_adjust(bottom=0.30)

    plt.savefig('charts/appear.png')
    plt.clf()
    return