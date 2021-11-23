# #Task1

inp_string = input("Enter a word: ")

if len(inp_string) > 1:
    outp_string = inp_string[0:2] + inp_string[-2:]
    print(outp_string)
else:
    print("")


# #Task2 phone number validation


def num_validation():
    num_check = False
    while num_check == False:
        inp_phone_num = input("Enter a phone number: ")
        if "+" in inp_phone_num:
            inp_phone_num = inp_phone_num.replace("+", "")
            #print(inp_phone_num)

        if inp_phone_num.isdigit() == True:
            #print("is digit")
            num_check = True
        else:
            print("Incorrect")
            num_validation()

        if len(inp_phone_num) == 10:
            print(f"Valid phone number. Thanks. +{inp_phone_num}")
            num_check = True
        elif len(inp_phone_num) < 10:
            print("Not enough numbers.")
            num_validation()
        elif len(inp_phone_num) > 10:
            print("Too much numbers.")
            num_validation()

if __name__ == '__main__':
    num_validation()


#Task3 namecheck

name = "tyler"
answ = input("Enter a name(tyler): ")
if answ.lower() == name:
    print("Correct")

#git Task1/Task2
holiday = False
day_of_week = int(input("Enter a day of week: "))
if day_of_week > 7 or day_of_week < 1:
    print("Ошибка! Дни недели считаются 1-7 ни больше ни меньше!")
elif day_of_week > 0 and day_of_week < 6:
    holiday = False
    print("Рабочий день")
elif day_of_week > 5 and day_of_week < 8:
    holiday = True
    print("Выходной")

wallet = int(input("Enter amount money u have: "))


if holiday == True and wallet == 0:
    print("оно то и можно погулять но не на что")
elif holiday == True and wallet > 1000:
    print("пиво и чипсы на большее денег нет")
elif holiday == True and wallet > 5000:
    print("гуляем в ресторане, всех угощаю")
elif holiday == False and wallet == 0:
    print("После Безоса следующим лечу я. И моя любимая кошка!")
else:
    print("работаем")

#git Task3

x = 0
while x <101:
    y = 3*x + 12
    print(y)
    x += 1

#git Task4 num validation

number = input("Enter a phone number (+38 *** *** *** **): ")
if "+" in number:
    number = number.replace("+", "")

if number[2:5] == "050":
    print("МТС")
elif number[2:5] == "067":
    print("Киевстар")
elif number[2:5] == "099":
    print("Водафон")
elif number[2:5] == "063":
    print("Лайф")

#git Task5

question = 'Маленькое беленькое на потолко висит не светит'
answer = 'лампочка'
exam = False
while exam == False:
    inp_ans = input(f"Отгадай загадку. {question} ").lower()
    if inp_ans == "q":
        print(f"Ok. Ans was {answer}")
        exam = True
    elif inp_ans == answer:
        print("Congrats!!! You win")
        exam = True
    else:
        print("Получше ничего не мог придумать?")

#git Task6

torment = True
ans = input("здравствуй, если хочешь узнать акции нажми 1, если тариф 2, если погоду 3  ")
while torment == True:
    if ans == "2":
        ans = input("узнать свой тариф 1, остаток по счету 3 ")
    elif ans == "3":
        ans = input("остаток по основному счету 1 остаток по бонусному 2 ")
    elif ans == "1":
        ans = input("остаток в гривнах 3 остаток в минутах/гигабайтах 2 ")
    elif ans.lower() == "q":
        print("на вашем счету 5 грн")
        torment = False
