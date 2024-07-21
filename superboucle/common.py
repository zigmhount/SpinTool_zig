# Vars and functions common to all application

import math
import datetime
import json

def init():

    # Application

    global APP_VERSION
    APP_VERSION = "v 20.10.04"
    global WIKI_LINK
    WIKI_LINK = "https://github.com/manucontrovento/SpinTool/wiki"

    # File exensions

    global SONG_FILE_TYPE
    SONG_FILE_TYPE = 'SpinTool Song (*.sbs)'

    global SONG_FILE_EXT 
    SONG_FILE_EXT = 'sbs'

    global PLAYLIST_FILE_TYPE 
    PLAYLIST_FILE_TYPE = 'SpinTool Playlist (*.sbp)'

    global PLAYLIST_FILE_EXT 
    PLAYLIST_FILE_EXT = 'sbp'    

    global PORTLIST_FILE_TYPE
    PORTLIST_FILE_TYPE = 'SpinTool Portlist (*.sbl)'

    global DEVICE_MAPPING_TYPE 
    DEVICE_MAPPING_TYPE = 'SpinTool Mapping (*.sbm)'

    global DEVICE_MAPPING_EXT 
    DEVICE_MAPPING_EXT = 'sbm'

    global ALL_FILE_TYPE
    ALL_FILE_TYPE = 'All files (*.*)'

    # Massive clip edit mode

    global CLIPS_EDIT_MODE_ALL_SELECTED
    CLIPS_EDIT_MODE_ALL_SELECTED = 1
    
    global CLIPS_EDIT_MODE_BY_OUTPUT_PORT 
    CLIPS_EDIT_MODE_BY_OUTPUT_PORT = 2

    global CLIPS_EDIT_MODE_BY_MUTE_GROUP 
    CLIPS_EDIT_MODE_BY_MUTE_GROUP = 3

    # Volume change mode

    global SET_VOLUME
    SET_VOLUME = 1

    global INCREASE_VOLUME
    INCREASE_VOLUME = 2

    global DECREASE_VOLUME
    DECREASE_VOLUME = 3  

    # PORTS management

    global LEFT_CHANNEL
    LEFT_CHANNEL = "_L"

    global RIGHT_CHANNEL
    RIGHT_CHANNEL = "_R"

    global MASTER_PORT
    MASTER_PORT = "Master"

    global MASTER_PORT_CHANNELS
    MASTER_PORT_CHANNELS = [MASTER_PORT + LEFT_CHANNEL, MASTER_PORT + RIGHT_CHANNEL]

    global CLICK_PORT
    CLICK_PORT = "Click"

    global CLICK_PORT_CHANNELS
    CLICK_PORT_CHANNELS = [CLICK_PORT + LEFT_CHANNEL, CLICK_PORT + RIGHT_CHANNEL]

    global SEND1_PORT
    SEND1_PORT = "Send1"

    global SEND1_PORT_CHANNELS
    SEND1_PORT_CHANNELS = [SEND1_PORT + LEFT_CHANNEL, SEND1_PORT + RIGHT_CHANNEL]

    global SEND2_PORT
    SEND2_PORT = "Send2"

    global SEND2_PORT_CHANNELS
    SEND2_PORT_CHANNELS = [SEND2_PORT + LEFT_CHANNEL, SEND2_PORT + RIGHT_CHANNEL]
    
    global DEFAULT_PORT
    DEFAULT_PORT = "Default"

    global DEFAULT_PORT_CHANNELS
    DEFAULT_PORT_CHANNELS = [DEFAULT_PORT + LEFT_CHANNEL, DEFAULT_PORT + RIGHT_CHANNEL]

    # Dict elements definitions:
    
    global PORT_VOLUME_DEF
    PORT_VOLUME_DEF = "vol"
    
    global PORT_MUTE_DEF
    PORT_MUTE_DEF = "mute"
    
    global PORT_GAIN_DEF
    PORT_GAIN_DEF = "gain"
    
    global PORT_SEND1_DEF
    PORT_SEND1_DEF = "send1"
    
    global PORT_SEND2_DEF
    PORT_SEND2_DEF = "send2"
    
    global PORT_TO_MASTER_DEF
    PORT_TO_MASTER_DEF = "to_master"

    # default mixer dict
    global DEFAULT_MIXER_DICT
    DEFAULT_MIXER_DICT = {PORT_VOLUME_DEF:1, PORT_MUTE_DEF:False, PORT_GAIN_DEF:0.5, PORT_SEND1_DEF:0, PORT_SEND2_DEF:0, PORT_TO_MASTER_DEF: True}

    # this dict contains current channels values {'port_L':value, 'port_R':value, etc}
    global CurrentChannelsValues
    CurrentChannelsValues = {}


    # JACK transport management
    global previous_beat
    previous_beat = 0


    # Clipping
    global clipping
    clipping = False

    global is_clipping
    is_clipping = False



    # mixer mode
    global mixer_mode
    mixer_mode = False

    # last scene triggered by scene manager

    global last_gui_triggered_scene
    last_gui_triggered_scene = None


