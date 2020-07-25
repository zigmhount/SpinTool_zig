from PyQt5.QtCore import Qt
from superboucle.assistant import Assistant
from PyQt5.QtGui import QCursor
import help
from PyQt5.QtWidgets import QDialog, QApplication
from superboucle.add_clip_ui import Ui_Dialog
from superboucle.clip import Clip, basename
import os
import settings
import common


class AddClipDialog(QDialog, Ui_Dialog):
    def __init__(self, parent, cell):
        super(AddClipDialog, self).__init__(parent)
        self.gui = parent
        self.cell = cell
        self.type = None
        self.setupUi(self)

        # default choice
        self.newButton.setChecked(True)
        self.type = 'new'
        self.fileList.setEnabled(False)

        self.newButton.clicked.connect(self.onNew)
        self.useButton.clicked.connect(self.onUse)
        self.emptyButton.clicked.connect(self.onEmpty)
        self.accepted.connect(self.onOk)
        self.cBoxMetronomeClip.stateChanged.connect(self.onMetronomeClip)

        for wav_id in self.gui.song.data:
            self.fileList.addItem(wav_id)

        self.setModal(True)
        self.show()

    def onNew(self):
        self.type = 'new'

    def onUse(self):
        self.type = 'use'


    def onEmpty(self):
        self.type = 'empty'


    def onMetronomeClip(self):
        if self.cBoxMetronomeClip.isChecked():
            
            if self.emptyButton.isChecked():
                self.newButton.setChecked(True)
            self.emptyButton.setEnabled(False)
            self.cBoxLockRec.setChecked(False)
            self.cBoxOneShotClip.setChecked(False)
            self.cBoxLockRec.setEnabled(False)
            self.cBoxOneShotClip.setEnabled(False)
        
        else:

            self.emptyButton.setEnabled(True)
            self.cBoxLockRec.setEnabled(True)
            self.cBoxOneShotClip.setEnabled(True)


    def onOk(self):

        new_clip = None

        if self.type == 'new':
            new_clip = self.cell.openClip()

        elif self.type == 'use':
            wav_id = self.fileList.currentText()
            new_clip = Clip(audio_file=basename(wav_id), name=os.path.splitext(basename(wav_id))[0])

        elif self.type == 'empty':
            new_clip = Clip(audio_file=None,
                            name='audio-%02d' % len(self.gui.song.clips))
            
        if new_clip:
            new_clip.one_shot = self.cBoxOneShotClip.isChecked()
            new_clip.lock_rec = self.cBoxLockRec.isChecked()

            
            if self.cBoxMetronomeClip.isChecked():
                
                new_clip.always_play = True
                new_clip.mute_group = 0

                # checking if CLICK output port exists; creating it otherwise 
                click_st_port = common.checkClickPort(settings.output_ports)

                # adding it to jack, ST ports and GUI selection, un-route to master
                if click_st_port == False:
                    self.gui.addPort(common.CLICK_PORT, False)
                    #settings.output_ports[common.CLICK_PORT]["to_master"] = False  # -> un-route port from master
                    #self.gui.output_mixer.updateGui(settings.output_ports) # -> re-update mixer
                    #print(settings.output_ports[common.CLICK_PORT])


                # Assigning CLICK port to clip
                new_clip.output = common.CLICK_PORT


            self.cell.setClip(new_clip)
        
        if settings.auto_assign_new_clip_column:
            self.gui.autoAssignClipColumn(new_clip)


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
