#!/usr/bin/env python3

import random

def transform(an_integer: int=5, a_float: float=4.592, a_string: str="yum"):
    """
    this function is stateless -- each use is independent
    """
    return an_integer*3, a_float*2, a_string+" ilo"
