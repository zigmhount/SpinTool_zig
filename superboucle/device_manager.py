from PyQt5.QtWidgets import QDialog
from superboucle.device_manager_ui import Ui_Dialog
from superboucle.learn import LearnDialog
from superboucle.device import Device
from superboucle.clip import verify_ext
import json
import common
from PyQt5.QtWidgets import QMessageBox

class ManageDialog(QDialog, Ui_Dialog):
    def __init__(self, parent):
        super(ManageDialog, self).__init__(parent)
        self.gui = parent
        self.setupUi(self)

        self.updateDeviceList()

        self.editButton.clicked.connect(self.onEdit)
        self.deleteButton.clicked.connect(self.onDelete)
        self.importButton.clicked.connect(self.onImport)
        self.exportButton.clicked.connect(self.onExport)
        self.finished.connect(self.onFinished)
        
        self.setModal(True)
        self.show()


    def onEdit(self):
        if self.gui._jack_client.transport_state == 1: # ROLLING

            response = QMessageBox.question(self, "Enter device configuration?", "The song execution will be stopped")
            if response == QMessageBox.No:
                return
            
            self.gui._jack_client.transport_stop()
            self.gui._jack_client.transport_locate(0)  

        if self.list.currentRow() != -1:
            device = self.gui.devices[self.list.currentRow() + 1]
            self.gui.learn_device = LearnDialog(self.gui,
                                                self.updateDevice,
                                                device)
            self.gui.is_learn_device_mode = True
            self.gui.update()



    def onDelete(self):
        if self.list.currentRow() != -1:
            response = QMessageBox.question(self, "Delete MIDI configuration?", "Are you sure you want to delete this MIDI configuration?")
            if response == QMessageBox.No:
                return

            device = self.gui.devices[self.list.currentRow() + 1]
            self.gui.devices.remove(device)
            self.list.takeItem(self.list.currentRow())



    def onImport(self):
        file_name, a = self.gui.getOpenFileName('Import MIDI configuration',
                                                common.DEVICE_MAPPING_TYPE,
                                                self)
        with open(file_name, 'r') as f:
            read_data = f.read()
        mapping = json.loads(read_data)
        self.list.addItem(mapping['name'])
        self.gui.devices.append(Device(mapping))


    def onExport(self):
        device = self.gui.devices[self.list.currentRow() + 1]
        file_name, a = self.gui.getSaveFileName('Export MIDI configuration',
                                                common.DEVICE_MAPPING_TYPE,
                                                self)
        if file_name:
            file_name = verify_ext(file_name, common.DEVICE_MAPPING_EXT)
            with open(file_name, 'w') as f:
                f.write(json.dumps(device.mapping))


    def onFinished(self):
        self.gui.updateDevices()


    def updateDevice(self, device):
        self.updateDeviceList()

        self.gui.is_learn_device_mode = False
        self.gui.redraw()


    def updateDeviceList(self):
        self.list.clear()
        for device in self.gui.devices[1:]:
            self.list.addItem(device.name)


