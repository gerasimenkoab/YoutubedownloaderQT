from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget, QTextEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView  # Import QWebEngineView
from PyQt5.QtCore import QUrl  # Import QUrl

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 220)
        MainWindow.setMinimumSize(QtCore.QSize(640, 220))
        MainWindow.setMaximumSize(QtCore.QSize(640, 220))
        self.mainWidget = QtWidgets.QWidget(parent=MainWindow)
        self.mainWidget.setObjectName("mainWidget")
        self.infoFrame = QtWidgets.QFrame(parent=self.mainWidget)
        self.infoFrame.setGeometry(QtCore.QRect(0, 0, 531, 171))
        self.infoFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.infoFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.infoFrame.setObjectName("infoFrame")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.infoFrame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 531, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(5, 2, 2, 2)
        self.gridLayout.setObjectName("gridLayout")
        self.optionsListLabel = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.optionsListLabel.setObjectName("optionsListLabel")
        self.gridLayout.addWidget(self.optionsListLabel, 3, 0, 1, 1)
        self.optionsList = QtWidgets.QListWidget(parent=self.gridLayoutWidget)
        self.optionsList.setMaximumSize(QtCore.QSize(500, 100))
        self.optionsList.setObjectName("optionsList")
        self.gridLayout.addWidget(self.optionsList, 3, 1, 1, 1)
        self.urlLabel = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.urlLabel.sizePolicy().hasHeightForWidth())

        self.urlLabel.setSizePolicy(sizePolicy)
        self.urlLabel.setMaximumSize(QtCore.QSize(20, 30))
        self.urlLabel.setObjectName("urlLabel")
        self.gridLayout.addWidget(self.urlLabel, 0, 0, 1, 1)
        self.urlText = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.urlText.setObjectName("urlText")
        self.gridLayout.addWidget(self.urlText, 0, 1, 1, 1)

        self.loadProgressBar = QtWidgets.QProgressBar(parent=self.mainWidget)
        self.loadProgressBar.setGeometry(QtCore.QRect(10, 180, 611, 16))
        self.loadProgressBar.setProperty("value", 0)
        self.loadProgressBar.setObjectName("loadProgressBar")

        self.buttonsFrame = QtWidgets.QFrame(parent=self.mainWidget)
        self.buttonsFrame.setGeometry(QtCore.QRect(530, 0, 111, 171))
        self.buttonsFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.buttonsFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.buttonsFrame.setObjectName("buttonsFrame")

        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.buttonsFrame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 101, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")

        self.getInfoButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.getInfoButton.setObjectName("getInfoButton")
        self.verticalLayout.addWidget(self.getInfoButton)

        self.preview_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.preview_button.setObjectName("Preview")
        self.verticalLayout.addWidget(self.preview_button)

        self.downloadButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.downloadButton.setObjectName("downloadButton")
        self.verticalLayout.addWidget(self.downloadButton)

        self.closeButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout.addWidget(self.closeButton)
        MainWindow.setCentralWidget(self.mainWidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YTD"))
        self.optionsListLabel.setText(_translate("MainWindow", "Options:"))
        self.urlLabel.setText(_translate("MainWindow", "URL:"))
        self.getInfoButton.setText(_translate("MainWindow", "Get URL Info"))
        self.preview_button.setText( _translate("MainWindow", "Preview"))
        self.downloadButton.setText(_translate("MainWindow", "Download"))
        self.closeButton.setText(_translate("MainWindow", "Close"))

class ViewUI(Ui_MainWindow):
    def __init__(self, mainWindow = None):
        super().__init__()
        self.setupUi(mainWindow)

    def ShowStatusbarInfo(self, messageText = ''):
            self.statusbar.showMessage(messageText)

    def ListToListWidget(self, streamsList):
        for item in streamsList:
            QtWidgets.QListWidgetItem(str(item), self.optionsList)
        self.optionsList.setCurrentRow(0)

    def SaveAsDialog(self):
        return QtWidgets.QFileDialog.getSaveFileName( )
    

class PreviewWindow(QMainWindow):
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


