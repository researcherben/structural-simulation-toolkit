#!/usr/bin/env python3

import random

def mylist(lower: int, upper: int):
    """
    unlike "data_transform" which is stateless, 
    this function maintains state between calls
    """
    for element in range(5):
        yield random.randint(lower, upper)
