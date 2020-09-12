from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5 import uic
import os
import json

from src.fs_utils import FsUtils

class Settings(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent=parent) 
        uic.loadUi(FsUtils.get_resource("/ui/settings.ui"), self)
        self.pushChangeDirectory.clicked.connect(self.changeDictory)
        self.accepted.connect(self.saveSettings)

    def changeDictory(self):
        dlg = QFileDialog(self, "Pick a Books Directory", "~/")
        dlg.setFileMode(QFileDialog.FileMode.Directory)
        dlg.setOption(QFileDialog.ShowDirsOnly)
        dlg.fileSelected.connect(self.onDirectorySelected)
        dlg.exec()

    def onDirectorySelected(self, path):
        FsUtils.set_books_dir(path)

    def saveSettings(self):
        settings = FsUtils.get_resource("settings.json")
        with open(settings, 'w') as fp:
            json.dump({"books_path": FsUtils.book_path}, fp)