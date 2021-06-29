#!/usr/bin/env python3

"""
assumptions regarding SST components:
 * the SST components are buildings (house, grocery_store) and roads
 * everything that is not a component is an abstraction
 * each abstraction is comprised of components or other abstractions

assumptions about the model:
 * buildings have lat/long location
 * buildings are connected to other buildings via roads
 * roads connect houses directly and have properties like (number of lanes) and (paved xor gravel)
 * assemblies of buildings and roads can be created, e.g., neighborhoods, cities, states.

"""

# commenting style guide:
# https://google.github.io/styleguide/pyguide.html

# https://dbader.org/blog/abstract-base-classes-in-python
from abc import ABCMeta, abstractmethod
import sst


def max_index_for(list_of_ints: list) -> int:
    """
    Each SST component has an index
    When adding a new component, need to identify an unused index

    The indices in use are tracked in a list that is a value in a dictionary
    This function takes that list as an argument
    """
    if len(list_of_ints)==0:
        return -1
    else:
        return max(list_of_ints)
# previous approach used try/except
    # try:
    #     max_index = max(list_of_ints)
    # except ValueError: # list is unpopulated
    #     max_index = -1
    # return max_index

class Connector(metaclass=ABCMeta):
    """gravel_road and road inherit from this class

    base class - do not instantiate this
    TODO: figure out how to prevent instantiation

    the relevance of including the lat/long of both from and to
    is to be able to determine properties like "length" of the connector

    Normally in SST we'd use a link to connect components,
    but here we want to be able to assign other properties
    like "number of lanes" and "gravel vs paved"
    to each the edge between buildings.
    These properties are independent of the components they connect.

    Attributes:
        from_building: SST component that one end of this connector is associated with
        from_lat: latitude of the "from" component
        from_long: longitude of the "from" component
        to_building: other SST component that this connector is associated with
        to_lat: latitude of the "to" component
        to_long: longitude of the "to" component

    """
    # not instantiable; see https://stackoverflow.com/a/7990308/1164295
    # def __new__(cls, *args, **kwargs):
    #     if cls is Connector:
    #         raise TypeError("base class may not be instantiated")
    #     return object.__new__(cls, *args, **kwargs)

    def __init__(self, from_building, from_lat: float, from_long: float, from_port: str,
                to_building, to_lat: float, to_long: float, to_port: str):
        self.from_building = from_building
        self.from_lat = from_lat
        self.from_long = from_long
        self.from_port = from_port
        self.to_building = to_building
        self.to_lat = to_lat
        self.to_long = to_long
        self.to_port = to_port
    pass

class GravelRoad(Connector):
    """a type of connector

    Attributes:
        link_delay: propagation delay between SST components, e.g., "2ns"
        component_indicies_dict: dictionary to track the indicies in use for each category of SST component
        clock: Simulation clock rate, e.g. "1GHz"
        clockTicks: Number of clock ticks before the simulation ends
        debug: level, e.g., 0 = FATAL, 1 = WARN, 2 = INFO, 3 = DEBUG, 4 = TRACE, 5 = ALL
    """
    def __init__(self, prefix: str, index: int, from_building, from_lat: float, from_long: float, from_port: str,
                 to_building, to_lat: float, to_long: float, to_port: str,
                 link_delay: str, link_indicies: list,
                 clock: str, clockTicks: str, debug: str):
        Connector.__init__(self, from_building, from_lat, from_long, from_port,
                    to_building, to_lat, to_long, to_port)
        max_link_index = max_index_for(link_indicies)

        obj = sst.Component(prefix+"gravel road_"+str(index), "road.RoadComponent")
        obj.addParams({
             "from": self.from_building, "from_lat": self.from_lat, "from_long": self.from_long, "from_port": self.from_port,
             "to":   self.to_building,   "to_lat":   self.to_lat,   "to_long": self.to_long, "to_port": self.to_port,
             "clock": clock, "clockTicks": clockTicks, "debug": debug})
        sst.Link("link"+str(max_link_index+1)).connect((from_building, from_port, link_delay),
                                                 (obj, "port_a", link_delay))
        link_indicies.append(max_link_index+1)
        sst.Link("link"+str(max_link_index+2)).connect((obj, "port_b", link_delay),
                                                 (to_building, to_port, link_delay))
        link_indicies.append(max_link_index+2)



class Building(metaclass=ABCMeta):
    """
    abstraction -- house and grocery_store and Capitol_building inherit from this

    base class - do not instantiate this
    TODO: figure out how to prevent instantiation

    Attributes:
        lat: latitude of center of building
        long: longitude of center of building
    """
    # not instantiable; see https://stackoverflow.com/a/7990308/1164295
    # def __new__(cls, *args, **kwargs):
    #     if cls is Building:
    #         raise TypeError("base class may not be instantiated")
    #     return object.__new__(cls, *args, **kwargs)

    def __init__(self, lat: float, long: float):
        self.lat = lat
        self.long = long

