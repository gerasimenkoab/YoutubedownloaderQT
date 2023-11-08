#from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import validators # for URL text validation
import re
import sys

from pytube.exceptions import VideoUnavailable
from .model import ModelActions
from .view_ui import ViewUI, PreviewWindow


class ControllerMain():
    # def __init__(self, app_main = None):
    #     if app_main is None:
    #         self.app = QApplication(sys.argv)
    #         self.app.setStyle('Fusion')
    #         self.view.ShowStatusbarInfo('QApp created. Style Fusion')

    #     else:
    #         self.app = app_main


    def Run(self):
        self.app = QApplication(sys.argv)
        self.app.setStyle('Fusion')
        MainWindow = QMainWindow()
        self.view = ViewUI(MainWindow)
        self.view.ShowStatusbarInfo('QApp created. Style Fusion')
        MainWindow.show()
        self.model = ModelActions()
        self.BindActions()
        sys.exit(self.app.exec())
        

    def BindActions(self):
        self.view.getInfoButton.clicked.connect(self.GetInfo)
        self.view.downloadButton.clicked.connect(self.DownloadFile)
        self.view.preview_button.clicked.connect(self.open_preview_window)
        self.view.closeButton.clicked.connect(self.CloseApp)

    def open_preview_window(self):
        url = self.view.urlText.text()#self.url_input.toPlainText().strip()
        if not url:
            return

        self.preview_window = PreviewWindow(url)
        self.preview_window.show()

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
        self.model.yt.register_on_progress_callback( self.update_progress )
        dirPAth = self.view.SaveAsDialog()
        if dirPAth:
            pathSplit = dirPAth[0].rsplit('/',1)
            print("dirPath:",dirPAth, ' pathSplit: ', pathSplit)
            stream.download(output_path= pathSplit[0], filename=pathSplit[1] )

    def update_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        download_percentage = int(bytes_downloaded / total_size * 100)
        self.view.loadProgressBar.setValue(download_percentage)


    def CloseApp(self):
        self.app.quit()
