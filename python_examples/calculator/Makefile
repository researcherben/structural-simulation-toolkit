


# no output produced; just checks that the file doesn't contain syntax errors
calc:
	python3 calc.py


# how to figure out where pybind11 lives: use 
#     python3 -c "import pybind11; print(pybind11.get_include());"
# how to figure out where Python.h lives: use 
#     python3-config --includes
# I also tried using
#     python3-config --cflags --ldflags
# based on https://stackoverflow.com/a/34643949/1164295

call_calc:
	g++ -I /usr/local/lib/python3.6/dist-packages/pybind11/include \
            -I -I/usr/include/python3.6m -I/usr/include/python3.6m call_calc.cpp


