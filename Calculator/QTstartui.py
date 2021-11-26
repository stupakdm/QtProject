import sys
#from PyQt5 import QtWidgets
from PySide2 import QtWidgets
from Ui_MainWindow import UI_MainWindow
from PySide2 import QtCore

symbols = {
QtCore.Qt.Key_1:"1",
QtCore.Qt.Key_2:"2",
QtCore.Qt.Key_3:"3",
QtCore.Qt.Key_4:"4",
QtCore.Qt.Key_5:"5",
QtCore.Qt.Key_6:"6",
QtCore.Qt.Key_7:"7",
QtCore.Qt.Key_8:"8",
QtCore.Qt.Key_9:"9",
QtCore.Qt.Key_0:"0",
QtCore.Qt.Key_Period:"."}
oper = {
QtCore.Qt.Key_Plus:"+",
QtCore.Qt.Key_Minus:"-",
QtCore.Qt.Key_Asterisk:"*",
QtCore.Qt.Key_Slash:"/"}

class MainWindow(QtWidgets.QMainWindow, UI_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

    def keyPressEvent(self, event):
        if event.key() in symbols.keys():
            self.write_number(symbols[event.key()])
        if event.key() in oper.keys():
            self.basic_operations(oper[event.key()])
        if event.key() == QtCore.Qt.Key_Return:
            self.result()
        if event.key() == QtCore.Qt.Key_Delete or event.key() == QtCore.Qt.Key_Backspace:
            l = len(self.label_curr.text())
            if (l >1):
                self.label_curr.setText(self.label_curr.text()[0:l-1])
            else:
                self.label_curr.setText('0')
        if event.key() == QtCore.Qt.Key_Left or event.key() == QtCore.Qt.Key_A:
            self.turn_left()
        if event.key() == QtCore.Qt.Key_Right or event.key() == QtCore.Qt.Key_D:
            self.turn_right()
        if event.key() == QtCore.Qt.Key_C:
            self.clean()
        if event.key() == QtCore.Qt.Key_Z:
            self.reset()
        if event.key() ==  QtCore.Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
