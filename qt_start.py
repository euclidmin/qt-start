import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui
# from PyQt5 import uic
from PySide2.QtWidgets import QMainWindow, QWidget
# import pyside2uic.QtDesigner
from color_ui import Ui_Form

# color_set_form_class = uic.loadUiType("color_se1.ui")[0]
#
#
#
# class MyWidget(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
#
#         self.button = QtWidgets.QPushButton("click me!")
#         self.text = QtWidgets.QLabel("Hello world")
#         self.text.setAlignment(QtCore.Qt.AlignCenter)
#
#         self.layout = QtWidgets.QVBoxLayout()
#         self.layout.addWidget(self.text)
#         self.layout.addWidget(self.button)
#         self.setLayout(self.layout)
#
#         self.button.clicked.connect(self.magic)
#
#     def magic(self):
#         self.text.setText(random.choice(self.hello))



class ColorForm(QMainWindow, Ui_Form):
    def __init__(self):
        super(ColorForm, self).__init__()
        self.setupUi(self)



if __name__=="__main__":
    app = QtWidgets.QApplication([])

    # widget = MyWidget()
    # widget.resize(800, 600)
    # widget.show()

    main_window = QWidget()
    ui = Ui_Form()
    # ui = color_set_form_class
    ui.setupUi(main_window)
    main_window.show()
    #
    # color_form = ColorForm()
    # # color_form.__init__()
    # # color_form.resize(800, 800)
    # color_form.show()
    sys.exit(app.exec_())

