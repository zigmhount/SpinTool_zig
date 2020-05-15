from PyQt5.QtWidgets import QDialog, QFileDialog
from superboucle.export_samples_ui import Ui_Dialog

class ExportAllSamplesDialog(QDialog, Ui_Dialog):
    def __init__(self, parent):
        super(ExportAllSamplesDialog, self).__init__(parent)

        self.gui = parent
        self.setupUi(self)
        self.accepted.connect(self.onOk)
        self.btnPath.clicked.connect(self.onPath)
        self.proceed = False

        self.setFixedSize(self.size())
        self.setModal(True)
        self.show()

    def setPath(self, path):
        self.labelPath.setText(path)

    def getPath(self):
        return self.labelPath.text()

    def getNormalize(self):
        return self.cBoxNormalize.isChecked()
    
    def getX(self):
        return self.lineX.text()

    def getY(self):
        return self.lineY.text()  

    def onPath(self):
        self.labelPath.setText(QFileDialog.getExistingDirectory(self, 'Select export directory'))

    def onOk(self):
        self.proceed = True

    def onFinished(self):
        pass        