
I suspect that if I can build a three-component simulation with a fully-connected graph I will be able to scale to larger simulations.

What progression will enable that?
1. create a component
1. register a component with SST
1. create and register 2 instances of the same component
1. create a link between 2 instances of the same component
1. send a message between 2 instances of the same components
1. create two different components that are connected by a link
1. send a message between 2 different components
1. create and register 3 components with 3 links (1 link per pair)
1. create a component simulation that includes a sleep in each component
1. use MPI to load-balance components. --> Is the MPI-based sim faster than serial?
