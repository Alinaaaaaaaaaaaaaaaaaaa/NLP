import codecs
import re

def open_file(name):
    file_1 = codecs.open(name, encoding='utf-8', mode='r') # Открытие файлов
    file = file_1.read()
    alg_changes(name, file)

def alg_changes(name, file): # обработка файла заменяемых слов
    file_4 = codecs.open("changes.csv", encoding='utf-8', mode='r')  # Открытие файла
    changes = file_4.read()
    list = changes.split()

    isxod, zamen = [], []

    for i in range(1, len(list)):
        for j in range(1, len(list[i])):
            if list[i][j] == ',':
                isxod.append(list[i][:j]) # массив со словами, которые требуется заменить
                zamen.append(list[i][j+1:]) # массив со словами, НА которые требуется заменить исходные слова

    alina(name, file, isxod, zamen)

def alina(name, file, isxod, zamen):
    k = file
    symbol_start = [' ','_', '—', '-', '(', '[', '\n'] # символы, которые могует встретиться перед искомой строкой
    symbol_fin = [':', ',', ';', '-', '!','_', '—', ' ', '\n', '.', ']', ')'] #  символы, которые могует встретиться после искомой строки

    for i in range(len(zamen)):
        for j in symbol_start:
            for q in symbol_fin:
                IS = isxod[i][0].capitalize() + isxod[i][1:] # поиск исходной строки, если она начинается с заглавной буквы
                ZAM = zamen[i][0].capitalize() + zamen[i][1:] # замена на такую же заглавную букву
                kkk = '\\' + j + isxod[i] + '\\'+ q # добавление экранирования для всех символов, чтобы они не читались в re.sub как регулярные выражения,->
                new = '\\' + j + IS + '\\'+ q # /W использовать не удалось, так как необходимо знать какие символы были перед строкой и после ->
                aaa = j + zamen[i] + q # для их сохранения в строке
                new_zamena = j + ZAM + q
                k = re.sub(kkk, aaa, k)
                k = re.sub(new, new_zamena, k)
    write_txt(name, k)

def write_txt(name, k): # запись в файл
    name1 = 'duplicate'+name
    my_file = open(name1, encoding='utf-8', mode="w")
    my_file.write(k) # при записи текста в файл добавляются лишние пустые строки из-за кодировки (скорее всего)
    my_file.close()

open_file("Язык.txt")
open_file("Goty_subkultura.txt")
open_file("Обыкновенный ёж.txt")




