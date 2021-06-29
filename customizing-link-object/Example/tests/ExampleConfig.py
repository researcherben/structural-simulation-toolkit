# Execute from the command line with the command:
#   sst exampleConfig.py 2>&1 | tee test.log
#
import sst

# Create the python Connection class to connect the components.
#
class Connection:
    def __init__(self, subcomponent):
        self._subcomponent = subcomponent
    
    def connect(self, component0, component1, delay):
        '''
        Connects two components through a link.
        Each component is describged by a tuple
        [0] - component object
        [1] - name of the slot array into which the connection subcomponent is to be inserted
        [2] - slot array index into which the connection subcomponent is to be inserted
        Example:  (component0, "slot_", 0) indicates to insert the connection subcomponent at index 0
        of the "slot_" vector contained in component 0.
        '''
        self._connection0 = component0[0].setSubComponent(component0[1], self._subcomponent, component0[2])
        self._connection1 = component1[0].setSubComponent(component1[1], self._subcomponent, component1[2])
        self._link = sst.Link("link0")
        self._link.connect((self._connection0, "link_", delay), (self._connection1, "link_", delay))


# Initialize local variables.
#
clock = "1GHz"

# Define the component.
#
# The parameters are a dictionary and can be any key/value pair defined
# by the component itself.
#
# The second parameter is <library>.<registered_name> specified in
# SST_ELI_REGISTER_COMPONENT.
#
component0 = sst.Component("component0", "example.ExampleComponent")
component0.addParams({
    "clock"      : clock,
    })

component1 = sst.Component("component1", "example.ExampleComponent")
component1.addParams({
    "clock"      : clock,
})

connection = Connection("example.EvenOddConnection")   # Defines the subcomponent representing the connection.
connection.connect((component0, "slot_", 0), (component1, "slot_", 0), "5ns")
