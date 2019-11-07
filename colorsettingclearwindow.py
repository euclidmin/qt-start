# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'color_set_clear.ui',
# licensing of 'color_set_clear.ui' applies.
#
# Created: Mon Nov  4 18:45:53 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ColorSettingWindow(object):
    def setupUi(self, ColorSettingWindow):
        ColorSettingWindow.setObjectName("ColorSettingWindow")
        ColorSettingWindow.resize(606, 478)
        ColorSettingWindow.setMouseTracking(False)
        self.widget = QtWidgets.QWidget(ColorSettingWindow)
        self.widget.setGeometry(QtCore.QRect(171, 21, 331, 421))
        self.widget.setObjectName("widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(self.widget)
        self.spinBox.setMaximum(255)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_3.addWidget(self.spinBox)
        self.verticalSlider = QtWidgets.QSlider(self.widget)
        self.verticalSlider.setMaximum(255)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalLayout_3.addWidget(self.verticalSlider)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.spinBox_3 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_3.setMaximum(255)
        self.spinBox_3.setObjectName("spinBox_3")
        self.verticalLayout_4.addWidget(self.spinBox_3)
        self.verticalSlider_3 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_3.setMaximum(255)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.verticalLayout_4.addWidget(self.verticalSlider_3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.spinBox_2 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_2.setMaximum(255)
        self.spinBox_2.setObjectName("spinBox_2")
        self.verticalLayout_5.addWidget(self.spinBox_2)
        self.verticalSlider_2 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_2.setMaximum(255)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.verticalLayout_5.addWidget(self.verticalSlider_2)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_6.addWidget(self.pushButton)

        self.retranslateUi(ColorSettingWindow)
        QtCore.QObject.connect(self.spinBox, QtCore.SIGNAL("valueChanged(int)"), self.verticalSlider.setValue)
        QtCore.QObject.connect(self.verticalSlider, QtCore.SIGNAL("valueChanged(int)"), self.spinBox.setValue)
        QtCore.QObject.connect(self.spinBox_2, QtCore.SIGNAL("valueChanged(int)"), self.verticalSlider_2.setValue)
        QtCore.QObject.connect(self.verticalSlider_2, QtCore.SIGNAL("valueChanged(int)"), self.spinBox_2.setValue)
        QtCore.QObject.connect(self.spinBox_3, QtCore.SIGNAL("valueChanged(int)"), self.verticalSlider_3.setValue)
        QtCore.QObject.connect(self.verticalSlider_3, QtCore.SIGNAL("valueChanged(int)"), self.spinBox_3.setValue)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.spinBox_2.clear)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.spinBox.clear)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.spinBox_3.clear)
        QtCore.QMetaObject.connectSlotsByName(ColorSettingWindow)

    def retranslateUi(self, ColorSettingWindow):
        ColorSettingWindow.setWindowTitle(QtWidgets.QApplication.translate("ColorSettingWindow", "color setting", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("ColorSettingWindow", "RED", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("ColorSettingWindow", "BLUE", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("ColorSettingWindow", "GREEN", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("ColorSettingWindow", "PushButton", None, -1))

