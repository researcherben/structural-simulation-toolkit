This tutorial covers the containerization of SST using Docker and how to create a component outside the container.

For context of what SST is and when SST is useful, see


# Step 0: install Docker

Download Docker
https://docs.docker.com/get-docker/

The installation directions are specific to your operating system.
https://docs.docker.com/desktop/

# Step 1: create a Dockerfile for SST

The Dockerfile contains all the software dependencies for SST, as well as the initialization steps needed for configuration of SST.

The Dockerfile assumes the file `sstcore-10.0.0.tar.gz` is available in the same directory. That file is available from
https://github.com/sstsimulator/sst-core/releases/tag/v10.0.0_Final


    cat << EOF > Dockerfile
    # Use baseimage-docker which is a modified Ubuntu specifically for Docker
    # https://hub.docker.com/r/phusion/baseimage
    # https://github.com/phusion/baseimage-docker
    FROM phusion/baseimage:0.11
    
    # Use baseimage-docker's init system
    CMD ["/sbin/my_init"]
    
    # Update and install packages
    RUN apt update && apt -y upgrade && apt -y install \
        build-essential \
        doxygen \
        libtool-bin \
        graphviz \
        time \
        mpich \
        python3-dev \
        python3-pip \
        automake
    
    # Clean up apt mess
    RUN apt clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
    
    ARG USER=sst
    ARG UID=1000
    ARG GID=1000
    # default password for user
    ARG PW=sst
    
    RUN useradd -m ${USER} --uid=${UID} && echo "${USER}:${PW}" | chpasswd
    
    USER ${UID}:${GID}
    WORKDIR /home/${USER}
    
    # Setup Environment for SST
    ARG dir=/home/sst/build
    RUN mkdir -p $dir
    ARG SST_CORE_HOME=/home/sst/sst-core
    ENV SST_CORE_HOME=/home/sst/sst-core
    ENV PATH="$PATH:$SST_CORE_HOME/bin"
    
    WORKDIR $dir
    
    # from https://github.com/sstsimulator/sst-core/releases/tag/v10.0.0_Final
    COPY sstcore-10.0.0.tar.gz .
    RUN tar zxvf sstcore-10.0.0.tar.gz
    RUN mv sstcore-10.0.0 sst-core
    
    # Build SST Core
    RUN cd $dir/sst-core && ./autogen.sh && \
      	./configure --prefix=$SST_CORE_HOME && \
    	  make all install
    
    WORKDIR /home/sst/
    
    # Clean up SST junk
    #RUN rm -rf $dir
    EOF

# Step 2: build image

Once the Dockerfile exists, build the image

    docker build -t sst_10 .

# Step 3: verify the container works

Using the `sst_10` image, verify the container has a working `sst` command

    docker run --rm \
      -v `pwd`:/scratch \
      --user $(id -u):$(id -g) \
      sst_10 sst --version

which should produce the output

    SST-Core Version (10.0.0)

# Step 4: create a C++ component

