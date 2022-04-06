#                                “Вычисления с помощью Numpy”

#Задание 1
#Импортируйте библиотеку Numpy и дайте ей псевдоним np.
#Создайте массив Numpy под названием a размером 5x2, то есть состоящий из 5 строк и 2 столбцов.
# Первый столбец должен содержать числа 1, 2, 3, 3, 1, а второй - числа 6, 8, 11, 10, 7. Будем считать, что каждый столбец - это признак, а строка - наблюдение. Затем найдите среднее значение по каждому признаку, используя метод mean массива Numpy. Результат запишите в массив mean_a, в нем должно быть 2 элемента.

import numpy as np
a = np.array([[1, 6],
             [2, 8],
             [3, 11],
             [3, 10],
             [1, 7]])
mean_a = a.mean(axis=0)
print(mean_a)
# [2.  8.4]

# Задание 2
# Вычислите массив a_centered, отняв от значений массива “а” средние значения соответствующих признаков, содержащиеся в массиве mean_a. 
# Вычисление должно производиться в одно действие. Получившийся массив должен иметь размер 5x2.

import numpy as np
a = np.array([[1, 6],
             [2, 8],
             [3, 11],
             [3, 10],
             [1, 7]])
mean_a = a.mean(axis=0)
a_centered = a - mean_a
print(a_centered)

# [[-1.  -2.4]
#  [ 0.  -0.4]
#  [ 1.   2.6]
#  [ 1.   1.6]
#  [-1.  -1.4]]



# Задание 3
# Найдите скалярное произведение столбцов массива a_centered. 
# В результате должна получиться величина a_centered_sp. Затем поделите a_centered_sp на N-1, где N - число наблюдений.


a_centered_sp = a_centered.T[0] @ a_centered.T[1]
print(a_centered_sp)
# 8
print(a_centered_sp / (a_centered.shape[0] - 1))
# 2



#                                               Тема “Работа с данными в Pandas”
# Задание 1
# Импортируйте библиотеку Pandas и дайте ей псевдоним pd. 
# Создайте датафрейм authors со столбцами author_id и author_name, 
# в которых соответственно содержатся данные: [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].


import pandas as pd

authors = pd.DataFrame({'author_id':[1, 2, 3],
                     'author_name':['Тургенев', 'Чехов', 'Островский']})
print(authors)


book = pd.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3],
                     'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
                     'price':[450, 300, 350, 500, 450, 370, 290]})
print(book)


# Задание 2
# Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.

authors_price = book.merge(authors, left_on='author_id', right_on='author_id', how='left')
print(authors_price)



# Задание 3
# Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.

top5 = authors_price.nlargest(5, 'price')
print(top5)


# Задание 4
# Создайте датафрейм authors_stat на основе информации из authors_price. 
# В датафрейме authors_stat должны быть четыре столбца:
# author_name, min_price, max_price и mean_price,
# в которых должны содержаться соответственно имя автора, минимальная, максимальная и средняя цена на книги этого автора.

authors_stat = pd.DataFrame(columns = ['author_name', 'min_price', 'max_price', 'mean_price'])
authors_stat['author_name'] = list(set(authors_price['author_name']))

for i in range(len(authors_stat)):
    ds = authors_price[authors_price['author_name'] == authors_stat.loc[i,'author_name'] ]
    authors_stat.loc[i, 'min_price']  = np.min(ds['price'])
    authors_stat.loc[i, 'max_price']  = np.max(ds['price'])
    authors_stat.loc[i, 'mean_price']  = np.mean(ds['price'])
print(authors_stat)















