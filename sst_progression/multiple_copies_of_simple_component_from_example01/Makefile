CXX=$(shell sst-config --CXX)
CXXFLAGS=$(shell sst-config --ELEMENT_CXXFLAGS)
LDFLAGS=$(shell sst-config --ELEMENT_LDFLAGS)

ifndef CONFIG
CONFIG="config_network"
$(info no "CONFIG" was provided, so defaulting to "config_network")
endif

# as per https://stackoverflow.com/a/11843480/1164295
# shared object library must start with "lib"
all: clean libswitch.so libwire.so libserver.so install picture run

.PHONY: libswitch.so
libswitch.so: component_switch.cpp\
	            component_switch.h
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $<
.PHONY: libwire.so
libwire.so: component_wire.cpp\
	            component_wire.h
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $<
.PHONY: libserver.so
libserver.so: component_server.cpp\
	            component_server.h
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $<

install: clean libserver.so libwire.so libswitch.so
	sst-register server server_LIBDIR=$(CURDIR)
	sst-register switch switch_LIBDIR=$(CURDIR)
	sst-register wire wire_LIBDIR=$(CURDIR)

clean:
	rm -f *.o *.so *.png *.gv

picture: install
	sst --output-dot=$(CONFIG).gv --run-mode=init $(CONFIG).py
	dot $(CONFIG).gv -Tpng > $(CONFIG).png

run: install
	time sst $(CONFIG).py

mpirun: install
	time mpirun -np 2 sst $(CONFIG).py
