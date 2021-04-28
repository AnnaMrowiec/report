
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.image as image


def share_of_voice():
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

    keyword_1 = df[df['Tresc wypowiedzi'].str.contains("plastik")].count()
    keyword_2 = df[df['Tresc wypowiedzi'].str.contains("wegiel")].count()
    keyword_3 = df[df['Tresc wypowiedzi'].str.contains("smieci")].count()
    keyword_4 = df[df['Tresc wypowiedzi'].str.contains("ziemi")].count()
    keyword_5 = df[df['Tresc wypowiedzi'].str.contains("energ")].count()
    keyword_6 = df[df['Tresc wypowiedzi'].str.contains("efekt")].count()
    keyword_7 = df[df['Tresc wypowiedzi'].str.contains("smog")].count()

    k1_mentions = keyword_1['Tresc wypowiedzi']
    k2_mentions = keyword_2['Tresc wypowiedzi']
    k3_mentions = keyword_3['Tresc wypowiedzi']
    k4_mentions = keyword_4['Tresc wypowiedzi']
    k5_mentions = keyword_5['Tresc wypowiedzi']
    k6_mentions = keyword_6['Tresc wypowiedzi']
    k7_mentions = keyword_7['Tresc wypowiedzi']

    hashtag_1 = round((k1_mentions/all_mentions)*100, 2)
    hashtag_2 = round((k2_mentions/all_mentions)*100, 2)
    hashtag_3 = round((k3_mentions/all_mentions)*100, 2)
    hashtag_4 = round((k4_mentions/all_mentions)*100, 2)
    hashtag_5 = round((k5_mentions/all_mentions)*100, 2)
    hashtag_6 = round((k6_mentions/all_mentions)*100, 2)
    hashtag_7 = round((k7_mentions/all_mentions)*100, 2)

    best_hashtags = hashtag_1, hashtag_2, hashtag_3, hashtag_4, hashtag_5, hashtag_6, hashtag_7

    with cbook.get_sample_data(r'C:\Users\Anna Kaczmarczyk\Desktop\raport_buzz\sot.png') as file:
        img = image.imread(file)

    font1 = {'family': 'serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}

    x = ['Plastik', 'Węgiel', 'Śmieci', 'Ziemia', 'Energia', 'Efekt', 'Smog']
    width = 0.8

    fig, ax = plt.subplots()
    ax.bar(x, best_hashtags, width)

    ax.grid(axis='y', color='gray', ls='-.', lw=0.25)
    # ax.set_xticklabels(labels=x, rotation=45)

    ax.set_title('Najpopularniejsze hashtagi', fontdict=font1)
    ax.set_ylabel('Share of Voice', fontdict=font2)
    ax.set_xlabel('Hashtag', fontdict=font2)

    # plt.subplots_adjust(bottom=0.25)
    plt.figimage(img, xo=100, yo=250, zorder=1, alpha=0.25)
    plt.savefig('share.png')
    plt.clf()
    return