# RESET MIXER VALUES ----------------------------------------------------------------------------

def resetGain(output_ports):
    for i in output_ports:
        output_ports[i][PORT_GAIN_DEF] = 0.5

def resetSend1(output_ports):
    for i in output_ports:
        output_ports[i][PORT_SEND1_DEF] = 0

def resetSend2(output_ports):
    for i in output_ports:
        output_ports[i][PORT_SEND2_DEF] = 0

def resetVolume(output_ports):
    for i in output_ports:
        output_ports[i][PORT_VOLUME_DEF] = 1

def resetMute(output_ports):
    for i in output_ports:
        output_ports[i][PORT_MUTE_DEF] = False

# DICT UTILS ------------------------------------------------------------------------------------

def renameDictItem(old_dict, old_name, new_name):
    new_dict = {}
    for key,value in zip(old_dict.keys(),old_dict.values()):
        new_key = key if key != old_name else new_name
        new_dict[new_key] = old_dict[key]
    return new_dict

# VOLUME values conversion functions ------------------------------------------------------------

def toDigitalVolumeValue(analogValue):
    return round(analogValue * 100)

def toStoredSongVolumeValue(displayValue):
    return displayValue / 100

def toAnalogClipVolumeValue(digitalValue):
    return digitalValue / 100

def toAnalogVolumeValue(controllerValue):
    return controllerValue / 256

def toControllerVolumeValue(analogValue):
    return int(analogValue * 256)

def fromControllerAnalogVolume(controllerValue):
    return controllerValue / 127

# PORTS management ---------------------------------------------------------------------------

# it provides a newly initialized output port dictionary (so, with just one default output)
def getDefaultOutputPorts():
    ports = {DEFAULT_PORT: DEFAULT_MIXER_DICT}
    return ports

# it accepts a dictionary of SpinTool ports (st_ports, which has some performance info too) and
# it provides a port list, for ports management (e.g. if required from Jack client)
def toPortsList(st_ports, sorted = True):
    ports_list = []

    for st_port in st_ports.keys():
        ports_list.append(st_port)        

    if sorted == True:
        ports_list.sort() 
        
    return ports_list

# it accepts a dictionary of SpinTool ports (st_ports, which has some performance info too) and
# it provides a port set, for ports file saving
def toPortsSet(st_ports):
    ports_set = set()

    for st_port in st_ports.keys():
        ports_set.add(st_port)        
        
    return ports_set


# it accepts a list/set of SpinTool ports (st_ports_list) and it provides a ports dictionary, 
def toPortsDict(st_ports_list):
    ports_dict = {}

    for st_port in st_ports_list:
        ports_dict[st_port] = DEFAULT_MIXER_DICT
        
    return ports_dict

def getOutputPortByIndex(st_ports, index):
    cycleIndex = 0
    for port in st_ports:
        if index == cycleIndex:
            return port
        cycleIndex = cycleIndex + 1
    
    return None

def getJackPortName_L(st_port_name):
    return st_port_name + LEFT_CHANNEL

def getJackPortName_R(st_port_name):
    return st_port_name + RIGHT_CHANNEL


def isSpinToolReservedJackPort(port_name):
    if (port_name != MASTER_PORT_CHANNELS[0] and port_name != MASTER_PORT_CHANNELS[1] and 
        port_name != SEND1_PORT_CHANNELS[0] and port_name != SEND1_PORT_CHANNELS[1] and
        port_name != SEND2_PORT_CHANNELS[0] and port_name != SEND2_PORT_CHANNELS[1]):

        return False
    
    else:
        return True