class House(Building):
    """
    Houses exist within neighborhoods
    Houses have a location

    Attributes:
        component_indicies_dict: dictionary to track the indicies in use for each category of SST component
        clock: Simulation clock rate, e.g. "1GHz"
        clockTicks: Number of clock ticks before the simulation ends
        debug: level, e.g., 0 = FATAL, 1 = WARN, 2 = INFO, 3 = DEBUG, 4 = TRACE, 5 = ALL
    """
    def __init__(self, prefix: str, index: int, lat: float, long: float,
                 clock: str, clockTicks: str, debug: str):
        Building.__init__(self, lat, long)

        self.obj = sst.Component(prefix+"house_"+str(index), "house.HouseComponent")
        self.obj.addParams({"clock": clock, "clockTicks": clockTicks, "debug": debug})


# abstractions
class Region(metaclass=ABCMeta): # base class for all abstractions.
    """
    abstraction
    base class - do not instantiate this

    Attributes:
        lat: latitude
        long: longitude
        width:
        length:
    """
    # not instantiable; see https://stackoverflow.com/a/7990308/1164295
    # def __new__(cls, *args, **kwargs):
    #     if cls is Region:
    #         raise TypeError("base class may not be instantiated")
    #     return super(Region, cls).__new__(cls, *args, **kwargs)

    def __init__(self, lat: float, long: float, width: float, length: float):
        self.lat = lat
        self.long = long
        self.width = width
        self.length = length
    pass

class EmptyNeighborhood(Region):
    """
    abstraction -- this is not an SST component
    neighborhoods exist within cities.

    user is expected to add buildings (e.g., houses) and
    connectors (e.g., roads) after instantiation

    Attributes:
        neighborhood_lat: latitude of center of neighborhood
        neighborhood_long: longitude of center of neighborhood
        neighborhood_width: width of neighborhood
        neighborhood_length: length of neighborhood

    Methods:
        add_house()
        add_gravel_road()
        list_houses()
        list_gravel_roads()

    """
    def __init__(self, neighborhood_lat: float, neighborhood_long: float,
                 neighborhood_width: float, neighborhood_length: float):
        Region.__init__(self, neighborhood_lat, neighborhood_long, neighborhood_width, neighborhood_length)
        self.houses = {}
        self.gravel_roads = {}

    def add_house(self, prefix, index, house_lat, house_long,
                                    clock, clockTicks, debug):
        """
        add house within this neighborhood
        """
        self.houses[house_index] = House(prefix, index, house_lat, house_long, component_indicies_dict,
                                        clock, clockTicks, debug)
        house_index+=1
        return

    def add_gravel_road(self, house_index):
        """
        add a gravel road within this neighborhood
        """
        self.gravel_roads[gr_index] = GravelRoad(prefix,
                self.houses[house_index].obj, self.houses[house_index].lat, self.houses[house_index].long, "port_a",
                self.houses[house_index-1].obj, self.houses[house_index-1].lat, self.houses[house_index-1].long, "port_b",
                        link_delay, link_indicies,
                        clock, clockTicks, debug)
        gr_index+=1
        return

    def list_houses(self):
        """
        list houses within this neighborhood

        Yields:
        """
        for house_index, house_obj in self.houses.items():
            yield (house_index, house_obj)

    def list_gravel_roads(self):
        """
        list gravel roads within this neighborhood
        """
        for gr_index, gr_obj in self.gravel_roads.items():
            yield (gr_index, gr_obj)
    pass # TODO

class MyNeighborhood(EmptyNeighborhood):
    """
    abstraction containing houses and roads.
    neighborhoods exist within cities.

    Attributes:

    """
    def __init__(self, prefix:str, neighborhood_lat: float, neighborhood_long: float,
                 neighborhood_width: float, neighborhood_length: float,
                 link_delay: str, number_of_houses: int,
                 link_indicies: list,
                 clock: str, clockTicks: str, debug: str):
        EmptyNeighborhood.__init__(self, neighborhood_lat, neighborhood_long,
                                         neighborhood_width, neighborhood_length)
        gr_index=0 # gravel road index within this neighborhood
        for house_index in range(number_of_houses):
            house_lat = neighborhood_lat + 1 + house_index
            house_long = neighborhood_long + 1 + house_index
            self.houses[house_index] = House(prefix,house_index,
            house_lat, house_long, clock, clockTicks, debug)
            # connect all houses within a neighborhood
            if house_index>0:
                # connect house_index to house_index-1
                self.gravel_roads[gr_index] = GravelRoad(prefix, gr_index,
                            self.houses[house_index].obj, self.houses[house_index].lat, self.houses[house_index].long,  "port_a",
                            self.houses[house_index-1].obj, self.houses[house_index-1].lat, self.houses[house_index-1].long, "port_b",
                             link_delay, link_indicies,
                                 clock, clockTicks, debug)
                gr_index+=1
            if house_index==number_of_houses-1:
                self.gravel_roads[gr_index] = GravelRoad(prefix, gr_index,
                            self.houses[house_index].obj, self.houses[house_index].lat, self.houses[house_index].long, "port_b",
                            self.houses[0].obj, self.houses[0].lat, self.houses[0].long, "port_a",
                             link_delay, link_indicies,
                                 clock, clockTicks, debug)
                gr_index+=1



