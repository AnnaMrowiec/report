# created on 2021-04-16 at 12:46 by Anna Mrowiec
# ended on 2021-04-16 at 16:45 by Anna Mrowiec

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.image as image

'''
Graph 1 is collecting data from chart1.csv
- It represents the data of the number of mentions in the project
Graph 2 is collecting data from chart2.csv
- It represents the data of the reach of mentions in the project
Graph 3 is collecting data from chart3.csv
- It represents the amount of mentions per specific source
Graph 4 is collecting data from chart4.csv
- It represents the amount of mentions per gender of the user
Graph 5 is collecting data from chart4.csv
- It represents the calculated value of percentage amount of gender in all mentions
'''

def graph1():
    chart = pd.read_csv('chart1.csv', delimiter=';', usecols=["Date", "Number"])
    date = chart['Date']
    number = chart['Number']

    # Setting fonts and colours for the chart
    font1 = {'family': 'serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}

    with cbook.get_sample_data(r'C:\Users\Anna Kaczmarczyk\Desktop\raport_buzz\sot.png') as file:
        img = image.imread(file)

    plt.plot(date, number, '#ee8e3b')   # color orange
    plt.grid(axis="y", color='gray', ls='-.', lw=0.25)
    plt.xticks(np.arange(0, len(date) + 1, 7))
    plt.ticklabel_format(useOffset=False, style='plain', axis='y')
    plt.ylim(ymin=0)
    plt.xlim(xmin=0)
    plt.title('Rozkład wzmianek w czasie', fontdict=font1)
    plt.xlabel('Czas', fontdict=font2)
    plt.ylabel('Liczba wzmianek', fontdict=font2)

    plt.figimage(img, xo=100, yo=200, zorder=1, alpha=0.25)
    plt.savefig('chart1.png', dpi=96)
    plt.clf()
    return

def graph2():
    chart = pd.read_csv('chart2.csv', delimiter=';', usecols=["Date", "Number"])
    date = chart['Date']
    number = chart['Number']

    # Setting fonts and colours for the chart
    font1 = {'family': 'serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}

    with cbook.get_sample_data(r'C:\Users\Anna Kaczmarczyk\Desktop\raport_buzz\sot.png') as file:
        img = image.imread(file)

    plt.plot(date, number, '#ee8e3b')   # color orange
    plt.grid(axis="y", color='gray', ls='-.', lw=0.25)
    plt.xticks(np.arange(0, len(date) + 1, 7))
    plt.ticklabel_format(useOffset=False, style='plain', axis='y')
    plt.subplots_adjust(left=0.16)
    plt.ylim(ymin=0)
    plt.xlim(xmin=0)
    plt.title('Zasięg wzmianek w czasie', fontdict=font1)
    plt.xlabel('Czas', fontdict=font2)
    plt.ylabel('Zasięg', fontdict=font2)

    plt.figimage(img, xo=100, yo=200, zorder=1, alpha=0.25)
    plt.savefig('chart2.png', dpi=96)
    plt.clf()
    return

def graph3():
    chart = pd.read_csv('chart3.csv', delimiter=';', usecols=["Date", "Twitter", "Fora", "Facebook", "Portale"])
    date = chart['Date']
    twitter = chart["Twitter"]
    fora = chart["Fora"]
    facebook = chart["Facebook"]
    portals = chart["Portale"]

     # Setting fonts and colours for the chart
    font1 = {'family': 'serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}

    with cbook.get_sample_data(r'C:\Users\Anna Kaczmarczyk\Desktop\raport_buzz\sot.png') as file:
        img = image.imread(file)

    plt.plot(date, twitter, '#ee8e3b', label="Twitter")    # color orange
    plt.plot(date, facebook, '#5cb85c', label="Facebook")  # color green
    plt.plot(date, portals, '#4c95ff', label="Portals")    # color blue
    plt.legend(loc="upper left", labels=['Twitter', 'Facebook', 'Portals'])
    plt.grid(axis="y", color='gray', ls='-.', lw=0.25)
    plt.xticks(np.arange(0, len(date) + 1, 7))
    plt.ylim(ymin=0)
    plt.xlim(xmin=0)
    plt.title('Rozkład wzmianek w czasie wg źródeł', fontdict=font1)
    plt.xlabel('Czas', fontdict=font2)
    plt.ylabel('Liczba wzmianek', fontdict=font2)

    plt.figimage(img, xo=100, yo=200, zorder=1, alpha=0.25)
    plt.savefig('graph3.png', dpi=96)
    plt.clf()
    return

def graph4():
    chart = pd.read_csv('chart4.csv', delimiter=';', usecols=["Date", "Kobiety", "Mezczyzni"])
    date = chart['Date']
    women = chart['Kobiety']
    men = chart['Mezczyzni']

    # Setting fonts and colours for the chart
    font1 = {'family': 'serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}

    with cbook.get_sample_data(r'C:\Users\Anna Kaczmarczyk\Desktop\raport_buzz\sot.png') as file:
        img = image.imread(file)

    plt.plot(date, women, '#ee8e3b', label='Kobiety')  # color orange
    plt.plot(date, men, '#5cb85c', label='Mężczyźni')  # color green
    plt.legend(loc="upper left")
    plt.grid(axis="y", color='gray', ls='-.', lw=0.25)
    plt.xticks(np.arange(0, len(date) + 1, 7))
    plt.ylim(ymin=0)
    plt.xlim(xmin=0)
    plt.title('Rozkład wzmianek w czasie wg płci autora', fontdict=font1)
    plt.xlabel('Czas', fontdict=font2)
    plt.ylabel('Liczba wzmianek', fontdict=font2)

    plt.figimage(img, xo=100, yo=200, zorder=1, alpha=0.25)
    plt.savefig('graph4.png', dpi=96)
    plt.clf()
    return

def graph5():
    chart = pd.read_csv('chart4.csv', delimiter=';', usecols=["Date", "Kobiety", "Mezczyzni"])
    date = chart['Date']
    sum_gender = chart['Sum'] = chart.sum(axis=1)
    total_number_mentions = chart['Sum'].sum()
    percent_mentions_women = round((chart['Kobiety'] * 100)/total_number_mentions, 2)
    percent_mentions_men = round((chart['Mezczyzni'] * 100)/total_number_mentions, 2)

    '''
    sum_gender = sum of mentions per each day men + women
    total_number_mentions = sum of all mentions in all days
    percent_mentions = percent of mentions per each gender and each day 
    '''

    font1 = {'family': 'serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}

    with cbook.get_sample_data(r'C:\Users\Anna Kaczmarczyk\Desktop\raport_buzz\sot.png') as file:
        img = image.imread(file)

    plt.plot(date, percent_mentions_women, '#ee8e3b', label='Kobiety')  # color orange
    plt.plot(date, percent_mentions_men, '#5cb85c', label='Mężczyźni')  # color green
    plt.grid(axis="y", color='gray', ls='-.', lw=0.25)
    plt.xticks(np.arange(0, len(date) + 1, 7))
    plt.ylim(ymin=0)
    plt.xlim(xmin=0)
    plt.legend(loc="upper left")
    plt.title('Procentowy udział płci', fontdict=font1)
    plt.xlabel('Czas', fontdict=font2)
    plt.ylabel('Procent wzmianek', fontdict=font2)

    plt.figimage(img, xo=100, yo=200, zorder=1, alpha=0.25)
    plt.savefig('graph5.png', dpi=96)
    plt.clf()
    return
