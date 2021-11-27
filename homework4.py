#Task1
# Заполните лист 10ю рандомными значениями в промежутке 1-100. (Испольуя метод randint модуля random)
# Пока длинна листа меньше 10ти добавляйте к листу элемент.
# Пройдитесь циклом и найдите минимальное и максимальное значение Не используя встроенные методы.
# Выведете минимальное и максимальное значение списка используя встроенные методы.

from random import randint

new_list = []

while len(new_list) < 10:
    num = randint(1, 100)
    new_list.append(num)
print(new_list)

ans_max = 0
ans_min = 100

for element in new_list:
    if element > ans_max:
        ans_max = element
    if element < ans_min:
        ans_min = element

print(ans_max, ans_min)
print(max(new_list), min(new_list))


# Task2
#Преобразование типов и слайсы.
#Превратите полученную от пользователя строку в тапл.
# Выведите строку содержащую только буквы на четных позициях.

# exmpl = "Привіт"
# # ваш код
# # var1 = .....
# assert var1 == "Пиі"

word = "Привіт"
word = tuple(word)
index = 0
new_word = ""
#print(word)
for elem in word:
    if index %2 == 0:
        new_word += word[index]
    index += 1
print(new_word)



# Task3
# Сортировка и слайсы.
# В цикле пока пользователь не введет Q запрашивайте Фамилии игроков.
# Сложите их в лист. Отсортируйте лист используя втсроенную функцию.
# Выведите на экран получившийся список.
#
# Теперь пройдитесь циклом по списку и выведите
# Абрам играет с Яков
# Борис играет м Эдик
# (первый с последним, второй с предпоследним)


import random

new_list = []
while True:
    ans = input("Введите имя игрока. (Q for quit): ")
    if ans.lower() == "q":
        break
    if ans == "":
        continue
    new_list.append(ans)
new_list = sorted(new_list)
print(new_list)


first_index = 0
last_index = len(new_list)-1

n = 0
while n < len(new_list)/2:
    if len(new_list) == 1:
        add_more_player = input(f"{new_list[0]} не хочет играть сам с собой =( \nВведите имя второго игрока: ")
        new_list.append(add_more_player)
        print(f"{new_list[0]} играет с {new_list[1]}")
        break
    print(f"{new_list[first_index]} играет с {new_list[last_index]}")
    first_index += 1
    last_index -= 1
    if first_index == last_index:
        print(f"{new_list[first_index]} не играет ни с кем")
        last_player = input("Хотите, чтобы оставшийся игрок сыграл со случайным игроком? (Y\\N)")
        if last_player.lower() == "y":
            answer = random.choice([x for x in new_list if x != new_list[first_index]])
            print(f"{new_list[first_index]} играет с {answer}")
        break
    n += 1
print("Удачной игры!!!")



#task4
# Реверс.
# Создайте лист длинной 10 с подряд идущими значениями.
# Используя цикл переверните лист.
# (для этого надо поменять первый с последним, второй с предпоследним и так далее)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#var1
my_list.reverse()
print(my_list)

#var2
new_list = []
for i in my_list[::-1]:
    new_list.append(i)
print(new_list)

#var3
my_list = my_list[::-1]
print(my_list)

#var3
index_first = 0
index_last = len(my_list)-1
x = 0
while x < len(my_list)/2:
    my_list[index_first], my_list[index_last] = my_list[index_last], my_list[index_first]
    index_first += 1
    index_last -= 1
    x += 1
print(my_list)