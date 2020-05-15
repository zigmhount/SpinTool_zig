import math

def init():

    # Application

    global APP_VERSION
    APP_VERSION = "v 20.05.16"
    
    global WIKI_LINK
    WIKI_LINK = "https://github.com/manucontrovento/SpinTool/wiki"

    # File exensions

    global SONG_FILE_TYPE 
    SONG_FILE_TYPE = 'SpinTool Song (*.sbs)'

    global SONG_FILE_EXT 
    SONG_FILE_EXT = 'sbs'

    global PLAYLIST_FILE_TYPE 
    PLAYLIST_FILE_TYPE = 'SpinTool Playlist (*.sbp)'

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

def toDigitalVolumeValue(analogValue):
    return math.trunc(analogValue * 100)

def toAnalogClipVolumeValue(digitalValue):
    return digitalValue / 100

def toAnalogVolumeValue(controllerValue):
    return controllerValue / 256

def toControllerVolumeValue(analogValue):
    return analogValue * 256