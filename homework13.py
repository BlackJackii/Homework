"""Task 1
Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!
For example:
 "add called with 4, 5"
"""


def logger(func):
    def decorator(*args):
        print(f"{func.__name__} called with {args}")
        return func(*args)
    return decorator


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


if __name__ == '__main__':
    print(add(2, 5))
    print(square_all(3, 8))


"""Task 2
Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
"""


def stop_words(words: list):
    def decorator(func):
        def new_decor_func(name):
            new_func = func(name)
            for word in words:
                new_func = new_func.replace(word, "*")
            return new_func
        return new_decor_func
    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"


if __name__ == '__main__':
    print(create_slogan("Max"))


"""Task 3
Write a decorator `arg_rules` that validates arguments passed to the function.
A decorator should take 3 arguments:
max_length: 15
type_: str
contains: [] - list of symbols that an argument should contain
If some of the rules' checks returns False, the function should return False and print the reason it failed; 
otherwise, return the result.
"""


def arg_rules(type_: type, max_length: int, contains: list):
    def new_decor(func):
        def decored_func(name):
            if type(name) == type_ and len(name) <= max_length:
                for i in contains:
                    if i in name:
                        continue
                    return False
                return func(name)
            return False
        return decored_func
    return new_decor


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

