
# computer simulation is an overloaded phrase

There are many types of [computer simulation](https://en.wikipedia.org/wiki/Computer_simulation), including
* [finite element analysis](https://en.wikipedia.org/wiki/Finite_element_method) for structural analysis, electromagnetics, etc
* [discrete event simulation](https://en.wikipedia.org/wiki/Discrete-event_simulation) -- useful for timing in the context of multiple queues
* numerical simulation, e.g., differential equations for fluid dynamics (weather models)

# Discrete-event simulation

<https://www.southampton.ac.uk/~mb1a10/sim/Discrete_Event.pdf>  

<https://en.wikipedia.org/wiki/DEVS>; see also ["Formal Framework for Discrete-Event Simulation"](https://hal.archives-ouvertes.fr/hal-01562929/document)

Domains that share the DES label but are not in scope for SST because they feature person-in-the-loop: [hospital simulations](https://www.ncbi.nlm.nih.gov/books/NBK293948/) and military training in aviation.


DES jargon: A "referent" is the thing being simulated.

# SST is one of many Discrete-event simulators

Other DES software:
* Python SimPy - <https://en.wikipedia.org/wiki/SimPy> and <https://www.researchgate.net/publication/322949363_Discrete_Event_Simulation_It's_Easy_with_SimPy>
* R - <https://rdrr.io/cran/simmer/>
* <https://www.nsnam.org/docs/models/html/distributed.html>

See also <https://en.wikipedia.org/wiki/List_of_discrete_event_simulation_software>


## What makes SST distinct from other DES options?

SST as a framework for DES simulators is not focused on a specific problem or domain. 

SST supports distributed computation using MPI.



