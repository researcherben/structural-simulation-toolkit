#!/usr/bin/env bash

readme_filename=README.md

rm ${readme_filename}

cat << endofsnippet > ${readme_filename}
This tutorial covers the containerization of SST using Docker and how to create a component outside the container.

For context of what SST is and when SST is useful, see


# Step 0: install Docker

Download Docker
https://docs.docker.com/get-docker/

The installation directions are specific to your operating system.
https://docs.docker.com/desktop/

# Step 1: create a Dockerfile for SST

The Dockerfile contains all the software dependencies for SST, as well as the initialization steps needed for configuration of SST.

The Dockerfile assumes the file \`sstcore-10.0.0.tar.gz\` is available in the same directory. That file is available from
https://github.com/sstsimulator/sst-core/releases/tag/v10.0.0_Final


    cat << EOF > Dockerfile
endofsnippet
cat Dockerfile | sed -e 's/^/    /g' >> ${readme_filename}
cat << endofsnippet >> ${readme_filename}
    EOF

# Step 2: build image

Once the Dockerfile exists, build the image

docker build -t sst_10 .

# Step 3: verify the container works

Using the \`sst_10\` image, verify the container has a working \`sst\` command

    docker run --rm \\
      -v \`pwd\`:/scratch \\
      --user \$(id -u):\$(id -g) \\
      sst_10 sst --version

which should produce the output

    SST-Core Version (10.0.0)

# Step 4: create a C++ component

The component in SST is written in C++

    cat << EOF > ExampleComponent.cc
endofsnippet
curl https://raw.githubusercontent.com/researcherben/structural-simulation-toolkit/master/sst_tutorial/Example00/ExampleComponent.cc > ExampleComponent.cc
cat ExampleComponent.cc | sed -e 's/^/    /g' >> ${readme_filename}
cat << endofsnippet >> ${readme_filename}
    EOF

    cat << EOF > ExampleComponent.h
endofsnippet
curl https://raw.githubusercontent.com/researcherben/structural-simulation-toolkit/master/sst_tutorial/Example00/ExampleComponent.h > ExampleComponent.h
cat ExampleComponent.h | sed -e 's/^/    /g' >> ${readme_filename}
cat << endofsnippet >> ${readme_filename}
    EOF

# Step 5: create a Python driver file

The Python driver file specifies the graph of SST components.

    cat << EOF > ExampleConfig.py
endofsnippet
curl https://raw.githubusercontent.com/researcherben/structural-simulation-toolkit/master/sst_tutorial/Example00/tests/ExampleConfig.py > ExampleConfig.py
cat ExampleConfig.py | sed -e 's/^/    /g' >> ${readme_filename}
cat << endofsnippet >> ${readme_filename}
    EOF

# Step 6: create a Makefile

Having a Makefile for the build process steps ensures a consistent and repeatable process. The Makefile will become even more useful as more components are created.

    cat << EOF > Makefile
endofsnippet
curl https://raw.githubusercontent.com/researcherben/structural-simulation-toolkit/master/sst_tutorial/Example00/Makefile > Makefile
cat Makefile | sed -e 's/^/    /g' >> ${readme_filename}
cat << endofsnippet >> ${readme_filename}
    EOF

# Step 7: build .so for component

Use the Makefile to generate the .so and register with SST.

The configuration for SST's components is in the file \`/home/sst/sst-core/etc/sst/sstsimulator.conf\`
We could have made that file writable inside the image using

    RUN chmod a+w /home/sst/sst-core/etc/sst/sstsimulator.conf

but we want the registration to persist outside the image. Therefore, use a
[Docker mount](https://docs.docker.com/storage/bind-mounts/)

    touch sstsimulator.conf
    docker run --rm \\
      --volume \`pwd\`:/scratch \\
      --mount type=bind,source=\`pwd\`/sstsimulator.conf,target=/home/sst/sst-core/etc/sst/sstsimulator.conf \\
      --user \$(id -u):\$(id -g) \\
      -w /scratch \\
      sst_10 make

# Step 8: check that the component is registered

The \`sst-info\` command returns registered components

    docker run --rm \\
      --volume \`pwd\`:/scratch \\
      --mount type=bind,source=\`pwd\`/sstsimulator.conf,target=/home/sst/sst-core/etc/sst/sstsimulator.conf \\
      --user \$(id -u):\$(id -g) \\
      -w /scratch \\
      sst_10 sst-info

which should return something like

    PROCESSED 1 .so (SST ELEMENT) FILES FOUND IN DIRECTORY(s) /scratch
    ================================================================================
    ELEMENT 0 = example ()
    Num Components = 1
          Component 0: ExampleComponent

# Step 9: run the simulation

    docker run -it --rm \\
      --volume \`pwd\`:/scratch \\
      --mount type=bind,source=\`pwd\`/sstsimulator.conf,target=/home/sst/sst-core/etc/sst/sstsimulator.conf \\
      --user \$(id -u):\$(id -g) \\
      -w /scratch \\
      sst_10 sst ExampleConfig.py

which should return something like

    WARNING: Building component "example00" with no links assigned.
    Time=0; File=ExampleComponent.cc; Func=ExampleComponent; Line=33; Thread=0 -- Initializing component 0.
    Time=0; File=ExampleComponent.cc; Func=ExampleComponent; Line=36; Thread=0 -- Constructing new Example Instance.
    Time=0; File=ExampleComponent.cc; Func=ExampleComponent; Line=43; Thread=0 -- Successfully initialized clock.
    Time=1000; File=ExampleComponent.cc; Func=clockTick; Line=90; Thread=0 -- Clock tick count = 1 out of 10
    Time=2000; File=ExampleComponent.cc; Func=clockTick; Line=90; Thread=0 -- Clock tick count = 2 out of 10
    Time=3000; File=ExampleComponent.cc; Func=clockTick; Line=90; Thread=0 -- Clock tick count = 3 out of 10
    Time=4000; File=ExampleComponent.cc; Func=clockTick; Line=90; Thread=0 -- Clock tick count = 4 out of 10
    Time=5000; File=ExampleComponent.cc; Func=clockTick; Line=90; Thread=0 -- Clock tick count = 5 out of 10
    Time=6000; File=ExampleComponent.cc; Func=clockTick; Line=90; Thread=0 -- Clock tick count = 6 out of 10
    Time=7000; File=ExampleComponent.cc; Func=clockTick; Line=90; Thread=0 -- Clock tick count = 7 out of 10
    Time=8000; File=ExampleComponent.cc; Func=clockTick; Line=90; Thread=0 -- Clock tick count = 8 out of 10
    Time=9000; File=ExampleComponent.cc; Func=clockTick; Line=90; Thread=0 -- Clock tick count = 9 out of 10
    Time=10000; File=ExampleComponent.cc; Func=clockTick; Line=90; Thread=0 -- Clock tick count = 10 out of 10
    Time=10000; File=ExampleComponent.cc; Func=clockTick; Line=93; Thread=0 -- Ending sim.
    Simulation is complete, simulated time: 10 ns

# Step 10: generate a picture of the component graph

Generate the GraphViz file using

    docker run --rm \\
      --volume \`pwd\`:/scratch \\
      --mount type=bind,source=\`pwd\`/sstsimulator.conf,target=/home/sst/sst-core/etc/sst/sstsimulator.conf \\
      --user \$(id -u):\$(id -g) \\
      -w /scratch \\
      sst_10 sst --output-dot=ExampleConfig.gv --run-mode=init ExampleConfig.py

which should return something like

    WARNING: Building component "example00" with no links assigned.
    Time=0; File=ExampleComponent.cc; Func=ExampleComponent; Line=33; Thread=0 -- Initializing component 0.
    Time=0; File=ExampleComponent.cc; Func=ExampleComponent; Line=36; Thread=0 -- Constructing new Example Instance.
    Time=0; File=ExampleComponent.cc; Func=ExampleComponent; Line=43; Thread=0 -- Successfully initialized clock.
    Simulation is complete, simulated time: 0 s

Generate the PNG using

    docker run --rm \\
      --volume \`pwd\`:/scratch \\
      --mount type=bind,source=\`pwd\`/sstsimulator.conf,target=/home/sst/sst-core/etc/sst/sstsimulator.conf \\
      --user \$(id -u):\$(id -g) \\
      -w /scratch \\
      sst_10 dot ExampleConfig.gv -Tpng > ExampleConfig.png
endofsnippet

# EOF
