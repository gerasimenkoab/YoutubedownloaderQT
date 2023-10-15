from PyQt6 import QtCore, QtGui, QtWidgets
import validators # for URL text validation
import re
import sys

from pytube.exceptions import VideoUnavailable
from .model import ModelActions
from .view_ui import ViewUI


class ControllerMain():
    def __init__(self, app_main = None):
        if app_main is None:
            self.app = QtWidgets.QApplication(sys.argv)
            self.app.setStyle('Fusion')
        else:
            self.app = app_main


    def Run(self):
        MainWindow = QtWidgets.QMainWindow()
        self.view = ViewUI(MainWindow)
        MainWindow.show()
        self.model = ModelActions()
        self.BindActions()
        sys.exit(self.app.exec())
        

    def BindActions(self):
        self.view.getInfoButton.clicked.connect(self.GetInfo)
        self.view.downloadButton.clicked.connect(self.DownloadFile)
        self.view.closeButton.clicked.connect(self.CloseApp)

    def GetInfo(self):
        try:
            url_link = self.view.urlText.text()
        except:
            self.view.ShowStatusbarInfo('Cant read URL input')
            return
        if not validators.url(url_link):
            self.view.ShowStatusbarInfo('Enter valid URL')
            return
        try:
            self.model.GetInfoFromURL(url_link)
        except VideoUnavailable:
            self.view.ShowStatusbarInfo(f'Video {url_link} is unavaialable.')
            return
        self.view.optionsList.clear()
        videoTitle = self.model.yt.title
        self.view.ShowStatusbarInfo(f'Got sources for: {videoTitle} from: {url_link}')
        thumbnail = self.model.yt.thumbnail_url
        streamsList = self.model.yt.streams
        self.view.ListToListWidget(streamsList)


    def DownloadFile(self):
        selectedStream = self.view.optionsList.currentItem().text()
        ### itag="([0-9]+)"    or   itag="(.*?)"   regex
        selectedTag = re.search( r'itag="([0-9]+)"' , selectedStream).group(1)
        stream  = self.model.GetStream(selectedTag)
        dirPAth = self.view.SaveAsDialog()
        if dirPAth:
            stream.download(output_path=dirPAth[0] )

    def CloseApp(self):
        self.app.quit()
