# Performance benchmarking and Regression testing

Questions to address:
* how many empty nodes can be instantiated?
* how many empty nodes in a ring can be instantiated?
* for a ring with N empty nodes, how many node-to-node messages can be sent in 1 wall clock minute? (one message going around the ring)
* for a ring with N empty nodes, how many node-to-node messages can be sent concurrently in 1 wall clock minute?
The above questions can be investigated for both serial simulations and threaded simulations and with MPI nodes

# Memory profiling

How to use Valgrind with SST:
<https://sst-simulator.org/SSTPages/SSTDeveloperValgrind/>

Not relevant to this effort: SST CPU Trace Model based on Linux Valgrind
<https://github.com/sstsimulator/sst-valgrind-tracer>
