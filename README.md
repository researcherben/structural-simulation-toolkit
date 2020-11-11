# structural-simulation-toolkit
Sandia National Lab's Structural Simulation Toolkit - https://github.com/sstsimulator

## documentation
* https://sst-simulator.org/SSTPages/SSTDeveloperSSTForNewbies/
* http://sst-simulator.org/sst-website/
* http://sst-simulator.org/SSTPages/SSTMainDocumentation/
* https://sst-simulator.org/SSTPages/SSTDeveloperCreateYourOwnElement/
* https://sst-simulator.org/SSTPages/SSTDeveloperIntegrateYourElementWithSST/
* https://sst-simulator.org/SSTPages/SSTDeveloper10dot0PythonModule/
* https://sst-simulator.org/SSTPages/SSTDeveloperElementSummaryInfo/

## content

File types present:
* `*.cc` - C++ source code
* `*.h` - header files for C++
* `*.m4` - https://en.wikipedia.org/wiki/M4_(computer_language)
* Makefile
* `*.py` - Python files
* `*.lo` - libtool object file; generated by libtool

## build Docker

    make docker

The initial build process takes 1.5 hours from source for core+elements

## use

What version of SST is this?

    sst --version

what components are registered?

    sst-info

test an example by running

    sst build/sst-elements/src/sst/elements/simpleElementExample/tests/test_simpleRNGComponent_mersenne.py
    sst build/sst-elements/src/sst/elements/simpleElementExample/tests/test_simpleClockerComponent.py
    sst build/sst-elements/src/sst/elements/simpleElementExample/tests/test_simpleLookupTable.py
    sst build/sst-elements/src/sst/elements/simpleSimulation/tests/test_simpleCarWash.py

Each of the .py scripts is a configuration for a simulation (SST jargon: "Project Driver file"). The components are compiled from .cc and .h file.
See https://sst-simulator.org/SSTPages/SSTUserPythonFileFormat/
All of the examples are a single isolated component. (Nothing demonstrating a link?)

To generate a graphviz of the components and links, use

    sst --output-dot=${outfile}.gv --run-mode=init ${cfgfile}.py

where "outfile" is the name of the graphviz file produced and "cfgfile" is the Python Project Driver file.

    docker run -it --rm -v `pwd`:/scratch sst:latest sst --output-dot=/scratch/file.gv --run-mode=init /home/sst/build/sst-elements/src/sst/elements/simpleElementExample/tests/subcomponent_tests/test_sc_2a.py
    docker run -it --rm -v `pwd`:/scratch sst:latest dot /scratch/file.gv -Tpng > file.png

## demos examples tutorials

see https://sst-simulator.org/SSTPages/SSTMainDownloads/#SSTutorials and https://github.rcac.purdue.edu/green349/sst-tutorial/tree/master/exercises (which has more than https://github.com/sstsimulator/sst-tutorials/tree/master/exercises)

## SST jargon

* Elements = dynamically loaded libraries.
* ELI = Element Library Information
* Components - These are top level simulation objects. Most Elements contain at least one of these
* SubComponents - An simulation objects that can be loaded by other Components.
* Python Module Generators - C++ extensions that can be loaded and run from the SST Python Input file.
* Events - Data objects to be passed between Components and SubComponents.
* Links: components communicate using Links to pass events. Every link contains a name, port, and latency
* Ports = specifies which port of the link we are connecting to
