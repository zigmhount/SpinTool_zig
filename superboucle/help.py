import enum

# on each window, the functions
# def keyPressEvent(self, event) and
# def showContextHelp(self, wantedHelp)
# needs to be implemented. Eg in learn.py

class Context(enum.Enum):
    Help_Undefined = 0
    
    # GUI
    Help_Transport_Generic = "Help_Transport_Generic" 
    Help_Transport_Rec = "Help_Transport_Rec"
    Help_Transport_GoToPosition = "Help_Transport_GoToPosition"
    Help_Song_Volume = "Help_Song_Volume"
    Help_Song_BPM = "Help_Song_BPM"
    Help_Song_BeatPerBar = "Help_Song_BeatPerBar"
    Help_Clip_Info = "Help_Clip_Info"
    Help_Clip_BeatAmount = "Help_Clip_BeatAmount"
    Help_Clip_Offset = "Help_Clip_Offset"
    Help_Clip_OutputPort = "Help_Clip_OutputPort"
    Help_Clip_SoloGroup = "Help_Clip_SoloGroup"
    Help_Clip_OneShot = "Help_Clip_OneShot"
    Help_Clip_LockRec = "Help_Clip_LockRec"
    Help_Clip_AlwaysPlay = "Help_Clip_AlwaysPlay"
    Help_Clip_CopyDetails = "Help_Clip_CopyDetails"
    Help_Clip_PasteDetails = "Help_Clip_PasteDetails"
    Help_Clip_Revert = "Help_Clip_Revert"
    Help_Clip_Normalize = "Help_Clip_Normalize"
    
    # Add clip
    Help_Clip_Metronome = "Help_Clip_Metronome"
    
    # Add scene
    Help_Scene_Include = "Help_Scene_Include"
    
    # Cell
    Help_Cell_Info = "Help_Cell_Info"
    
    # MIDI Learn
    Help_Learn_Transport = "Help_Learn_Transport"
    Help_Learn_OtherFunctions = "Help_Learn_OtherFunctions"
    Help_Learn_OutputPortsControls = "Help_Learn_OutputPortsControls"
    Help_Learn_SongVolume = "Help_Learn_SongVolume"
    Help_Learn_StartStopButtons = "Help_Learn_StartStopButtons"
    Help_Learn_Scenes = "Help_Learn_Scenes"
    Help_Learn_Colors = "Help_Learn_Colors"
    Help_Learn_Init = "Help_Learn_Init"
    Help_Learn_Send_Controls = "Help_Learn_Send_Controls"
    
    # Mixer
    Help_Mixer_SongVolume = "Help_Mixer_SongVolume"
    Help_Mixer_MasterVolume = "Help_Mixer_MasterVolume"
    Help_Mixer_Reset = "Help_Mixer_Reset"
    Help_Mixer_Unlink = "Help_Mixer_Unlink"
    Help_Mixer_OutputPorts = "Help_Mixer_OutputPorts"
    
    # Preferences
    Help_Prefs_Environment = "Help_Prefs_Environment"
    Help_Prefs_Performance = "Help_Prefs_Performance"
    Help_Prefs_Mixer = "Help_Prefs_Mixer"
    Help_Prefs_Experimental = "Help_Prefs_Experimental"


class ManualSection(enum.Enum):
    Manual_Undefined = "Manual_Undefined"
    Manual_All = "Manual_All"

    Manual_Overview = "Manual_Overview"
    Manual_MainWindow = "Manual_MainWindow"
    Manual_SongMenu = "Manual_SongMenu"
    Manual_Scenes = "Manual_Scenes"
    Manual_Playlist = "Manual_Playlist"
    Manual_Ports = "Manual_Ports"
    Manual_SongAnnotation = "Manual_SongAnnotation"
    Manual_Mixer = "Manual_Mixer"


