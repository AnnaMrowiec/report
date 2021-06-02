import pandas as pd
import matplotlib.pyplot as plt
import re

desired_width = 620
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 44)
pd.set_option('display.max_rows', 100)


def share():
    df = pd.read_csv('CSV/source.csv',
                     usecols=["Rodzaj wzmianki", "Autor", "Tresc wypowiedzi", "Data stworzenia", "Domena", "Sentyment",
                              "Grupa domen", "Link do wypowiedzi", "Slowa kluczowe", "Plec", "comments", "followers",
                              "influenceScore"], delimiter=';', low_memory=False, encoding='latin-1')

    df = df['Slowa kluczowe']
    freq = df.value_counts()
    all_keywords = sum(freq)

    eko = freq['recyclingowi'] + freq['zmiany klimatyczne'] + freq['zielen'] + freq['fotowoltaiki'] + freq[
        'ekologiczne'] + freq['ekologii'] + freq['ekologiczna'] + freq['ekologiczny'] + freq['ekologia'] + freq[
              'ekologii'] + freq['ekologicznie'] + freq['ekologiczny']
    carbon = freq['wegla'] + freq['Wegiel'] + freq['weglem'] + freq['kopalni'] + freq['wegiel'] + freq['brunatny'] + \
             freq['weglu'] + freq['kopaln wegla']
    plastic = freq['plastikowych'] + freq['plastiku'] + freq['plastikowe'] + freq['plastikowy'] + freq['plastik'] + \
              freq['plastikowa']
    contamination = freq['zanieczyszczonej'] + freq['dwutlenku wegla'] + freq['zanieczyszczone'] + freq['dwutlenek'] + \
                    freq['zanieczyszcza'] + freq['smog'] + freq['emisje CO2'] + freq['smogiem'] + freq[
                        'czyste powietrze']
    other = freq['Unii Europejskiej'] + freq['Unia Europejska'] + freq['Greenpeace'] + freq['dnia Ziemi']

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('equal')
    label = ['Węgiel', 'Plastik', 'Zanieczyszczenie', 'Ekologia', 'Inne']
    data = [carbon, plastic, contamination, eko, other]

    font1 = {'family': 'sans-serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'sans-serif', 'color': 'black', 'size': 10}

    myexplode = [0.1, 0.1, 0.1]
    mycolors = ['#ab3e3e', '#4c95ff', '#ee8e3b', '#5cb85c', '#b7c92c']
    ax.pie(data, labels=label, autopct='%1.2f%%', shadow=False, startangle=0, colors=mycolors, textprops={'color': "w"})
    plt.legend(labels=label, loc='right', fontsize=10, prop={'size': 10}, bbox_to_anchor=(1.1, 0.5))
    plt.subplots_adjust(left=0.0, bottom=0.1, right=1)
    plt.title('SHARE OF VOICE', fontdict=font1, loc='center')

    plt.savefig('charts/share.png', bbox_inches='tight')
    plt.clf()
    return


def gender():
    df = pd.read_csv('CSV/source.csv',
                     usecols=["Rodzaj wzmianki", "Autor", "Tresc wypowiedzi", "Data stworzenia", "Domena", "Sentyment",
                              "Grupa domen", "Link do wypowiedzi", "Slowa kluczowe", "Plec", "comments", "followers",
                              "influenceScore"], delimiter=';', low_memory=False, encoding='latin-1')

    df['Plec'] = df['Plec'].astype(str)
    m = df[df['Plec'].str.contains("m", regex=False, flags=re.IGNORECASE)].count()
    men = m['Plec']

    f = df[df['Plec'].str.contains("f", regex=False, flags=re.IGNORECASE)].count()
    female = f['Plec']

    u = df[df['Plec'].str.contains("u", regex=False, flags=re.IGNORECASE)].count()
    unisex = u['Plec']

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('equal')
    label = ['Mężczyźni', 'Kobiety', 'Niesprecyzowane']
    data = [men, female, unisex]

    font1 = {'family': 'sans-serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'sans-serif', 'color': 'black', 'size': 10}

    myexplode = [0.1, 0.1, 0.1]
    mycolors = ['#ab3e3e', '#4c95ff', '#ee8e3b']
    ax.pie(data, labels=label, autopct='%1.2f%%', shadow=False, startangle=0, colors=mycolors, textprops={'color': "w"})
    plt.legend(labels=label, loc='right', fontsize=10, prop={'size': 10}, bbox_to_anchor=(1.1, 0.5))
    plt.subplots_adjust(left=0.0, bottom=0.1, right=1)
    plt.title('UDZIAŁ PŁCI W DYSKUSJI', fontdict=font1, loc='center')

    plt.savefig('charts/gender.png', bbox_inches='tight')
    plt.clf()
    return
