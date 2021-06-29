#!/usr/bin/env python3

import regional_planning_library as rplib
import sst

component_indicies_dict = {'house': [],
                           'grocery store': [],
                           'gravel road': [],
                           'interstate road': [],
                           'link': []}

n1 = rplib.City_Baltimore(prefix="", city_lat=252, city_long=53522,
                        city_width=242, city_length=23,
                        number_of_neighborhoods_per_city=2,
             link_delay="1ns",
             component_indicies_dict=component_indicies_dict,
             clock = "1GHz",      # Simulation clock rate
             clockTicks = "2",   # Number of clock ticks before the simulation ends
             debug = "2"         # debug level
                                 # 0 = FATAL, 1 = WARN, 2 = INFO, 3 = DEBUG, 4 = TRACE, 5 = ALL
             )

# to edit the graphviz and get the "desired" hypernode graph,
# - remove the "simulation" graph (second gv)
# - remove "graph [style=invis];" from line 5
# - insert "graph [style=invis];" after each "subgraph cluster_"
# - (manually) indent appropriate subgraphs
# - (manually) insert appropriate "subgraph cluster_? {" and associated "}"