def getUserManual(st_manual_section):
    text = ""
    
    if st_manual_section == ManualSection.Manual_Undefined:
        return "Not available"
    
    if st_manual_section == ManualSection.Manual_Overview or st_manual_section == ManualSection.Manual_All:
        text += "OVERVIEW\n\n" + \
                "First of all, remember you can access context-help pointing at an element of the focused window and pressing " + \
                "H key.\n\n" + \
                "SpinTool is a loop based software fully controllable with any MIDI device, synced with Jack transport. "+ \
                "You can use it on live performance or for composition. SpinTool is composed of a matrix of samples controllable on screen "+ \
                "or with MIDI devices. SpinTool will send back information to the MIDI device, lighting up the buttons. Samples will always "+ \
                "be synchronized, starting and stopping on a beat or group of beats. You can adjust the duration of sample (loop period) "+ \
                "in beat and offset. But you can also adjust sample offset in raw frame count negative or positive. Which mean that the "+ \
                "sample can start before next beat (useful for reversed samples). You can also record loop of any size, adjust BPM, reverse, "+ \
                "and normalize samples.\n\n"+ \
                "Typical usage:\n"+ \
                "* You need to control jack transport (play, pause, rewind) with MIDI devices\n"+ \
                "* You have some instruments patterns but you have no idea of song structure\n"+ \
                "* You make live performances with pre-recorded instruments (you have no bass player for example) and you don’t want to have "+ \
                "a predefined structure for the song (e.g. part 2 will be longer on some live performance...)\n"+ \
                "* You want to perform all the arrangements on-the-fly on stage\n\n"+ \
                "At now, to keep some compatibility with SuperBoucle, SpinTools keeps using all SuperBoucle standards and file structures, "+ \
                "e.g. song files extensions still is .sbs, midi controller script extensions is .sbm, etc\n\n"

    if st_manual_section == ManualSection.Manual_MainWindow or st_manual_section == ManualSection.Manual_All:
        text += "MAIN WINDOW\n\n"+ \
                "Add clip: To open the “Add Clip Dialog”, left click on an empty clip. Ctrl+left click will open the file search dialog straight "+ \
                "away. You can also add clips via Drag’n’Drop (just drop your loops in the wanted clips).\n"+ \
                "New clips are by default created with the same beat amount of the song.\n\n"+ \
                "Colors: By default, these are the colors of the clips (on screen and on controller buttons both)\n"+ \
                "CLIP IS RED: Clip is not playing. RED BLINKING: Clip is playing and is triggered to stop.\n"+ \
                "CLIP IS GREEN: Clip is playing. GREEN BLINKING: Clip is stopped and is triggered to play.\n"+ \
                "CLIP IS AMBER: Clip is recording. AMBER BLINKING: Clip is triggered to record.\n"+ \
                "From Preference windows anyway you could switch to another setting, which has AMBER for clips not playing and RED for recording "+ \
                "clips (as you see in these images).\n\n"

    if st_manual_section == ManualSection.Manual_SongMenu or st_manual_section == ManualSection.Manual_All:
        text += "SONG MENU\n\n"+ \
                "In Song menu you can find some functions to process many clips at the same time.\n\n"+ \
                "Export all samples: This function allows you to export (and normalize before exporting, if required) all samples contained "+ \
                "in the clips of the song. You can select the export directory and define a prefix for column and row, which will be the "+ \
                "prefix of the sample file name.\n\n"+ \
                "Edit all selected clips: To access the Selected clips editor, you have to select some clips (SHIFT + left click on clip). "+ \
                "For all the parameters, it is possible to get the value from current clip details, using the 'copy from current clip' button. "+ \
                "It is possible to check 'Unselect clips after processing', which is the same as using the same command from the Song menu\n\n"+ \
                "Edit clips by output group: This function allows you to change Volume and Mute group parameters for all the clips which have "+ \
                "a specified Output port.\n\n"+ \
                "Edit clips by mute group: This function allows you to change Volume and Output port parameters for all the clips which have "+ \
                "a specified Mute group.\n\n"+ \
                "Unselect all clips: To cancel current clips selection.\n\n"+ \
                "Stop all clips: To massively stop all clips in the grid\n\n"+ \
                "Auto-assign Output port And/Or Solo Group to all clips: To automatically assign 'by columns' ports and solo groups (you may " + \
                "want a clips column to represent an 'instrument' in your song)\n\n"


    if st_manual_section == ManualSection.Manual_Scenes or st_manual_section == ManualSection.Manual_All:
        text += "SCENES\n\n"+ \
                "Here you can create specific scenes and arrangements for the song.\n"+ \
                "* Double left click on a scene with the mouse to trigger it.\n"+ \
                "* Select a scene with the arrow keys and trigger it with enter.\n"+ \
                "* Trigger scene from MIDI controller and use SHIFT button too to shift scenes selection and have access to more scenes.\n"+ \
                "You can also change the order of the scenes (select and drag them with the mouse).\n\n"+ \
                "SET INITIAL SCENE: This will mark the selected scene as Initial Scene (red) which is started first while loading a (new) song.\n\n"+ \
                "Selecting 'Use custom fonts' option, scenes names will be resized using custom fonts (useful on stage if you are far from PC)\n\n"


    if st_manual_section == ManualSection.Manual_Playlist or st_manual_section == ManualSection.Manual_All:
        text += "PLAYLIST\n\n"+ \
                "Here you can create your complete performance set and load the songs really easily:\n"+ \
                "* Double left click on a song with the mouse\n"+ \
                "* Select a song with the arrow keys and load it with enter\n"+ \
                "You can also change the order of the songs (select and drag them with the mouse)\n\n"+ \
                "Starting SpinTool with a playlist file path as argument will automatically import the playlist "+ \
                "and first song will be loaded\n"+ \
                "(e.g. python3 superboucle/spin.py ""/home/my_playlist.sbp"")\n\n"+ \
                "Starting SpinTool with a song file path as argument will automatically load the song\n"+ \
                "(e.g. python3 superboucle/spin.py ""/home/my_song.sbp"")\n\n"+ \
                "Selecting 'Use custom fonts' option, songs names will be resized using custom fonts (useful on stage if you are far from PC)\n\n"

    if st_manual_section == ManualSection.Manual_Ports or st_manual_section == ManualSection.Manual_All:
        text += "OUTPUT PORTS\n\n" +\
                "Here you can create and remove the dedicated audio outputs.\n" +\
                "A port list can be exported and imported. Output ports will be managed by mixer as mixer stripes.\n" +\
                "All ports are stereo (L+R)\n\n"

    if st_manual_section == ManualSection.Manual_SongAnnotation or st_manual_section == ManualSection.Manual_All:
        text += "SONG ANNOTATION\n\n" +\
                "If you need to write some details about your song, you can use Song annotation.\n" +\
                "Think about it as post-it where you can write some notes and avoid to keep them by heart or to use some external notepads. " +\
                "E.g: you need to know which synth preset on stage you will play on this song. Or you still have to finish the song and you want " +\
                "to write some ideas on arrangement.\n\n"

    if st_manual_section == ManualSection.Manual_Mixer or st_manual_section == ManualSection.Manual_All:
        text += "MIXER\n\n" + \
                "From Mixer window you can manage the volume level of your song, of Master channels, and all stripes controls (volume, gain, " + \
                "Send1, Send2, Mute, and Routing to Master)\n" + \
                "Volume, Send1, Send2 and Mute have a binding to MIDI device, to manage them during performance from your MIDI controller. Use Gain to adjust " + \
                "the overall level of an Output port, and Send1/Send2 to adjust the level of the Output port audio in the dedicated Send1 and " + \
                "Send2 outputs.\n" + \
                "In Preferences window, in Mixer section you can decide which Mixer values will be preserved (and restored) when leaving SpinTool\n\n" + \
                "Use the Unlink button to temporary disable the binding from SpinTool mixer stripes and your MIDI controller (this is useful if you " + \
                "need to do some adjustments/calibration of your controller knobs or sliders without affecting your performance/song volume values or after a custom reset.)" + \
                "Use Advanced Mixer (ADV) to show routing-to-master option. All checked stripes will route the signal of the output port to the master port."
    
    return text

