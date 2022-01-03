"""Task 1
Method overloading.

Create a base class named Animal with a method called
talk and then create two subclasses:
Dog and Cat, and make their own implementation
of the method talk be different.
For instance, Dog’s can be to print ‘woof woof’,
while Cat’s can be to print ‘meow’.

Also, create a simple generic function,
which takes as input instance of a Cat or Dog classes and performs
talk method on input parameter.  """

class Animal:
    def talk(self):
        return


class Dog(Animal):
    def talk(self):
        return "woof woof"


class Cat(Animal):
    def talk(self):
        return "meow"


def animals_say_hello(animal):
    return animal.talk()


cat = Cat()
dog = Dog()

print(animals_say_hello(dog))


"""Task2
Library
Write a class structure that implements a library. Classes:
1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []

Library class
Methods:
- new_book(name: str, year: int, author: Author) - returns an instance of Book class 
and adds the book to the books list for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the specified author
- group_by_year(year: int) - returns a list of all the books grouped by the specified year
All 3 classes must have a readable __repr__ and __str__ methods.
Also, the book class should have a class variable which holds the amount of all existing books
"""


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def add_new_book(self, new_book):
        if new_book not in self.books:
            self.books.append(new_book)
        if new_book.author not in self.authors:
            self.authors.append(new_book.author)

    def group_by_authors(self, author):
        author_list = []
        for i in self.authors:
            if i.name == author:
                author_list.append(i)
        return author_list

    def group_by_year(self, year: int):
        book_list = []
        for i in self.books:
            if i.year == year:
                book_list.append(i)
        return book_list

    def __repr__(self):
        return f"Books {self.books}, authors {self.authors}"

    def __str__(self):
        return f"Books {self.books}, authors {self.authors}"


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday

    def __repr__(self):
        return f" {self.name}, {self.country}, {self.birthday}"

    def __str__(self):
        return f" {self.name}, {self.country}, {self.birthday}"


class Book:
    amount = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __repr__(self):
        return f" {self.name}, {self.year}, {self.author}"

    def __str__(self):
        return f" {self.name}, {self.year}, {self.author}"


a = Author("Anton", "Ukraine", "28.03.1967")
b = Author("Igor", "Spain", "23.08.1933")
c = Author("Igor", "Alabama", "1.01.2001")

book1 = Book("Princes", 2001, a)
book2 = Book("Antares", 2008, b)
book3 = Book("Gogilama", 2001, c)

lib = Library("First lib")

lib.add_new_book(book1)
lib.add_new_book(book2)
lib.add_new_book(book3)

print(lib.group_by_year(2001))


"""Task 3
Fraction
Create a Fraction class, which will represent all basic arithmetic logic 
for fractions (+, -, /, *) with appropriate checking and error handling
"""

from fractions import Fraction

x = Fraction(1/2)
y = Fraction(1/4)
print(x+y)