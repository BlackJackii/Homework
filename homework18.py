"""Расширенные контекстные менеджеры"""

"""Task 1

File Context Manager class
Create your own class, which can behave like a built-in function `open`.
Also, you need to extend its functionality with counter and logging.
Pay special attention to the implementation of `__exit__` method,
which has to cover all the requirements to context managers mentioned here:
https://docs.python.org/3.7/library/stdtypes.html#typecontextmanager
https://docs.python.org/3.7/reference/compound_stmts.html#with
"""

import datetime


class LikeOpen:
    counter = 0

    def __init__(self, *args):
        self._log_file = open("logs.txt", "a")
        self.args = args
        self.new_file = None

    def __enter__(self):
        LikeOpen.counter += 1
        self.new_file = open(*self.args)
        self._log_file.write(f"{datetime.datetime.now()}, file opened. {LikeOpen.counter} times\n")
        return self.new_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._log_file.write(f"{datetime.datetime.now()}, file closed.\n")
        self._log_file.close()
        self.new_file.close()


if __name__ == '__main__':
    with LikeOpen("test_test.txt", "a") as file:
        file.write("Hi there123123123\n")
    with LikeOpen("test_test.txt", "a") as file:
        file.write("HELLOOOOOO\n")
    with LikeOpen("test_test.txt", "a") as file:
        file.write("HIHIIHIHI\n")

"""
Task 2
Writing tests for context manager
Take your implementation of the context manager class from Task 1
and write tests for it. Try to cover as many use cases as you can,
positive ones when a file exists and everything works as designed.
And also, write tests when your class raises errors
or you have errors in the runtime context suite."""

import unittest
from unittest import TestCase
from unittest.mock import patch, Mock
import os

class TestManager(TestCase):
    def test_create_new_file(self):
        with LikeOpen("unittest_new_file.txt", "w") as file:
            file.write("test2")
        assert os.path.exists("unittest_new_file.txt")

    def test_logs(self):
        assert os.path.exists("logs.txt")
        with open("logs.txt", "r") as file:
            self.assertEqual(file.readline()[:10], str(datetime.datetime.now())[:10])








"""
Task 3 (Optional)
Pytest fixtures with context manager
Create a simple function, which performs any logic of your
choice with text data, which it obtains from a file object,
passed to this function ( def test(file_obj) ).
Create a test case for this function using pytest library
(https://docs.pytest.org/en/latest/contents.html).
Create pytest fixture, which uses your implementation of
the context manager to return a file object,
which could be used inside your function."""