import codecs
import re
import matplotlib.pyplot as plt

def getting_text(): # получение списков стоп-слов и списка из исходного текста
    file = codecs.open("female.txt", encoding='utf-8', mode='r')
    female = file.read()
    text_rus = female.lower()
    rus = re.compile("([а-яА-ЯёЁ]+)") # убираем все то, что состоит не из русских букв
    text = rus.findall(text_rus)

    file_2 = codecs.open("stopwords-ru.txt", encoding='utf-8', mode='r')
    stop = file_2.read()
    stoplist = stop.split()

    counting_and_cleaning(text, stoplist)

def counting_and_cleaning(text, stoplist):
    itog = []

    flag = True
    for i in range(len(text)): # убираем из списка слов все стоп-слова
        for j in range(len(stoplist)):
            if text[i] == stoplist[j]:
                flag = False
                break
        if flag:
            itog.append(text[i])
        flag = True

    slovar = {}
    for key in itog:  # словарь ключ - слово, значение - кол-во повторений данного слова
        if key in slovar:
            value = slovar[key]
            slovar[key] = value + 1
        else:
            slovar[key] = 1

    sort_graph(slovar)


def sort_graph(slovar):

    w, num = [], []
    t = sorted(slovar.items(), key=lambda i: i[1], reverse=True) # сортировка по убыванию

    for i in t: # 20 самых частотных слов
        if len(w) < 20:
            w.append(i[0])
            num.append(i[1])

    plt.figure(figsize=(30, 30))
    plt.tick_params(axis='x', rotation=90)  # поворот подписи по оси х на 90 градусов
    plt.barh(w, num, color='purple')
    plt.xticks(rotation=0)
    plt.show()  # вывод гистограммы

getting_text()
