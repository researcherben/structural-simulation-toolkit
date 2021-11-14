# Assumptions

This directory assumes `sst` is available.

# Use

```bash
$ sst config_network.py 
ERROR: two arguments required:
   number of clock ticks [integer]>0
   number of nodes [integer]>0
```

```bash
$ /usr/bin/time sst config_network.py 3 10
ticks: 3
nodes: 10
Simulation is complete, simulated time: 4 ns
0.03user 0.03system 0:00.24elapsed 30%CPU (0avgtext+0avgdata 30408maxresident)k
0inputs+0outputs (0major+5292minor)pagefaults 0swaps
```

```bash
$ /usr/bin/time sst config_network.py 3 1000
ticks: 3
nodes: 1000
Simulation is complete, simulated time: 4 ns
0.16user 0.09system 0:04.48elapsed 5%CPU (0avgtext+0avgdata 33304maxresident)k
0inputs+0outputs (0major+6006minor)pagefaults 0swaps
```

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


