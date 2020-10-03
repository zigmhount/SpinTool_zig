# SpinTool

SpinTool is a loop based software fully controllable with any midi device,
synced with Jack transport. This version derives from original Vampouille's
SuperBoucle, starting from a fork of the original repository.

Check user manual (from Info menu of application) for a description of 
usage and functions.
Press the H key for integrated help to have a quick
help on what the mouse cursor is pointing at.

Usage Wiki for Starting:
https://github.com/manucontrovento/SpinTool/wiki

DEV BRANCH MANU


## Features

* Jack Transport
* Record
* Audio input / output
* Midi input / output
* Normalize and revert samples
* Negative sample offset, sample offset in beats or frames
* Load several formats: WAV, FLAC, AIFF, ...  (no MP3 at the moment)
* Playlist management
* Scenes management
* Full intuitive MIDI learn interface
* Support any MIDI device: generic keyboard, pad, BCF, Akai APC, ...
* Fully controllable by MIDI device or mouse/keyboard
* One-shot clips
* Light-on all midi device buttons (scenes and transport too)
* Preferences Window
* Start a clip just after recording it
* Show clip details when triggered for start/stop
* Show clip details when its volume is changed from controller
* Preferred grid size, to match your controller's buttons grid
* Choice of clip recording color (amber is default, red available)
* Open scenes and playlist windows on start up
* New grid cells style, showing clip volume
* New massive clips edit functions to change clips parameters and column instrument-wise assignment
* New Export-all samples function 
* Mixer for output ports with full MIDI support
* Integrated Help/Manual
* Force clips play/stop

SpinTool releases start from version 20.04.07

## Requirements

### Linux

* Python 3
* Pip for python 3
* Python modules : Cffi, PySoundFile, Numpy, PyQT 5, psUtil
* Running jack server

Recommended:
* a2jmidid to access midi controller
* Carla to save connections

## Installation

* Install Jack server :

        sudo aptitude install jackd2 qjackctl

* Install midi bridge (optional) : 

        sudo aptitude install a2jmidid

* Install python modules : 

        sudo aptitude install python3 python3-pip python3-cffi python3-numpy python3-pyqt5
        sudo pip3 install PySoundFile

* Download and extract last version of SpinTool from https://github.com/manucontrovento/SpinTool/releases/

## Running

Start Jack audio server and then run SpinTool.sh script from SpinTool directory :

	./SpinTool.sh

## Credits and links

I have to thank first of all Vampouille, who created SuperBoucle and fixed some
issues I reported, and Vince who helped me understanding how to start and proceed
in my development.

Original SuperBoucle master repository is here: 
	https://github.com/Vampouille/superboucle

and Vince activities website:
	https://www.sonejo.net/

