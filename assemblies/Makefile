CXX=$(shell sst-config --CXX)
CXXFLAGS=$(shell sst-config --ELEMENT_CXXFLAGS)
LDFLAGS=$(shell sst-config --ELEMENT_LDFLAGS)

ifndef CONFIG
CONFIG=buildings_and_roads_call_classes
$(info no "CONFIG" was provided, so defaulting to "buildings_and_roads_call_classes")
endif

# as per https://stackoverflow.com/a/11843480/1164295
# shared object library must start with "lib"
all: clean libbuilding.so libroad.so install picture

.PHONY: libbuilding.so
libbuilding.so: component_building.cpp\
	            component_building.h
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $<

.PHONY: libroad.so
libroad.so: component_road.cpp\
	            component_road.h
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $<

install: clean libroad.so libbuilding.so
	sst-register building building_LIBDIR=$(CURDIR)
	sst-register road road_LIBDIR=$(CURDIR)

clean:
	rm -f *.o *.so *.png *.gv

picture: install
	sst --output-dot=$(CONFIG).gv --run-mode=init $(CONFIG).py
	dot $(CONFIG).gv -Tpng > $(CONFIG).png

run: install
	time sst $(CONFIG).py

mpirun: install
	time mpirun -np 2 sst $(CONFIG).py
