#ifndef EVENODDCONNECTION_SUBCOMPONENT_H
#define EVENODDCONNECTION_SUBCOMPONENT_H

#include <functional>
#include <optional>

#include <sst/core/subcomponent.h>
#include <sst/core/output.h>
#include <sst/core/link.h>

#include "ExampleEvent.h"
#include "Logger.hpp"

using namespace SST;
using namespace SSTLogger;

extern SSTLogger::Logger logger_;

namespace Example
{
    class EvenOddConnection : public SST::SubComponent
    {
        private:
            // Link to connect to matching subcomponent.
            // The link connects to the opposite subcomponents port.
            //
            SST::Link* link_ = nullptr;

            // Callback provided by the parent component.
            //            
            std::function<void(SST::Event*)> callback_ = nullptr;
            
            // Count sent to the connected subcomponent.
            //
            uint64_t componentId_;      // Id associated with the parent component.
            uint64_t slotNumber_;       // Slot number associated with the subcomponent.

            // Private methods
            //
            // Event handler for incoming messages.
            //
            void messageHandler(SST::Event* event)
            {
                logger_.logTrace(CALL_INFO, "Entering connection messageHandler()\n");

                // Call the specified message handler.
                //
                if (callback_ != nullptr)
                    callback_(event);

                // Don't forget to delete the event when you're done with it.
                // Otherwise you'll get a serious memory leak.
                //
                if (event != nullptr)
                    delete event;

                logger_.logTrace(CALL_INFO, "Leaving connection messageHandler()\n");
            }

        public:

            // Updated constructors.  As of SST V10 no longer pass in a parent.
            // Instead, use a component id.
            //
            EvenOddConnection(ComponentId_t id) :
                SubComponent(id)
            { 
                componentId_ = id;
                logger_.logDebug(CALL_INFO, "Constructing connection for component id %u\n", componentId_);
            }

            EvenOddConnection(ComponentId_t id, Params& UNUSED(params)) :
                SubComponent(id)
            {   
                componentId_ = id;     
                logger_.logDebug(CALL_INFO, "Constructing connection for component id %u\n", componentId_);
            }

            virtual ~EvenOddConnection() {}


            // Method to initialize the connection.  Serves the same purpose as the 
            // start() method in a component.  However, it must bge called explicitly.
            //
            void start(
                uint64_t slotNumber,
                SST::Params &params) 
            {
                logger_.logTrace(CALL_INFO, "Initializing connection, slot number %u in component id %u\n", 
                    slotNumber, componentId_);

                // Process the incoming paramaters.
                //
                slotNumber_ = slotNumber;
                std::string clock = 
                    params.find<std::string>("clock", "1GHz");  // Simulation clock rate.  Default to 1 GHz.
                
                // Configure the attached link.
                //
                link_ = configureLink("link_", clock,
                    new SST::Event::Handler<EvenOddConnection>(this, &EvenOddConnection::messageHandler)); 
                
                logger_.logTrace(CALL_INFO, "Connection initialized.\n");
            }


            // Event handler for incoming messages.
            //
            void setMessageHandler(std::function<void(SST::Event*)> callback)
            {
                logger_.logTrace(CALL_INFO, "Entering subcomponent setMessageHandler() method on component %u, slot %u\n",
                    componentId_, 
                    slotNumber_);

                callback_ = callback;

                logger_.logTrace(CALL_INFO, "Leaving subcomponent messageHandler()\n");
            }


            // Send the event message over the link.
            //
            void send(SST::Event* event) 
            {
                logger_.logTrace(CALL_INFO, "Entering subcomponent send() method on component %u, slot %u\n",
                    componentId_, slotNumber_);

                // Only send the message if the payload is an even number.
                //                
                int32_t payload = static_cast<ExampleEvent*>(event)->getPayload();
                if ((payload %2) == 0)
                {
                    logger_.logInfo(CALL_INFO, "Payload is even.  Sending message from component %u, slot %u\n", 
                        componentId_, slotNumber_);
                    link_->send(event);
                }
                else
                {
                    logger_.logInfo(CALL_INFO, "Payload is odd.  Dropping message.\n");
                }

                logger_.logTrace(CALL_INFO, "Leaving subcomponent method sendCount()\n");
            }


            // Clock handler.  This is the method called from the parent clock event.
            //
            virtual void clockTick(Cycle_t) 
            {
                logger_.logTrace(CALL_INFO, "Entering subcomponent method clock\n");
                logger_.logTrace(CALL_INFO, "Leaving subcomponent method clock\n");
            }


            // Document the component ports.
            //
            // Port name, description, vector fo supported events.
            //
            // Port name is just a name.  It can be anything that makes sense but will
            // be used later to refer to this port.
            //
            // Description is just that.  Can be anything.
            //
            // Support events is a std::vector of the names of supported events.  These
            // are initialized as {"lib1.event1", "lib1.event2", "lib2.event3"}.
            // Note these are the names as strings, not types.
            //
            SST_ELI_DOCUMENT_PORTS(
                { "link_", "Message port", {}}
            )

            // Register the subcomponent API.
            //
            SST_ELI_REGISTER_SUBCOMPONENT_API(Example::EvenOddConnection)

            // Register the subcomponent.
            //
            SST_ELI_REGISTER_SUBCOMPONENT_DERIVED(
                EvenOddConnection,                  // Name of the class being registered.
                                                    // INSERT_CLASS_NAME
                "example",                          // Element library.  Name of the .so.
                "EvenOddConnection",                // Name used to reference the subcomponent.
                                                    // Can be anything but typically set to
                                                    // the class name.
                SST_ELI_ELEMENT_VERSION(1, 0, 0),   // 
                "Example subcomponent",             // Brief subcomponent description
                Example::EvenOddConnection          // Name of the subcomponent interface the
                                                    // subcomponent inherits from.  Should be
                                                    // the full parent class name, matching the
                                                    // name used when registering the
                                                    // subcomponent API.
                                                    // "INSERT_FULL_PARENT_CLASS_NAME" or 
                                                    // "INSERT_COMPLETE_NAMESPACE::INSERT_PARENT_CLASS_NAME"
            )
    };
}

#endif
