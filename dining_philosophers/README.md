
Motivation: contention in parallel systems

Problem description: 
<https://www.mathworks.com/help/simevents/ug/dining-philosophers-problem.html>  
<https://en.wikipedia.org/wiki/Dining_philosophers_problem>

# create a mockup to explore design choices

A mockup is useful to investigate "what is a component in the system?" and "what is the interface between components?"


# create a functional prototype

* what data is exchanged between components?
* What data transformation is applied by components?
* What is logged by each component?
* When does the simulation end?

# create a discrete event simulation

Challenges:
* Identify a condition that creates [deadlock](https://en.wikipedia.org/wiki/Deadlock)
* Identify a condition that creates [livelock](https://en.wikipedia.org/wiki/Deadlock#Livelock)

