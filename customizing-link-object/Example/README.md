# Customizing Link Object Example

This folder contains code demonstrating how a subcomponent and link
can be used is combination to connect two SST components.


The general idea is illustrated below.
```

                       Connection
   ┌───────────────────────────────────────────────┐
   │                                               │
   │ ┌──────────────┐             ┌──────────────┐ │
   │ │              │     Link    │              │ │
   │ │ Subcomponent ├─────────────┤ Subcomponent │ │
   │ │              │             │              │ │
   │ └──────────────┘             └──────────────┘ │
   │                                               │
   └───────────────────────────────────────────────┘

    ┌───────────────┐             ┌───────────────┐
    │               │  Connection │               │
    │   Component   ├─────────────┤   Component   │
    │               │             │               │
    └───────────────┘             └───────────────┘
```
A Connection is defined as a composite consisting of two subcomponents
and a link.  The subcomponent interface contains a method for sending
a message over the connection and another to insert a callback to be
called whenever a message is received by the subcomponent.

The components to be connected each have a slot into which the 
Connection subcomponents are inserted. Communication between the 
components can be customized by code included in the subcomponent
send method.  It's done this way since there is no direct way to
inherit from an SST::Link and it was deemed desirable to not have to
modify SST in any way.

Connecting two components through subcomponents rather than links also
has the advantage that the number of connections does not have to be 
known at compile time.  A single slot in a component can contain
multiple subcomponents, whereas a link object in a component can only
contain a single link.

It is expected the Connection subcomponents will be objects of the
same class but that is not a requirement so long as they present the
same interface to the containing component.