The component in SST is written in C++

    cat << EOF > ExampleComponent.cc
    // Created for SST-Core Version (9.1.0)
    //
    #include "ExampleComponent.h"
    #include <iostream>
    
    using namespace Example00;
    
    // Component constructor.
    //
    ExampleComponent::ExampleComponent(SST::ComponentId_t id, SST::Params &params) :
        SST::Component(id),
        componentId_(id),
        clockTickCount_(0)
    {
        // Read in the parameters from the python config file.  See SST_ELI_DOCUMENT_PARAMS
        // for an explanation of what each parameter represents.
        //
        std::string clock =
            params.find<std::string>("clock", "1GHz");
        clockTicks_ = static_cast<uint64_t>(
            params.find<int>("clockTicks", 10));
        unsigned int debug =
            params.find<int>("debug", ALL);
    
        // Create the logger.
        //
        logger_ = SST::Output("Time=@t; File=@f; Func=@p; Line=@l; Thread=@I -- ", debug, 0x01, SST::Output::STDOUT);
        logger_.verbose(CALL_INFO, TRACE, 0x00, "Entering constructor for component id %lu\n", componentId_);
    
        // Initialize the debug output instance.
        // Strings for debug output use the printf format.
        //
        logger_.verbose(CALL_INFO, INFO,  0x00, "Initializing component %lu.\n", id);
        logger_.verbose(CALL_INFO, DEBUG, 0x00, "Parameters successfully read from config file.\n");
        logger_.verbose(CALL_INFO, DEBUG, 0x00, "clockTicks = %lu\n", clockTicks_);
        logger_.verbose(CALL_INFO, INFO,  0x00, "Constructing new Example Instance.\n");
    
        // Configure the component clock.
        //
        logger_.verbose(CALL_INFO, DEBUG, 0x00, "Clock rate is: %s\n", clock.c_str());
        registerClock(clock,
            new SST::Clock::Handler<ExampleComponent>(this, &ExampleComponent::clockTick));
        logger_.verbose(CALL_INFO, INFO,  0x00, "Successfully initialized clock.\n");
    
        // Register this component with the simulation.
        //
        registerAsPrimaryComponent();
        logger_.verbose(CALL_INFO, DEBUG, 0x00, "Component registered as primary component.\n");
        primaryComponentDoNotEndSim();
        logger_.verbose(CALL_INFO, DEBUG, 0x00, "Simulation notified it should not end.\n");
        logger_.verbose(CALL_INFO, TRACE, 0x00, "Leaving constructor for component id %lu\n", componentId_);
    }
    
    
    // Called after all components have been constructed and initialization
    // has completed, but before simulation time has begin.
    //
    // This is where you should do any other initialization that needs to be done
    // but could be accomplished in the constructure.
    //
    void ExampleComponent::setup(void)
    {
        logger_.verbose(CALL_INFO, TRACE, 0x00, "Entering setup for component id %lu\n", componentId_);
        logger_.verbose(CALL_INFO, TRACE, 0x00, "Leaving setup for component id %lu\n", componentId_);
    }
    
    
    // Called after the simulation is complete but before the objects are
    // destroyed.  This is a good place to print out statistics.
    //
    void ExampleComponent::finish(void)
    {
        logger_.verbose(CALL_INFO, TRACE, 0x00, "Entering finish for component id %lu\n", componentId_);
        logger_.verbose(CALL_INFO, TRACE, 0x00, "Leaving finish for component id %lu\n", componentId_);
    }
    
    
    // Clock event handler.
    //
    bool ExampleComponent::clockTick(SST::Cycle_t cycle)
    {
        logger_.verbose(CALL_INFO, TRACE, 0x00, "Entering clock for component id %lu\n", componentId_);
    
        // Increment the clock tick counter and end when you get to
        // the specified value.
        //
        clockTickCount_ += 1;
        bool done = (clockTickCount_ == clockTicks_);
    
        logger_.verbose(CALL_INFO, INFO, 0x00, "Clock tick count = %lu out of %lu\n", clockTickCount_, clockTicks_);
        if (done)
        {
            logger_.verbose(CALL_INFO, INFO, 0x00, "Ending sim.\n");
            primaryComponentOKToEndSim();
        }
    
        logger_.verbose(CALL_INFO, TRACE, 0x00, "Leaving clock for component id %lu\n", componentId_);
        return done;
    }
    EOF

    cat << EOF > ExampleComponent.h
    #ifndef MY_COMPONENT_H
    #define MY_COMPONENT_H
    
    #include <sst/core/component.h>
    #include <sst/core/output.h>
    #include <sst/core/params.h>
    
    namespace Example00
    {
        // Define the log levels.  Each level displays its own message and the
        // levels above it.
        //
        // For example, ALL displays all log messages, INFO displays INFO, WARN,
        // and FATAL messages, FATAL displays only FATAL messages.
        //
        const uint64_t FATAL = 0;
        const uint64_t WARN  = 1;
        const uint64_t INFO  = 2;
        const uint64_t DEBUG = 3;
        const uint64_t TRACE = 4;
        const uint64_t ALL   = 5;
    
        // This is a very simple component.  It only registers a clock and 
        // prints log messages as the clock handler is called.
        //
        // Remember, all components inherit from SST::Component
        //
        class ExampleComponent : public SST::Component
        {
            public:
                // Constructor/Destructor
                //
                ExampleComponent(SST::ComponentId_t id, SST::Params &params);
                ~ExampleComponent() {}
    
                // Standard SST::Component functions.  These all need to
                // be implemented in the component, even if they are empty.
                //
                void setup(void);
                void finish(void);
    
                // Clock handler.  This is the method called from the clock event.
                //
                bool clockTick(SST::Cycle_t cycle);
    
                // Shared documentation macros. 
                //
                SST_ELI_DOCUMENT_PARAMS(
                    { "debug", "Debug location:  (0: NONE, 1: STDOUT, 2: STDERR, 3: FILE)", "0" },
                    { "clock", "Component clock rate", "1GHz" },
                    { "clockTicks", "Number of times the handler is called before ending.", "10" }
                )
                
                SST_ELI_REGISTER_COMPONENT(
                    ExampleComponent,                       // Class name
                    "example",                              // Library name (the *.so)
                    "ExampleComponent",                     // Name used to reference the component.  This can be
                                                            // whatever you want it to be and will be referenced
                                                            // in the python configuration file.
                    SST_ELI_ELEMENT_VERSION( 1, 0, 0 ),     // Version number
                    "Clock element example",                // Description                 
                    COMPONENT_CATEGORY_UNCATEGORIZED        // Component category
                )
    
            private:
                // Member variables for this example.
                //
                SST::Output logger_;        // For displaying log messages.
                uint64_t componentId_;      // SST supplied component id.
                uint64_t clockTicks_;       // Maximum number of clock ticks.
                uint64_t clockTickCount_;   // Clock ticks counter.
    
        };  // Close the class
    }   // Close the namespace
    
    #endif
    EOF

