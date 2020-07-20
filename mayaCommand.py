import maya.cmds as cmds
import maya.mel as mel

port_id = "7777"
host_adress = "127.0.0.1:{0}".format(port_id)

proc_name="portData"

# Our mel global proc.
melproc = """
global proc {0}(string $arg){
    python(("{0}(\\"" + $arg + "\\")"));
}
""".format(proc_name)
mel.eval(melproc)

def open_port():
    # Open the commandPort. 
    # The 'prefix' argument string is calling to the defined
    # mel script above (which then calls to our Python function 
    # of the same name):
    cmds.commandPort(
        name=host_adress,
        echoOutput=False,
        noreturn=False,
        prefix=proc_name,
        returnNumCommands=True
    )
    cmds.commandPort(
        name=port_id,
        echoOutput=False,
        noreturn=False,
        prefix=proc_name,
        returnNumCommands=True
    )

# Our Python function that can be changed to do whatever we want:
def portData(arg):
    """
    Read the 'serial' data passed in from the commandPort
    """
    print "Recieved!: ", arg

    # Some silly example code to scale a sphere:
    mappedVal = (1-float(arg))*1 + float(arg)*2
    if cmds.objExists('_000_sphere'):
        cmds.setAttr('_000_sphere.scale', mappedVal, mappedVal, mappedVal)

open_port()
