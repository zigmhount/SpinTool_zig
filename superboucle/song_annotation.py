from PyQt5.QtWidgets import QDialog
from superboucle.song_annotation_ui import Ui_Dialog
import copy
import settings
   
class SongAnnotation(QDialog, Ui_Dialog):
    
    def __init__(self, parent):
        super(SongAnnotation, self).__init__(parent)
        self.gui = parent
        self.setupUi(self)
        self.txtAnnotation.clear()
        self.txtAnnotation.setText(self.gui.song.annotation)
        self.txtAnnotation.textChanged.connect(self.onTextChanged)
        
        self.setLayout(self.formLayout)
        
        if settings.song_annotation_geometry:
            self.restoreGeometry(settings.song_annotation_geometry)        
        
        self.show()

    # Saving window position

    def onTextChanged(self):
        self.gui.song.annotation = str(self.txtAnnotation.toPlainText())

    def moveEvent(self, event):
        self.geometry = self.saveGeometry()
        settings.song_annotation_geometry = copy.deepcopy(self.geometry) 

    def updateText(self, text):
        self.txtAnnotation.setText(text) 

    def hideEvent(self, event):
        self.onHide()

    def onHide(self):
        self.gui.song.annotation = str(self.txtAnnotation.toPlainText())
        self.gui.action_SongAnnotation.setEnabled(True)

    def onFinished(self):
        pass
