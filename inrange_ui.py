# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inrange_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ObjcetFilter(object):
    def setupUi(self, ObjcetFilter):
        ObjcetFilter.setObjectName("ObjcetFilter")
        ObjcetFilter.resize(1679, 956)
        self.centralwidget = QtWidgets.QWidget(ObjcetFilter)
        self.centralwidget.setObjectName("centralwidget")
        self.SliderLR = QtWidgets.QSlider(self.centralwidget)
        self.SliderLR.setEnabled(False)
        self.SliderLR.setGeometry(QtCore.QRect(35, 40, 165, 24))
        self.SliderLR.setMaximum(255)
        self.SliderLR.setOrientation(QtCore.Qt.Horizontal)
        self.SliderLR.setObjectName("SliderLR")
        self.ImageArea = QtWidgets.QLabel(self.centralwidget)
        self.ImageArea.setGeometry(QtCore.QRect(10, 129, 1661, 801))
        self.ImageArea.setText("")
        self.ImageArea.setObjectName("ImageArea")
        self.spinBoxLR = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxLR.setEnabled(False)
        self.spinBoxLR.setGeometry(QtCore.QRect(210, 40, 48, 24))
        self.spinBoxLR.setMaximum(255)
        self.spinBoxLR.setObjectName("spinBoxLR")
        self.spinBoxLG = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxLG.setEnabled(False)
        self.spinBoxLG.setGeometry(QtCore.QRect(210, 70, 48, 24))
        self.spinBoxLG.setMaximum(255)
        self.spinBoxLG.setObjectName("spinBoxLG")
        self.SliderLG = QtWidgets.QSlider(self.centralwidget)
        self.SliderLG.setEnabled(False)
        self.SliderLG.setGeometry(QtCore.QRect(35, 70, 165, 24))
        self.SliderLG.setMaximum(255)
        self.SliderLG.setOrientation(QtCore.Qt.Horizontal)
        self.SliderLG.setObjectName("SliderLG")
        self.spinBoxLB = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxLB.setEnabled(False)
        self.spinBoxLB.setGeometry(QtCore.QRect(210, 100, 48, 24))
        self.spinBoxLB.setMaximum(255)
        self.spinBoxLB.setObjectName("spinBoxLB")
        self.SliderLB = QtWidgets.QSlider(self.centralwidget)
        self.SliderLB.setEnabled(False)
        self.SliderLB.setGeometry(QtCore.QRect(35, 100, 165, 24))
        self.SliderLB.setMaximum(255)
        self.SliderLB.setOrientation(QtCore.Qt.Horizontal)
        self.SliderLB.setObjectName("SliderLB")
        self.NewConfigBtn = QtWidgets.QPushButton(self.centralwidget)
        self.NewConfigBtn.setEnabled(False)
        self.NewConfigBtn.setGeometry(QtCore.QRect(580, 40, 361, 32))
        self.NewConfigBtn.setObjectName("NewConfigBtn")
        self.SaveConfigBtn = QtWidgets.QPushButton(self.centralwidget)
        self.SaveConfigBtn.setEnabled(False)
        self.SaveConfigBtn.setGeometry(QtCore.QRect(585, 100, 171, 32))
        self.SaveConfigBtn.setObjectName("SaveConfigBtn")
        self.ConfigNameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.ConfigNameInput.setEnabled(False)
        self.ConfigNameInput.setGeometry(QtCore.QRect(680, 70, 151, 21))
        self.ConfigNameInput.setObjectName("ConfigNameInput")
        self.ConfigNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.ConfigNameLabel.setGeometry(QtCore.QRect(584, 70, 81, 20))
        self.ConfigNameLabel.setObjectName("ConfigNameLabel")
        self.LabelLR = QtWidgets.QLabel(self.centralwidget)
        self.LabelLR.setGeometry(QtCore.QRect(10, 40, 20, 20))
        self.LabelLR.setObjectName("LabelLR")
        self.LabelLG = QtWidgets.QLabel(self.centralwidget)
        self.LabelLG.setGeometry(QtCore.QRect(10, 70, 20, 20))
        self.LabelLG.setObjectName("LabelLG")
        self.LabelLB = QtWidgets.QLabel(self.centralwidget)
        self.LabelLB.setGeometry(QtCore.QRect(10, 100, 20, 20))
        self.LabelLB.setObjectName("LabelLB")
        self.FilePathInput = QtWidgets.QLineEdit(self.centralwidget)
        self.FilePathInput.setGeometry(QtCore.QRect(82, 15, 751, 21))
        self.FilePathInput.setObjectName("FilePathInput")
        self.FilePathLabel = QtWidgets.QLabel(self.centralwidget)
        self.FilePathLabel.setGeometry(QtCore.QRect(10, 15, 60, 21))
        self.FilePathLabel.setObjectName("FilePathLabel")
        self.LoadFileBtn = QtWidgets.QPushButton(self.centralwidget)
        self.LoadFileBtn.setGeometry(QtCore.QRect(840, 10, 101, 32))
        self.LoadFileBtn.setObjectName("LoadFileBtn")
        self.LabelHB = QtWidgets.QLabel(self.centralwidget)
        self.LabelHB.setGeometry(QtCore.QRect(285, 100, 20, 20))
        self.LabelHB.setObjectName("LabelHB")
        self.SliderHG = QtWidgets.QSlider(self.centralwidget)
        self.SliderHG.setEnabled(False)
        self.SliderHG.setGeometry(QtCore.QRect(310, 70, 165, 24))
        self.SliderHG.setMaximum(255)
        self.SliderHG.setOrientation(QtCore.Qt.Horizontal)
        self.SliderHG.setObjectName("SliderHG")
        self.spinBoxHR = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxHR.setEnabled(False)
        self.spinBoxHR.setGeometry(QtCore.QRect(485, 40, 48, 24))
        self.spinBoxHR.setMaximum(255)
        self.spinBoxHR.setObjectName("spinBoxHR")
        self.spinBoxHB = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxHB.setEnabled(False)
        self.spinBoxHB.setGeometry(QtCore.QRect(485, 100, 48, 24))
        self.spinBoxHB.setMaximum(255)
        self.spinBoxHB.setObjectName("spinBoxHB")
        self.LabelHG = QtWidgets.QLabel(self.centralwidget)
        self.LabelHG.setGeometry(QtCore.QRect(285, 70, 20, 20))
        self.LabelHG.setObjectName("LabelHG")
        self.spinBoxHG = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxHG.setEnabled(False)
        self.spinBoxHG.setGeometry(QtCore.QRect(485, 70, 48, 24))
        self.spinBoxHG.setMaximum(255)
        self.spinBoxHG.setObjectName("spinBoxHG")
        self.SliderHR = QtWidgets.QSlider(self.centralwidget)
        self.SliderHR.setEnabled(False)
        self.SliderHR.setGeometry(QtCore.QRect(310, 40, 165, 24))
        self.SliderHR.setMaximum(255)
        self.SliderHR.setOrientation(QtCore.Qt.Horizontal)
        self.SliderHR.setObjectName("SliderHR")
        self.LabelHR = QtWidgets.QLabel(self.centralwidget)
        self.LabelHR.setGeometry(QtCore.QRect(285, 40, 20, 20))
        self.LabelHR.setObjectName("LabelHR")
        self.SliderHB = QtWidgets.QSlider(self.centralwidget)
        self.SliderHB.setEnabled(False)
        self.SliderHB.setGeometry(QtCore.QRect(310, 100, 165, 24))
        self.SliderHB.setMaximum(255)
        self.SliderHB.setOrientation(QtCore.Qt.Horizontal)
        self.SliderHB.setObjectName("SliderHB")
        self.RenameConfigBtn = QtWidgets.QPushButton(self.centralwidget)
        self.RenameConfigBtn.setEnabled(False)
        self.RenameConfigBtn.setGeometry(QtCore.QRect(840, 66, 101, 32))
        self.RenameConfigBtn.setObjectName("RenameConfigBtn")
        self.DeleteConfigBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteConfigBtn.setEnabled(False)
        self.DeleteConfigBtn.setGeometry(QtCore.QRect(770, 100, 171, 32))
        self.DeleteConfigBtn.setObjectName("DeleteConfigBtn")
        self.ConfigListView = QtWidgets.QListView(self.centralwidget)
        self.ConfigListView.setGeometry(QtCore.QRect(940, 10, 221, 121))
        self.ConfigListView.setObjectName("ConfigListView")
        ObjcetFilter.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ObjcetFilter)
        self.statusbar.setObjectName("statusbar")
        ObjcetFilter.setStatusBar(self.statusbar)

        self.retranslateUi(ObjcetFilter)
        QtCore.QMetaObject.connectSlotsByName(ObjcetFilter)

    def retranslateUi(self, ObjcetFilter):
        _translate = QtCore.QCoreApplication.translate
        ObjcetFilter.setWindowTitle(_translate("ObjcetFilter", "Object Filter"))
        self.NewConfigBtn.setText(_translate("ObjcetFilter", "New Config"))
        self.SaveConfigBtn.setText(_translate("ObjcetFilter", "Save"))
        self.ConfigNameLabel.setText(_translate("ObjcetFilter", "Config Name"))
        self.LabelLR.setText(_translate("ObjcetFilter", "LR"))
        self.LabelLG.setText(_translate("ObjcetFilter", "LG"))
        self.LabelLB.setText(_translate("ObjcetFilter", "LB"))
        self.FilePathLabel.setText(_translate("ObjcetFilter", "File Path"))
        self.LoadFileBtn.setText(_translate("ObjcetFilter", "Load"))
        self.LabelHB.setText(_translate("ObjcetFilter", "HB"))
        self.LabelHG.setText(_translate("ObjcetFilter", "HG"))
        self.LabelHR.setText(_translate("ObjcetFilter", "HR"))
        self.RenameConfigBtn.setText(_translate("ObjcetFilter", "Rename"))
        self.DeleteConfigBtn.setText(_translate("ObjcetFilter", "Delete"))
