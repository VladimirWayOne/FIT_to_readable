# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './TR_mainframe.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TrainingResults(object):
    def setupUi(self, TrainingResults):
        TrainingResults.setObjectName("TrainingResults")
        TrainingResults.setEnabled(True)
        TrainingResults.resize(764, 411)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TrainingResults.sizePolicy().hasHeightForWidth())
        TrainingResults.setSizePolicy(sizePolicy)
        TrainingResults.setMinimumSize(QtCore.QSize(764, 411))
        TrainingResults.setMaximumSize(QtCore.QSize(764, 411))
        TrainingResults.setStyleSheet("background-color: rgb(213, 213, 213);")
        TrainingResults.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(TrainingResults)
        self.centralwidget.setObjectName("centralwidget")
        self.label_path_to_fit = QtWidgets.QLabel(self.centralwidget)
        self.label_path_to_fit.setGeometry(QtCore.QRect(40, 50, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_path_to_fit.setFont(font)
        self.label_path_to_fit.setObjectName("label_path_to_fit")
        self.text_path_to_fit = QtWidgets.QTextEdit(self.centralwidget)
        self.text_path_to_fit.setGeometry(QtCore.QRect(40, 70, 591, 31))
        self.text_path_to_fit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.text_path_to_fit.setObjectName("text_path_to_fit")
        self.btn_find_fit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_find_fit.setGeometry(QtCore.QRect(660, 70, 75, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_find_fit.setFont(font)
        self.btn_find_fit.setStyleSheet("background-color: rgba(0, 149, 255, 253);")
        self.btn_find_fit.setObjectName("btn_find_fit")
        self.label_path_to_save = QtWidgets.QLabel(self.centralwidget)
        self.label_path_to_save.setGeometry(QtCore.QRect(40, 230, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_path_to_save.setFont(font)
        self.label_path_to_save.setObjectName("label_path_to_save")
        self.text_path_to_save = QtWidgets.QTextEdit(self.centralwidget)
        self.text_path_to_save.setGeometry(QtCore.QRect(40, 250, 601, 31))
        self.text_path_to_save.setFocusPolicy(QtCore.Qt.NoFocus)
        self.text_path_to_save.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.text_path_to_save.setObjectName("text_path_to_save")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(660, 250, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save.setFont(font)
        self.btn_save.setStyleSheet("background-color: rgba(0, 149, 255, 253);")
        self.btn_save.setObjectName("btn_save")
        self.btn_txt = QtWidgets.QRadioButton(self.centralwidget)
        self.btn_txt.setGeometry(QtCore.QRect(50, 140, 171, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_txt.setFont(font)
        self.btn_txt.setMouseTracking(False)
        self.btn_txt.setAutoExclusive(False)
        self.btn_txt.setObjectName("btn_txt")
        self.btn_map = QtWidgets.QRadioButton(self.centralwidget)
        self.btn_map.setGeometry(QtCore.QRect(50, 190, 251, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_map.setFont(font)
        self.btn_map.setMouseTracking(False)
        self.btn_map.setAutoExclusive(False)
        self.btn_map.setObjectName("btn_map")
        self.btn_go = QtWidgets.QPushButton(self.centralwidget)
        self.btn_go.setGeometry(QtCore.QRect(340, 330, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_go.setFont(font)
        self.btn_go.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.btn_go.setObjectName("btn_go")
        TrainingResults.setCentralWidget(self.centralwidget)

        self.retranslateUi(TrainingResults)
        QtCore.QMetaObject.connectSlotsByName(TrainingResults)

    def retranslateUi(self, TrainingResults):
        _translate = QtCore.QCoreApplication.translate
        TrainingResults.setWindowTitle(_translate("TrainingResults", "Training Results"))
        self.label_path_to_fit.setText(_translate("TrainingResults", "Укажите путь к файлу"))
        self.btn_find_fit.setText(_translate("TrainingResults", "Загрузить"))
        self.label_path_to_save.setText(_translate("TrainingResults", "Сохранить результат в..."))
        self.btn_save.setText(_translate("TrainingResults", "Обзор"))
        self.btn_txt.setText(_translate("TrainingResults", "Создать txt-файл"))
        self.btn_map.setText(_translate("TrainingResults", "Создать html-файл трека"))
        self.btn_go.setText(_translate("TrainingResults", "GO"))