# Step 5: create a Python driver file

The Python driver file specifies the graph of SST components.

    cat << EOF > ExampleConfig.py
    # Execute from the command line with the command:
    #   sst Example00Config.py 2>&1 | tee test.log
    #
    import sst
    
    # Initialize local variables.
    #
    clockTicks = "10"   # Number of clock ticks before the simulation ends
    clock = "1GHz"      # Simulation clock rate
    debug = "2"         # debug level
                        # 0 = FATAL, 1 = WARN, 2 = INFO, 3 = DEBUG, 4 = TRACE, 5 = ALL
    
    componentName0 = "example00"
    
    # Define the component.
    #
    # The parameters are a dictionary and can be any key/value pair defined
    # by the component itself.
    #
    # The second parameter is <library>.<registered_name>
    # These correspond to the second and third parameters of the
    # SST_ELI_REGISTER_COMPONENT macro in Example00Component.h,
    # respectively.
    #
    obj = sst.Component(componentName0, "example.ExampleComponent")
    obj.addParams({
        "clock"      : clock,
        "clockTicks" : clockTicks,
        "debug"      : debug
        })
    EOF

# Step 6: create a Makefile

Having a Makefile for the build process steps ensures a consistent and repeatable process. The Makefile will become even more useful as more components are created.

    cat << EOF > Makefile
    
    CXX=$(shell sst-config --CXX)
    CXXFLAGS=$(shell sst-config --ELEMENT_CXXFLAGS)
    LDFLAGS=$(shell sst-config --ELEMENT_LDFLAGS)
    
    all: libexample.so install
    
    libexample.so: ExampleComponent.cc\
    	             ExampleComponent.h
    	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $<
    
    install:
    	sst-register example example_LIBDIR=$(CURDIR)
    
    clean:
    	rm -f *.o libexample.so
    EOF

# Step 7: build .so for component

Use the Makefile to generate the .so and register with SST.

The configuration for SST's components is in the file `/home/sst/sst-core/etc/sst/sstsimulator.conf`
We could have made that file writable inside the image using

    RUN chmod a+w /home/sst/sst-core/etc/sst/sstsimulator.conf

but we want the registration to persist outside the image. Therefore, use a
[Docker mount](https://docs.docker.com/storage/bind-mounts/)

    touch sstsimulator.conf
    docker run --rm \
      --volume `pwd`:/scratch \
      --mount type=bind,source=`pwd`/sstsimulator.conf,target=/home/sst/sst-core/etc/sst/sstsimulator.conf \
      --user $(id -u):$(id -g) \
      -w /scratch \
      sst_10 make

# Step 8: check that the component is registered

The `sst-info` command returns registered components

    docker run --rm \
      --volume `pwd`:/scratch \
      --mount type=bind,source=`pwd`/sstsimulator.conf,target=/home/sst/sst-core/etc/sst/sstsimulator.conf \
      --user $(id -u):$(id -g) \
      -w /scratch \
      sst_10 sst-info

which should return something like

    PROCESSED 1 .so (SST ELEMENT) FILES FOUND IN DIRECTORY(s) /scratch
    ================================================================================
    ELEMENT 0 = example ()
    Num Components = 1
          Component 0: ExampleComponent

# Step 9: run the simulation

    docker run -it --rm \
      --volume `pwd`:/scratch \
      --mount type=bind,source=`pwd`/sstsimulator.conf,target=/home/sst/sst-core/etc/sst/sstsimulator.conf \
      --user $(id -u):$(id -g) \
      -w /scratch \
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

    docker run --rm \
      --volume `pwd`:/scratch \
      --mount type=bind,source=`pwd`/sstsimulator.conf,target=/home/sst/sst-core/etc/sst/sstsimulator.conf \
      --user $(id -u):$(id -g) \
      -w /scratch \
      sst_10 sst --output-dot=ExampleConfig.gv --run-mode=init ExampleConfig.py

which should return something like

    WARNING: Building component "example00" with no links assigned.
    Time=0; File=ExampleComponent.cc; Func=ExampleComponent; Line=33; Thread=0 -- Initializing component 0.
    Time=0; File=ExampleComponent.cc; Func=ExampleComponent; Line=36; Thread=0 -- Constructing new Example Instance.
    Time=0; File=ExampleComponent.cc; Func=ExampleComponent; Line=43; Thread=0 -- Successfully initialized clock.
    Simulation is complete, simulated time: 0 s

Generate the PNG using

    docker run --rm \
      --volume `pwd`:/scratch \
      --mount type=bind,source=`pwd`/sstsimulator.conf,target=/home/sst/sst-core/etc/sst/sstsimulator.conf \
      --user $(id -u):$(id -g) \
      -w /scratch \
      sst_10 dot ExampleConfig.gv -Tpng > ExampleConfig.png
