import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
Bar 1-3 represents data from bar1.csv
Bar1 - Represents most popular sources
Bar2 - Represents calculated percent of mentions per source
Bar3 - Represents calculated percent of mentions per sentiment
'''

def bar1():
    chart = pd.read_csv('CSV/bar1.csv', delimiter=';', usecols=["Zrodlo", "Pozytywne", "Neutralne", "Negatywne"])
    source = chart['Zrodlo']
    positive = chart['Pozytywne']
    neutral = chart["Neutralne"]
    negative = chart["Negatywne"]

    font1 = {'family': 'sans-serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'sans-serif', 'color': 'black', 'size': 10}

    labels = source
    x = np.arange(len(labels))
    width = 0.4

    fig, ax = plt.subplots()

    ax.bar(x, neutral, width, color=('#22a1f0'), label='Neutralny')   # color blue
    ax.bar(x, negative, width, color=('#e60b00'), label='Negatywny')  # color red
    ax.bar(x, positive, width, color=('#5cb85c'), label='Pozytywny')  # color green

    ax.set_xticks(np.arange(len(source)))
    ax.set_xticklabels(labels, rotation=45, ha='right')

    ax.set_title('SENTYMENT NAJPOPULARNIEJSZYCH ŹRÓDEŁ', fontdict=font1)
    ax.set_ylabel('Liczba wzmianek', fontdict=font2)
    ax.legend(labels=['Neutralne', 'Negatywne', 'Pozytywne'])

    plt.subplots_adjust(bottom=0.25)
    plt.box(on=False)
    plt.tight_layout()

    plt.savefig('charts/bar1.png')
    plt.clf()
    return

def bar2():
    chart = pd.read_csv('CSV/bar1.csv', delimiter=';', usecols=["Zrodlo", "Pozytywne", "Neutralne", "Negatywne"])
    source = chart['Zrodlo']
    sum_mentions = chart['Sum'] = chart.sum(axis=1)
    total_number_mentions = chart['Sum'].sum()
    percent_mentions = round((chart['Sum'] * 100)/total_number_mentions, 2)

    '''
    sum_mentions = sum of positive, negative, and neutral mentions per each source
    total_number_mentions = sum of all mentions in all sources
    percent_mentions = it is a percent of mentions per each channel f.ex. the twitter covered 40% of all mentions
    '''

    font1 = {'family': 'sans-serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'sans-serif', 'color': 'black', 'size': 10}

    labels = source
    x = np.arange(len(labels))
    width = 0.4

    fig, ax = plt.subplots()
    ax.bar(x, percent_mentions, width, color=('#ee8e3b'))  # color orange

    ax.set_xticks(np.arange(len(source)))
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.set_title('UDZIAŁ PROCENTOWY ŹRÓDEŁ', fontdict=font1)
    ax.set_ylabel('Procent wmianek', fontdict=font2)
    plt.subplots_adjust(bottom=0.25)
    plt.box(on=False)

    plt.savefig('charts/bar2.png', dpi=96)
    plt.clf()
    return

def bar3():
    chart = pd.read_csv('CSV/bar1.csv', delimiter=';', usecols=["Zrodlo", "Pozytywne", "Neutralne", "Negatywne"])
    source = chart['Zrodlo']
    sum_mentions = chart['Sum'] = chart.sum(axis=1)
    total_number_mentions = chart['Sum'].sum()
    percent_mentions_positive = round((chart['Pozytywne'] * 100)/total_number_mentions, 2)
    percent_mentions_negative = round((chart['Negatywne'] * 100)/total_number_mentions, 2)
    percent_mentions_neutral = round((chart['Neutralne'] * 100)/total_number_mentions, 2)

    '''
    sum_mentions = sum of positive, negative, and neutral mentions per each source
    total_number_mentions = sum of all mentions in all sources
    percent_mentions_xyz = percent of mentions per each sentiment rate
    '''

    font1 = {'family': 'sans-serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'sans-serif', 'color': 'black', 'size': 10}

    labels = source
    x = np.arange(len(labels))
    width = 0.4

    fig, ax = plt.subplots()
    ax.bar(x, percent_mentions_neutral, width, color=('#22a1f0'), label='Neutralny')  # color blue
    ax.bar(x, percent_mentions_negative, width, color=('#e60b00'), label='Negatywny')  # color red
    ax.bar(x, percent_mentions_positive, width, color=('#5cb85c'), label='Pozytywny')  # color green

    ax.legend(labels=['Neutralne', 'Negatywne', 'Pozytywne'])

    ax.set_xticks(np.arange(len(source)))
    ax.set_xticklabels(labels, rotation=45, ha='right')

    ax.set_title('UDZIAŁ PROCENTOWY SENTYMENTU', fontdict=font1)
    ax.set_ylabel('Procent wmianek', fontdict=font2)
    plt.subplots_adjust(bottom=0.25)
    plt.box(on=False)

    plt.savefig('charts/bar3.png', dpi=96)
    plt.clf()
    return

def bar4():
    chart = pd.read_csv('CSV/bar1.csv', delimiter=';', usecols=["Zrodlo", "Pozytywne", "Neutralne", "Negatywne"])
    source = chart['Zrodlo']
    sum_mentions = chart['Sum'] = chart.sum(axis=1)
    total_number_mentions = chart['Sum'].sum()
    percent_mentions_positive = round((chart['Pozytywne'] * 100)/total_number_mentions, 2)
    percent_mentions_negative = round((chart['Negatywne'] * 100)/total_number_mentions, 2)

    '''
    sum_mentions = sum of positive, negative, and neutral mentions per each source
    total_number_mentions = sum of all mentions in all sources
    percent_mentions_xyz = percent of mentions per each sentiment rate
    '''

    font1 = {'family': 'sans-serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'sans-serif', 'color': 'black', 'size': 10}

    labels = source
    x = np.arange(len(labels))
    width = 0.4

    fig, ax = plt.subplots()
    ax.bar(x - (width/2), percent_mentions_positive, width, color=('#5cb85c'))  # color green
    ax.bar(x + (width/2), percent_mentions_negative, width, color=('#e60b00'))  # color red

    ax.legend(labels=['Pozytywne', 'Negatywne'])

    ax.set_xticks(np.arange(len(source)))
    ax.set_xticklabels(labels, rotation=45, ha='right')

    ax.set_title('UDZIAŁ PROCENTOWY SENTYMENTU', fontdict=font1)
    ax.set_ylabel('Procent wmianek', fontdict=font2)
    plt.subplots_adjust(bottom=0.25)
    plt.box(on=False)

    plt.savefig('charts/bar4.png', dpi=96)
    plt.clf()
    return

def bar5():
    df = pd.read_csv('CSV/source.csv', usecols=["Sentyment", "Slowa kluczowe"], delimiter=';', low_memory=False,
                     encoding='latin-1')

    positive = df[df['Sentyment'] == 'POSITIVE'][['Slowa kluczowe', 'Sentyment']]
    positive = positive['Slowa kluczowe']
    freq_pos = positive.value_counts()

    positive_carbon = freq_pos['wegla'] + freq_pos['weglem wegla'] + freq_pos['weglem'] + freq_pos['Wegiel Weglu'] + \
                      freq_pos['wegiel'] + freq_pos['wegla sektora weglowego'] + freq_pos['kopalnia'] + freq_pos[
                          'kopalnie'] + freq_pos['wegiel brunatny weglowych'] + freq_pos['@KopalniaR'] + freq_pos[
                          'Dzien wegla weglowej'] + freq_pos['Weglowe'] + freq_pos['wegiel Weglowych weglowych'] + \
                      freq_pos['weglem górniczych górnikami wydobycia wegla kamiennego Wegiel'] + freq_pos[
                          'kopaln Kopalnie'] + freq_pos['Górnik wegla'] + freq_pos['Wegiel Weglem!'] + freq_pos[
                          'weglem wegla sektora weglowego'] + freq_pos['kopalnianych'] + freq_pos['energii wegla'] + \
                      freq_pos['wegiel wegla'] + freq_pos['weglu'] + freq_pos['weglowe'] + freq_pos[
                          'weglowych weglowa'] + freq_pos['Górnicy górników kopaln Kopalnie'] + freq_pos[
                          'górnikami weglem'] + freq_pos['Weglu Wegiel Wegla']
    positive_plastic = freq_pos['plastikowych'] + freq_pos['plastikowe'] + freq_pos['plastiku'] + freq_pos[
        'Plastikowa plastikowa'] + freq_pos['plastik plastiku smieci plastikowych plastikowy'] + freq_pos['plastik'] + \
                       freq_pos['plastikowa'] + freq_pos['plastikowa plastiku'] + freq_pos['plastikowym'] + freq_pos[
                           'Plastik'] + freq_pos['plastiki'] + freq_pos['plastikowy'] + freq_pos['(plastikowa'] + \
                       freq_pos['(plastiki'] + freq_pos['plastikiem'] + freq_pos['smieci plastikowa'] + freq_pos[
                           'plastiku plastikowych plastik'] + freq_pos['plastikowymi'] + freq_pos[
                           'uniwersalna plastik'] + freq_pos['Smieci plastikowych'] + freq_pos['wydobywac plastików'] + \
                       freq_pos['plastików plastiku'] + freq_pos['plastikach'] + freq_pos[
                           'smieci Plastikowa smieciowe'] + freq_pos['dnia plastikowy']
    positive_contamination = freq_pos['dwutlenku wegla'] + freq_pos['zanieczyszczone'] + freq_pos['zanieczyszczonej'] + \
                             freq_pos['smogu'] + freq_pos['dwutlenek'] + freq_pos['dwutlenek wegla'] + freq_pos[
                                 'smieci zanieczyszczaja dwutlenku wegla'] + freq_pos['czystym klimat'] + freq_pos[
                                 'zanieczyszczone powietrze'] + freq_pos['zanieczyszcza']
    positive_eco = freq_pos['ekologiczne'] + freq_pos['zielen'] + freq_pos['ekologiczny'] + freq_pos['Ekologia'] + \
                   freq_pos['ekologiczna'] + freq_pos['#ekologia'] + freq_pos['ekologiczne dlugo'] + freq_pos[
                       'ekologicznego'] + freq_pos['ekologicznej'] + freq_pos['recyclingowi'] + freq_pos[
                       'fotowoltaiczne'] + freq_pos['sprzataniu swiata'] + freq_pos['energie Ekologicznie'] + freq_pos[
                       'czystym klimat'] + freq_pos['energii Ekologiczne'] + freq_pos[
                       'https://pvstar.pl/pol_m_Panele-fotowoltaiczne-152.html fotowoltaicznych'] + freq_pos[
                       'zmiana zielen'] + freq_pos['Energia dzien zielonej'] + freq_pos[
                       'smieci ekologie plastikowych dnia'] + freq_pos['zmiana recyclingowi'] + freq_pos[
                       'ekologicznie'] + freq_pos['Czystsze powietrze zielonym'] + freq_pos[
                       'KLIMAT zmianach klimatu #klimat'] + freq_pos['sprzatali swiat'] + freq_pos[
                       'odnawialnych zródel energii'] + freq_pos['ochrone srodowiska'] + freq_pos['Dzien ziemi'] + \
                   freq_pos['elektryczne fotowoltaicznych'] + freq_pos[
                       'Energy odnawialnych zródel energii fotowoltaiki ekologiczna'] + freq_pos['ekologiczne!'] + \
                   freq_pos['fotowoltaicznych'] + freq_pos['odnawialne zródla energii'] + freq_pos[
                       'fotowoltaicznych https://pvstar.pl/pol_m_Panele-fotowoltaiczne-152.html.'] + freq_pos[
                       'srodowisko ekologiczna'] + freq_pos['Ekologiczny'] + freq_pos[
                       'dzien-noc swiatla klimat czystosci'] + freq_pos['#czystepowietrze Dzien Czyste Powietrze'] + \
                   freq_pos['ekologa']

    negative = df[df['Sentyment'] == 'NEGATIVE'][['Slowa kluczowe', 'Sentyment']]
    negative = negative['Slowa kluczowe']
    freq = negative.value_counts()

    negative_carbon = freq['wegla'] + freq['kopaln wegla'] + freq['wegla sektora weglowego'] + freq['wegiel'] + freq[
        'górnikami weglem'] + freq['wegiel wegla'] + freq['weglem'] + freq['zanieczyszczone weglowych'] + freq[
                          'kopalni'] + freq['kopalnia'] + freq['weglu dwutlenku wegla'] + freq['kopalnie'] + freq[
                          'https://czyztak.pl/kategoria/informacje/duda-chce-zastapic-wegiel-atomem wegiel'] + freq[
                          'górnicy górnictwa wegla kamiennego Górnicy'] + freq['kopalniach'] + freq[
                          'go´rnikami kopalni we?glowych we?glowe Strajk'] + freq['wegiel Weglowych weglowych'] + freq[
                          'weglowego klimat https://www.bankier.pl/wiadomosc/Prezydent-Polska-partycypuje-w-ambitnych-dazeniach-UE-w-zakresie-ochrony-klimatu-8099145.html'] + \
                      freq['weglowej'] + freq['polityka wegla'] + freq[
                          'górników kopaln https://polityczek.pl/twitter/15090-jachira-kopalnie-powinny-byc-zamkniete-w-ciagu-10-lat-3 Kopalnie'] + \
                      freq['Weglowe'] + freq['wegla weglowej'] + freq['weglowe Strajk'] + freq[
                          'weglowych górnikami kopalnie wegla']
    negative_plastic = freq['plastikowych'] + freq['plastiku'] + freq['plastikowy'] + freq['plastik plastiku'] + freq[
        'plastikowa'] + freq['CZYSTEK plastikowych'] + freq['plastikami plastik smieci'] + freq['Unii plastikowych'] + \
                       freq['polityka plastikowych'] + freq['plastik plastikiem'] + freq['dnia plastikowych'] + freq[
                           'smieci plastiku'] + freq['smieci plastikiem']
    negative_contamination = freq['zanieczyszczone weglowych'] + freq['dwutlenku wegla (smiech'] + freq[
        'weglu dwutlenku wegla'] + freq['zanieczyszczonej'] + freq['emisje CO2'] + freq['smogiem'] + freq[
                                 'dwutlenek wegla'] + freq['palenie smieci'] + freq['dnia emisje CO2'] + freq[
                                 'emisji CO2'] + freq['smogu wegiel'] + freq['zanieczyszcza'] + freq[
                                 'weglem zanieczyszczone weglowych'] + freq['dwutlenkiem wegla'] + freq[
                                 'dwutlenku we?gla'] + freq['emisji cieplarnianych wegla'] + freq['@Smogowym']
    negative_eco = freq['recyclingowi'] + freq['ekologii'] + freq['ochrony srodowiska'] + freq['ekologicznie'] + freq[
        'fotowoltaike'] + freq['ochrone srodowiska'] + freq['Katastrofa ekologiczna'] + freq[
                       'neutralnosc klimatyczna swiata'] + freq['ekologicznego'] + freq['swiata ochrone srodowiska'] + \
                   freq['zmian klimatu czystej'] + freq['dzien dniem ziemi'] + freq['fotowoltaike Unii'] + freq[
                       'fotowoltaike https://www.wprost.pl/polityka/10437675/superwizjer-o-gigantycznych-srodkach-na-fotowoltaike-dlaspolek-parafialnych.html'] + \
                   freq['ekologii wegla'] + freq['recyclingu'] + freq[
                       'katastrofie polityke neutralnosci klimatycznej'] + freq['ochronie srodowiska'] + freq[
                       'ekologiczny wegla'] + freq['Dzien Ziemi sprzatanie'] + freq['ekologii ochronie klimatu']

    positive_mentions = [positive_carbon, positive_plastic, positive_contamination, positive_eco]
    negative_mentions = [negative_carbon, negative_plastic, negative_contamination, negative_eco]

    font1 = {'family': 'sans-serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'sans-serif', 'color': 'black', 'size': 10}

    labels = ['Węgiel', 'Plastik', 'Zanieczyszczenie', 'Ekologia']
    x = np.arange(len(labels))
    width = 0.4

    fig, ax = plt.subplots()
    ax.bar(x - (width / 2), positive_mentions, width, color=('#5cb85c'))  # color green
    ax.bar(x + (width / 2), negative_mentions, width, color=('#e60b00'))  # color red

    ax.legend(labels=['Pozytywne', 'Negatywne'])

    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha='right')

    ax.set_title('SENTYMENT WZMIANEK W TEMACIE', fontdict=font1)
    ax.set_ylabel('Liczba wzmianek', fontdict=font2)
    plt.subplots_adjust(bottom=0.25)
    plt.box(on=False)
    plt.savefig('charts/bar5.png', dpi=96)
    plt.clf()

    return

def bar6():
    df = pd.read_csv('CSV/source.csv',
                     usecols=["Rodzaj wzmianki", "Autor", "Tresc wypowiedzi", "Data stworzenia", "Domena", "Sentyment",
                              "Grupa domen", "Link do wypowiedzi", "Slowa kluczowe", "Plec", "comments", "followers",
                              "influenceScore"], delimiter=';', low_memory=False, encoding='latin-1')

    df['Plec'] = df['Plec'].astype(str)
    m = df[df['Plec'].str.contains("m", regex=False, flags=re.IGNORECASE)].count()
    men = m['Plec']

    f = df[df['Plec'].str.contains("f", regex=False, flags=re.IGNORECASE)].count()
    female = f['Plec']

    font1 = {'family': 'sans-serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'sans-serif', 'color': 'black', 'size': 10}

    labels = ['Płeć']
    x = np.arange(len(labels))
    width = 0.4

    fig, ax = plt.subplots()
    ax.bar(x - (width / 2), men, width, color=('#5cb85c'))  # color green
    ax.bar(x + (width / 2), female, width, color=('#22a1f0'))  # color blue

    ax.legend(labels=['Mężczyźni', 'Kobiety'])

    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha='right')

    ax.set_title('LICZBA WZMIANEK WG PŁCI', fontdict=font1)
    ax.set_ylabel('Liczba wzmianek', fontdict=font2)
    plt.subplots_adjust(bottom=0.25)
    plt.box(on=False)
    plt.savefig('charts/bar6.png', dpi=96)
    plt.clf()
    return
