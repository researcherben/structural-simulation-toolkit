Parameterize links

There is currently no way to extend the Link class.

# component-component-component

Diagrammatically,

    +-------------+   link   +-----------+   link   +-------------+
    | component A +----------+ component +----------+ component B |
    +-------------+          |   wire    |          +-------------+
                             +-----------+

This is costly computationally due to the extra component

The extra link means the minimum time is two ticks.

# parameters in subcomponents

The value of SST Subcomponents is dynamic loading at runtime. Subcomponents have unique ports and unique statistics. Parent component does not need to be aware of subcomponent's ports.  Subcomponents can be specified directly in Python or as parameters.

Diagrammatically,

    +-------------+                          +-----------------+
    | component A |                          | component B     |
    |      +------+----------+     link   +--+--------------+  |
    +------+ subcomponent A0 +------------+ subcomponent B0 +--+
           +-----------------+            +-----------------+

SST Python Driver file

    component0 = sst.Component("component0", "example.ExampleComponent")
    component0.addParams({
        "clock"      : clock,
        "clockTicks" : clockTicks,
        "debug"      : debug
        })
    subcomponent0_0 = component0.setSubComponent("slot_", "example.ExampleSubComponent", 0)
    subcomponent0_0.addParam("length_in_meters", 4.2)


# What won't work: modules

Modules don't access base class API. Statistics are not available. Ports are not available. User facing. Can be specified in Python as a parameter


# Credit for images

https://asciiflow.com/
