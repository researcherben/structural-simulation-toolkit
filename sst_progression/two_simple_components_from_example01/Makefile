CXX=$(shell sst-config --CXX)
CXXFLAGS=$(shell sst-config --ELEMENT_CXXFLAGS)
LDFLAGS=$(shell sst-config --ELEMENT_LDFLAGS)

ifndef CONFIG
CONFIG="config_two_components_one_link"
$(info no "CONFIG" was provided, so defaulting to "config_two_components_one_link")
endif


# as per https://stackoverflow.com/a/11843480/1164295
# shared object library must start with "lib"
all: clean libtwoexample.so install picture run



.PHONY: libtwoexample.so
libtwoexample.so: some_component.cpp\
	                some_component.h
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $<

install:
	sst-register two_example two_example_LIBDIR=$(CURDIR)

clean:
	rm -f *.o *.so *.png *.gv

picture:
	sst --output-dot=$(CONFIG).gv --run-mode=init $(CONFIG).py
	dot $(CONFIG).gv -Tpng > $(CONFIG).png

run:
	sst $(CONFIG).py
