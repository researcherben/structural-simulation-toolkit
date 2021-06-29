#ifndef EXAMPLE_COMPONENT_H
#define EXAMPLE_COMPONENT_H

#include <sst/core/component.h>
#include <sst/core/subcomponent.h>
#include <sst/core/link.h>
#include <sst/core/output.h>
#include <sst/core/params.h>

#include "Logger.hpp"
#include "EvenOddConnection.h"

namespace Example
{
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

            // Slot to hold a subcomponent.
            //
            std::vector<EvenOddConnection*> connections_;

            // Clock handler.  This is the method called from the clock event.
            //
            bool clockTick(SST::Cycle_t cycle);

            // Shared documentation macros. 
            //
            SST_ELI_DOCUMENT_PARAMS(
                { "clock", "Component clock rate", "1GHz" },
                { "clockTicks", "Number of times the handler is called before ending.", "10" }
            )
            
            SST_ELI_REGISTER_COMPONENT(
                ExampleComponent,                       // Class name
                "example",                              // Library name (the *.so)
                "ExampleComponent",                     // Named use to reference the component.  This can be
                                                        // whatever you want it to be and will be referenced
                                                        // in the python configuration file.
                SST_ELI_ELEMENT_VERSION( 1, 0, 0 ),     // Version number
                "Clock element example",                // Description                 
                COMPONENT_CATEGORY_UNCATEGORIZED        // Component category
            )

            // Document the subcomponent slots.
            //
            SST_ELI_DOCUMENT_SUBCOMPONENT_SLOTS(
                // Slot name, description, slot type
                //
                // Slot name is just a name.  It can be anything that makes sense but will
                // be used later to refer to this slot.
                //
                // Description is just that.  Can be anything.
                //
                // Slot type is the subcomponent fully qualified class name.
                //
                {"slot_", "Slot to hold a subcomponent", "Example::EvenOddConnection"}
            )

        private:

            // Member variables for this example.
            //
            uint64_t componentId_;      // SST supplied component id.
            uint64_t clockTickCount_;   // 
            uint32_t clockCount_;       //
            uint64_t clockTicks_;       // Maximum number of allowed clock ticks.

            void messageHandler(SST::Event* event);
            std::vector<EvenOddConnection*> configureSubComponents(SST::Params &params);
            
    };  // Close the class
}   // Close the namespace

#endif