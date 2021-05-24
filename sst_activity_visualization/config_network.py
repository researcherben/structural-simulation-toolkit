# Execute from the command line with the command:
#   sst ExampleConfig.py 2>&1 | tee test.log
#
import sst
import sys

if len(sys.argv)!=3:
    print("ERROR: two arguments required:")
    print("   number of clock ticks [integer]>0")
    print("   number of nodes [integer]>0")
    exit()
try:
    clockTicks = int(sys.argv[1])
except ValueError:
    print("ERROR for arg 1: number of clock ticks [integer]>0")
    exit()

try:
    number_of_nodes = int(sys.argv[2])
except ValueError:
    print("ERROR for arg 2: number of nodes [integer]>0")
    exit()

if clockTicks<1:
    print("ERROR: clockTicks less than 1 creates an infinite loop")
    exit()
if number_of_nodes<1:
    print("ERROR: invalid configuration")
    exit()

print("ticks:",clockTicks)
print("nodes:",number_of_nodes)
# Initialize local variables.
#
clockTicks = sys.argv[1]   # Number of clock ticks before the simulation ends
clock = "1GHz"      # Simulation clock rate
debug = "3"         # debug level
                    # 0 = FATAL, 1 = WARN, 2 = INFO, 3 = DEBUG, 4 = TRACE, 5 = ALL

link_delay="0ns"

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
#number_of_nodes = int(sys.argv[2])

node_dict = {}

node_dict[0] = sst.Component("node_0", "twoexample.ExampleComponent")
node_dict[0].addParams({
    "clock"      : clock,
    "clockTicks" : clockTicks,
    "debug"      : debug
})

link_index = 0
for index in range(1,number_of_nodes):

    node_dict[index] = sst.Component("node_"+str(index), "twoexample.ExampleComponent")
    node_dict[index].addParams({
        "clock"      : clock,
        "clockTicks" : clockTicks,
        "debug"      : debug
    })

    sst.Link("link"+str(link_index)).connect((node_dict[index], "port_a", link_delay),
                                             (node_dict[index-1], "port_b",  link_delay))
    link_index+=1

sst.Link("link"+str(link_index)).connect((node_dict[number_of_nodes-1], "port_b", link_delay),
                                         (node_dict[0], "port_a",  link_delay))
