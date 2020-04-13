from PyQt5.QtWidgets import QDialog
from superboucle.song_annotation_ui import Ui_Dialog
import copy
   
class SongAnnotation(QDialog, Ui_Dialog):
    
    def __init__(self, parent):
        super(SongAnnotation, self).__init__(parent)
        self.gui = parent
        self.setupUi(self)
        self.txtAnnotation.clear()
        self.txtAnnotation.setText(self.gui.song.annotation) 
        
        self.setLayout(self.formLayout)
        
        if self.gui.song_annotation_geometry:
            self.restoreGeometry(self.gui.song_annotation_geometry)        
        
        self.show()

    # Saving window position

    def moveEvent(self, event):
        self.geometry = self.saveGeometry()
        self.gui.song_annotation_geometry = copy.deepcopy(self.geometry) # deep copy

    def updateText(self, text):
        self.txtAnnotation.setText(text) 

    def hideEvent(self, event):
        self.onHide() 

    def onHide(self):
        self.gui.song.annotation = str(self.txtAnnotation.toPlainText())
        self.gui.action_SongAnnotation.setEnabled(True)

    def onFinished(self):
        pass
