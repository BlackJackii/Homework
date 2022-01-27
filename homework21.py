"""Рекурсия"""

"""#############################################
# All tasks should be solved using recursion
#############################################
"""



"""
Task 1
"""

from typing import Union


def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    if exp > 1:
        return to_power(x, exp - 1) * x
    if exp <= 0:
        raise ValueError("This function works only with exp > 0.")
    return x


# Returns  x ^ exp
assert to_power(2, 3) == 8
assert to_power(3.5, 2) == 12.25





"""
Task 2
"""


def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if looking_str[index] == looking_str[-1-index]:
        if index >= len(looking_str)//2:
            return True
        return is_palindrome(looking_str, index+1)
    return False



assert is_palindrome("mamama") == False
assert is_palindrome("333111") == False
assert is_palindrome('mom') == True
assert is_palindrome('sassas') == True
assert is_palindrome('o') == True
assert is_palindrome('123321') == True
assert is_palindrome('111') == True
assert is_palindrome('1') == True





"""
Task 3
"""


def mult(a: int, n: int) -> int:
    if a == 1:
        return n
    return n + mult(a - 1, n)


# This function works only with positive integers
assert mult(2, 4) == 8
assert mult(2, 0) == 0
# assert mult(2, -4) == ValueError("This function works only with postive integers")





"""
Task 4
"""

def reverse(input_str: str) -> str:
    if len(input_str) == 0:
        return input_str
    return reverse(input_str[1:]) + input_str[0]


# Function returns reversed input string
assert reverse("hello") == "olleh"
assert reverse("o") == "o"
assert reverse("oa") == "ao"

print(reverse("Anton"))
print(reverse("СЛОВО"))






"""
Task 5
"""

def sum_of_digits(digit_string: str) -> int:
    if digit_string.isdigit():
        if len(digit_string) > 1:
            return sum_of_digits(digit_string[1:]) + int(digit_string[0])
        return int(digit_string)
    else:
        ValueError("input string must be digit string")



assert sum_of_digits('26') == 8
# assert sum_of_digits('test') == ValueError("input string must be digit string")

print(sum_of_digits("123"))
print(sum_of_digits("558"))
print(sum_of_digits("736666"))
