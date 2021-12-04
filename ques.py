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