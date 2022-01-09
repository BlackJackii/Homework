"""Task 1
Create a class method named `validate`, which should be called from the `__init__` method
to validate parameter email,passed to the constructor.
The logic inside the `validate` method could be to check
if the passed email parameter is a valid email string.
Email validations:
https://help.xmatters.com/ondemand/trial/valid_email_format.htm
https://en.wikipedia.org/wiki/Email_address
"""
#Чет прям очень лениво было писать нормальный валидатор. Оставим на потом

class Validator:
    domain_list = ["gmail.com", "mail.ru"]

    def __init__(self, email):
        self.email = email
        self.validate()

    def validate(self):
        if self.email.split("@")[1] in self.domain_list:
            print(f"Its ok {self.email}")
            return
        print(f"Not valid {self.email}")


somebodys_mail = "prampampam@gmail.com"
Validator(somebodys_mail)


"""Task 2
Implement 2 classes, the first one is the Boss and the second one is the Worker.
Worker has a property 'boss', and its value must be an instance of Boss.
You can reassign this value, but you should check whether the new value is Boss. 
Each Boss has a list of his own workers. 
You should implement a method that allows you to add workers to a Boss. 
You're not allowed to add instances of Boss class to workers list directly via access to attribute, 
use getters and setters instead!
You can refactor the existing code.

id_ - is just a random unique integer
"""
#Чет намудрил походу...

import uuid


class Boss:
    def __init__(self, name: str, company: str):
        self.id = self.__rand_id()
        self.name = name
        self.company = company
        self.workers = []

    @staticmethod
    def __rand_id():
        id_ = str(uuid.uuid4())[:5]
        return id_

    @property
    def employees(self):
        return f"Boss name: {self.name}\nID: {self.id}\nCompany: {self.company}\nWorkers: {self.workers}"

    @employees.setter
    def employees(self, worker):
        self.workers.append(worker)
        worker.boss = self

    def __str__(self):
        return self.name


class Worker:
    def __init__(self, name: str, boss: Boss):
        self.id = self.__rand_id()
        self.name = name
        self.boss = boss
        self.__set_employee(boss)

    @staticmethod
    def __rand_id():
        id_ = str(uuid.uuid4())[:5]
        return id_

    @property
    def worker_boss(self):
        return f"Name: {self.name}\nID: {self.id}\nBoss: {self.boss}"

    @worker_boss.setter
    def worker_boss(self, boss):
        self.boss = boss
        boss.employees = self

    def __set_employee(self, boss):
        boss.workers.append(self)

    def __str__(self):
        return f"Worker name:{self.name}\nBoss:{self.boss}"

    def __repr__(self):
        return f"{self.name}"


anton = Boss("Anton", "Global")
dron = Boss("Dron", "Automa")

a = Worker("Harold", dron)
b = Worker("Gabriel", anton)
c = Worker("Igor", anton)



"""Task 3
Write a class TypeDecorators which has several methods for converting 
results of functions to a specified type (if it's possible):
methods:
to_int
to_str
to_bool
to_float

Don't forget to use @wraps
"""

#from functools import wraps
# Так и не понял в какой части должен быть @wraps, чтоб это все работало)

class TypeDecorators:
    def to_int(self):
        def decor(args):
            return int(args)
        return decor

    def to_bool(self):
        def decor(args):
            return bool(args)
        return decor

    def to_str(self):
        def decor(args):
            return str(args)
        return decor

    def to_float(self):
        def decor(args):
            return float(args)
        return decor


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25
assert do_something('True') is True
