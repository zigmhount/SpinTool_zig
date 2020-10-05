#!/usr/bin/env python3

print("Initialize settings")

import time
import settings
settings.init()

print("Settings initialized")

print("Initialize common")

import common
common.init()

print("Common initialized")

if settings.output_ports is None:
    print("No output ports dictionary found. Creating new dictionary with default output ports")
    settings.output_ports = common.getDefaultOutputPorts()

import superboucle.jack as jack
import sys, os.path
from superboucle.clip import Clip, Song, load_song_from_file
from superboucle.gui import Gui
from PyQt5.QtWidgets import QApplication, QStyleFactory
from queue import Empty
import argparse
from superboucle.preferences import Preferences
import soundfile as sf
import numpy as np
import math
import datetime

parser = argparse.ArgumentParser(description='launch SpinTool')
parser.add_argument("file", nargs="?", help="loads the playlist and its first song, or just a song")
args = parser.parse_args()

song = None

# on starting, a playlist can be loaded and stored in settings.playlist, as for when loading it from playlist manager,
# and first song of playlist is loaded:
if args.file:

    if os.path.isfile(args.file):
        
        ext = args.file[-3:]

        # SONG argument found:
        if ext.lower() == common.SONG_FILE_EXT:
            
            print("Loading song")
            try:
                song = load_song_from_file(args.file)
            
            except:
                sys.exit("error loading song")
        
        # PLAYLIST argument found:
        if ext.lower() == common.PLAYLIST_FILE_EXT:

            print("Loading playlist: " + args.file)
            try:
                common.updateSettingsPlaylist(args.file, settings)

                print("Loading first song")
                try:
                    song_file_name = settings.playlist[0]
                    song = load_song_from_file(song_file_name)
                
                except:
                    sys.exit("error loading first song")

            except:
                sys.exit("error loading playlist")
        
    else:
        sys.exit("File {} does not exist.".format(args.file))     


else:
    # new song (using default user preferred settings)
    song  = Song(int(settings.grid_columns), 
                 int(settings.grid_rows),
                 common.toStoredSongVolumeValue(int(settings.new_song_master_volume)),
                 int(settings.new_song_bpm),
                 int(settings.new_song_beats))

# Jack client for SpinTool:
client = jack.Client("SpinTool")

# play sound file buffersize
play_file_buffersize = 20

# creating SpinTool midi ports
midi_in = client.midi_inports.register("input")
midi_out = client.midi_outports.register("output")

# creating SpinTool audio ins
inL = client.inports.register("input_L")
inR = client.inports.register("input_R")

# creating SpinTool Master outs
masterL = client.outports.register(common.MASTER_PORT_CHANNELS[0])
masterR = client.outports.register(common.MASTER_PORT_CHANNELS[1])

# creating SpinTool Send1 outs
send1L = client.outports.register(common.SEND1_PORT_CHANNELS[0])
send1R = client.outports.register(common.SEND1_PORT_CHANNELS[1])

# creating SpinTool Send2 outs
send2L = client.outports.register(common.SEND2_PORT_CHANNELS[0])
send2R = client.outports.register(common.SEND2_PORT_CHANNELS[1])


# creating SpinTool audio out (reading ports list from settings)
common._createJackOutputPorts(client, settings.output_ports)

# application init
app = QApplication(sys.argv)
gui = Gui(song, client, app)

# option to start playing the clip just after recording:
# if settings.value('play_clip_after_record', False) == False:
if settings.play_clip_after_record == False:

    CLIP_TRANSITION = {Clip.STARTING: Clip.START,
                       Clip.STOPPING: Clip.STOP,
                       Clip.PREPARE_RECORD: Clip.RECORDING,
                       Clip.RECORDING: Clip.STOP}
else:
    
    CLIP_TRANSITION = {Clip.STARTING: Clip.START,
                       Clip.STOPPING: Clip.STOP,
                       Clip.PREPARE_RECORD: Clip.RECORDING,
                       Clip.RECORDING: Clip.START}        


def updateCurrentChannelsValues(): 
    # is it a good idea to have it in the callback? one could also update it only on mixer changes
    for port_name in settings.output_ports.keys():

        # get volume values
        vol = settings.output_ports[port_name][common.PORT_VOLUME_DEF]
        mute = (1-int(settings.output_ports[port_name][common.PORT_MUTE_DEF]))
        gain = settings.output_ports[port_name][common.PORT_GAIN_DEF]

        # calculate channels final volume
        final_volume = vol * mute * gain * 2 # -> since default gain is 0.5, then * 2 goes back to the original volume

        # get sends values
        send1 = settings.output_ports[port_name][common.PORT_SEND1_DEF]
        send2 = settings.output_ports[port_name][common.PORT_SEND2_DEF]

        #to master
        to_master = settings.output_ports[port_name][common.PORT_TO_MASTER_DEF]

        # create channel sub dict
        channel_subdict = {"final_vol": final_volume, "send1": send1, "send2": send2, 
                           "to_master": to_master}


        # assigne channel sub dict to each channel
        common.CurrentChannelsValues[common.getJackPortName_L(port_name)] = channel_subdict # continous call of getJackPortName
        common.CurrentChannelsValues[common.getJackPortName_R(port_name)] = channel_subdict

    #print(channel_subdict)


