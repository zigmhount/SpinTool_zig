from PyQt5.QtWidgets import QDialog
from superboucle.assistant_ui import Ui_Dialog
import copy
import settings
   
class Assistant(QDialog, Ui_Dialog):

    MODE_MANUAL = 1
    MODE_CONTEXT = 2
    
    def __init__(self, parent, text, mode):
        super(Assistant, self).__init__(parent)
        self.gui = parent

        self.setupUi(self)
        self.updateText(text)
        
        self.txtHelp.setReadOnly(True)
        self.labelLogo.setDisabled(True)

        self.setLayout(self.verticalLayout)

        if mode == self.MODE_MANUAL:
            self.displayAsManual()
        elif mode == self.MODE_CONTEXT:
            self.displayAsContext()

        self.show()


    def updateText(self, text):
        self.txtHelp.setText(text)

    def displayAsContext(self):
        self.labelAssistant.setText("Assistant")
        self.resize(680, 460)

    def displayAsManual(self):
        self.labelAssistant.setText("User Manual")
        self.resize(790, 650)

    def onFinished(self):
        pass