def getContextHelp(st_context):
    text = ""

    if st_context == Context.Help_Undefined:
        return "Not available"
    
    # GUI
    
    elif st_context == Context.Help_Transport_Generic: #DONE
        text = "JACK TRANSPORT\n\n" + \
                "Rewind, Play, Stop (& rewind), Pause, Record, Go to position\n" + \
                "Check Rec & Go to position help for more info"
               
    elif st_context == Context.Help_Transport_Rec: #DONE
        text = "RECORD\n\n" + \
               "The command sets SpinTool in 'ready to rec' mode: " + \
               "triggering an exhisting clip will make the recording start. " + \
               "So, to record a clip, press Record transport button on screen or Record button on MIDI controller, " + \
               "then trigger an exhisting clip on the grid (clicking on it or from MIDI controller). " + \
               "Recording duration depends on clip size (beat amount) and audio source depends on what's connected to SpinTool main input ports"
                          
    elif st_context == Context.Help_Transport_GoToPosition: #DONE
        text = "GO TO POSITION\n\n" + \
                "Select the song position (= bar) you want to reach while clicking the Go To Position Button. "+ \
                "This is useful when running SpinTool together with other applications: it makes Jack transport to jump to the N-th bar of the song. "+ \
                "So, if you are running e.g. Hydrogen together with SpinTool, and you set it to 10, GO TO makes playing together SpinTool at beat 1 "+ \
                "of its cycle, and Hydrogen at beat 1 of bar 10 of the song..."
        
    elif st_context == Context.Help_Song_Volume: #DONE
        text = "SONG VOLUME\n\n" + \
                "Song volume is a property of each song, it will be saved and restored along all the other song properties, " + \
                "while Master Volume is common to all songs (= the overall SpinTool volume)"
        
    elif st_context == Context.Help_Song_BPM: #DONE
        text = "BPM\n\n" + \
                "Beat per Minutes (the timing of the song).  Set up the BPM of the Song (depending of the BPM of the loops). " + \
                "Ideally, use loops with the same BPM amount"
                  
    elif st_context == Context.Help_Song_BeatPerBar: #DONE
        text = "BEAT PER BAR\n\n" + \
                "Set up how many beats are in one bar of the song"
    
    elif st_context == Context.Help_Clip_Info: #DONE
        text = "CLIP INFO\n\n" + \
                "Select which clip information you want to see on each clip in the grid (volume, file name, output port, etc.)"
                
    elif st_context == Context.Help_Clip_BeatAmount: #DONE
        text = "BEAT AMOUNT\n\n" + \
                "How many beats are in your clip? If you are not sure have a look to the black INFO BOX"
        
    elif st_context == Context.Help_Clip_Offset: #DONE
        text = "CLIP OFFSET\n\n" + \
                "You can give a sample offset or a beat offset to your loop (move it forward or backward in the time). " + \
                "Sample offset is usually used for fine tuning, while 1.0 beat offset will offset the loop to one beat, " + \
                "0.5 to half a beat, etc."
        
    elif st_context == Context.Help_Clip_OutputPort: #DONE
        text = "OUTPUT PORT\n\n" + \
                "SpinTool has a Default stereo output, but if you need to use a dedicated output (for mixing or multiple live outs) " + \
                "then select here in which port you want to route your selected clip. You can create new ports in the Port Manager. " + \
                "All output ports are also routed to Master output by default (you can change this behaviour in advanced Mixer view)\n" + \
                "Note: 'Default', 'Click', 'Send1', 'Send2' and 'Master' are SpinTool reserved port names, so you can't create new ports " + \
                "which these names: please choose another one.\n" + \
                "All the Ports in SpinTool are stereo (L, R)"
        
    elif st_context == Context.Help_Clip_SoloGroup: #DONE
        text = "SOLO CLIP GROUP\n\n" + \
                "Assign a solo group to the clip: all clips in a Solo Group will be linked, so triggering one clip will mute the others " + \
                "in the group. (0 = No Group)"
        
    elif st_context == Context.Help_Clip_OneShot:
        text = "ONE-SHOT CLIP\n\n" + \
                "If you select one-shot, this clip will not be looped and therefore it will play once. To make it play again, start the clip " + \
                "again or launch a scene which includes this clip. Useful also for song final bar"
        
    elif st_context == Context.Help_Clip_LockRec:
        text = "LOCK REC\n\n" + \
                "Select Lock Rec if you want to prevent the clip from being used for recording (and/or overwritten). When in recording mode, " + \
                "triggering this clip will have no effect and nothing will be recorded"
        
    elif st_context == Context.Help_Clip_AlwaysPlay:
        text = "ALWAYS PLAY\n\n" + \
                "Select Always play if you want the clip always playing (when the song is playing), despite of scenes"
        
    elif st_context == Context.Help_Clip_CopyDetails:
        text = "COPY DETAILS\n\n" + \
                "To copy in memory the current clip details (all clip properties except from clip name and related audio file. So you won't copy " + \
                "the clip. You will copy its details and behaviour)"
        
    elif st_context == Context.Help_Clip_PasteDetails:
        text = "PASTE DETAILS\n\n" + \
                "To paste the details from memory into the current clip"
        
    elif st_context == Context.Help_Clip_Revert:
        text = "REVERT\n\n" + \
                "To reverse the loop audio file"
        
    elif st_context == Context.Help_Clip_Normalize:
        text = "NORMALIZE\n\n" + \
                "To normalize the loop (maximum amplitude of volume)"
    
    # Add clip
    elif st_context == Context.Help_Clip_Metronome:
        text = "METRONOME CLIP\n\n" + \
                "A Metronome (click) clip will be automatically set as Always play, an output port named Click will be created if not " + \
                "existing, and automatically assigned as Output port for this clip"
    
    # Add scene
    elif st_context == Context.Help_Scene_Include:
        text = "CLIPS IN A SCENE\n\n" + \
                "These options define which clips will be included in the scene you are creating.\n" + \
                "* Include selected clips: include in scene clips which have been selected by user (SHIFT + left click)\n" + \
                "* Include playing / starting clips: include in scene clips which are currently playing or selected to play"
                    
    # Cell
    elif st_context == Context.Help_Cell_Info: #DONE
        text = "CLIP COMMANDS\n\n" + \
                "Left click on empty clip: assign a sample to a clip\n\n" + \
                "CTRL + left click on empty clip (or drag & drop): assign a sample choosing a new file\n\n" + \
                "CTRL + left click on clip: force playing/stopping clip\n\n" + \
                "Left click: start / stop playing\n\n" + \
                "Right click: show clip details in main window clip details section\n\n" + \
                "SHIFT + left click: select the clip (for massive clips selection)"
    
    # MIDI Learn
    elif st_context == Context.Help_Learn_Transport:
        text = "TRANSPORT\n\n" + \
                "Some buttons can be associated to transport actions. In 'Transport' section, click one transport button and press the " + \
                "desired button on midi device. You will see a description of the new button"
        
    elif st_context == Context.Help_Learn_OtherFunctions:
        text = "OTHER MIDI FUNCTIONS\n\n" + \
                "In addition to transport, some buttons can be associated to other actions. If you have a Shift button available on " + \
                "controller you can assign it here, to access more MIDI functions (e.g. to access more scenes or force clip playing/stopping). " + \
                "An Unlink mixer stripes " + \
                "control is available too, to temporary disable the binding from SpinTool mixer stripes and your MIDI controller " + \
                "(this is useful if you need to do some adjustments/calibration of your controller knobs or sliders without affecting " + \
                "your performance/song volume values)" + \
                "The custom reset button resets mixer controls according to the custom reset choices in Preferences "

    elif st_context == Context.Help_Learn_OutputPortsControls:
        text = "OUTPUT PORTS\n\n" + \
                "If you have knobs or sliders, and the same amount of available buttons, you can configure them to adjust volume of mixer " + \
                "stripes (= output ports) and mute/unmute them. You'll have to assign one button and one controller for each output port; " + \
                "the assigned buttons and controllers will act of stripes in the order you see them on mixer window.\n" + \
                "At first click on 'Learn volume controllers' button and move each controller (in correct order), then press 'Stop'. " + \
                "Then, press 'Learn mute buttons' and press buttons in the same order, and in the end press 'stop'."

    elif st_context == Context.Help_Learn_Send_Controls:
        text = "SENDS\n\n" + \
                "Lean the midi controllers for the mixer sends."

    elif st_context == Context.Help_Learn_SongVolume:
        text = "SONG VOLUME\n\n" + \
                "A knob or slider of your midi device can be associated to Song volume. Click on 'Song volume controller' and move " + \
                "controller on midi device. You will see a description of the new controller (channel and controller id)"
    
    elif st_context == Context.Help_Learn_StartStopButtons:
        text = "START/STOP CLIPS\n\n" + \
                "Click 'Learn first line' button and press each button of the first line on midi device from left to right. " + \
                "For all remaining rows press 'Add next line' button and press each button on device further buttons row. " + \
                "Finally, press 'stop' button. First midi event received for a particular channel and pitch will be associated " + \
                "to the clip. For example, if your device sends a Note On when key is pressed and a Note Off when key is released, " + \
                "then Note On will be used to start or stop clip and the other message will be ignored. Velocity is also used: " + \
                "if device send Note On with velocity 127 when pressed and Note On with velocity 0 when released, then only Note On " + \
                "with velocity 127 will be used to start / stop clip"
        
    elif st_context == Context.Help_Learn_Scenes:
        text = "SCENES\n\n" + \
                "Like the start/stop clips configuration, but for the scenes. Just map the midi buttons you want to use for " + \
                "each scene of the song, in the order from first to last. If your controller has a SHIFT button too, it will " + \
                "shift your scenes selection giving access to further scenes. E.g. you could configure 8 buttons for scenes " + \
                "and trigger up to 16 scenes using the SHIFT button first"

    elif st_context == Context.Help_Learn_Colors:
        text = "COLORS\n\n" + \
                "SpinTool will send information to MIDI controller to set clip/sample status. Default colors are:\n\n" + \
                "* black / no light → no clip\n" + \
                "* blink green → clip will start\n" + \
                "* green → clip is playing\n" + \
                "* blink red → clip will stop\n" + \
                "* red → clip is stopped\n" + \
                "* blink amber → clip will record\n" + \
                "* amber → clip is recording\n\n" + \
                "As you will see in Preferences it is possible to switch recording color to RED.\n\n" + \
                "In order to light button on MIDI device, SpinTool will send Note On midi message corresponding to channel and " + \
                "pitch of buttons in 'start/stop' section. Velocity of those messages is used to set color. In this part you will " + \
                "configure velocity value to correct color. When you press 'Test' button, SpinTool will light up all buttons currently " + \
                "configured. Adjust each color value to get corresponding color. For example, for green color, change value until MIDI " + \
                "device shows a green color"

    elif st_context == Context.Help_Learn_Init:
        text = "INIT COMMAND\n\n" + \
                "If you have a reset command or a particular midi command to send to your midi device, you can put those commands " + \
                "here. One command per line in decimal value separated by comma. For example, for LaunchPad S this will reset all " + \
                "buttons (176,0,0) and switch to hardware blinking mode (176,0,40)"

    # Mixer

    elif st_context == Context.Help_Mixer_SongVolume:
        text = "SONG VOLUME\n\n" + \
                "Song volume is a property of each song and it is possible to link it to a MIDI controller knob or slider. It will be " + \
                "saved and restored along all the other song properties"

    elif st_context == Context.Help_Mixer_MasterVolume:
        text = "MASTER VOLUME\n\n" + \
                "Master volume is the performance overall SpinTool volume. By default all SpinTool output ports are routed also to the " + \
                "master volumer automatically"

    elif st_context == Context.Help_Mixer_Reset:
        text = "MIXER RESET\n\n" + \
                "These buttons allow to reset to default point the controls (Gain, Send1, Send2, Volume and Mute) for each strip. " + \
                "The Custom reset button allows to reset just some controls (which you can define in Preferences)"

    elif st_context == Context.Help_Mixer_Unlink:
        text = "UNLINK MIXER STRIPES CONTROLS\n\n" + \
                "This button allows to temporary disable the binding from SpinTool mixer stripes and your MIDI controller " + \
                "(this is useful if you need to do some adjustments/calibration of your controller without affecting " + \
                "your performance/song volume values)"

    elif st_context == Context.Help_Mixer_OutputPorts:
        text = "OUTPUT PORTS\n\n" + \
                "Each mixer strip handles the volume level and other controls (Gain amount, Send1 volume amount, Send2, etc) " + \
                "of an output port (L+R). Also Default port and Click port (if present) are listed as output ports. " + \
                "On MIDI controller, first to last Mute and Volume manage the output ports listed in mixer, " + \
                "from left to right"

    return text