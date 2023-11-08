

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QTextEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView  # Import QWebEngineView
from PyQt5.QtCore import QUrl  # Import QUrl
from pytube import YouTube
class MainApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("YouTube Video Previewer")
        self.setGeometry(100, 100, 400, 200)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.url_input = QTextEdit()
        self.layout.addWidget(self.url_input)

        self.preview_button = QPushButton("Preview")
        self.preview_button.clicked.connect(self.open_preview_window)
        self.layout.addWidget(self.preview_button)

    def open_preview_window(self):
        url = self.url_input.toPlainText().strip()
        if not url:
            return

        self.preview_window = PreviewWindow(url)
        self.preview_window.show()

class PreviewWindow(QWidget):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.initUI()

    def initUI(self):
        self.setWindowTitle("YouTube Video Preview")
        self.setGeometry(200, 200, 640, 360)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.web_view = QWebEngineView()
        self.layout.addWidget(self.web_view)

        self.web_view.setUrl(QUrl(self.url))

def main():
    app = QApplication(sys.argv)
    window = MainApplication()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
