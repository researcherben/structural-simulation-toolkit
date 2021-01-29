#!/usr/bin/env python3

import producer
import data_transform

print("calling producer")
for element in producer.mylist(2, 6):
    print(element)

print("calling transform")
x, y, z = data_transform.transform(10, 449.2, "hello")
print("x = ", x)
print("y = ", y)
print("z = ", z)
