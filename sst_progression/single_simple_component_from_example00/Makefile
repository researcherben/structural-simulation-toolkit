CXX=$(shell sst-config --CXX)
CXXFLAGS=$(shell sst-config --ELEMENT_CXXFLAGS)
LDFLAGS=$(shell sst-config --ELEMENT_LDFLAGS)

# as per https://stackoverflow.com/a/11843480/1164295
# shared object library must start with "lib"
all: clean libminexample.so install run

.PHONY: libminexample.so
libminexample.so: example_component.cpp\
	                example_component.h
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $<

install:
	sst-register minimal_example minimal_example_LIBDIR=$(CURDIR)

clean:
	rm -f *.so *.o

run:
	sst ExampleConfig.py
