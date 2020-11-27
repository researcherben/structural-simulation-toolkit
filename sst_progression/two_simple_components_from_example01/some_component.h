// #ifndef and #define are known as header guards.
// Their primary purpose is to prevent C++ header
// files from being included multiple times.
// This is a "best practice" for C++ and is not specific to SST
#ifndef MY_COMPONENT_H
#define MY_COMPONENT_H


// defines the SST base component from which all SST components are derived.
#include <sst/core/component.h>

// contains definitions used for logging.
#include <sst/core/output.h>

// contains definitions used to process incoming parameters
// from the simulation configuration file
#include <sst/core/params.h>

#include <sst/core/link.h>


// not strictly necessary to create a C++ namespace but is useful to prevent name clashes
namespace ExampleTwo
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
    // all components inherit from SST::Component
    //
    class ExampleComponent : public SST::Component
    {
        // access modifier to override the default of "private"
        public:
            // Constructor/Destructor
            // A class constructor is a special member function of a class that
            // is executed whenever we create new objects of that class.
            // Must have exact same name as the class and
            // it does not have any return type
            ExampleComponent(SST::ComponentId_t id, SST::Params &params);
            // purpose of C++ destructor is to deallocate the memory of an object.
            ~ExampleComponent() {}

            // Standard SST::Component functions.  These all need to
            // be implemented in the component, even if they are empty.
            void setup(void);
            void finish(void);

            // Links to connect to other component.
            // The link connects to the components port.
            //
            SST::Link* this_port;
            SST::Link* port_a;
            SST::Link* port_b;
            // bhp - not clear how to make this a vector
            // std::vector<SST::Link*> ports;
            // for (int index=0; index<=5; ++index)
            // {
            //     ports.push_back( SST::Link* port_0 );
            // }
            SST::Link* port_0;
            SST::Link* port_1;
            SST::Link* port_2;
            SST::Link* port_3;
            SST::Link* port_4;
            SST::Link* port_5;

            // Clock handler.  This is the method called from the clock event.
            //
            bool clockTick(SST::Cycle_t cycle);

            // Shared documentation macros.
            // see https://sst-simulator.org/SSTPages/SSTDeveloperNewELIMigrationGuide/#parameters
            SST_ELI_DOCUMENT_PARAMS(
                // triples of "name", "description", "default value"
                { "debug", "Debug location:  (0: NONE, 1: STDOUT, 2: STDERR, 3: FILE)", "0" },
                { "clock", "Component clock rate", "1GHz" },
                { "clockTicks", "Number of times the handler is called before ending.", "10" }
            )
            // these values will be overridden by the Python configuration if supplied

            // see https://sst-simulator.org/SSTPages/SSTDeveloperNewELIMigrationGuide/#component
            SST_ELI_REGISTER_COMPONENT(
                ExampleComponent,                       // Class name
                "twoexample",                              // Library name (the *.so)
                "ExampleComponent",                     // Name used to reference the component.  This can be
                                                        // whatever you want it to be and will be referenced
                                                        // in the python configuration file.
                                                        // The full name of the component will be library.name
                SST_ELI_ELEMENT_VERSION( 1, 0, 0 ),     // Version number
                "Clock element example",                // Description
                COMPONENT_CATEGORY_UNCATEGORIZED        // Component category; see elibase.h for options
            )

            //std::vector<char> supported_events = {"none"};
            //std::tuple<char, char, std::vector<char>> example = { "port_a", "the port", supported_events};

            // bhp - if I can build a vector of the ports, I could build the port list using a for loop
            // std::vector<std::vector> my_list;
            // my_list.push_back({ "port_a", "the port", {}});
            // my_list.push_back({ "port_b", "the port", {}});
            // my_list.push_back({ "port_0", "the port", {}});
            // my_list.push_back({ "port_1", "the port", {}});
            // my_list.push_back({ "port_2", "the port", {}});
            // my_list.push_back({ "port_3", "the port", {}});
            // my_list.push_back({ "port_4", "the port", {}});
            // my_list.push_back({ "port_5", "the port", {}});

            // see https://sst-simulator.org/SSTPages/SSTDeveloperNewELIMigrationGuide/#ports
            // the following isn't conducive to a loop
            SST_ELI_DOCUMENT_PORTS(
              { "port_a", "the port", {}},
              { "port_b", "the port", {}},
              { "port_0", "the port", {}},
              { "port_1", "the port", {}},
              { "port_2", "the port", {}},
              { "port_3", "the port", {}},
              { "port_4", "the port", {}},
              { "port_5", "the port", {}}
              )

        private:
            // Member variables for this example.
            // Data members of C++ classes have trailing underscores
            // as per https://google.github.io/styleguide/cppguide.html
            SST::Output logger_;        // For displaying log messages.
            uint64_t componentId_;      // SST supplied component id.
            uint64_t clockTicks_;       // Maximum number of clock ticks.
            uint64_t clockTickCount_;   // Clock ticks counter.

    };  // Close the class
}   // Close the namespace

#endif
