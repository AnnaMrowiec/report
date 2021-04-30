import pandas as pd
import matplotlib.pyplot as plt

desired_width = 620
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 44)
pd.set_option('display.max_rows', 100)

def pie1():
    df = pd.read_csv('source.csv', usecols=["Rodzaj wzmianki", "Autor", "Tresc wypowiedzi", "Data stworzenia", "Domena", "Sentyment", "Grupa domen", "Link do wypowiedzi", "Slowa kluczowe", "Plec", "comments", "followers", "influenceScore"], delimiter=';', low_memory=False, encoding='latin-1')

    df = df['Slowa kluczowe']
    freq = df.value_counts()
    all_keywords = sum(freq)

    eko = freq['recyclingowi'] + freq['zmiany klimatyczne'] + freq['zielen'] + freq['fotowoltaiki'] + freq['ekologiczne'] + freq['ekologii'] + freq['ekologiczna'] + freq['ekologiczny'] + freq['ekologia'] + freq['ekologii'] + freq['ekologicznie'] + freq['ekologiczny']
    carbon = freq['wegla'] + freq['Wegiel'] + freq['weglem'] + freq['kopalni'] + freq['wegiel'] + freq['brunatny'] + freq['weglu'] + freq['kopaln wegla']
    plastic = freq['plastikowych'] + freq['plastiku'] + freq['plastikowe'] + freq['plastikowy'] + freq['plastik'] + freq['plastikowa']
    contamination = freq['zanieczyszczonej'] + freq['dwutlenku wegla'] + freq['zanieczyszczone'] + freq['dwutlenek'] + freq['zanieczyszcza'] + freq['smog'] + freq['emisje CO2'] + freq['smogiem'] + freq['czyste powietrze']
    other = freq['Unii Europejskiej'] + freq['Unia Europejska'] + freq['Greenpeace'] + freq['dnia Ziemi']

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('equal')
    label = ['Ekologia', 'Zanieczyszczenie', 'Węgiel', 'Plastik', 'Inne']
    data = [eko, contamination, carbon, plastic, other]

    font1 = {'family': 'serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}

    myexplode = [0.1, 0.1, 0.1]
    mycolors = ['#5cb85c', '#ee8e3b', '#ab3e3e', '#4c95ff', '#b7c92c']
    ax.pie(data, labels=label, autopct='%1.2f%%', shadow=False, startangle=180, colors=mycolors, textprops={'color': "w"})
    plt.legend(labels=label, loc='right', fontsize=10, prop={'size': 10}, bbox_to_anchor=(1.1, 0.5))
    plt.subplots_adjust(left=0.0, bottom=0.1, right=1)
    plt.title('Udział procentowy tematów w łącznej liczbie wzmianek', fontdict=font1, loc='left')

    plt.savefig('pie.png', bbox_inches='tight')
    plt.clf()
    return