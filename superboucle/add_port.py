from PyQt5.QtWidgets import QDialog, QMessageBox
from superboucle.add_port_ui import Ui_Dialog

import common
import settings

class AddPortDialog(QDialog, Ui_Dialog):
    def __init__(self, gui, callback=None):
        super(AddPortDialog, self).__init__(gui)
        self.gui = gui
        self.callback = callback
        self.setupUi(self)
        self.accepted.connect(self.onOk)
        self.rejected.connect(self.onCancel)
        self.show()
        self.name.setFocus()

    def onOk(self):

        port_name = self.name.text().upper().strip()

        if (port_name == common.DEFAULT_PORT.upper() or port_name == common.MASTER_PORT.upper()
           or port_name == common.CLICK_PORT.upper() or port_name == common.SEND1_PORT.upper()
           or port_name == common.SEND2_PORT.upper()):

            message = QMessageBox(self)
            message.setWindowTitle("Can't create port " + self.name.text())
            message.setText(self.name.text() + " is a reserved SpinTool system port")
            message.show()
            return

        if "_L" in port_name or "_R" in port_name:
            message = QMessageBox(self)
            message.setWindowTitle("Can't create port " + self.name.text())
            message.setText("_L and _R are reserved by SpinTool and are not allowed in port name")
            message.show()
            return

        for existingPort in settings.output_ports.keys():
            if port_name == existingPort.upper():
                message = QMessageBox(self)
                message.setWindowTitle("Can't create port " + self.name.text())
                message.setText(self.name.text() + " output port is already existing")
                message.show()
                return

        self.gui.addPort(self.name.text())

        if self.callback:
            self.callback()


    def onCancel(self):
        if self.gui.last_clip:
            self.gui.output.setCurrentText(self.gui.last_clip.output)