class EmptyCity(Region):
    """
    abstraction -- this is not an SST component
    user is expected to add neighborhoods
    """
    def __init__(self,
                 city_lat: float, city_long: float,
                 city_width: float, city_length: float):
        Region.__init__(self, city_lat, city_long,city_width, city_length)
        self.neighborhood_list = []
    def add_neighborhood(self, neighborhood_lat: float, neighborhood_long: float,
                 neighborhood_width: float, neighborhood_length: float,
                 link_delay: str, number_of_houses: int,
                 component_indicies_dict: dict,
                 clock: str, clockTicks: str, debug: str):
        n = Neighborhood_FellsPoint(neighborhood_lat, neighborhood_long,
                                neighborhood_width, neighborhood_length,
                     link_delay, number_of_houses,
                     component_indicies_dict,
                     clock, clockTicks, debug)
        self.neighborhood_list.append(n)

class City_Baltimore(EmptyCity):
    """
    abstraction
    """
    def __init__(self, prefix: str, city_lat: float, city_long: float, city_width: float, city_length: float,
         number_of_neighborhoods_per_city: int,
         link_delay: str,
         component_indicies_dict: dict,
         clock: str, clockTicks: str, debug: str):
        EmptyCity.__init__(self, city_lat, city_long, city_width, city_length)
        self.number_of_neighborhoods_per_city = number_of_neighborhoods_per_city

        nc = Neighborhood_Catonsville(prefix+"balt_", neighborhood_lat=111, neighborhood_long=222,
                            neighborhood_width=42, neighborhood_length=2,
                 link_delay=link_delay, number_of_houses=4,
                 component_indicies_dict=component_indicies_dict,
                 clock=clock,      # Simulation clock rate
                 clockTicks = clockTicks,   # Number of clock ticks before the simulation ends
                 debug = debug)
        self.neighborhood_list.append(nc)
        nfp = Neighborhood_FellsPoint(prefix+"balt_", neighborhood_lat=333, neighborhood_long=444,
                            neighborhood_width=2412, neighborhood_length=2311,
                 link_delay=link_delay, number_of_houses=4,
                 component_indicies_dict=component_indicies_dict,
                 clock=clock,      # Simulation clock rate
                 clockTicks = clockTicks,   # Number of clock ticks before the simulation ends
                 debug = debug)
        self.neighborhood_list.append(nfp)

        first_house_in_nc = list(nc.houses.keys())[0]
        first_house_in_nfp = list(nfp.houses.keys())[0]

        pr = PavedRoad(prefix+"balt_", nc.houses[first_house_in_nc].obj, nc.houses[first_house_in_nc].lat, nc.houses[first_house_in_nc].long,
                        nfp.houses[first_house_in_nfp].obj, nfp.houses[first_house_in_nfp].lat, nfp.houses[first_house_in_nfp].long,
                        link_delay=link_delay, component_indicies_dict=component_indicies_dict,
                        clock=clock, clockTicks=clockTicks, debug=debug)

        last_house_in_nc = list(nc.houses.keys())[-1]
        last_house_in_nfp = list(nfp.houses.keys())[-1]

        pr = PavedRoad(prefix+"balt_", nc.houses[last_house_in_nc].obj, nc.houses[last_house_in_nc].lat, nc.houses[last_house_in_nc].long,
                        nfp.houses[last_house_in_nfp].obj, nfp.houses[last_house_in_nfp].lat, nfp.houses[last_house_in_nfp].long,
                        link_delay=link_delay, component_indicies_dict=component_indicies_dict,
                        clock=clock, clockTicks=clockTicks, debug=debug)



class EmptyState(Region):
    """
    abstraction -- this is not an SST component
    user is expected to add cities
    """
    def __init__(self, state_lat: float, state_long: float, state_width: float, state_length: float,
          number_of_cities_per_state: int,
          number_of_neighborhoods_per_city: int,
          link_delay: str,
          component_indicies_dict: dict,
          clock: str, clockTicks: str, debug: str):
        self.state_lat = state_lat
        self.state_long = state_long
    def add_Baltimore():
        city_bmore = City_Baltimore()

class State_Maryland(EmptyState):
    """
    abstraction -- this is not an SST component

    """
    def __init__(self, state_lat: float, state_long: float, state_width: float, state_length: float,
          number_of_cities_per_state: int,
          number_of_neighborhoods_per_city: int,
          link_delay: str,
          component_indicies_dict: dict,
          clock: str, clockTicks: str, debug: str):
        EmptyState.__init__(self, state_lat, state_long)
