CXX=$(shell sst-config --CXX)
CXXFLAGS=$(shell sst-config --ELEMENT_CXXFLAGS)
LDFLAGS=$(shell sst-config --ELEMENT_LDFLAGS)

ifndef CONFIG
CONFIG=regional_planning_example1_inheritance
$(info no "CONFIG" was provided, so defaulting to "regional_planning_example1_inheritance")
endif

# as per https://stackoverflow.com/a/11843480/1164295
# shared object library must start with "lib"
all: libhouse.so libgrocery.so libroad.so libneighborhood.so libcity.so install picture

clean:
	rm -f *.o *.so *.png *.gv


#.PHONY: libhouse.so
libhouse.so: component_house.cpp\
	            component_house.h
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $<

#.PHONY: libgrocery.so
libgrocery.so: component_grocery.cpp\
	            component_grocery.h
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $<

#.PHONY: libcity.so
libcity.so: component_city.cpp\
	            component_city.h
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $<

#.PHONY: libneighborhood.so
libneighborhood.so: component_neighborhood.cpp\
	            component_neighborhood.h
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $<


#.PHONY: libroad.so
libroad.so: component_road.cpp\
	            component_road.h
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $<

install: libroad.so libhouse.so libgrocery.so
	sst-register city city_LIBDIR=$(CURDIR)
	sst-register neighborhood neighborhood_LIBDIR=$(CURDIR)
	sst-register house house_LIBDIR=$(CURDIR)
	sst-register grocery grocery_LIBDIR=$(CURDIR)
	sst-register road road_LIBDIR=$(CURDIR)

picture: install
	sst --output-dot=$(CONFIG).gv --run-mode=init $(CONFIG).py
	dot $(CONFIG).gv -Tpng > $(CONFIG).png

run: install
	time sst $(CONFIG).py

mpirun: install
	time mpirun -np 2 sst $(CONFIG).py
