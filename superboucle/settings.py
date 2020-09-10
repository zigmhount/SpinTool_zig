from PyQt5.QtCore import QSettings

def init():

    global COMPANY
    COMPANY = "MeltinPop"

    # SECTIONS ------------------------------- 

    global APPLICATION
    APPLICATION = "SpinTool"

    global DEVICES
    DEVICES = "Devices"

    global PORTS
    PORTS = "Ports"

    # Enums ----------------------------------

    global COLOR_RED
    COLOR_RED = "RED"

    global COLOR_AMBER
    COLOR_AMBER = "AMBER"


    # APPLICATION ------------------------------------------------------------------------------------------

    appSettings = QSettings(COMPANY, APPLICATION)

    # Load preferences

    global use_big_fonts_playlist
    use_big_fonts_playlist = appSettings.value('use_big_fonts_playlist', 'false')  == 'true' 

    global use_big_fonts_scenes
    use_big_fonts_scenes = appSettings.value('use_big_fonts_scenes', 'false') == 'true'

    global auto_connect_output
    auto_connect_output = appSettings.value('auto_connect_output','true') == 'true'

    global auto_connect_input
    auto_connect_input = appSettings.value('auto_connect_input','true') == 'true'

    # save mixer settings
    global save_mixerstrip_gain
    save_mixerstrip_gain = appSettings.value('save_mixerstrip_gain', 'false') == 'true'

    global save_mixerstrip_send1
    save_mixerstrip_send1 = appSettings.value('save_mixerstrip_send1', 'false') == 'true'
    
    global save_mixerstrip_send2
    save_mixerstrip_send2 = appSettings.value('save_mixerstrip_send2', 'false') == 'true'

    global save_mixerstrip_volume
    save_mixerstrip_volume = appSettings.value('save_mixerstrip_volume', 'false') == 'true'

    global save_mixerstrip_mute
    save_mixerstrip_mute = appSettings.value('save_mixerstrip_mute', 'false') == 'true'

    global save_mixerstrip_to_master
    save_mixerstrip_to_master = appSettings.value('save_mixerstrip_to_master', 'false') == 'true'


    # reset all
    global customreset_mixerstrip_gain
    customreset_mixerstrip_gain = appSettings.value('customreset_mixerstrip_gain', 'false') == 'true'

    global customreset_mixerstrip_send1
    customreset_mixerstrip_send1 = appSettings.value('customreset_mixerstrip_send1', 'false') == 'true'

    global customreset_mixerstrip_send2
    customreset_mixerstrip_send2 = appSettings.value('customreset_mixerstrip_send2', 'false') == 'true'

    global customreset_mixerstrip_volume
    customreset_mixerstrip_volume = appSettings.value('customreset_mixerstrip_volume', 'false') == 'true'

    global customreset_mixerstrip_mute
    customreset_mixerstrip_mute = appSettings.value('customreset_mixerstrip_mute', 'false') == 'true'


    # Performance
    global disable_shift_after_processing
    disable_shift_after_processing = appSettings.value('disable_shift_after_processing','true') == 'true'

    global show_clip_details_on_trigger
    show_clip_details_on_trigger = appSettings.value('show_clip_details_on_trigger','false') == 'true'

    global play_clip_after_record
    play_clip_after_record = appSettings.value('play_clip_after_record','false')  == 'true'

    global show_scenes_on_start
    show_scenes_on_start = appSettings.value('show_scenes_on_start','false') == 'true'

    global allow_record_empty_clip
    allow_record_empty_clip = appSettings.value('allow_record_empty_clip', 'false') == 'true'

    global auto_assign_new_clip_column
    auto_assign_new_clip_column = appSettings.value('auto_assign_new_clip_column', 'false') == 'true'

    global show_playlist_on_start
    show_playlist_on_start = appSettings.value('show_playlist_on_start','false')  == 'true'

    global show_song_annotation_on_load
    show_song_annotation_on_load = appSettings.value('show_song_annotation_on_load','false') == 'true'

    global slower_processing
    slower_processing = appSettings.value('slower_processing','false') == 'true'

    global system_monitoring
    system_monitoring = appSettings.value('system_monitoring','false') == 'true'

    global rec_color
    rec_color = appSettings.value('rec_color', COLOR_AMBER)

    global grid_rows
    grid_rows = int(appSettings.value('grid_rows', 8))

    global grid_columns
    grid_columns = int(appSettings.value('grid_columns', 8))

    global new_song_master_volume
    new_song_master_volume = int(appSettings.value('new_song_master_volume', 50))

    global new_song_bpm
    new_song_bpm = int(appSettings.value('new_song_bpm', 120))

    global new_song_beats
    new_song_beats = int(appSettings.value('new_song_beats', 4))     

    global bigFontSize
    bigFontSize = int(appSettings.value('bigFontSize', 14))

    global prevent_song_save
    prevent_song_save = appSettings.value('prevent_song_save','false')  == 'true'


    # and windows positions

    global playlist_geometry
    playlist_geometry = appSettings.value('playlist_geometry', None)

    global scenes_geometry
    scenes_geometry = appSettings.value('scenes_geometry', None)
    
    global gui_geometry
    gui_geometry = appSettings.value('gui_geometry', None)
    
    global song_annotation_geometry
    song_annotation_geometry = appSettings.value('song_annotation_geometry', None)

    global mixer_geometry
    mixer_geometry = appSettings.value('mixer_geometry', None)


    # session

    global paths_used
    paths_used = appSettings.value('paths_used', {})

    global playlist
    playlist = appSettings.value('playlist', []) or []


    # DEVICE ---------------------------------------------------------------------------------------------

    devSettings = QSettings(COMPANY, DEVICES)

    global devices
    devices = devSettings.value('devices', None)

    global hasDevices
    hasDevices = devSettings.contains('devices')


    # PORTS AND MIXER VALUES ------------------------------------------------------------------------------

    portSettings = QSettings(COMPANY, PORTS)

    # A dict maintaining the output ports. Every item of the list is a dict
    # which defines elements like: name:{"vol", "mute", "gain"}
    # e.g. output_ports = {"vol":1, "mute":False, "gain":0.5, "send1":0, "send2":0}
    # the default dict can be found in common.py
    global output_ports
    output_ports = portSettings.value('output_ports', None)

    # master port final volume
    global master_port_final_volume
    master_port_final_volume = float(portSettings.value('master_port_final_volume', 1))

    # master port mute
    global master_port_mute
    master_port_mute = portSettings.value('master_port_mute', 'false') == 'true'




