This directory contains various scaling studies

TODO: scaling of options described in <https://github.com/researcherben/structural-simulation-toolkit/tree/master/customizing-link-object>

TODO: topologies to benchmark: ring, tree

# Performance benchmarking and Regression testing

Questions to address:
* how long does it take to instantiate `N` empty nodes (no links)?
* how much memory does it take to instantiate `N` empty nodes (no links)?
* how long does it take to instantiate `N` empty nodes in a ring (connected by links)?
* how much memory does it take to instantiate `N` empty nodes in a ring (connected by links)?
* for a ring with N empty nodes, after instantiation, how many node-to-node messages can be sent in 1 wall clock minute? (one message going around the ring)
* for a ring with N empty nodes, after instantiation, how many node-to-node messages can be sent concurrently in 1 wall clock minute?
The above questions can be investigated for both serial simulations and threaded simulations and with MPI nodes

# Memory profiling

How to use Valgrind with SST:
<https://sst-simulator.org/SSTPages/SSTDeveloperValgrind/>

Not relevant to this effort: SST CPU Trace Model based on Linux Valgrind
<https://github.com/sstsimulator/sst-valgrind-tracer>
 
