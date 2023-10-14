from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout,QPushButton, QGridLayout,QLineEdit
from PyQt5.QtWidgets import QGroupBox


def on_buttonYes():
    responseWidget.setText('Yes i like it!')

def on_buttonNo():
    responseWidget.setText('Nooooo!')

app = QApplication([])
app.setStyle('Fusion')
# app.setStyle('Windows')
window1 = QWidget()
window1.setWindowTitle('Test questionare')
# layout0 = QGridLayout(window1)
layout0 = QHBoxLayout(window1)

group1 = QGroupBox()
layout1_0 = QVBoxLayout()
text1 = QLineEdit('aaaa')
text2 = QLineEdit('bbb')
layout1_0.addWidget(text1)
layout1_0.addWidget(text2)
group1.setLayout(layout1_0)

group2 = QGroupBox()
layout1 = QVBoxLayout()
question = QLabel('Do you like Qt?')
layout1.addWidget(question)
buttonYes = QPushButton('Yes')
buttonNo = QPushButton('No')
layout1.addWidget(buttonYes)
layout1.addWidget(buttonNo)
responseWidget = QLabel('')
layout1.addWidget(responseWidget)
group2.setLayout(layout1)


layout0.addWidget(group1)
layout0.addWidget(group2)


buttonYes.clicked.connect(on_buttonYes)
buttonNo.clicked.connect(on_buttonNo)

window1.show()
app.exec()