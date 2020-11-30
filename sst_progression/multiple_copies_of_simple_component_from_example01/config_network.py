# Execute from the command line with the command:
#   sst ExampleConfig.py 2>&1 | tee test.log
#
import sst

# Initialize local variables.
#
clockTicks = "2"   # Number of clock ticks before the simulation ends
clock = "1GHz"      # Simulation clock rate
debug = "2"         # debug level
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

server_dict={}
server_dict["main"] = sst.Component("main server", "server.ServerComponent")
server_dict["main"].addParams({
    "x"          : 0,
    "x_length"   : 1,
    "x_length_units": "m",
    "y"          : 0,
    "y_length"   : 1,
    "y_length_units": "m",
    "z"          : 0,
    "z_length"   : 1,
    "z_length_units": "m",
    "clock"      : clock,
    "clockTicks" : clockTicks,
    "debug"      : debug
    })

wire_dict={}
wire_dict["main"] = sst.Component("wire to main", "wire.WireComponent")
wire_dict["main"].addParams({
    "x_start"    : 0,
    "y_start"    : 0,
    "z_start"    : 0,
    "x_end"      : 1,
    "y_end"      : 1,
    "z_end"      : 1,
    "clock"      : clock,
    "clockTicks" : clockTicks,
    "debug"      : debug
    })

link_index=0
sst.Link("link"+str(link_index)).connect((server_dict["main"], "port_a", link_delay),
                                         (wire_dict["main"], "port_a",  link_delay))
link_index+=1

switch = sst.Component("switch", "switch.SwitchComponent")
switch.addParams({
    "x"          : 0,
    "x_length"   : 1,
    "x_length_units": "m",
    "y"          : 0,
    "y_length"   : 1,
    "y_length_units": "m",
    "z"          : 0,
    "z_length"   : 1,
    "z_length_units": "m",
    "clock"      : clock,
    "clockTicks" : clockTicks,
    "debug"      : debug
    })

sst.Link("link"+str(link_index)).connect((wire_dict["main"], "port_b",  link_delay),
                                         (switch, "port_0", link_delay))
link_index+=1


for index in range(5):
    wire_dict[index] = sst.Component("wire to server_"+str(index), "wire.WireComponent")
    wire_dict[index].addParams({
        "x_start"    : 0,
        "y_start"    : 0,
        "z_start"    : 0,
        "x_end"      : 1,
        "y_end"      : 1,
        "z_end"      : 1,
        "clock"      : clock,
        "clockTicks" : clockTicks,
        "debug"      : debug
        })

    sst.Link("link"+str(link_index)).connect((wire_dict[index], "port_a", link_delay),
                                             (switch, "port_"+str(index+1),  link_delay))
    link_index+=1

    server_dict[index] = sst.Component("server_"+str(index), "server.ServerComponent")
    server_dict[index].addParams({
        "x"          : 0,
        "x_length"   : 1,
        "x_length_units": "m",
        "y"          : 0,
        "y_length"   : 1,
        "y_length_units": "m",
        "z"          : 0,
        "z_length"   : 1,
        "z_length_units": "m",
        "clock"      : clock,
        "clockTicks" : clockTicks,
        "debug"      : debug
    })

    sst.Link("link"+str(link_index)).connect((server_dict[index], "port_a", link_delay),
                                             (wire_dict[index], "port_b",  link_delay))
    link_index+=1


# Connect the objects to each other.
#
