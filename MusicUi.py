# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MusicUi.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(381, 216)
        self.Auto_music = QtWidgets.QLabel(Form)
        self.Auto_music.setEnabled(True)
        self.Auto_music.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.Auto_music.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Auto_music.setObjectName("Auto_music")
        self.ok_button = QtWidgets.QPushButton(Form)
        self.ok_button.setGeometry(QtCore.QRect(120, 150, 141, 51))
        self.ok_button.setObjectName("ok_button")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(7, 10, 367, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(215)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.open_button = QtWidgets.QPushButton(self.layoutWidget)
        self.open_button.setAutoRepeatDelay(300)
        self.open_button.setObjectName("open_button")
        self.horizontalLayout.addWidget(self.open_button)
        self.save_button = QtWidgets.QPushButton(self.layoutWidget)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout.addWidget(self.save_button)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(135, 78, 231, 16))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_tone = QtWidgets.QLabel(self.layoutWidget1)
        self.label_tone.setObjectName("label_tone")
        self.horizontalLayout_2.addWidget(self.label_tone)
        self.label_volume = QtWidgets.QLabel(self.layoutWidget1)
        self.label_volume.setObjectName("label_volume")
        self.horizontalLayout_2.addWidget(self.label_volume)
        self.label_speed = QtWidgets.QLabel(self.layoutWidget1)
        self.label_speed.setObjectName("label_speed")
        self.horizontalLayout_2.addWidget(self.label_speed)
        self.comboBox_select = QtWidgets.QComboBox(Form)
        self.comboBox_select.setGeometry(QtCore.QRect(20, 110, 101, 20))
        self.comboBox_select.setObjectName("comboBox_select")
        self.comboBox_select.addItem("")
        self.comboBox_select.addItem("")
        self.comboBox_select.addItem("")
        self.comboBox_select.addItem("")
        self.Box_tone = QtWidgets.QSpinBox(Form)
        self.Box_tone.setGeometry(QtCore.QRect(137, 110, 41, 20))
        self.Box_tone.setMaximum(15)
        self.Box_tone.setProperty("value", 5)
        self.Box_tone.setObjectName("Box_tone")
        self.Box_speed = QtWidgets.QSpinBox(Form)
        self.Box_speed.setGeometry(QtCore.QRect(292, 109, 41, 20))
        self.Box_speed.setMaximum(9)
        self.Box_speed.setProperty("value", 5)
        self.Box_speed.setObjectName("Box_speed")
        self.Box_volume = QtWidgets.QSpinBox(Form)
        self.Box_volume.setGeometry(QtCore.QRect(213, 110, 41, 20))
        self.Box_volume.setMaximum(9)
        self.Box_volume.setProperty("value", 5)
        self.Box_volume.setObjectName("Box_volume")
        self.label_people = QtWidgets.QLabel(Form)
        self.label_people.setGeometry(QtCore.QRect(30, 80, 36, 14))
        self.label_people.setObjectName("label_people")

        self.retranslateUi(Form)
        self.open_button.clicked.connect(Form.open_files)
        self.save_button.clicked.connect(Form.save_file)
        self.ok_button.clicked.connect(Form.start_compound)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Auto_music.setText(_translate("Form", "语音合成设置："))
        self.ok_button.setText(_translate("Form", "OK"))
        self.open_button.setText(_translate("Form", "Open"))
        self.save_button.setText(_translate("Form", "Save"))
        self.label_tone.setText(_translate("Form", "音调"))
        self.label_volume.setText(_translate("Form", "音量"))
        self.label_speed.setText(_translate("Form", "语速"))
        self.comboBox_select.setItemText(0, _translate("Form", "0   女声(默认)"))
        self.comboBox_select.setItemText(1, _translate("Form", "1   男声"))
        self.comboBox_select.setItemText(2, _translate("Form", "3   度逍遥"))
        self.comboBox_select.setItemText(3, _translate("Form", "4   度丫丫"))
        self.label_people.setText(_translate("Form", "发音人"))
