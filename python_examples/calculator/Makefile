
.PHONY: help
help:
	@echo "make help"
	@echo "      this message"
	@echo "==== Targets inside container ===="
	@echo "make call_calc"
	@echo "      c++ and pybind11 example"
	@echo "==== Targets outside container ===="
	@echo "make docker_build"
	@echo "      create container for g++ and pybind11"


.PHONY: docker docker_build docker_run
docker: docker_build docker_run
docker_build:
	time docker build -f Dockerfile -t pb11 .
docker_run:
	docker run -it -v `pwd`:/scratch --rm pb11 /bin/bash
docker_build_fresh:
	time docker build --no-cache -f Dockerfile -t pb11 .


call_cpp_from_py:
	g++ -O3 -Wall -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` example_call_cpp_from_py.cpp -o example`python3-config --extension-suffix`
# in an interactive Python REPL,
# import example
# example.add(1, 2)

hello_world_py_inside:
	g++ -O3 -Wall -shared -std=c++17 -fPIC `python3 -m pybind11 --includes` example_hello_world_py_inside.cpp

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
	g++ -I/usr/local/lib/python3.6/dist-packages/pybind11/include \
            -I/usr/include/python3.6m \
	    -Wno-unused-result -Wsign-compare -g -fdebug-prefix-map=/build/python3.6-e9shER/python3.6-3.6.9=. -specs=/usr/share/dpkg/no-pie-compile.specs -fstack-protector -Wformat -Werror=format-security  -DNDEBUG -g -fwrapv -O3 -Wall -L/usr/lib/python3.6/config-3.6m-x86_64-linux-gnu \
	    -L/usr/lib -lpython3.6m -lpthread -ldl  -lutil -lm  -Xlinker -export-dynamic -Wl,-O1 -Wl,-Bsymbolic-functions \
	    -std=c++14 \
	    -fPIC \
            call_calc.cpp


