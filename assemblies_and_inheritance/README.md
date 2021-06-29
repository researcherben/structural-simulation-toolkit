
Tested with SST-core v10.0 by bhpayne

This directory contains three examples, each with a different concept.
First, use of C++ inheritance is demonstrated in the context of three houses connected by roads.
In the second example, the concept of "assemblies" is introduced in the context of houses being part of neighborhoods.
Third, the concept of mixed fidelity is demonstrated. Abstractions used in the Python driver file (neighborhoods as classes) can be mixed with neighborhoods-as-SST-components. 



In the highest fidelity model, a "neighborhood" is an abstraction used in the SST Python driver file where
* a neighborhood has one or more houses
* a neighborhood has zero or more grocery stores
and a "city" is an abstraction that has one or more neighborhoods

To tune one aspect of simulation fidelity, the neighborhood can be an SST component, and the city can be an SST component.

# Example 1: a neighborhood with three houses

To run this model, use

    make

Here the "house" component inherits from "building" and "weather"

An example neighborhood comprised of SST components would be

          +---------+
          | house_0 |
          +---------+
          |         |
    +-----+---+     ++---------+
    | house_1 |      | house_2 |
    +---------+------+---------+

In the example above, the houses are fully connected by roads.

( ASCII art is from http://asciiflow.com/ )

The Python driver file for SST is already becoming unwieldy and the graph is relatively small!
To combat this complexity, group SST components into classes. (Functions are also viable, but lack inheritance.)

# Example 2: assemblies as abstractions in the SST Python driver file

To run this model, use

    make CONFIG=regional_planning_example2_assemblies

The C++ SST components leverage inheritance, and (separately) the Python driver file uses classes and inheritance.

TODO: not clear how to sync the C++ and Python abstractions. Not clear what aspects of the C++ and Python need to be sync'd.

To create UML diagrams of the respective inheritances for C++ and Python

    doxygen -g

then follow https://stackoverflow.com/a/9488742/1164295

Four neighborhoods could be

                                                                   +----------------+
                                                                   | house_0        |
    +---------------+----------------+-----------------------------+ neighborhood_1 |
    |               | house_0        |                             +----------------+-----------+
    |     +---------+ neighborhood_0 +-+                       +---+                            |
    |     |         +----------------+ |                       |                                |
    |     |                            |                       |   +----------------+     +-----+----------+
    |    ++----------------+         +-+--------------+        |   | house_1        |     | house_2        |
    |    |  house_1        |         | house_2        |        |   | neighborhood_1 +-----+ neighborhood_1 |
    |    |  neighborhood_0 |         | neighborhood_0 |        |   +----------------+     +----------------+
    |    +-----------------+         +----------------+        |
    |                                                          +-------+
    |                                                                  |
    |                        +-------------------------------------+---+------------+
    |        +----------------+                                    | house_0        +---------------+
    +--------+ house_0        +-----+                           +--+ neighborhood_3 |               |
             | neighborhood_2 |     |                           |  +----------------+               |
             ++---------------+     |                           |                                   |
              |                   +-+--------------+            |                              +----+-----------+
              |                   | house_2        |            +----------------+             | house_2        |
       +------+---------+         | neighborhood_2 |            | house_1        +-------------+ neighborhood_3 |
       | house_1        +---------+----------------+            | neighborhood_3 |             +----------------+
       | neighborhood_2 |                                       +----------------+
       +----------------+

While the use of abstractions in the form of classes in the SST Python driver file improves the ability to scale up,
the computational cost of this increased scaling is problematic. 
Therefore, replacing some of the neighborhoods with a single SST component would be useful.

# Example 3: mixed fidelity of houses and neighborhoods

To use this model, run

    make CONFIG=regional_planning_example3_mixedFidelity

With a mixed fidelity,

                                                                   +----------------+
                                                                   | house_0        |
    +---------------+----------------+-----------------------------+ neighborhood_1 |
    |               | house_0        |                             +----------------+-----------+
    |     +---------+ neighborhood_0 +-+                       +---+                            |
    |     |         +----------------+ |                       |                                |
    |     |                            |                       |   +----------------+     +-----+----------+
    |    ++----------------+         +-+--------------+        |   | house_1        |     | house_2        |
    |    |  house_1        |         | house_2        |        |   | neighborhood_1 +-----+ neighborhood_1 |
    |    |  neighborhood_0 |         | neighborhood_0 |        |   +----------------+     +----------------+
    |    +-----------------+         +----------------+        |
    |                                                          +-------+
    |                                                                  |
    |                        +-------------------------------------+---+------------+
    |        +----------------+                                    |                |
    +--------+                |                                    | neighborhood_3 |
             | neighborhood_2 |                                    +----------------+
             +----------------+



# to edit the graphviz files and get the "desired" hypernode graph,
* remove the "simulation" graph (second gv)
* remove "graph [style=invis];" from line 5
* insert "graph [style=invis];" after each "subgraph cluster_"
* indent appropriate subgraphs
* insert appropriate "subgraph cluster_? {" and associated "}"


