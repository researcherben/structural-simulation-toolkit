CXX=$(shell sst-config --CXX)
CXXFLAGS=$(shell sst-config --ELEMENT_CXXFLAGS)
LDFLAGS=$(shell sst-config --ELEMENT_LDFLAGS)

ifndef CONFIG
CONFIG=config_network
$(info no "CONFIG" was provided, so defaulting to "config_network")
endif

ifndef TICKS
TICKS=3
$(info no "TICKS" was provided, so defaulting to "3")
endif

ifndef NODES
NODES=5
$(info no "NODES" was provided, so defaulting to "5")
endif


# as per https://stackoverflow.com/a/11843480/1164295
# shared object library must start with "lib"
all: clean libtwoexample.so install picture run

.PHONY: libtwoexample.so
libtwoexample.so: some_component.cpp\
	                some_component.h
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $<

install: libtwoexample.so
	/usr/bin/time sst-register two_example two_example_LIBDIR=$(CURDIR)

clean:
	rm -f *.o *.so *.png *.gv

picture: 
	sst --output-dot=$(CONFIG).gv --run-mode=init $(CONFIG).py $(TICKS) $(NODES)
	dot $(CONFIG).gv -Tpng > $(CONFIG).png

run: 
	/usr/bin/time sst $(CONFIG).py $(TICKS) $(NODES)

mpirun: 
	/usr/bin/time mpirun -np 2 sst $(CONFIG).py $(TICKS) $(NODES)