def isSpinToolReservedPort(port_name):
    if (port_name != MASTER_PORT and
        port_name != SEND1_PORT and
        port_name != SEND2_PORT):

        return False
    
    else:
        return True

def checkClickPort(st_output_ports):
    if CLICK_PORT in st_output_ports.keys():
        print("Click port already exists")
        return True
    else:
        return False

# Unregistering ALL output ports in Jack client and registering current ports
def _createJackOutputPorts(jack_client, st_output_ports):

    ports_to_remove = []

    # clearing all output jack ports:
    for jack_port in jack_client.outports:
        
        #... except from Master - sends outs:
        if isSpinToolReservedJackPort(jack_port.shortname) == False:
            
            ports_to_remove.append(jack_port)   # I really don't know why I have to do like this!
 
    for jack_port in ports_to_remove:
            
            jack_port.unregister()              # I really don't know why I have to do like this!

    # registering output ports:
    for st_port in sorted(st_output_ports.keys()):
        
        #... except from Master - sends outs:
        if isSpinToolReservedPort(st_port) == False:

            jack_client.outports.register(getJackPortName_L(st_port))

            jack_client.outports.register(getJackPortName_R(st_port))


# Original method: compares current jack ports with a dict of ports, removes unused ports, 
# adds new ports, keeps existing common ports
def _updateJackOutputPorts(jack_client, new_st_output_ports):

    new_ports = toPortsList(new_st_output_ports)

    current_jack_ports = set()
    for port in jack_client.outports:
        current_jack_ports.add(port.shortname)

    wanted_ports = set()
    for port in new_ports:
        wanted_ports.add(getJackPortName_L(port))
        wanted_ports.add(getJackPortName_R(port))

    # remove unwanted ports
    port_to_remove = []
    for port in jack_client.outports:
        if port.shortname not in wanted_ports:
            current_jack_ports.remove(port.shortname)
            port_to_remove.append(port)
    for port in port_to_remove:
        port.unregister()

    # sort port list
    activate_ports = sorted(list(wanted_ports - current_jack_ports))

    # create new ports
    for new_port_name in activate_ports:
        jack_client.outports.register(new_port_name)

def _addJackOutputPort(jack_client, st_output_port_name):
    
        jack_client.outports.register(getJackPortName_L(st_output_port_name))
        jack_client.outports.register(getJackPortName_R(st_output_port_name))


def _removeJackOutputPort(jack_client, st_output_port_name):

        jack_port_L = getJackPortName_L(st_output_port_name)
        jack_port_R = getJackPortName_R(st_output_port_name)

        ports_to_remove = []

        for jack_port in jack_client.outports:
            if jack_port.shortname == jack_port_L or jack_port.shortname == jack_port_R:
                ports_to_remove.append(jack_port)   # I really don't know why I have to do like this!

        for jack_port in ports_to_remove:
                jack_port.unregister()              # I really don't know why I have to do like this!


def addOutputPort(st_ports, port_name, jack_client = None, mixer_window = None):

    st_ports[port_name] = DEFAULT_MIXER_DICT
    
    if jack_client:
        _addJackOutputPort(jack_client, port_name)

    if mixer_window:
        mixer_window.updateGui(st_ports)


def removeOutputPort(st_ports, port_name, jack_client = None, mixer_window = None):
    
    del st_ports[port_name]

    if jack_client:
        _removeJackOutputPort(jack_client, port_name)

    if mixer_window:
        mixer_window.updateGui(st_ports)


def createOutputPorts(st_ports, jack_client = None, mixer_window = None):

    if jack_client:
        _createJackOutputPorts(jack_client, st_ports)

    if mixer_window:
        mixer_window.updateGui(st_ports)

def updateOutputPorts(st_ports, jack_client = None, mixer_window = None):
    
    if jack_client:
        _updateJackOutputPorts(jack_client, st_ports)

    if mixer_window:
        mixer_window.updateGui(st_ports)


# Playlist and songs management --------------------------------------------------------------------

# updates settings.playlist with a playlist from file
def updateSettingsPlaylist(file_name, settings):
    with open(file_name, 'r') as f:
        read_data = f.read()
    
    settings.playlist = json.loads(read_data)



# Graphics -----------------------------------------------------------------------------

def clearLayout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget() is not None:
            child.widget().deleteLater()
        elif child.layout() is not None:
            clearLayout(child.layout())