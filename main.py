import random
# импортирование random для рандомного выбора

# числа, буквы для генерации паролей
generation = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

# запрос количества паролей
number = input('Введите количество паролей для генерации:  ' + "\n")
# запрос длины для паролей 
length = input('Введите нужную длину для пароля(-лей):  ' + "\n")

# преобразование введенных значений в числа
number = int(number)
length = int(length)

# цикл для генерации количества паролей
for n in range(number):
    # создание пустой переменной
    password = ''
    
    # цикл для генерации пароля с учетом введенной длины
    for i in range(length):
        # заполнение переменной сгенерированными паролями
        password += random.choice(generation)

    # вывод паролей
    print(password)
