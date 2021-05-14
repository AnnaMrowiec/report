
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

    font1 = {'family': 'serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}

    labels = source
    x = np.arange(len(labels))
    width = 0.4

    fig, ax = plt.subplots()

    ax.bar(x, neutral, width, color=('#0242d6'), label='Neutralny')   # color blue
    ax.bar(x, negative, width, color=('#e60b00'), label='Negatywny')  # color red
    ax.bar(x, positive, width, color=('#5cb85c'), label='Pozytywny')  # color green

    ax.set_xticks(np.arange(len(source)))
    ax.set_xticklabels(labels, rotation=45, ha='right')

    ax.set_title('Sentyment najpopularniejszych źródeł', fontdict=font1)
    ax.set_ylabel('Liczba wzmianek', fontdict=font2)
    ax.legend(labels=['Neutralne', 'Negatywne', 'Pozytywne'])

    plt.subplots_adjust(bottom=0.25)
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

    font1 = {'family': 'serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}

    labels = source
    x = np.arange(len(labels))
    width = 0.4

    fig, ax = plt.subplots()
    ax.bar(x, percent_mentions, width, color=('#ee8e3b'))  # color orange

    ax.set_xticks(np.arange(len(source)))
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.set_title('Udział procentowy źródeł', fontdict=font1)
    ax.set_ylabel('Procent wmianek', fontdict=font2)
    plt.subplots_adjust(bottom=0.25)

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

    font1 = {'family': 'serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}

    labels = source
    x = np.arange(len(labels))
    width = 0.4

    fig, ax = plt.subplots()
    ax.bar(x, percent_mentions_neutral, width, color=('#0242d6'), label='Neutralny')  # color blue
    ax.bar(x, percent_mentions_negative, width, color=('#e60b00'), label='Negatywny')  # color red
    ax.bar(x, percent_mentions_positive, width, color=('#5cb85c'), label='Pozytywny')  # color green

    ax.legend(labels=['Neutralne', 'Negatywne', 'Pozytywne'])

    ax.set_xticks(np.arange(len(source)))
    ax.set_xticklabels(labels, rotation=45, ha='right')

    ax.set_title('Udział procentowy sentymentu', fontdict=font1)
    ax.set_ylabel('Procent wmianek', fontdict=font2)
    plt.subplots_adjust(bottom=0.25)

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

    font1 = {'family': 'serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}

    labels = source
    x = np.arange(len(labels))
    width = 0.4

    fig, ax = plt.subplots()
    ax.bar(x - (width/2), percent_mentions_positive, width, color=('#5cb85c'))  # color green
    ax.bar(x + (width/2), percent_mentions_negative, width, color=('#e60b00'))  # color red

    ax.legend(labels=['Pozytywne', 'Negatywne'])

    ax.set_xticks(np.arange(len(source)))
    ax.set_xticklabels(labels, rotation=45, ha='right')

    ax.set_title('Udział procentowy sentymentu', fontdict=font1)
    ax.set_ylabel('Procent wmianek', fontdict=font2)
    plt.subplots_adjust(bottom=0.25)

    plt.savefig('charts/bar4.png', dpi=96)
    plt.clf()
    return