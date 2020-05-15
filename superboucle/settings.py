from PyQt5.QtCore import QSettings
#import superboucle.settings

def init():

    global COMPANY
    COMPANY = "MeltinPop"

    global APPLICATION
    APPLICATION = "SpinTool"

    global DEVICES
    DEVICES = "Devices"

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

    global show_clip_details_on_trigger
    show_clip_details_on_trigger = appSettings.value('show_clip_details_on_trigger','false') == 'true'

    global show_clip_details_on_volume
    show_clip_details_on_volume = appSettings.value('show_clip_details_on_volume','false') == 'true'

    global play_clip_after_record
    play_clip_after_record = appSettings.value('play_clip_after_record','false')  == 'true'

    global show_scenes_on_start
    show_scenes_on_start = appSettings.value('show_scenes_on_start','false') == 'true'

    global allow_record_empty_clip
    allow_record_empty_clip = appSettings.value('allow_record_empty_clip', 'false') == 'true'

    global show_playlist_on_start
    show_playlist_on_start = appSettings.value('show_playlist_on_start','false')  == 'true'

    global show_song_annotation_on_load
    show_song_annotation_on_load = appSettings.value('show_song_annotation_on_load','false') == 'true'

    global slower_processing
    slower_processing = appSettings.value('slower_processing','false') == 'true'

    global rec_color
    rec_color = appSettings.value('rec_color', COLOR_AMBER)

    global grid_rows
    grid_rows = int(appSettings.value('grid_rows', 8))

    global grid_columns
    grid_columns = int(appSettings.value('grid_columns', 8))

    global bigFontSize
    bigFontSize = int(appSettings.value('bigFontSize', 10))

    # and windows position

    global playlist_geometry
    playlist_geometry = appSettings.value('playlist_geometry', None)

    global scenes_geometry
    scenes_geometry = appSettings.value('scenes_geometry', None)
    
    global gui_geometry
    gui_geometry = appSettings.value('gui_geometry', None)
    
    global song_annotation_geometry
    song_annotation_geometry = appSettings.value('song_annotation_geometry', None)

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


def update():

    # APPLICATION ------------------------------------------------------------------------------------------

    appSettings = QSettings(COMPANY, APPLICATION)

    # Saving preferences
    appSettings.setValue('auto_connect_output', auto_connect_output)
    appSettings.setValue('auto_connect_input', auto_connect_input)
    appSettings.setValue('show_clip_details_on_trigger', show_clip_details_on_trigger)
    appSettings.setValue('use_big_fonts_playlist', use_big_fonts_playlist)
    appSettings.setValue('use_big_fonts_scenes', use_big_fonts_scenes)
    appSettings.setValue('allow_record_empty_clip', allow_record_empty_clip)
    appSettings.setValue('show_clip_details_on_volume', show_clip_details_on_volume)
    appSettings.setValue('play_clip_after_record', play_clip_after_record)
    appSettings.setValue('show_scenes_on_start', show_scenes_on_start)
    appSettings.setValue('show_playlist_on_start', show_playlist_on_start)
    appSettings.setValue('show_song_annotation_on_load', show_song_annotation_on_load)
    appSettings.setValue('slower_processing', slower_processing)
    appSettings.setValue('rec_color', rec_color)
    appSettings.setValue('grid_rows', str(grid_rows))
    appSettings.setValue('grid_columns', str(grid_columns))
    appSettings.setValue('bigFontSize', str(bigFontSize))   

    # and windows position
    appSettings.setValue("gui_geometry", gui_geometry)
    appSettings.setValue("scenes_geometry", scenes_geometry)
    appSettings.setValue("playlist_geometry", playlist_geometry)
    appSettings.setValue("song_annotation_geometry", song_annotation_geometry)

    # session
    appSettings.setValue('paths_used', paths_used)
    appSettings.value('playlist',  playlist)

    appSettings.sync()

    # DEVICE ---------------------------------------------------------------------------------------------

    devSettings = QSettings(COMPANY, DEVICES)

    devSettings.setValue('devices', devices)

    devSettings.sync()