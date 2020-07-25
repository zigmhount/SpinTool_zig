from PyQt5.QtCore import Qt
from superboucle.assistant import Assistant
from PyQt5.QtGui import QCursor
import help
from PyQt5.QtWidgets import QDialog, QApplication
from superboucle.add_scene_ui import Ui_Dialog

class AddSceneDialog(QDialog, Ui_Dialog):
    def __init__(self, gui, callback=None):
        super(AddSceneDialog, self).__init__(gui)
        self.gui = gui
        self.callback = callback
        self.setupUi(self)
        self.accepted.connect(self.onOk)

        if self.gui.song.selectedClips().__len__() > 0:
            # if there are some Selected clip in Song, including them is suggested:
            self.checkBoxIncludeSelected.setChecked(True)
            self.checkBoxIncludeStart.setChecked(False)
        else:
            # otherwise including starting / playing clips is suggested:
            self.checkBoxIncludeSelected.setChecked(False)
            self.checkBoxIncludeStart.setChecked(True)        

        self.show()
        self.name.setFocus()

    def onOk(self):
        self.gui.song.addScene(self.name.text(), self.checkBoxIncludeStart.isChecked(), self.checkBoxIncludeSelected.isChecked())
        if self.callback:
            self.callback()

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