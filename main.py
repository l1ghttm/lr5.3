with open('text.txt', 'r') as file:
    spis = file.read()

words= spis.split()

length=len(words)
print('Количество слов равно:',length)