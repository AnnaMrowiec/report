
import pandas as pd
import matplotlib.pyplot as plt

def share_of_voice():
    desired_width = 620
    pd.set_option('display.width', desired_width)
    pd.set_option('display.max_columns', 44)
    df = pd.read_csv('source.csv', usecols=["Tresc wypowiedzi"], delimiter=';', low_memory=False, encoding='latin-1')

    pd.set_option('display.max_rows', df.shape[0] + 1)
    df['Tresc wypowiedzi'] = df['Tresc wypowiedzi'].astype(str)
    all_mentions = df['Tresc wypowiedzi'].count()

    keyword_1 = df[df['Tresc wypowiedzi'].str.contains("plastik", regex=False, flags=re.IGNORECASE)].count()
    keyword_2 = df[df['Tresc wypowiedzi'].str.contains("wegiel", regex=False, flags=re.IGNORECASE)].count()
    keyword_3 = df[df['Tresc wypowiedzi'].str.contains("kopaln", regex=False, flags=re.IGNORECASE)].count()
    keyword_4 = df[df['Tresc wypowiedzi'].str.contains("zanieczy", regex=False, flags=re.IGNORECASE)].count()
    keyword_5 = df[df['Tresc wypowiedzi'].str.contains("ekolog", regex=False, flags=re.IGNORECASE)].count()
    keyword_6 = df[df['Tresc wypowiedzi'].str.contains("klimat", regex=False, flags=re.IGNORECASE)].count()

    k1_mentions = keyword_1['Tresc wypowiedzi']
    k2_mentions = keyword_2['Tresc wypowiedzi']
    k3_mentions = keyword_3['Tresc wypowiedzi']
    k4_mentions = keyword_4['Tresc wypowiedzi']
    k5_mentions = keyword_5['Tresc wypowiedzi']
    k6_mentions = keyword_6['Tresc wypowiedzi']

    hashtag_1 = round((k1_mentions/all_mentions)*100, 2)
    hashtag_2 = round((k2_mentions/all_mentions)*100, 2)
    hashtag_3 = round((k3_mentions/all_mentions)*100, 2)
    hashtag_4 = round((k4_mentions/all_mentions)*100, 2)
    hashtag_5 = round((k5_mentions/all_mentions)*100, 2)
    hashtag_6 = round((k6_mentions/all_mentions)*100, 2)

    best_hashtags = hashtag_1, hashtag_2, hashtag_3, hashtag_4, hashtag_5, hashtag_6

    font1 = {'family': 'serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}

    x = ['Plastik', 'Węgiel', 'Kopalnia', 'Zieleń', 'Ekologiczne', 'Klimat']
    width = 0.8

    fig, ax = plt.subplots()
    ax.bar(x, best_hashtags, width, color=('#ee8e3b'))

    ax.set_title('Najpopularniejsze hashtagi', fontdict=font1)
    ax.set_ylabel('Share of Voice', fontdict=font2)
    ax.set_xlabel('Hashtag', fontdict=font2)

    plt.savefig('share.png')
    plt.clf()
    return