def update():

    # APPLICATION ------------------------------------------------------------------------------------------

    appSettings = QSettings(COMPANY, APPLICATION)

    # Saving preferences
    appSettings.setValue('auto_connect_output', auto_connect_output)
    appSettings.setValue('auto_connect_input', auto_connect_input)

    # save mixer settings
    appSettings.setValue('save_mixerstrip_gain', save_mixerstrip_gain)
    appSettings.setValue('save_mixerstrip_send1', save_mixerstrip_send1)
    appSettings.setValue('save_mixerstrip_send2', save_mixerstrip_send2)
    appSettings.setValue('save_mixerstrip_volume', save_mixerstrip_volume)
    appSettings.setValue('save_mixerstrip_mute', save_mixerstrip_mute)
    appSettings.setValue('save_mixerstrip_to_master', save_mixerstrip_to_master)

    # customreset
    appSettings.setValue('customreset_mixerstrip_gain', customreset_mixerstrip_gain)
    appSettings.setValue('customreset_mixerstrip_send1', customreset_mixerstrip_send1)
    appSettings.setValue('customreset_mixerstrip_send2', customreset_mixerstrip_send2)  
    appSettings.setValue('customreset_mixerstrip_volume', customreset_mixerstrip_volume)
    appSettings.setValue('customreset_mixerstrip_mute', customreset_mixerstrip_mute)

    # Performance
    appSettings.setValue('disable_shift_after_processing', disable_shift_after_processing)
    appSettings.setValue('show_clip_details_on_trigger', show_clip_details_on_trigger)
    appSettings.setValue('use_big_fonts_playlist', use_big_fonts_playlist)
    appSettings.setValue('use_big_fonts_scenes', use_big_fonts_scenes)
    appSettings.setValue('allow_record_empty_clip', allow_record_empty_clip)
    appSettings.setValue('auto_assign_new_clip_column', auto_assign_new_clip_column)
    appSettings.setValue('play_clip_after_record', play_clip_after_record)
    appSettings.setValue('show_scenes_on_start', show_scenes_on_start)
    appSettings.setValue('show_playlist_on_start', show_playlist_on_start)
    appSettings.setValue('show_song_annotation_on_load', show_song_annotation_on_load)
    appSettings.setValue('slower_processing', slower_processing)
    appSettings.setValue('system_monitoring', system_monitoring)
    appSettings.setValue('rec_color', rec_color)
    appSettings.setValue('grid_rows', str(grid_rows))
    appSettings.setValue('grid_columns', str(grid_columns))
    appSettings.setValue('bigFontSize', str(bigFontSize))
    appSettings.setValue('new_song_master_volume', str(new_song_master_volume))
    appSettings.setValue('new_song_bpm', str(new_song_bpm))
    appSettings.setValue('new_song_beats', str(new_song_beats))
    appSettings.setValue('prevent_song_save', prevent_song_save)

    # and windows position and geometry
    appSettings.setValue("gui_geometry", gui_geometry)
    appSettings.setValue("scenes_geometry", scenes_geometry)
    appSettings.setValue("playlist_geometry", playlist_geometry)
    appSettings.setValue("song_annotation_geometry", song_annotation_geometry)
    appSettings.setValue("mixer_geometry", mixer_geometry)

    # session
    appSettings.setValue('paths_used', paths_used)
    appSettings.value('playlist',  playlist)

    appSettings.sync()

    # DEVICE ---------------------------------------------------------------------------------------------

    devSettings = QSettings(COMPANY, DEVICES)

    devSettings.setValue('devices', devices)

    devSettings.sync()

    # PORTS ---------------------------------------------------------------------------------------------

    portSettings = QSettings(COMPANY, PORTS)

    portSettings.setValue('output_ports', output_ports)

    portSettings.setValue('master_port_final_volume', str(master_port_final_volume))
    portSettings.setValue('master_port_mute', master_port_mute)

    portSettings.sync()
