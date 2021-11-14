# Assumptions

This directory assumes `sst` is available.

# Use

What version of SST is being used?
```bash
$ sst --version
SST-Core Version (11.1.0)
```

Prior to running the benchmark, need to register the components
```bash
make install
no "CONFIG" was provided, so defaulting to "config_network"
g++  -std=c++1y -D__STDC_FORMAT_MACROS -fPIC -DHAVE_CONFIG_H -I/home/sst/sst-core/include -shared -fno-common -Wl,-undefined -Wl,dynamic_lookup -o libtwoexample.so some_component.cpp
sst-register two_example two_example_LIBDIR=/scratch/ring
```

Try running the Python driver file
```bash
$ sst config_network.py 
ERROR: two arguments required:
   number of clock ticks [integer]>0
   number of nodes [integer]>0
```

Run the Python driver file, providing the necessary command-line arguments
```bash
$ /usr/bin/time sst config_network.py 3 10
ticks: 3
nodes: 10
Simulation is complete, simulated time: 4 ns
0.03user 0.03system 0:00.24elapsed 30%CPU (0avgtext+0avgdata 30408maxresident)k
0inputs+0outputs (0major+5292minor)pagefaults 0swaps
```

Create a PNG showing the graph
```bash
$ make picture
no "CONFIG" was provided, so defaulting to "config_network"
no "TICKS" was provided, so defaulting to "3"
no "NODES" was provided, so defaulting to "5"
sst --output-dot=config_network.gv --run-mode=init config_network.py 3 5
ticks: 3
nodes: 5
Simulation is complete, simulated time: 0 s
dot config_network.gv -Tpng > config_network.png
```

Wallclock is longer when there are more nodes
```bash
$ /usr/bin/time sst config_network.py 3 1000
ticks: 3
nodes: 1000
Simulation is complete, simulated time: 4 ns
0.16user 0.09system 0:04.48elapsed 5%CPU (0avgtext+0avgdata 33304maxresident)k
0inputs+0outputs (0major+6006minor)pagefaults 0swaps
```

Loop over number of nodes and write values to file
```bash
for node in {1..300..100}; do 
   echo ${node}; 
   /usr/bin/time sst config_network.py 3 ${node} &>> ring_3concurrent_messages_upto300nodes_step100.dat; 
done
```
