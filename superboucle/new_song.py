from PyQt5.QtWidgets import QDialog
from superboucle.new_song_ui import Ui_Dialog
from superboucle.clip import Song
from PyQt5.QtCore import QSettings
from superboucle.preferences import Preferences
import settings
import common

class NewSongDialog(QDialog, Ui_Dialog):

    def __init__(self, parent):
        super(NewSongDialog, self).__init__(parent)
        self.gui = parent
        self.setupUi(self)

        self.widthSpinBox.setValue(settings.grid_columns)
        self.heightSpinBox.setValue(settings.grid_rows)
        self.spinBeats.setValue(settings.new_song_beats)
        self.spinBPM.setValue(settings.new_song_bpm)
        self.spinMasterVolume.setValue(settings.new_song_master_volume)

        self.show()

    def accept(self):
        volume = common.toStoredSongVolumeValue(self.spinMasterVolume.value())
        self.gui.initUI(Song(self.widthSpinBox.value(),
                             self.heightSpinBox.value(),
                             volume,
                             self.spinBPM.value(),
                             self.spinBeats.value()))
                             
        super(NewSongDialog, self).accept()
