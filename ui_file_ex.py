import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from PySide2.QtCore import QFile
from colorsettingwindow import Ui_ColorSettingWindow
from PySide2.QtUiTools import QUiLoader



class ColorSettingWindow(QMainWindow):
    def __init__(self):
        super(ColorSettingWindow, self).__init__()
        self.ui = Ui_ColorSettingWindow()
        self.ui.setupUi(self)
# app = QApplication(sys.argv)

def ui_class_loading():
    app = QApplication()

    main_window = QWidget()
    ui = Ui_ColorSettingWindow()
    ui.setupUi(main_window)
    main_window.show()

    # window = ColorSettingWindow()
    # window.show()

    sys.exit(app.exec_())

def direct_ui_loading():
    app = QApplication(sys.argv)

    ui_file = QFile("color_set_clear.ui")
    ui_file.open(QFile.ReadOnly)

    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    # ui_class_loading()
    direct_ui_loading()