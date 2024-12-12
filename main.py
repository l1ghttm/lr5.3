with open('text.txt', 'r', encoding='utf-8') as file: # открытие файла 
    spis = file.read() #присваивание переменной к файлу

words = spis.split() #присваивание переменной через spis

length=len(words) #подчет переменной word
print('Количество слов равно:',length) #вывод
