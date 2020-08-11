from PyQt5.QtCore import Qt
from superboucle.assistant import Assistant
from PyQt5.QtGui import QCursor
import help
from PyQt5.QtWidgets import QDialog, QWidget, QMessageBox, QApplication
from PyQt5.QtCore import pyqtSignal
import struct
from copy import deepcopy
from queue import Queue, Empty
from superboucle.learn_cell_ui import Ui_LearnCell
from superboucle.learn_ui import Ui_Dialog
from superboucle.device import Device
import re
import common

_init_cmd_regexp = re.compile("^\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*$")

class LearnCell(QWidget, Ui_LearnCell):
    def __init__(self, parent):
        super(LearnCell, self).__init__(parent)
        self.setupUi(self)

class LearnDialog(QDialog, Ui_Dialog):
    NOTEON = 0x9
    NOTEOFF = 0x8
    MIDICTRL = 11

    MIDI_LEARNING = "learning..."

    NEW_CELL_STYLE = ("#cell_frame {border: 0px; "
                      "border-radius: 5px; "
                      "background-color: rgb(215, 215, 215);}")
                      
    NEW_CELL_STYLE_ROUND = ("#cell_frame {border: 0px; "
                            "border-radius: 20px; "
                            "background-color: rgb(215, 215, 215);}")

    NOTE_NAME = ['C', 'C#',
                 'D', 'D#',
                 'E',
                 'F', 'F#',
                 'G', 'G#',
                 'A', 'A#',
                 'B']

    # send_midi_to values :
    START_STOP = 0
    MASTER_VOLUME_CTRL = 1
    CTRLS = 2
    MUTE_BUTTONS = 3
    PLAY_BTN = 4
    PAUSE_BTN = 5
    REWIND_BTN = 6
    GOTO_BTN = 7
    RECORD_BTN = 8
    SCENES_BTN = 9
    STOP_BTN = 10
    SHIFT_BTN = 11
    UNLINK_STRIPES_BTN = 12
    CUSTOM_RESET_BTN = 13
    SEND1_CTRLS = 14
    SEND2_CTRLS = 15

    updateUi = pyqtSignal()

    def __init__(self, parent, callback, device=None):
        super(LearnDialog, self).__init__(parent)
        self.gui = parent
        self.setupUi(self)
        self.callback = callback
        self.queue = Queue()

        if device is None:
            self.original_device = Device()
        else:
            self.original_device = device
            self.setWindowTitle("Edit %s" % device.name)

        # perform deep copy in order to keep original values if cancel is
        # clicked

        self.device = Device(deepcopy(self.original_device.mapping))
        self.current_line = None
        self.current_row = None
        self.current_line_pitch = []
        self.knownCtrl = set()  # this keeps the already assigned controls (knobs, sliders)
        self.knownBtn = set()   # this keeps the already assigned notes (button)
        self.mute_bts_list = []
        self.send_midi_to = None
        self.updateUi.connect(self.update)

        # set (restore) current device values

        self.name.setText(self.device.name)
        self.plainTextEditDescription.setPlainText(self.device.description)
        self.black_vel.setValue(self.device.black_vel)
        self.green_vel.setValue(self.device.green_vel)
        self.blink_green_vel.setValue(self.device.blink_green_vel)
        self.red_vel.setValue(self.device.red_vel)
        self.blink_red_vel.setValue(self.device.blink_red_vel)
        self.amber_vel.setValue(self.device.amber_vel)
        self.blink_amber_vel.setValue(self.device.blink_amber_vel)

        if self.device.song_volume_ctrl:
            (self.label_song_volume_ctrl.setText(
                self.displayCtrl(self.device.song_volume_ctrl)))

        if self.device.play_btn:
            self.playLabel.setText(self.displayBtn(self.device.play_btn))

        if self.device.pause_btn:
            self.pauseLabel.setText(self.displayBtn(self.device.pause_btn))

        if self.device.rewind_btn:
            self.rewindLabel.setText(self.displayBtn(self.device.rewind_btn))

        if self.device.goto_btn:
            self.gotoLabel.setText(self.displayBtn(self.device.goto_btn))

        if self.device.record_btn:
            self.recordLabel.setText(self.displayBtn(self.device.record_btn))

        if self.device.stop_btn:
            self.stopLabel.setText(self.displayBtn(self.device.stop_btn))

        if self.device.shift_btn:
            self.shiftLabel.setText(self.displayBtn(self.device.shift_btn))

        if self.device.unlink_stripes_btn:
            self.unlinkStripeControlsLabel.setText(self.displayBtn(self.device.unlink_stripes_btn))

        if self.device.custom_reset_btn:
            self.customResetLabel.setText(self.displayBtn(self.device.custom_reset_btn))

        (self.init_command
         .setText("\n".join([", ".join([str(num)
                                        for num in init_cmd])
                             for init_cmd in self.device.init_command])))

        for scene_btn in self.device.scene_buttons:
            (msg_type, channel, pitch, velocity) = scene_btn
            cell = LearnCell(self)
            cell.label.setText("Ch %s\n%s"
                               % (channel + 1,
                                  self.displayNote(pitch)))
            cell.setStyleSheet(self.NEW_CELL_STYLE)
            self.scenesHorizontalLayout.addWidget(cell)
        
        for mute_btn in self.device.mute_buttons:
            (msg_type, channel, pitch, velocity) = mute_btn
            cell = LearnCell(self)
            cell.label.setText("Ch %s\n%s"
                               % (channel + 1,
                                  self.displayNote(pitch)))
            cell.setStyleSheet(self.NEW_CELL_STYLE)
            self.btsHorizontalLayout.addWidget(cell)

        for vol_ctrl in self.device.ctrls:
            (msg_type, channel, pitch) = vol_ctrl
            cell = LearnCell(self)
            cell.label.setText("Ch %s\n%s"
                               % (channel + 1, pitch))
            cell.setStyleSheet(self.NEW_CELL_STYLE_ROUND)
            self.ctrlsHorizontalLayout.addWidget(cell)

        for send1_ctrl in self.device.send1ctrls:
            (msg_type, channel, pitch) = send1_ctrl
            cell = LearnCell(self)
            cell.label.setText("Ch %s\n%s"
                               % (channel + 1, pitch))
            cell.setStyleSheet(self.NEW_CELL_STYLE_ROUND)
            self.send1HorizontalLayout.addWidget(cell)

        for send2_ctrl in self.device.send2ctrls:
            (msg_type, channel, pitch) = send2_ctrl
            cell = LearnCell(self)
            cell.label.setText("Ch %s\n%s"
                               % (channel + 1, pitch))
            cell.setStyleSheet(self.NEW_CELL_STYLE_ROUND)
            self.send2HorizontalLayout.addWidget(cell)


        for line in self.device.start_stop:
            if self.current_line is None:
                self.current_line = 0
                self.firstLine.setText("Add Next line")
            else:
                self.current_line += 1
            self.current_row = 0

            for btn_key in line:
                (msg_type, channel, pitch, velocity) = btn_key
                cell = LearnCell(self)
                cell.label.setText("Ch %s\n%s"
                                   % (channel + 1,
                                      self.displayNote(pitch)))
                cell.setStyleSheet(self.NEW_CELL_STYLE)
                self.gridLayout.addWidget(cell,
                                          self.current_line,
                                          self.current_row)
                self.current_row += 1

        # connect signals
        self.accepted.connect(self.onSave)
        self.firstLine.clicked.connect(self.onFirstLineClicked)
        self.learn_song_volume_ctrl.clicked.connect(self.onMasterVolumeCtrl)
        self.playButton.clicked.connect(self.onPlayButton)
        self.pauseButton.clicked.connect(self.onPauseButton)
        self.rewindButton.clicked.connect(self.onRewindButton)
        self.stopButton.clicked.connect(self.onStopButton)
        self.shiftButton.clicked.connect(self.onShiftButton)
        self.customResetButton.clicked.connect(self.onCustomResetButton)
        self.unlinkStripeControlsButton.clicked.connect(self.onUnlinkMixerStripesButton)
        self.gotoButton.clicked.connect(self.onGotoButton)
        self.recordButton.clicked.connect(self.onRecordButton)
        self.sendInitButton.clicked.connect(self.onSendInit)
        self.learn_ctrls.clicked.connect(self.onCtrls)

        self.learn_send1_ctrls.clicked.connect(self.onSend1Ctrls)
        self.learn_send2_ctrls.clicked.connect(self.onSend2Ctrls)

        self.learn_mute_bts.clicked.connect(self.onMuteBts)
        self.learn_scenes.clicked.connect(self.onScenesButton)
        self.stop1.clicked.connect(self.onStopClicked)
        self.stop2.clicked.connect(self.onStopClicked)
        self.stop3.clicked.connect(self.onStopClicked)
        self.stop4.clicked.connect(self.onStopClicked)
        self.stop_send1_ctrls.clicked.connect(self.onStopClicked)
        self.stop_send2_ctrls.clicked.connect(self.onStopClicked)

        self.learn_black.clicked.connect(self.onBlack)
        self.learn_green.clicked.connect(self.onGreen)
        self.learn_blink_green.clicked.connect(self.onBlinkGreen)
        self.learn_red.clicked.connect(self.onRed)
        self.learn_blink_red.clicked.connect(self.onBlinkRed)
        self.learn_amber.clicked.connect(self.onAmber)
        self.learn_blink_amber.clicked.connect(self.onBlinkAmber)
        self.black_vel.valueChanged.connect(self.onBlack)
        self.green_vel.valueChanged.connect(self.onGreen)
        self.blink_green_vel.valueChanged.connect(self.onBlinkGreen)
        self.red_vel.valueChanged.connect(self.onRed)
        self.blink_red_vel.valueChanged.connect(self.onBlinkRed)
        self.amber_vel.valueChanged.connect(self.onAmber)
        self.blink_amber_vel.valueChanged.connect(self.onBlinkAmber)
        self.test_color_vel.valueChanged.connect(self.onTestAllColors)
        self.test_color_checkbox.clicked.connect(self.onTestAllColors)

        self.btnResetClips.clicked.connect(self.onResetClips)
        self.btnResetSongVol.clicked.connect(self.onResetSongVol)
        self.btnResetMute.clicked.connect(self.onResetMute)
        self.btnResetOtherFunctions.clicked.connect(self.onResetOtherFunctions)
        self.btnResetScenes.clicked.connect(self.onResetScenes)
        self.btnResetTransport.clicked.connect(self.onResetTransport)
        self.btnResetVolumes.clicked.connect(self.onResetVolumes)

        self.btnReset_send1_ctrls.clicked.connect(self.onResetSend1)
        self.btnReset_send2_ctrls.clicked.connect(self.onResetSend2)

        
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.setModal(True)

        self.tabMIDI.setCurrentIndex(0)
        self.notifyMidiLearning(False)

        if device:
            self.gui.lightDownDevice()
        
        self.show()

    def notifyMidiLearning(self, value):
        if value == True:
            self.labelMessage.setText(self.MIDI_LEARNING)
        else:
            self.labelMessage.setText("")

    def onFirstLineClicked(self):
        self.notifyMidiLearning(True)
        self.send_midi_to = self.START_STOP

        if self.current_line is None:
            self.current_line = 0
            self.firstLine.setText("Add next line")
        else:
            self.current_line += 1

        self.current_line_pitch = []
        self.device.start_stop.append(self.current_line_pitch)
        self.firstLine.setEnabled(False)
        self.current_row = 0
        cell = LearnCell(self)
        self.gridLayout.addWidget(cell,
                                  self.current_line,
                                  self.current_row)

    def onMasterVolumeCtrl(self):
        self.notifyMidiLearning(True)
        self.send_midi_to = self.MASTER_VOLUME_CTRL

    def onPlayButton(self):
        self.notifyMidiLearning(True)
        self.send_midi_to = self.PLAY_BTN

    def onPauseButton(self):
        self.notifyMidiLearning(True)
        self.send_midi_to = self.PAUSE_BTN

    def onShiftButton(self):
        self.notifyMidiLearning(True)
        self.send_midi_to = self.SHIFT_BTN

    def onCustomResetButton(self):
        self.notifyMidiLearning(True)
        self.send_midi_to = self.CUSTOM_RESET_BTN

    def onUnlinkMixerStripesButton(self):
        self.notifyMidiLearning(True)
        self.send_midi_to = self.UNLINK_STRIPES_BTN

    def onStopButton(self):
        self.notifyMidiLearning(True)
        self.send_midi_to = self.STOP_BTN

    def onRewindButton(self):
        self.notifyMidiLearning(True)
        self.send_midi_to = self.REWIND_BTN

    def onGotoButton(self):
        self.notifyMidiLearning(True)
        self.send_midi_to = self.GOTO_BTN

    def onRecordButton(self):
        self.notifyMidiLearning(True)
        self.send_midi_to = self.RECORD_BTN

    def onScenesButton(self):
        self.notifyMidiLearning(True)
        self.send_midi_to = self.SCENES_BTN

    def onSendInit(self):
        try:
            for note in self.parseInitCommand():
                self.gui.queue_out.put(note)
        except Exception as ex:
            QMessageBox.critical(self,
                                 "Invalid init commands",
                                 str(ex))

    def onCtrls(self): # strip volume
        self.notifyMidiLearning(True)
        self.send_midi_to = self.CTRLS

    def onSend1Ctrls(self):
        self.notifyMidiLearning(True)
        self.send_midi_to = self.SEND1_CTRLS

    def onSend2Ctrls(self):
        self.notifyMidiLearning(True)
        self.send_midi_to = self.SEND2_CTRLS



    def onMuteBts(self):
        self.notifyMidiLearning(True)
        self.send_midi_to = self.MUTE_BUTTONS

    def onStopClicked(self):
        self.notifyMidiLearning(False)
        self.send_midi_to = None

    def onBlack(self):
        self.lightAllCell(self.black_vel.value())

    def onGreen(self):
        self.lightAllCell(self.green_vel.value())

    def onBlinkGreen(self):
        self.lightAllCell(self.blink_green_vel.value())

    def onRed(self):
        self.lightAllCell(self.red_vel.value())

    def onBlinkRed(self):
        self.lightAllCell(self.blink_red_vel.value())

    def onAmber(self):
        self.lightAllCell(self.amber_vel.value())

    def onBlinkAmber(self):
        self.lightAllCell(self.blink_amber_vel.value())


    def onTestAllColors(self):
        self.onBlack()
        if self.test_color_checkbox.isChecked() == True:
            self.lightAllCell(self.test_color_vel.value())


    def lightAllCell(self, color):
        self.device.setAllCellsColor(self.gui.queue_out, color)



    def update(self):
        try:
            while True:
                data = self.queue.get(block=False)
                if len(data) == 3:
                    status, pitch, vel = struct.unpack('3B', data)
                    self.processNote(status, pitch, vel)
        except Empty:
            pass

    # Function for learning
    def processNote(self, status, pitch, velocity):

        channel = status & 0xF
        msg_type = status >> 4

        # -1: special value for velocity sensitive pad
        btn_id = (msg_type,
                  channel,
                  pitch,
                  -1 if velocity not in [0, 127] else velocity)
        btn_key = (msg_type >> 1, channel, pitch)
        ctrl_key = (msg_type, channel, pitch)
        key_OFF = (self.NOTEOFF, channel, pitch)

        if ctrl_key not in self.knownCtrl:
            # process controller

            # Master volume
            if self.send_midi_to == self.MASTER_VOLUME_CTRL:
                if msg_type == self.MIDICTRL:
                    self.device.song_volume_ctrl = ctrl_key
                    (self.label_song_volume_ctrl
                     .setText(self.displayCtrl(ctrl_key)))
                    self.knownCtrl.add(ctrl_key)
                    self.send_midi_to = None
                    self.notifyMidiLearning(False)

            # transport Play
            elif self.send_midi_to == self.PLAY_BTN:
                self.send_midi_to = None
                self.addToKnown(ctrl_key, btn_key, key_OFF)
                self.device.play_btn = btn_id
                self.playLabel.setText(self.displayCtrl(ctrl_key))
                self.notifyMidiLearning(False)
            
            # transport pause
            elif self.send_midi_to == self.PAUSE_BTN:
                self.send_midi_to = None
                self.addToKnown(ctrl_key, btn_key, key_OFF)
                self.device.pause_btn = btn_id
                self.pauseLabel.setText(self.displayCtrl(ctrl_key))
                self.notifyMidiLearning(False)

            # transport rewind
            elif self.send_midi_to == self.REWIND_BTN:
                self.send_midi_to = None
                self.addToKnown(ctrl_key, btn_key, key_OFF)
                self.device.rewind_btn = btn_id
                self.rewindLabel.setText(self.displayCtrl(ctrl_key))
                self.notifyMidiLearning(False)

            # transport Stop
            elif self.send_midi_to == self.STOP_BTN:
                self.send_midi_to = None
                self.addToKnown(ctrl_key, btn_key, key_OFF)
                self.device.stop_btn = btn_id
                self.stopLabel.setText(self.displayCtrl(ctrl_key))
                self.notifyMidiLearning(False)

            # transport Go to position
            elif self.send_midi_to == self.GOTO_BTN:
                self.send_midi_to = None
                self.addToKnown(ctrl_key, btn_key, key_OFF)
                self.device.goto_btn = btn_id
                self.gotoLabel.setText(self.displayCtrl(ctrl_key))
                self.notifyMidiLearning(False)

            # transport Record 
            elif self.send_midi_to == self.RECORD_BTN:
                self.send_midi_to = None
                self.addToKnown(ctrl_key, btn_key, key_OFF)
                self.device.record_btn = btn_id
                self.recordLabel.setText(self.displayCtrl(ctrl_key))
                self.notifyMidiLearning(False)

            # shift button 
            elif self.send_midi_to == self.SHIFT_BTN:
                self.send_midi_to = None
                self.addToKnown(ctrl_key, btn_key, key_OFF)
                self.device.shift_btn = btn_id
                self.shiftLabel.setText(self.displayCtrl(ctrl_key))
                self.notifyMidiLearning(False)

            # custom reset button
            elif self.send_midi_to == self.CUSTOM_RESET_BTN:
                self.send_midi_to = None
                self.addToKnown(ctrl_key, btn_key, key_OFF)
                self.device.custom_reset_btn = btn_id
                self.customResetLabel.setText(self.displayCtrl(ctrl_key))
                self.notifyMidiLearning(False)

            # unlink mixer stripes button 
            elif self.send_midi_to == self.UNLINK_STRIPES_BTN:
                self.send_midi_to = None
                self.addToKnown(ctrl_key, btn_key, key_OFF)
                self.device.unlink_stripes_btn = btn_id
                self.unlinkStripeControlsLabel.setText(self.displayCtrl(ctrl_key))
                self.notifyMidiLearning(False)

            # mixer output ports volumes:
            elif self.send_midi_to == self.CTRLS:
                if msg_type == self.MIDICTRL:
                    cell = LearnCell(self)
                    cell.label.setText("Ch %s\n%s"
                                       % (channel + 1, pitch))
                    cell.setStyleSheet(self.NEW_CELL_STYLE_ROUND)
                    self.ctrlsHorizontalLayout.addWidget(cell)
                    self.device.ctrls.append(ctrl_key)
                    self.knownCtrl.add(ctrl_key)

            # mixer send1
            elif self.send_midi_to == self.SEND1_CTRLS:
                if msg_type == self.MIDICTRL:
                    cell = LearnCell(self)
                    cell.label.setText("Ch %s\n%s"
                                       % (channel + 1, pitch))
                    cell.setStyleSheet(self.NEW_CELL_STYLE_ROUND)
                    self.send1HorizontalLayout.addWidget(cell)
                    self.device.send1ctrls.append(ctrl_key)
                    self.knownCtrl.add(ctrl_key)

            # mixer send2
            elif self.send_midi_to == self.SEND2_CTRLS:
                if msg_type == self.MIDICTRL:
                    cell = LearnCell(self)
                    cell.label.setText("Ch %s\n%s"
                                       % (channel + 1, pitch))
                    cell.setStyleSheet(self.NEW_CELL_STYLE_ROUND)
                    self.send2HorizontalLayout.addWidget(cell)
                    self.device.send2ctrls.append(ctrl_key)
                    self.knownCtrl.add(ctrl_key)



            # then process other
            elif btn_key not in self.knownBtn:

                # Scenes buttons
                if self.send_midi_to == self.SCENES_BTN:
                    cell = LearnCell(self)
                    cell.label.setText("Ch %s\n%s"
                                       % (channel + 1,
                                          self.displayNote(pitch)))
                    cell.setStyleSheet(self.NEW_CELL_STYLE)
                    self.scenesHorizontalLayout.addWidget(cell)
                    self.device.scene_buttons.append(btn_id)
                    self.addToKnown(ctrl_key, btn_key, key_OFF)
                
                # Mute buttons
                if self.send_midi_to == self.MUTE_BUTTONS:
                    cell = LearnCell(self)
                    cell.label.setText("Ch %s\n%s"
                                       % (channel + 1,
                                          self.displayNote(pitch)))
                    cell.setStyleSheet(self.NEW_CELL_STYLE)
                    self.btsHorizontalLayout.addWidget(cell)
                    self.device.mute_buttons.append(btn_id)
                    self.addToKnown(ctrl_key, btn_key, key_OFF)

                # Clips
                elif self.send_midi_to == self.START_STOP:
                    self.current_line_pitch.append(btn_id)
                    cell = LearnCell(self)
                    cell.label.setText("Ch %s\n%s"
                                       % (channel + 1,
                                          self.displayNote(pitch)))
                    cell.setStyleSheet(self.NEW_CELL_STYLE)
                    self.gridLayout.addWidget(cell,
                                              self.current_line,
                                              self.current_row)
                    self.current_row += 1
                    self.firstLine.setEnabled(True)
                    self.addToKnown(ctrl_key, btn_key, key_OFF)

        #else:
        #    QMessageBox.warning(self, "Already used MIDI control/note", "Choose another control/note")

    def addToKnown(self, ctrl_key, btn_key, key_OFF):
        self.knownCtrl.add(ctrl_key)
        self.knownCtrl.add(key_OFF)
        self.knownBtn.add(btn_key)
        self.knownBtn.add(key_OFF)

    def accept(self):
        if self.name.text().strip() == "":
            QMessageBox.critical(self, "Invalid configuration name", "Enter a configuration name")
            return

        try:
            self.parseInitCommand()
            super(LearnDialog, self).accept()
        except Exception as ex:
            QMessageBox.critical(self,
                                 "Invalid init commands",
                                 str(ex))

    def reject(self):
        self.gui.is_learn_device_mode = False
        self.onBlack()
        self.gui.redraw()
        super(LearnDialog, self).reject()


    def onSave(self):
        self.device.name = str(self.name.text())
        self.device.description = str(self.plainTextEditDescription.toPlainText())
        self.device.black_vel = int(self.black_vel.value())
        self.device.green_vel = int(self.green_vel.value())
        self.device.blink_green_vel = int(self.blink_green_vel.value())
        self.device.red_vel = int(self.red_vel.value())
        self.device.blink_red_vel = int(self.blink_red_vel.value())
        self.device.amber_vel = int(self.amber_vel.value())
        self.device.blink_amber_vel = int(self.blink_amber_vel.value())
        self.device.mapping['init_command'] = self.parseInitCommand()
        self.original_device.updateMapping(self.device.mapping)
        self.gui.is_learn_device_mode = False
        self.callback(self.original_device)
        self.onBlack()
        self.gui.redraw()
        self.gui.update()


    def displayNote(self, note_dec):
        octave, note = divmod(note_dec, 12)
        octave += 1
        note_str = self.NOTE_NAME[note]
        return note_str[:1] + str(octave) + note_str[1:]

    def displayCtrl(self, ctrl_key):
        (msg_type, channel, pitch) = ctrl_key
        if msg_type == self.NOTEON:
            type = "Note On"
            note = self.displayNote(pitch)
        elif msg_type == self.NOTEOFF:
            type = "Note Off"
            note = self.displayNote(pitch)
        elif msg_type == self.MIDICTRL:
            type = "Controller"
            note = str(pitch)
        else:
            type = "Type=%s" % msg_type
        return "Channel %s %s %s" % (channel + 1,
                                     type,
                                     note)

    def displayBtn(self, btn_id):
        (msg_type, channel, pitch, velocity) = btn_id
        ctrl_key = (msg_type, channel, pitch)
        return self.displayCtrl(ctrl_key)

    def parseInitCommand(self):
        raw_str = str(self.init_command.toPlainText())
        init_commands = []
        line = 1
        for raw_line in raw_str.split("\n"):
            matches = _init_cmd_regexp.match(raw_line)
            if matches:
                byte1 = int(matches.group(1))
                byte2 = int(matches.group(2))
                byte3 = int(matches.group(3))
                if not 0 <= byte1 < 256:
                    raise Exception("First number out of range on line %s"
                                    % line)
                if not 0 <= byte2 < 256:
                    raise Exception("Second number out of range on line %s"
                                    % line)
                if not 0 <= byte3 < 256:
                    raise Exception("Third number out of range on line %s"
                                    % line)
                init_commands.append((byte1, byte2, byte3))
            elif len(raw_line):
                raise Exception("Invalid format for Line %s :\n%s"
                                % (line, raw_line))
            line = line + 1
        return init_commands


    def onResetClips(self):

        for clipsLine in self.device.start_stop:
            self.discardNotes(self.knownCtrl, clipsLine)
            self.discardNotes(self.knownBtn, clipsLine)
        self.device.start_stop = []
        common.clearLayout(self.gridLayout)

        self.current_line = None
        self.current_row = None
        self.current_line_pitch = []
        self.firstLine.setText("Learn first line")

    def onResetSongVol(self):
        if self.device.song_volume_ctrl is not False:
            self.discardValue(self.knownCtrl, self.device.song_volume_ctrl)
            self.device.song_volume_ctrl = False
        self.label_song_volume_ctrl.setText("")

    def onResetMute(self):
        self.discardNotes(self.knownCtrl, self.device.mute_buttons)
        self.discardNotes(self.knownBtn, self.device.mute_buttons)
        self.device.mute_buttons = []
        common.clearLayout(self.btsHorizontalLayout)

    def onResetOtherFunctions(self):
        # shift button
        if self.device.shift_btn is not False:
            self.discardNote(self.knownCtrl, self.device.shift_btn)
            self.discardNote(self.knownBtn, self.device.shift_btn)
            self.device.shift_btn = False
        self.shiftLabel.setText("")
        # unlink button
        if self.device.unlink_stripes_btn is not False:
            self.discardNote(self.knownCtrl, self.device.unlink_stripes_btn)
            self.discardNote(self.knownBtn, self.device.unlink_stripes_btn)
            self.device.unlink_stripes_btn = False
        self.unlinkStripeControlsLabel.setText("")
        # custom reset button
        if self.device.custom_reset_btn is not False:
            self.discardNote(self.knownCtrl, self.device.custom_reset_btn)
            self.discardNote(self.knownBtn, self.device.custom_reset_btn)
            self.device.custom_reset_btn = False
        self.customResetLabel.setText("")

    def onResetScenes(self):
        self.discardNotes(self.knownCtrl, self.device.scene_buttons)
        self.discardNotes(self.knownBtn, self.device.scene_buttons)        
        self.device.scene_buttons = []
        common.clearLayout(self.scenesHorizontalLayout)

    def onResetTransport(self):
        # play button
        if self.device.play_btn is not False:
            self.discardNote(self.knownCtrl, self.device.play_btn)
            self.discardNote(self.knownBtn, self.device.play_btn)
            self.device.play_btn = False
        self.playLabel.setText("")
        # pause button
        if self.device.pause_btn is not False:
            self.discardNote(self.knownCtrl, self.device.pause_btn)
            self.discardNote(self.knownBtn, self.device.pause_btn)
            self.device.pause_btn = False
        self.pauseLabel.setText("")
        # record button
        if self.device.record_btn is not False:
            self.discardNote(self.knownCtrl, self.device.record_btn)
            self.discardNote(self.knownBtn, self.device.record_btn)
            self.device.record_btn = False
        self.recordLabel.setText("")
        # rewind button
        if self.device.rewind_btn is not False:
            self.discardNote(self.knownCtrl, self.device.rewind_btn)
            self.discardNote(self.knownBtn, self.device.rewind_btn)
            self.device.rewind_btn = False
        self.rewindLabel.setText("")   
        # goto button
        if self.device.goto_btn is not False:
            self.discardNote(self.knownCtrl, self.device.goto_btn)
            self.discardNote(self.knownBtn, self.device.goto_btn)
            self.device.goto_btn = False
        self.gotoLabel.setText("")
        # stop button
        if self.device.stop_btn is not False:
            self.discardNote(self.knownCtrl, self.device.stop_btn)
            self.discardNote(self.knownBtn, self.device.stop_btn)
            self.device.stop_btn = False
        self.stopLabel.setText("")             

    def onResetVolumes(self):
        self.discardValues(self.knownCtrl, self.device.ctrls)
        self.device.ctrls = []
        common.clearLayout(self.ctrlsHorizontalLayout)

    def onResetSend1(self):
        self.discardValues(self.knownCtrl, self.device.send1ctrls)
        self.device.send1ctrls = []
        common.clearLayout(self.send1HorizontalLayout)

    def onResetSend2(self):
        self.discardValues(self.knownCtrl, self.device.send2ctrls)
        self.device.send2ctrls = []
        common.clearLayout(self.send2HorizontalLayout)

    def discardValues(self, knownControls, assignedControls):
        for control in assignedControls:
            self.discardValue(knownControls, control)
    
    def discardValue(self, knownControls, assignedControl):
        par1, par2, par3 = assignedControl
        knownControls.discard((par1, par2, par3))

    def discardNotes(self, knownControls, assignedControls):
        for control in assignedControls:
            self.discardNote(knownControls, control)

    def discardNote(self, knownControls, assignedControl):
        par1, par2, par3, par4 = assignedControl
        knownControls.discard((self.NOTEON, par2, par3))
        knownControls.discard((self.NOTEOFF, par2, par3))
        knownControls.discard((0x4, par2, par3)) # temporary. Why did I have to do this?
                                                 # On my controller note-off is 0x4
   

    # HELP management ---------------------------------------------------------

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_H:  # if pressed key is H (help)

            pos = QCursor.pos()
            widget = QApplication.widgetAt(pos)   # this is widget under cursor

            if widget is None: return
            accName = widget.accessibleName()     # this is widget accessible name
            
            if accName != "":
                wantedHelp = help.Context(accName)  # Conversion of string accessible name to Context enum
                self.showContextHelp(wantedHelp)
                

    def showContextHelp(self, wantedHelp):
        helpText = help.getContextHelp(wantedHelp)
        Assistant(self, helpText, Assistant.MODE_CONTEXT)