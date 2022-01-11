"""Task 1
Create your own implementation of a built-in function enumerate,
named `with_index`, which takes two parameters:
`iterable` and `start`, default is 0.
Tips: see the documentation for the enumerate function
"""


def with_index(iterable, start=0):
    for i in enumerate(iterable, start):
        print(i)

with_index("qwerty")



"""Task 2
Create your own implementation of a built-in function range, 
named in_range(), which takes three parameters: `start`, `end`, 
and optional step. Tips: See the documentation for `range` function
"""


def in_range(start, end, step=1):
    for i in range(start, end, step):
        print(i)

in_range(1, 10, 2)



"""Task 3
Create your own implementation of an iterable, 
which could be used inside for-in loop. 
Also, add logic for retrieving elements using square brackets syntax.
"""

list_of_smth = ["Каждый", "день", "топчу", "асфальт"]


class IterSomething:
    def __iter__(self):
        self.iter_position = 0
        return self

    def __next__(self):
        if self.iter_position == len(list_of_smth):
            raise StopIteration
        rez = list_of_smth[self.iter_position]
        self.iter_position += 1
        return rez


iterate = IterSomething()
for i in iterate:
    print(i)


"""Task4*
Задание под звездочкой: написать генератор который будет из файла с реестра данных 
(ссылку кинул в чате в слаке) брать кусок xml превращать его в дикт и йелдом возвращать. """

import xmltodict
import json
import os


file_name = "17.2-EX_XML_EDR_FOP_FULL_04.01.2022.xml"


def new_gen(file_n):
    n = 1
    with open(file_n, "r") as file:
        for line in file:
            yield line
            print(f"Line counter = {n}")
            n += 1
            if n == 100:
                raise StopIteration


def read_json():
    with open("fop.json", "r", encoding="utf8") as file:
        return json.load(file)


def write_json(new_data):
    with open("fop.json", "w", encoding="utf8") as file:
        json.dump(new_data, file, ensure_ascii=False, indent=4)


def write_to_file(what_to_write):
    if os.path.exists("fop.json"):
        file = read_json()
        file.update(what_to_write)
        write_json(file)
    else:
        write_json(what_to_write)


def start():
    for line in new_gen(file_name):
        try:
            data = dict(xmltodict.parse(line)['SUBJECT'])
            key = data["RECORD"]
            new_dict = {}
            new_dict[key] = data["NAME"]
            write_to_file(new_dict)
        except:
            continue


if __name__ == '__main__':
    start()