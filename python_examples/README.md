
Call Python3 from C++

There are multiple methods listed on
https://stackoverflow.com/questions/49137/calling-python-from-a-c-program-for-distribution
including
* system call to Python interpreter - https://stackoverflow.com/a/54383046/1164295
* pybind11 for running Python within C++ -- https://stackoverflow.com/a/53325201/1164295 -- https://pybind11.readthedocs.io/en/stable/advanced/embedding.html
* Boost -- https://stackoverflow.com/a/328451/1164295 -- https://www.boost.org/doc/libs/1_74_0/libs/python/doc/html/index.html
* https://docs.python.org/3/extending/embedding.html -- provides low-level overview


See also
* https://www.codeproject.com/Articles/820116/Embedding-Python-program-in-a-C-Cplusplus-code
* https://www.codeproject.com/Articles/11805/Embedding-Python-in-C-C-Part-I
* https://www.codeproject.com/Articles/11843/Embedding-Python-in-C-C-Part-II 


from https://docs.python.org/3/extending/embedding.html
When embedding Python, the interface code does:
1. Convert data values from C to Python,
1. Perform a function call to a Python interface routine using the converted values, and
1. Convert the data values from the call from Python to C.

