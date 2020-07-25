from PyQt5.QtWidgets import QDialog, QFileDialog, QAbstractItemView, QMessageBox
from superboucle.playlist_ui import Ui_Dialog
from superboucle.clip import verify_ext
#from superboucle.clip import load_song_from_file, verify_ext
import json
from os.path import basename, splitext
import settings
import common

class PlaylistDialog(QDialog, Ui_Dialog):
    
    current_song_id = None
    
    def __init__(self, parent):
        super(PlaylistDialog, self).__init__(parent)
        self.gui = parent
        self.setupUi(self)
        self.updateList()
        self.removeSongBtn.clicked.connect(self.onRemove)
        self.addSongsBtn.clicked.connect(self.onAddSongs)
        self.loadPlaylistBtn.clicked.connect(self.onLoadPlaylist)
        self.savePlaylistBtn.clicked.connect(self.onSavePlaylist)
        self.loadSongBtn.clicked.connect(self.onLoadSong)
        self.playlistList.itemDoubleClicked.connect(self.onSongDoubleClick)
        self.playlistList.setDragDropMode(QAbstractItemView.InternalMove)
        self.playlistList.model().rowsMoved.connect(self.onMoveRows)
        self.cBoxBigFonts.setChecked(settings.use_big_fonts_playlist)
        self.cBoxBigFonts.stateChanged.connect(self.onBigFonts)        
        
        self.geometry = settings.playlist_geometry
        
        if self.geometry:
            self.restoreGeometry(self.geometry)
        
        if self.isVisible() == False:
            self.show()

        self.useBigFonts(settings.use_big_fonts_playlist)
        
    def updateList(self):
        self.playlistList.clear()
        for i, song in enumerate(settings.playlist):
            name, ext = splitext(basename(song))  # song.file_name
            self.playlistList.addItem('{}. {}'.format(i + 1, name))

    def onRemove(self):
        response = QMessageBox.question(self, "Remove Song?", "Are you sure you want to remove this song from the playlist?")
        if response == QMessageBox.No:
            return

        id = self.playlistList.currentRow()
        if id != -1:
            del settings.playlist[id]
            self.updateList()

    def onMoveRows(self, sourceParent, sourceStart, sourceEnd,
                   destinationParent, destinationRow):
        l = settings.playlist
        destinationRow -= destinationRow > sourceStart
        l.insert(destinationRow, l.pop(sourceStart))
        self.updateList()

    def onAddSongs(self):
        file_names, a = self.gui.getOpenFileName('Add Songs',
                                                 common.SONG_FILE_TYPE,
                                                 self,
                                                 QFileDialog.getOpenFileNames)
        settings.playlist += file_names
        self.updateList()

    def onLoadPlaylist(self):

        file_name, a = self.gui.getOpenFileName('Import Playlist',
                                                    common.PLAYLIST_FILE_TYPE,
                                                    self)        
        if not file_name:
            return

        common.updateSettingsPlaylist(file_name, settings)
        self.updateList()

    def onSavePlaylist(self):
        file_name, a = self.gui.getSaveFileName('Export Playlist',
                                                common.PLAYLIST_FILE_TYPE,
                                                self)

        if file_name:
            file_name = verify_ext(file_name, 'sbp')
            with open(file_name, 'w') as f:
                f.write(json.dumps(settings.playlist))

    def onBigFonts(self):
        settings.use_big_fonts_playlist = self.cBoxBigFonts.isChecked()
        self.useBigFonts(settings.use_big_fonts_playlist)

    def onLoadSong(self):
        id = self.playlistList.currentRow()
        self.loadSong(id)

    def onSongDoubleClick(self, item):
        id = self.playlistList.row(item)
        self.loadSong(id)

    def loadSong(self, id):
        if id == -1:
            return
        file_name = settings.playlist[id]
        try:
            self.gui.openSongFromDisk(file_name)
            # self.current_song_id = id
        except Exception as e:
            print("could not load File {}.\nError: {}".format(file_name, e))
    

    def useBigFonts(self, use = False):
        self.bigFontSize = settings.bigFontSize

        if use == False:
            stylesheet = 'font: 10pt "Noto Sans";'
        else:
            stylesheet = 'font: bold ' + str(self.bigFontSize) + 'pt "Noto Sans";'
         
        self.playlistList.setStyleSheet(stylesheet)
       
    # saving window position
    
    def resizeEvent(self, event):
        self.geometry = self.saveGeometry()
        settings.playlist_geometry = self.geometry

    def moveEvent(self, event):
        self.geometry = self.saveGeometry()
        settings.playlist_geometry = self.geometry
    
    def hideEvent(self, event):
        self.gui.actionPlaylist_Editor.setEnabled(True)
