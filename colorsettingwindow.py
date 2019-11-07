# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'color_set.ui',
# licensing of 'color_set.ui' applies.
#
# Created: Mon Nov  4 17:48:45 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ColorSettingWindow(object):
    def setupUi(self, ColorSettingWindow):
        ColorSettingWindow.setObjectName("ColorSettingWindow")
        ColorSettingWindow.resize(748, 732)
        ColorSettingWindow.setMouseTracking(False)
        self.gridLayout_4 = QtWidgets.QGridLayout(ColorSettingWindow)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(ColorSettingWindow)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(ColorSettingWindow)
        self.spinBox.setMaximum(255)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 0, 1, 1)
        self.verticalSlider = QtWidgets.QSlider(ColorSettingWindow)
        self.verticalSlider.setMaximum(255)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout.addWidget(self.verticalSlider, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(ColorSettingWindow)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(ColorSettingWindow)
        self.spinBox_2.setMaximum(255)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_2.addWidget(self.spinBox_2, 1, 0, 1, 1)
        self.verticalSlider_2 = QtWidgets.QSlider(ColorSettingWindow)
        self.verticalSlider_2.setMaximum(255)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.gridLayout_2.addWidget(self.verticalSlider_2, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(ColorSettingWindow)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(ColorSettingWindow)
        self.spinBox_3.setMaximum(255)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout_3.addWidget(self.spinBox_3, 1, 0, 1, 1)
        self.verticalSlider_3 = QtWidgets.QSlider(ColorSettingWindow)
        self.verticalSlider_3.setMaximum(255)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.gridLayout_3.addWidget(self.verticalSlider_3, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(ColorSettingWindow)
        QtCore.QObject.connect(self.spinBox, QtCore.SIGNAL("valueChanged(int)"), self.verticalSlider.setValue)
        QtCore.QObject.connect(self.verticalSlider, QtCore.SIGNAL("valueChanged(int)"), self.spinBox.setValue)
        QtCore.QObject.connect(self.spinBox_2, QtCore.SIGNAL("valueChanged(int)"), self.verticalSlider_2.setValue)
        QtCore.QObject.connect(self.verticalSlider_2, QtCore.SIGNAL("valueChanged(int)"), self.spinBox_2.setValue)
        QtCore.QObject.connect(self.spinBox_3, QtCore.SIGNAL("valueChanged(int)"), self.verticalSlider_3.setValue)
        QtCore.QObject.connect(self.verticalSlider_3, QtCore.SIGNAL("valueChanged(int)"), self.spinBox_3.setValue)
        QtCore.QMetaObject.connectSlotsByName(ColorSettingWindow)

    def retranslateUi(self, ColorSettingWindow):
        ColorSettingWindow.setWindowTitle(QtWidgets.QApplication.translate("ColorSettingWindow", "color setting", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("ColorSettingWindow", "RED", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("ColorSettingWindow", "GREEN", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("ColorSettingWindow", "BLUE", None, -1))

