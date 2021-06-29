// Component definition.
//
#include <iostream>
#include <functional>
#include "ExampleComponent.h"
#include "EvenOddConnection.h"
#include "ExampleEvent.h"
#include "Logger.hpp"

// Declare namespaces.
//
using namespace Example;
using namespace SSTLogger;

// Initialize the logger.
// Prefix contains Time, File, Function, Line, and Thread
// Log all messages of Info and above to STDOUT.
//
Logger logger_ = Logger("Time=@t; File=@f; Func=@p; Line=@l; Thread=@I -- ", Logger::LogLevel::Info, Logger::LogLocation::STDOUT);

// Component constructor.
//
ExampleComponent::ExampleComponent(SST::ComponentId_t id, SST::Params &params) :
    SST::Component(id),
    componentId_(id),
    clockTickCount_(0),
    clockCount_(0)
{
    // Read in the parameters from the python config file.  See SST_ELI_DOCUMENT_PARAMS
    // for an explanation of what each parameter represents.
    //
    std::string clock = 
        params.find<std::string>("clock", "1GHz");      // Clock defaults to 1GHz.
    clockTicks_ = static_cast<uint64_t>(
        params.find<int>("clockTicks", 5));             // Maximum clock ticks default to 10

    logger_.logTrace(CALL_INFO, "Entering constructor for component id %lu\n", componentId_);
 
    // Initialize the debug output instance.
    // Strings for debug output use the printf format.
    //
    logger_.logDebug(CALL_INFO, "Parameters successfully read from config file.\n");
    logger_.logDebug(CALL_INFO, "clockTicks = %lu\n", clockTicks_);
    logger_.logInfo(CALL_INFO, "Constructing new Example Instance.\n");

    // Configure the subcomponents.  The slot name is taken from where the 
    // subcomponent slot is documented in the component .h file.
    //
    connections_ = configureSubComponents(params);

    // Configure the component clock.
    //
    logger_.logDebug(CALL_INFO, "Clock rate is: %s\n", clock.c_str());
    registerClock(clock,
        new SST::Clock::Handler<ExampleComponent>(this, &ExampleComponent::clockTick));
    logger_.logInfo(CALL_INFO, "Successfully initialized clock.\n");

    // Register this component with the simulation.
    //
    registerAsPrimaryComponent();
    logger_.logDebug(CALL_INFO, "Component registered as primary component.\n");
    
    primaryComponentDoNotEndSim();
    logger_.logDebug(CALL_INFO, "Simulation notified it should not end.\n");
    logger_.logTrace(CALL_INFO, "Leaving constructor for component id %lu\n", componentId_);
}


// Called after all components have been constructed and initialization
// has completed, but before simulation time has begin.
//
// This is where you should do any other initialization that needs done
// but could be accomplished in the constructure.
//
void ExampleComponent::setup(void)
{
    logger_.logTrace(CALL_INFO, "Entering setup for component id %lu\n", componentId_);
    logger_.logTrace(CALL_INFO, "Leaving setup for component id %lu\n", componentId_);
}


// Called after the simulation is complete but before the objects are
// destroyed.  This is a good place to print out statistics.
//
void ExampleComponent::finish(void)
{
    logger_.logTrace(CALL_INFO, "Entering finish for component id %lu\n", componentId_);
    logger_.logTrace(CALL_INFO, "Leaving finish for component id %lu\n", componentId_);
}


// Clock event handler.
//
bool ExampleComponent::clockTick(SST::Cycle_t cycle)
{
    logger_.logTrace(CALL_INFO, "Entering clock for component id %lu\n", componentId_);
    bool done = false;

    // Call clockTick for each of the subcomponents.
    //
    logger_.logInfo(CALL_INFO, "Calling clock tick for subcomponents.\n");
    for ( auto connection : connections_) 
    {
        connection->clockTick(cycle);

        clockTickCount_++;
        connection->send(new ExampleEvent(clockTickCount_));
    }
    return done;
}

std::vector<EvenOddConnection*> ExampleComponent::configureSubComponents(SST::Params &params)
{
    logger_.logInfo(CALL_INFO, "Configuring subcomponents.\n");

    std::vector<EvenOddConnection*> connections {};

    SubComponentSlotInfo* info = getSubComponentSlotInfo("slot_");
    if ( !info ) 
    {
        // No defined subcomponents.  Print an error message and exit.
        //
        logger_.logFatal(CALL_INFO, "Must specify at least one SubComponent for slot.\n");
    }
    else
    {
        // Create all the defined subcomponents.
        //
        long unsigned int maxSlot = info->getMaxPopulatedSlotNumber();
        logger_.logDebug(CALL_INFO, "There are %lu subcomponent slot entries\n", maxSlot + 1);
        for (int i = 0; i <= maxSlot; i++)
        {
            // Check to see if the current slot is populated.
            //
            logger_.logDebug(CALL_INFO, "Examining subcomponent slot entry %d\n", i);
            if (!info->isPopulated(i))
            {
                logger_.logDebug(CALL_INFO, "Slot %d is not populated\n", i);
                continue;
            }

            // Create the subcomponent for this slot.
            //
            logger_.logDebug(CALL_INFO, "Loading subcomponent into slot entry %d\n", i);  
            EvenOddConnection* exSubComponent = info->create<EvenOddConnection>(i, ComponentInfo::SHARE_PORTS);
            logger_.logDebug(CALL_INFO, "Example subcomponent created.\n");

            // Define the message handler to be attached to the subcomponent.
            // The message handler is passed in as a lambda so you don't have
            // to declare it as static.
            //
            logger_.logDebug(CALL_INFO, "Create event handler.\n");
            exSubComponent->setMessageHandler([this](SST::Event* event)-> void
            { 
                logger_.logTrace(CALL_INFO, "Entering message handler.\n");

                clockCount_++;
                if (clockCount_ >= clockTicks_)
                {
                    primaryComponentOKToEndSim();
                }
                
                logger_.logTrace(CALL_INFO, "Leaving message handler.\n");
            });

            // Initialize and store the slot on the vector.
            //
            logger_.logDebug(CALL_INFO, "Initialize and store on the vector.\n");
            exSubComponent->start(i, params);
            connections.push_back(exSubComponent);

            logger_.logDebug(CALL_INFO, "Subcomponent %u initialized.\n", i);
        }
    }
    return connections;
}