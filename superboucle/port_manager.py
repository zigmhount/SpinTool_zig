from PyQt5.QtWidgets import QDialog, QListWidgetItem, QMessageBox
from superboucle.port_manager_ui import Ui_Dialog
from superboucle.add_port import AddPortDialog
from superboucle.clip import verify_ext, Clip
import json
import settings
import common

class PortManager(QDialog, Ui_Dialog):
    def __init__(self, parent):
        super(PortManager, self).__init__(parent)
        self.gui = parent
        self.setupUi(self)
        self.backup_indixes = []
        self.updateList()
        self.removePortBtn.clicked.connect(self.onRemove)
        self.addPortBtn.clicked.connect(self.onAddPort)
        self.loadPortlistBtn.clicked.connect(self.onLoadPortlist)
        self.savePortlistBtn.clicked.connect(self.onSavePortlist)
        self.autoconnectCBox.setChecked(settings.auto_connect_output)
        self.autoconnectCBox.stateChanged.connect(self.onCheckAutoconnect)
        self.finished.connect(self.onFinished)

        self.gui.updatePorts.connect(self.updateList)

        self.show()

    def updateList(self):
        self.portList.clear()
        self.backup_indixes = common.toPortsList(settings.output_ports)
        for name in self.backup_indixes:
            this_item = QListWidgetItem(name)
            this_item.setFlags(this_item.flags())
            self.portList.addItem(this_item)

    def onAddPort(self):
        AddPortDialog(self.gui, callback=self.updateList)

    def onRemove(self):
        response = QMessageBox.question(self, "Delete Port?", "Are you sure you want to delete this output port?")
        if response == QMessageBox.No:
            return

        currentItem = self.portList.currentItem()

        if currentItem:

            port_name = currentItem.text()

            if port_name == common.DEFAULT_PORT:

                message = QMessageBox(self)
                message.setWindowTitle("Can't remove port " + port_name)
                message.setText("It's not possible to remove this port since it's \n" +
                                "default clips output port")
                message.show()
                return

            # This condition should NEVER happen; however I keep the control here.
            if self.portList.count() == 1:

                message = QMessageBox(self)
                message.setWindowTitle("Can't remove port " + port_name)
                message.setText("SpinTool must have at least one output port defined \n" +
                                "therefore it's not possible to remove this port")
                message.show()
                return

            self.gui.removePort(port_name)
            self.updateList()


    def onLoadPortlist(self):
        file_name, a = (self.gui.getOpenFileName('Open Portlist', common.PORTLIST_FILE_TYPE, self))
        if not file_name:
            return

        result = QMessageBox.question(self,
                                      "JACK output ports",
                                      "Do you want to preserve connections, if some port already exixst? \n" +
                                      "If you choose 'No', existing ports will be reloaded and connections to these ports will be lost.",
                                      QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        if result == QMessageBox.Cancel:
            return

        with open(file_name, 'r') as f:
            read_data = f.read()
        data = json.loads(read_data)

        ports = data["outputs"]  # Getting from JSON data the output ports (set or list)
        settings.output_ports = common.toPortsDict(ports)

        # Updating Jack connections and Mixer layout
        # user could choose if deleting and creating from scratch all jack output ports,
        # or keeping existing jack output ports to preserve their connections
        if result == QMessageBox.Yes:
            common.updateOutputPorts(settings.output_ports, self.gui._jack_client)

        elif result == QMessageBox.No:
            common.createOutputPorts(settings.output_ports, self.gui._jack_client)


        self.gui.updatePorts.emit()
        if self.gui.output_mixer:
            self.gui.output_mixer.updateGui(settings.output_ports)

    def onSavePortlist(self):
        file_name, a = (self.gui.getSaveFileName('Save Portlist', common.PORTLIST_FILE_TYPE, self))

        if file_name:
            file_name = verify_ext(file_name, 'sbl')

            with open(file_name, 'w') as f:
                #data = {"clips": [[c.output if isinstance(c, Clip) else common.DEFAULT_PORT
                #        for c in cliprow] for cliprow in self.gui.song.clips_matrix],
                #        "outputs": common.toPortsList(settings.output_ports)}

                data = {"outputs": common.toPortsList(settings.output_ports)}

                f.write(json.dumps(data))

    def onCheckAutoconnect(self):
        settings.auto_connect_output = self.autoconnectCBox.isChecked()

    def hideEvent(self, event):
        self.gui.actionPort_Manager.setEnabled(True)

    def onFinished(self):
        pass
