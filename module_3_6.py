import numpy as np # linear algebra
import pandas as pd # data processing


class mySample():
    # using the __init__() function
    def __init__(self):
        self.first = 10
        self._second = 15
        self.__third = 20
    # defining a child class


class AnotherClass(mySample):

    def __init__(self):
        super().__init__()
        self.first = "Variable Overridden"
        self._second = "Variable Overridden"
        self.__third = "Variable Overridden"
    # instantiating the child class


def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)

print(factorial(42))