# check if signal is clipping and light up clipping label
def checkClipping(tick):
    # clip
    if common.clipping == True and common.is_clipping == False:
        # stylesheet = 'color: red;'
        # gui.clipping_label.setStyleSheet(stylesheet)
        common.is_clipping = True
        #print("clip")

    # unclip
    if common.is_clipping == True and tick < 100:
        # stylesheet = 'color: rgb(160, 6, 89);'
        # stylesheet = 'color: none;'
        # gui.clipping_label.setStyleSheet(stylesheet)
        common.clipping = False
        common.is_clipping = False
        #print("unclip")
    
    gui.updateClipping(common.is_clipping)

# MAIN AUDIO CALLBACK
def my_callback(frames):
    song = gui.song
    state, position = client.transport_query()

    # Updating channel volumes values
    updateCurrentChannelsValues()

    inL_buffer = inL.get_array()
    inR_buffer = inR.get_array()

    # output buffers (waveforms)
    ports_by_name = {port.shortname: port for port in client.outports}
    output_buffers = {k: v.get_array() for k, v in
                      ports_by_name.items()}

    for b in output_buffers.values():
        b[:] = 0

    # check midi in
    if gui.is_learn_device_mode:
        for offset, indata in midi_in.incoming_midi_events():
            gui.learn_device.queue.put(indata)
        gui.learn_device.updateUi.emit()
    else:
        for offset, indata in midi_in.incoming_midi_events():
            gui.queue_in.put(indata)
        gui.readQueueIn.emit()
    midi_out.clear_buffer()

    if ((state == 1 # == jack.ROLLING
         and 'beats_per_minute' in position
         and position['frame_rate'] != 0)):
        frame = position['frame']
        fps = position['frame_rate']
        fpm = fps * 60
        bpm = position['beats_per_minute']
        blocksize = client.blocksize

        for clip in song.clips:

            if (clip.always_play == True and clip.state != Clip.START and clip.state != Clip.STARTING): 
                clip.state = Clip.STARTING

            clip_buffers = []
            clip_buffers.append(output_buffers[common.getJackPortName_L(clip.output)])
            clip_buffers.append(output_buffers[common.getJackPortName_R(clip.output)])

            frame_per_beat = fpm / bpm
            clip_period = (fpm * clip.beat_diviser) / bpm  # length of the clip in frames
            total_frame_offset = clip.frame_offset + (clip.beat_offset * frame_per_beat)

            # frame_beat: how many times the clip has been played already
            # clip_offset: position in the clip about to be played
            frame_beat, clip_offset = divmod((frame - total_frame_offset) * bpm, fpm * clip.beat_diviser)
            clip_offset = round(clip_offset / bpm)

            # is next beat in block ?
            if (clip_offset + blocksize) > clip_period:
                next_clip_offset = (clip_offset + blocksize) - clip_period
                next_clip_offset = round(blocksize - next_clip_offset)

            else:
                next_clip_offset = None
            
                if clip.state == clip.START and clip.one_shot == True and clip.shot == False:
                    clip.shot = True
                    clip.state = Clip.STOPPING


            if (clip.state == Clip.START or clip.state == Clip.STOPPING):
                # is there enough audio data ?
                if clip_offset < song.length(clip):
                    length = min(song.length(clip) - clip_offset, frames)
                    for ch_id, buffer in zip(range(len(clip_buffers)),
                                             clip_buffers):
                        data = song.getData(clip,
                                            ch_id % song.channels(clip) ,
                                            clip_offset,
                                            length)
                        buffer[:length] += data

                    clip.last_offset = clip_offset

            if clip.state == Clip.RECORDING:
                if next_clip_offset:
                    song.writeData(clip,
                                   0,
                                   clip_offset,
                                   inL_buffer[:next_clip_offset])
                    song.writeData(clip,
                                   1,
                                   clip_offset,
                                   inR_buffer[:next_clip_offset])
                else:
                    song.writeData(clip,
                                   0,
                                   clip_offset,
                                   inL_buffer)
                    song.writeData(clip,
                                   1,
                                   clip_offset,
                                   inR_buffer)
                clip.last_offset = clip_offset

            if next_clip_offset and (clip.state == Clip.START or clip.state == Clip.STARTING):
                length = min(song.length(clip), blocksize - next_clip_offset)
                if length:
                    for ch_id, buffer in zip(range(len(clip_buffers)),
                                             clip_buffers):
                        data = song.getData(clip,
                                            ch_id % song.channels(clip),
                                            0,
                                            length)
                        buffer[next_clip_offset:] += data

                clip.last_offset = 0

            if next_clip_offset and clip.state == Clip.PREPARE_RECORD:
                song.writeData(clip,
                               0,
                               0,
                               inL_buffer[next_clip_offset:])
                song.writeData(clip,
                               1,
                               0,
                               inR_buffer[next_clip_offset:])

            # starting or stopping clip
            if clip_offset == 0 or next_clip_offset:
       
                try:
                    # reset record offset
                    if clip.state == Clip.RECORDING:
                        clip.frame_offset = 0
                    clip.state = CLIP_TRANSITION[clip.state]
                    clip.last_offset = 0
                    gui.updateUi.emit()
                except KeyError:
                    pass



        # MIXERS  ----------------------------------------------------------------------------------------

        # apply master volume AND mixerstrip channel values
        for key, value in output_buffers.items():

            # compute port final volume
            if common.isSpinToolReservedJackPort(key) == False:
                # set final volume to port
                value[:] *= song.volume * 2 * common.CurrentChannelsValues[key]["final_vol"] # the default song vol is 0.5, so multiply by 2 to come back to real volume

                # route all own ports into MASTER_PORT and SENDS
                # LEFT CHANNEL
                if common.LEFT_CHANNEL in key:
                    # master port L
                    output_buffers[common.MASTER_PORT_CHANNELS[0]][:] += value[:] * (settings.master_port_final_volume * settings.master_port_mute * common.CurrentChannelsValues[key]["to_master"])
                    # send1 L
                    output_buffers[common.SEND1_PORT_CHANNELS[0]][:] += value[:] * common.CurrentChannelsValues[key]["send1"]
                    # send2 L
                    output_buffers[common.SEND2_PORT_CHANNELS[0]][:] += value[:] * common.CurrentChannelsValues[key]["send2"]

                # RIGHT CHANNEL
                if common.RIGHT_CHANNEL in key:
                    # master port R
                    output_buffers[common.MASTER_PORT_CHANNELS[1]][:] += value[:] * (settings.master_port_final_volume * settings.master_port_mute * common.CurrentChannelsValues[key]["to_master"])
                    # send1 R
                    output_buffers[common.SEND1_PORT_CHANNELS[1]][:] += value[:] * common.CurrentChannelsValues[key]["send1"]
                    # send2 R
                    output_buffers[common.SEND2_PORT_CHANNELS[1]][:] += value[:] * common.CurrentChannelsValues[key]["send2"]


            # if any value clipping: still work in progress. For the moment leave comments

            #if any(value > 0.99):
            #    common.clipping = True


        # CHECK IF CLIPPING
        checkClipping(position["tick"])


        # MIXER AND MASTER_END -------------------------------------------
        

    try:
        i = 1
        while True:
            note = gui.queue_out.get(block=False)
            midi_out.write_midi_event(i, note)
            i += 1
    except Empty:
        pass

    return jack.CALL_AGAIN


client.set_process_callback(my_callback)


# activate !
def start():
    with client:

        # get out connections
        playback = client.get_ports(is_physical=True, is_input=True)
        if not playback:
            raise RuntimeError("No physical playback ports")
        
        # get in connections
        record = client.get_ports(is_physical=True, is_output=True)
        if not record:
            raise RuntimeError("No physical input ports")


        # autoconnect
        if settings.auto_connect_input:
            # connect inputs
            try:
                client.connect(record[0], inL)
                client.connect(record[1], inR)
            except:
                raise RuntimeError("Error connecting input ports. Check JACK Settings")

        if settings.auto_connect_output:
            # connect Master output:
            try:
                client.connect(masterL, playback[0])
                client.connect(masterR, playback[1])
            except:
                raise RuntimeError("Error connecting Master out ports. Check JACK Settings")                


        # forcing Qt theme to prevent graphics changes from original style
        #style = QStyleFactory.create('gtk2')
        style = QStyleFactory.create('Fusion')
        app.setStyle(style)

        #print(QStyleFactory.keys())

        # set themes
        #import superboucle.qtmodern.styles
        #import superboucle.qtmodern.windows
        #superboucle.qtmodern.styles.light(app)


        app.exec_()

if __name__ == "__main__":
    start()
