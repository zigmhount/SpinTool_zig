from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QSize, Qt
from superboucle.cell_ui import Ui_Cell
from superboucle.clip import basename, Clip
import numpy as np
import soundfile as sf
from PyQt5 import QtGui
from superboucle.preferences import Preferences
import settings
import common

ICON_EDIT_SIZE = QSize(28, 28)

class Cell(QWidget, Ui_Cell):

    GREEN = ("#cell_frame { border: 0px; border-radius: 10px; "
             "background-color: rgb(125,242,0);}")
    BLUE = ("#cell_frame { border: 0px; border-radius: 10px; "
            "background-color: rgb(0, 130, 240);}")
    RED = ("#cell_frame { border: 0px; border-radius: 10px; "
           "background-color: rgb(255, 21, 65);}")
    AMBER = ("#cell_frame { border: 0px; border-radius: 10px; "
             "background-color: rgb(255, 102, 0);}")
    PURPLE = ("#cell_frame { border: 0px; border-radius: 10px; "
              "background-color: rgb(130, 0, 240);}")
    DEFAULT = ("#cell_frame { border: 0px; border-radius: 10px; "
               "background-color: rgb(190, 190, 190);}")

    RECORD_BLINK = ("QPushButton {background-color: rgb(255, 255, 255);}"
                    "QPushButton:pressed {background-color: "
                    "rgb(98, 98, 98);}")

    RECORD_DEFAULT = ("QPushButton {background-color: rgb(0, 0, 0);}"
                      "QPushButton:pressed {background-color: "
                      "rgb(98, 98, 98);}")

    DEFAULT_CLIP_LABEL_STYLE = ('font: bold 13pt "Noto Sans"; color: rgb(0, 0, 0); text-align: center;')

    SELECTED_CLIP_LABEL_STYLE = ('font: bold 13pt "Noto Sans"; color: rgb(255, 255, 0); text-align: center;')

    # Managing recording color
    
    if settings.rec_color == settings.COLOR_RED:
        
        # RED color for recording
        STATE_COLORS = {Clip.STOP: AMBER,
                        Clip.STARTING: GREEN,
                        Clip.START: GREEN,
                        Clip.STOPPING: AMBER,
                        Clip.PREPARE_RECORD: RED,
                        Clip.RECORDING: RED}
    else:
        # default (AMBER color for recording)
        STATE_COLORS = {Clip.STOP: RED,
                        Clip.STARTING: GREEN,
                        Clip.START: GREEN,
                        Clip.STOPPING: RED,
                        Clip.PREPARE_RECORD: AMBER,
                        Clip.RECORDING: AMBER}
    
    STATE_BLINK = {Clip.STOP: False,
                   Clip.STARTING: True,
                   Clip.START: False,
                   Clip.STOPPING: True,
                   Clip.PREPARE_RECORD: True,
                   Clip.RECORDING: False}

    def __init__(self, parent, clip, x, y):
        super(Cell, self).__init__(parent)

        self.gui = parent
        self.pos_x, self.pos_y = x, y
        self.clip = clip
        self.blink, self.color = False, None
        self.setupUi(self)
        self.setStyleSheet(Cell.DEFAULT)
        self.setAcceptDrops(True)

        if clip:
            self.labelVolume.setText(str(common.toDigitalVolumeValue(clip.volume)))
            self.clip_name.setText(clip.name)
            self.start_stop.clicked.connect(parent.onStartStopClicked)
            self.edit.clicked.connect(parent.onEdit)
            self.setEditIcon()
        else:
            self.labelVolume.setText("")
            self.start_stop.setEnabled(False)
            self.clip_position.setEnabled(False)
            self.edit.setIcon(QtGui.QIcon(":/icons/icons/clip-add.png"))
            self.edit.clicked.connect(parent.onAddClipClicked)

    def setEditIcon(self):
        self.edit.setIcon(QtGui.QIcon(":/icons/icons/clip-edit.png"))
        self.edit.setIconSize(ICON_EDIT_SIZE)

    def clipSelect(self, value):
        if self.clip:
            self.clip.selected = value
            if (self.clip.selected) == True:
                self.clip_name.setStyleSheet(self.SELECTED_CLIP_LABEL_STYLE)
            else:
                self.clip_name.setStyleSheet(self.DEFAULT_CLIP_LABEL_STYLE)

    def mousePressEvent(self, event):
        if QApplication.keyboardModifiers() == Qt.ShiftModifier and self.clip:
            value = not(self.clip.selected)
            self.clipSelect(value)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if len(urls):
            path = urls[0].path()
            self.setClip(self.getClip(path))

    def setClip(self, new_clip, fromDialog = True):
        
        if not new_clip:
            return
        
        self.clip = new_clip
        self.clip_name.setText(new_clip.name)
        self.labelVolume.setText(str(common.toDigitalVolumeValue(new_clip.volume)))
        self.start_stop.clicked.connect(self.gui.onStartStopClicked)
        self.setEditIcon()
        if fromDialog == True:
            self.edit.clicked.disconnect(self.gui.onAddClipClicked)
        self.edit.clicked.connect(self.gui.onEdit)
        self.start_stop.setEnabled(True)
        self.clip_position.setEnabled(True)
        self.setAcceptDrops(False)
        self.gui.song.addClip(new_clip, self.pos_x, self.pos_y)
        self.gui.last_clip = new_clip
        self.gui.update()

    def openClip(self):
        audio_file, a = self.gui.getOpenFileName('Open Clip',
                                                 common.ALL_FILE_TYPE, self)
        if audio_file and a:
            return self.getClip(audio_file)

    def getClip(self, audio_file):
        wav_id = basename(audio_file)
        if wav_id in self.gui.song.data:
            i = 0
            while "%s-%02d" % (wav_id, i) in self.gui.song.data:
                i += 1
            wav_id = "%s-%02d" % (wav_id, i)

        data, samplerate = sf.read(audio_file, dtype=np.float32)
        self.gui.song.data[wav_id] = data
        self.gui.song.samplerate[wav_id] = samplerate

        return Clip(basename(wav_id))

    def setColor(self, state):
        self.setStyleSheet(Cell.STATE_COLORS[state])
        self.blink = Cell.STATE_BLINK[state]
        self.color = Cell.STATE_COLORS[state]
