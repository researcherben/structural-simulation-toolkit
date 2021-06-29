#ifndef _EXAMPLE_EVENT_H
#define _EXAMPLE_EVENT_H

// Basic include files from SST
//
#include <sst/core/event.h>

namespace BuildingsAndRoads
{
    // Class must inherit from SST::Event
    //
    class ExampleEvent : public SST::Event
    {
    public:
        // Constructor
        //
        ExampleEvent() : SST::Event() {}

        // Return the payload
        // size_t is an unsigned integer data type which can assign
        // only 0 and greater than 0 integer values. It measures bytes of
        // any object's size and returned by sizeof operator.
        size_t getPayload() const { return 0; }

    private:

        // Serialization code.  Serializes data before sending it out
        // over the link.
        //
        void serialize_order(SST::Core::Serialization::serializer &ser) override
        {
            Event::serialize_order(ser);
        }
        ImplementSerializable(ExampleEvent);
    };
}

#endif
