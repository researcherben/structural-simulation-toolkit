# Execute from the command line with the command:
#   sst ExampleConfig.py 2>&1 | tee test.log
#
import sst

# Initialize local variables.
#
clockTicks = "7"   # Number of clock ticks before the simulation ends
clock = "1GHz"      # Simulation clock rate
debug = "2"         # debug level
                    # 0 = FATAL, 1 = WARN, 2 = INFO, 3 = DEBUG, 4 = TRACE, 5 = ALL

componentName0 = "example_a"
componentName1 = "example_b"

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

obj0 = sst.Component(componentName0, "twoexample.ExampleComponent")
obj0.addParams({
    "clock"      : clock,
    "clockTicks" : clockTicks,
    "debug"      : debug
    })

obj1 = sst.Component(componentName1, "twoexample.ExampleComponent")
obj1.addParams({
    "clock"      : clock,
    "clockTicks" : clockTicks,
    "debug"      : debug
})

# Connect the objects to each other.
#
link = sst.Link("link0")
link.connect((obj0, "port_a", "5ns"), (obj1, "port_a",  "5ns"))
