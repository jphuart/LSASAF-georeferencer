# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_HDF5Georeferencer.ui'
#
# Created: Wed Aug 17 13:57:54 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(491, 569)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_6.addWidget(self.label)
        self.inputFilesLE = QtGui.QLineEdit(Form)
        self.inputFilesLE.setObjectName(_fromUtf8("inputFilesLE"))
        self.horizontalLayout_6.addWidget(self.inputFilesLE)
        self.inputFilesPB = QtGui.QPushButton(Form)
        self.inputFilesPB.setObjectName(_fromUtf8("inputFilesPB"))
        self.horizontalLayout_6.addWidget(self.inputFilesPB)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.loadFilePB = QtGui.QPushButton(Form)
        self.loadFilePB.setObjectName(_fromUtf8("loadFilePB"))
        self.horizontalLayout_7.addWidget(self.loadFilePB)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.datasetsLW = QtGui.QListWidget(Form)
        self.datasetsLW.setObjectName(_fromUtf8("datasetsLW"))
        self.verticalLayout.addWidget(self.datasetsLW)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.wgs84RB = QtGui.QRadioButton(Form)
        self.wgs84RB.setObjectName(_fromUtf8("wgs84RB"))
        self.horizontalLayout_8.addWidget(self.wgs84RB)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.customProjRB = QtGui.QRadioButton(Form)
        self.customProjRB.setObjectName(_fromUtf8("customProjRB"))
        self.horizontalLayout_9.addWidget(self.customProjRB)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.customProjectionTE = QtGui.QTextEdit(Form)
        self.customProjectionTE.setObjectName(_fromUtf8("customProjectionTE"))
        self.verticalLayout.addWidget(self.customProjectionTE)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.outputDirLE = QtGui.QLineEdit(Form)
        self.outputDirLE.setObjectName(_fromUtf8("outputDirLE"))
        self.horizontalLayout_3.addWidget(self.outputDirLE)
        self.outputDirPB = QtGui.QPushButton(Form)
        self.outputDirPB.setObjectName(_fromUtf8("outputDirPB"))
        self.horizontalLayout_3.addWidget(self.outputDirPB)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.deleteIntermediaryCB = QtGui.QCheckBox(Form)
        self.deleteIntermediaryCB.setObjectName(_fromUtf8("deleteIntermediaryCB"))
        self.horizontalLayout_2.addWidget(self.deleteIntermediaryCB)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setProperty(_fromUtf8("value"), 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.helpPB = QtGui.QPushButton(Form)
        self.helpPB.setObjectName(_fromUtf8("helpPB"))
        self.horizontalLayout.addWidget(self.helpPB)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.processFilesPB = QtGui.QPushButton(Form)
        self.processFilesPB.setObjectName(_fromUtf8("processFilesPB"))
        self.horizontalLayout.addWidget(self.processFilesPB)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label.setBuddy(self.inputFilesLE)
        self.label_3.setBuddy(self.outputDirLE)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.inputFilesLE, self.inputFilesPB)
        Form.setTabOrder(self.inputFilesPB, self.loadFilePB)
        Form.setTabOrder(self.loadFilePB, self.wgs84RB)
        Form.setTabOrder(self.wgs84RB, self.customProjRB)
        Form.setTabOrder(self.customProjRB, self.customProjectionTE)
        Form.setTabOrder(self.customProjectionTE, self.outputDirLE)
        Form.setTabOrder(self.outputDirLE, self.outputDirPB)
        Form.setTabOrder(self.outputDirPB, self.deleteIntermediaryCB)
        Form.setTabOrder(self.deleteIntermediaryCB, self.processFilesPB)
        Form.setTabOrder(self.processFilesPB, self.helpPB)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "HDF5 Georeferencer", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "HDF5 files", None, QtGui.QApplication.UnicodeUTF8))
        self.inputFilesPB.setText(QtGui.QApplication.translate("Form", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.loadFilePB.setText(QtGui.QApplication.translate("Form", "Load File(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Select dataset(s) to use", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Output projection string", None, QtGui.QApplication.UnicodeUTF8))
        self.wgs84RB.setText(QtGui.QApplication.translate("Form", "WGS84 (lat long)", None, QtGui.QApplication.UnicodeUTF8))
        self.customProjRB.setText(QtGui.QApplication.translate("Form", "Specify custom projection (use any Proj4 format)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Output directory", None, QtGui.QApplication.UnicodeUTF8))
        self.outputDirPB.setText(QtGui.QApplication.translate("Form", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteIntermediaryCB.setText(QtGui.QApplication.translate("Form", "Delete intermediary files", None, QtGui.QApplication.UnicodeUTF8))
        self.helpPB.setText(QtGui.QApplication.translate("Form", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.processFilesPB.setText(QtGui.QApplication.translate("Form", "Process files", None, QtGui.QApplication.UnicodeUTF8))
