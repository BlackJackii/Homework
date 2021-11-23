#Task1 Используя модуль random и его функции randint напишите игру "математика 5кл".

import random

formulas = ("y=2x+3", "y=3x+15", "y=x+7")
rand_form = random.choice(formulas)
print(rand_form)
rand_x = random.randint(1, 10)
print(f"x = {rand_x}")
if rand_form == "y=2x+3":
    right_ans = 2*rand_x+3
elif rand_form == "y=3x+15":
    right_ans = 3*rand_x+15
elif rand_form == "y=x+7":
    right_ans = rand_x+7
inp_ans = int(input("Введите ответ: "))
if right_ans == inp_ans:
    print("Congrats! You are right:")
else:
    print("Nope. Next time think better. ")

#Task2 combinations из модуля itertools
import random

inp_word = input("Gimme 5 letter word: ")
while len(inp_word) != 5:
    inp_word = input("Nope, 5 letter pls: ")
count = 5
while count > 0:
    count -= 1
    new_word = ""
    changed_word = inp_word
    while len(new_word) < 5:
        index = random.randint(0, len(changed_word)-1)
        new_word += changed_word[index]
        changed_word = changed_word[0:index]+changed_word[index+1:]
    print(new_word)

#Task3 (Task1) The Guessing Game.
import random
random_num = random.randint(1, 10)
ans = input("Угадай число от 1 до 10: ")
if ans == random_num:
    print(f"Угадал! это число {random_num}")
else:
    print(f"Не угадал ='( число было {random_num}")

#Task4 (Task2) The birthday greeting program.

name = input("Enter your name: ")
age = int(input("How old are you?: "))
print(f"Hello {name.lower().title()}, on your next birthday you’ll be {age + 1} years”   ")

