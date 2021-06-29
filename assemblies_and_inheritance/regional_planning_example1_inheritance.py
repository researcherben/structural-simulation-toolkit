#!/usr/bin/env python3
import sst

link_delay = "1ns"  # has to be non-zero to enable ordering of events
clock = "1GHz"      # Simulation clock rate
clockTicks = "2"    # Number of clock ticks before the simulation ends
debug = "2"         # debug level
                    # 0 = FATAL, 1 = WARN, 2 = INFO, 3 = DEBUG, 4 = TRACE, 5 = ALL


house0 = sst.Component("house_0", "house.HouseComponent")
house0.addParams({"clock": clock, "clockTicks": clockTicks, "debug": debug})

house1 = sst.Component("house_1", "house.HouseComponent")
house0.addParams({"clock": clock, "clockTicks": clockTicks, "debug": debug})

house2 = sst.Component("house_2", "house.HouseComponent")
house0.addParams({"clock": clock, "clockTicks": clockTicks, "debug": debug})

# houses are connected by roads
# The typical SST approach would be to use an sst.Link between components.
# Because there are multiple types of roads (e.g. paved, gravel, interstate),
# here we are inserting an sst.Component, and then using two sst.Links

road01 = sst.Component("road_0_1", "road.RoadComponent")
road01.addParams({"clock": clock, "clockTicks": clockTicks, "debug": debug})

sst.Link("link_house0_to_road01").connect((house0, "port_a", link_delay),
                                         (road01, "port_a", link_delay))
sst.Link("link_house1_to_road01").connect((road01, "port_b", link_delay),
                                         (house1, "port_b", link_delay))

road12 = sst.Component("road_1_2", "road.RoadComponent")
road12.addParams({"clock": clock, "clockTicks": clockTicks, "debug": debug})

sst.Link("link_house1_to_road12").connect((house1, "port_a", link_delay),
                                         (road12, "port_a", link_delay))
sst.Link("link_house2_to_road12").connect((road12, "port_b", link_delay),
                                         (house2, "port_b", link_delay))

road20 = sst.Component("road_2_0", "road.RoadComponent")
road20.addParams({"clock": clock, "clockTicks": clockTicks, "debug": debug})

sst.Link("link_house2_to_road20").connect((house2, "port_a", link_delay),
                                         (road20, "port_a", link_delay))
sst.Link("link_house0_to_road20").connect((road20, "port_b", link_delay),
                                         (house0, "port_b", link_delay))
