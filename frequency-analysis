import codecs
import re
import json
import pymorphy2
import plotly.express as px
import pandas #требуется для plotly.express


file = codecs.open("letnyayashkola_vk.json","r",encoding="utf-8")
text = file.read()
parsed_str = json.loads(text)

text_posts, text_comments  = [], []

def acquisition():
    # получение необходимых текстовых данных в списки для постов
    for i in range(len(parsed_str)): # для постов - title и сам пост
        if 'attachments' in dict.keys(parsed_str[i]):
            text_posts.append(parsed_str[i]['text'])
            for j in range(len(parsed_str[i]['attachments'])):
                if 'link' in dict.keys(parsed_str[i]['attachments'][j]):
                    if 'description' in dict.keys(parsed_str[i]['attachments'][j]['link']):
                        text_posts.append(parsed_str[i]['attachments'][j]['link']['title'])
    counting(text_posts, 'для постов')

def acquisition_1():
    for i in range(len(parsed_str)):
        if 'textcomment' in dict.keys(parsed_str[i]): #для комментов
            if 'items' in dict.keys(parsed_str[i]['textcomment']):
                for j in range(len(parsed_str[i]['textcomment']['items'])):
                    text_comments.append(parsed_str[i]['textcomment']['items'][j]['text'])
    counting(text_comments, 'для комментариев')

def pos(word, morth=pymorphy2.MorphAnalyzer()): # проверка граммер через морфологический словарь
    return morth.parse(word)[0].tag.POS

def word_processing(value): # обработка текста от чисел и предлогов
    mass = []
    #functors_pos = {'INTJ', 'PRCL', 'CONJ', 'PREP', 'NPRO'}  # убрать: междометье, частица, союз, предлог, местоимение
    text_1 = ' '.join(value)
    string = text_1.lower()
    string = list(string.split())
    for i in range(len(string)):
        symbol = re.sub("[^а-я-]", "", string[i])
        # .translate({ord(i): None for i in '?.()«°№1234567890=[]@""/''\|_>#<…:»;!,'})
        if len(symbol) > 1:
            #if pos(symbol) not in functors_pos: #удаление
            h = 0
            while symbol[h] == "-": # сохранение дефиса в середине слова, удаление, если "-" в конце слова или начале
                h += 1
                if len(symbol) <= h:
                    break
            symbol = symbol[h:]
            if len(symbol) >= 2:
                p = len(symbol)-1
                if symbol[p] == "-":
                    symbol = symbol[0:p]
            mass.append(symbol)
    return mass

def counting(value, signal): # составление словаря для подсчета самых часто встречающихся слов
    string = word_processing(value)
    text = {}

    for key in string: # создание частотного словаря из всех обратобанных слов, где ключ - слово, значение - кол-во повторений
        if key in text:
            value = text[key]
            text[key] = value + 1
        else:
            text[key] = 1
    word, count = [], []
    functors_pos = {'INFN', 'VERB'} #глаголы и инф.
    for k, v in text.items():
        if v >= 40: # провекра частоты повторений слова (беру от 40 раз)
            if pos(k) in functors_pos:
                word.append(str(k))
                count.append(int(v))
    grafic_return(word, count, signal)

def grafic_return(word, count, signal): # построение графиков
    fig = px.pie(word, values=count, names=word, title="Анализ частоты глаголов "+ signal)
    fig.show()

if __name__ == "__main__":
    acquisition() #посты
    acquisition_1() # #комментарии
