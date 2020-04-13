from PyQt5.QtWidgets import QDialog
from superboucle.about_ui import Ui_Dialog
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
   
class About(QDialog, Ui_Dialog):
    
    def __init__(self, parent):
        super(About, self).__init__(parent)
        self.gui = parent
        self.setupUi(self)
        self.webLink = "https://github.com/manucontrovento/SpinTool"
        self.btnWebLink.clicked.connect(self.onWebLinkDoubleClick)
        
        self.labelVersion.setText(self.gui.ApplicationVersion())
        
        self.btnWebLink.setText(self.webLink)
        
        self.labelText.setText("Current development by Manu Controvento (Meltin'Pop) \n" +
                               "Many many thanks go to Vampouille which developed SuperBoucle " + 
                               "which I started from to make SpinTool")
        
        self.labelLicense.setText("This is a free and open source application, " +
                                  "you can re-distribute and/or change it according to " + 
                                  "GNU General Public License version 2 or later")
        
        #self.setModal(True)
        self.show()

    def onWebLinkDoubleClick(self):
         QDesktopServices.openUrl(QUrl(self.webLink))

    def onHide(self):
        self.gui.actionAbout.setEnabled(True)

    def onFinished(self):
        pass
