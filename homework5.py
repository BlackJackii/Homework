#Task1
#
some_string = "Gogi 32 Anton 28 46 HuanPablo 348 Lolita 666 HuanPablo, Anton"
some_string = some_string.replace(",", "").split(" ")
new_dict = {}
for i in some_string:
    new_dict.update({i: some_string.count(i)})
print(new_dict)

#
#Task2
#Input data:

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
new_dict = {}
for i in stock:
    if i in prices:
        new_dict[i] = stock[i] * prices[i]

# new_dict = dict((stock[i]*prices[i] for i in stock if i in prices)) - пытался изобразить в выражении, но получается какой то бред. Как это сделать?
# print(new_dict)



#Task 3
#Use a list comprehension to make a list containing tuples (i, j)
# where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.
import random
j = [i**2 for i in range(1, 10)]
print(j)
