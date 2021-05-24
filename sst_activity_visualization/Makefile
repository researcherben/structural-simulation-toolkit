CXX=$(shell sst-config --CXX)
CXXFLAGS=$(shell sst-config --ELEMENT_CXXFLAGS)
LDFLAGS=$(shell sst-config --ELEMENT_LDFLAGS)

ifndef CONFIG
CONFIG=config_network
$(info no "CONFIG" was provided, so defaulting to "config_network")
endif

# as per https://stackoverflow.com/a/11843480/1164295
# shared object library must start with "lib"
all: clean libtwoexample.so install picture run

.PHONY: libtwoexample.so
libtwoexample.so: some_component.cpp\
	                some_component.h
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $<

install: libtwoexample.so
	sst-register two_example two_example_LIBDIR=$(CURDIR)

clean:
	rm -f *.o *.so *.png *.gv *.log

picture: install
	sst --output-dot=$(CONFIG).gv --dot-verbosity=10 --run-mode=init $(CONFIG).py 1 10
	sst --output-json=$(CONFIG).json --run-mode=init $(CONFIG).py 1 10
	dot $(CONFIG).gv -Tpng > $(CONFIG).png

run:
	time sst $(CONFIG).py 5 10 > simulation.log 2>&1
	cat simulation.log | grep { | sed 's/.*-- //' > simulation.dat

mpirun:
	time mpirun -np 2 sst $(CONFIG).py 5 10
