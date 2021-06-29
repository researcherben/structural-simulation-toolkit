#!/usr/bin/env python3
import sst
import regional_planning_library as rplib


link_delay = "1ns"  # has to be non-zero to enable ordering of events
clock = "1GHz"      # Simulation clock rate
clockTicks = "2"    # Number of clock ticks before the simulation ends
debug = "2"         # debug level
                    # 0 = FATAL, 1 = WARN, 2 = INFO, 3 = DEBUG, 4 = TRACE, 5 = ALL

# dictionary for tracking the indicies of respective components
link_indicies = []

neighborhood_0 = rplib.MyNeighborhood(prefix="n0_",
             neighborhood_lat=252, neighborhood_long=53522,
             neighborhood_width=242, neighborhood_length=23,
             link_delay="1ns",
             number_of_houses=3,
             link_indicies=link_indicies,
             clock = "1GHz",      # Simulation clock rate
             clockTicks = "2",   # Number of clock ticks before the simulation ends
             debug = "2"         # debug level
                                 # 0 = FATAL, 1 = WARN, 2 = INFO, 3 = DEBUG, 4 = TRACE, 5 = ALL
             )

neighborhood_1 = rplib.MyNeighborhood(prefix="n1_",
             neighborhood_lat=252, neighborhood_long=53522,
             neighborhood_width=242, neighborhood_length=23,
             link_delay="1ns",
             number_of_houses=3,
             link_indicies=link_indicies,
             clock = "1GHz",      # Simulation clock rate
             clockTicks = "2",   # Number of clock ticks before the simulation ends
             debug = "2"         # debug level
                                 # 0 = FATAL, 1 = WARN, 2 = INFO, 3 = DEBUG, 4 = TRACE, 5 = ALL
             )

neighborhood_2 = sst.Component("neighborhood_2", "neighborhood.NeighborhoodComponent")
neighborhood_2.addParams({"clock": clock, "clockTicks": clockTicks, "debug": debug})

neighborhood_3 = sst.Component("neighborhood_3", "neighborhood.NeighborhoodComponent")
neighborhood_3.addParams({"clock": clock, "clockTicks": clockTicks, "debug": debug})


road01 = sst.Component("road_n0_n1", "road.RoadComponent")
road01.addParams({"clock": clock, "clockTicks": clockTicks, "debug": debug})

sst.Link("link_n0_to_road01").connect((neighborhood_0.houses[0].obj, "port_c", link_delay),
                                      (road01, "port_a", link_delay))
sst.Link("link_n1_to_road01").connect((road01, "port_b", link_delay),
                                      (neighborhood_1.houses[0].obj, "port_d", link_delay))

road12 = sst.Component("road_n1_n2", "road.RoadComponent")
road12.addParams({"clock": clock, "clockTicks": clockTicks, "debug": debug})

sst.Link("link_n1_to_road12").connect((neighborhood_1.houses[0].obj, "port_c", link_delay),
                                      (road12, "port_a", link_delay))
sst.Link("link_n2_to_road12").connect((road12, "port_b", link_delay),
                                      (neighborhood_2, "port_d", link_delay))


road23 = sst.Component("road_n2_n3", "road.RoadComponent")
road23.addParams({"clock": clock, "clockTicks": clockTicks, "debug": debug})

sst.Link("link_n2_to_road23").connect((neighborhood_2, "port_c", link_delay),
                                      (road23, "port_a", link_delay))
sst.Link("link_n3_to_road23").connect((road23, "port_b", link_delay),
                                      (neighborhood_3, "port_d", link_delay))



road30 = sst.Component("road_n3_n0", "road.RoadComponent")
road30.addParams({"clock": clock, "clockTicks": clockTicks, "debug": debug})

sst.Link("link_n3_to_road30").connect((neighborhood_3, "port_c", link_delay),
                                      (road30, "port_a", link_delay))
sst.Link("link_n0_to_road30").connect((road30, "port_b", link_delay),
                                      (neighborhood_0.houses[0].obj, "port_d", link_delay))
