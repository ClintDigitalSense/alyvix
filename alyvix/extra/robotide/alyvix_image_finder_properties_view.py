# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alyvix_image_finder_properties_view.ui'
#
# Created: Sat Sep 05 14:20:37 2015
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(583, 351)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(9, 10, 566, 303))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_design = QtGui.QWidget()
        self.tab_design.setObjectName(_fromUtf8("tab_design"))
        self.widget = QtGui.QWidget(self.tab_design)
        self.widget.setGeometry(QtCore.QRect(172, 9, 381, 254))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayoutWidget = QtGui.QWidget(self.widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 380, 242))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.timeout_spinbox = QtGui.QSpinBox(self.gridLayoutWidget)
        self.timeout_spinbox.setMaximum(999999)
        self.timeout_spinbox.setObjectName(_fromUtf8("timeout_spinbox"))
        self.gridLayout.addWidget(self.timeout_spinbox, 4, 3, 1, 1)
        self.inserttext = QtGui.QLineEdit(self.gridLayoutWidget)
        self.inserttext.setObjectName(_fromUtf8("inserttext"))
        self.gridLayout.addWidget(self.inserttext, 9, 0, 1, 4)
        self.clickRadio = QtGui.QRadioButton(self.gridLayoutWidget)
        self.clickRadio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.clickRadio.setObjectName(_fromUtf8("clickRadio"))
        self.buttonGroup_2 = QtGui.QButtonGroup(Form)
        self.buttonGroup_2.setObjectName(_fromUtf8("buttonGroup_2"))
        self.buttonGroup_2.addButton(self.clickRadio)
        self.gridLayout.addWidget(self.clickRadio, 7, 0, 1, 1)
        self.timeout_label = QtGui.QLabel(self.gridLayoutWidget)
        self.timeout_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.timeout_label.setObjectName(_fromUtf8("timeout_label"))
        self.gridLayout.addWidget(self.timeout_label, 4, 2, 1, 1)
        self.line_8 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.gridLayout.addWidget(self.line_8, 3, 0, 1, 4)
        self.wait_radio = QtGui.QRadioButton(self.gridLayoutWidget)
        self.wait_radio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.wait_radio.setChecked(True)
        self.wait_radio.setObjectName(_fromUtf8("wait_radio"))
        self.buttonGroup_5 = QtGui.QButtonGroup(Form)
        self.buttonGroup_5.setObjectName(_fromUtf8("buttonGroup_5"))
        self.buttonGroup_5.addButton(self.wait_radio)
        self.gridLayout.addWidget(self.wait_radio, 4, 1, 1, 1)
        self.doubleSpinBoxThreshold = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBoxThreshold.setMaximum(1.0)
        self.doubleSpinBoxThreshold.setSingleStep(0.05)
        self.doubleSpinBoxThreshold.setObjectName(_fromUtf8("doubleSpinBoxThreshold"))
        self.gridLayout.addWidget(self.doubleSpinBoxThreshold, 2, 3, 1, 1)
        self.line_3 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 4)
        self.line_10 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.gridLayout.addWidget(self.line_10, 6, 0, 1, 4)
        self.find_radio = QtGui.QRadioButton(self.gridLayoutWidget)
        self.find_radio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.find_radio.setObjectName(_fromUtf8("find_radio"))
        self.buttonGroup_5.addButton(self.find_radio)
        self.gridLayout.addWidget(self.find_radio, 4, 0, 1, 1)
        self.namelineedit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.namelineedit.setObjectName(_fromUtf8("namelineedit"))
        self.gridLayout.addWidget(self.namelineedit, 0, 0, 1, 4)
        self.threshold_label = QtGui.QLabel(self.gridLayoutWidget)
        self.threshold_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.threshold_label.setObjectName(_fromUtf8("threshold_label"))
        self.gridLayout.addWidget(self.threshold_label, 2, 0, 1, 3)
        self.rightclickRadio = QtGui.QRadioButton(self.gridLayoutWidget)
        self.rightclickRadio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.rightclickRadio.setObjectName(_fromUtf8("rightclickRadio"))
        self.buttonGroup_2.addButton(self.rightclickRadio)
        self.gridLayout.addWidget(self.rightclickRadio, 7, 1, 1, 1)
        self.timeout_exception = QtGui.QCheckBox(self.gridLayoutWidget)
        self.timeout_exception.setChecked(True)
        self.timeout_exception.setObjectName(_fromUtf8("timeout_exception"))
        self.gridLayout.addWidget(self.timeout_exception, 5, 3, 1, 1)
        self.dontclickRadio = QtGui.QRadioButton(self.gridLayoutWidget)
        self.dontclickRadio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.dontclickRadio.setChecked(True)
        self.dontclickRadio.setObjectName(_fromUtf8("dontclickRadio"))
        self.buttonGroup_2.addButton(self.dontclickRadio)
        self.gridLayout.addWidget(self.dontclickRadio, 8, 3, 1, 1)
        self.doubleclickRadio = QtGui.QRadioButton(self.gridLayoutWidget)
        self.doubleclickRadio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.doubleclickRadio.setObjectName(_fromUtf8("doubleclickRadio"))
        self.buttonGroup_2.addButton(self.doubleclickRadio)
        self.gridLayout.addWidget(self.doubleclickRadio, 7, 2, 1, 1)
        self.movemouseRadio = QtGui.QRadioButton(self.gridLayoutWidget)
        self.movemouseRadio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.movemouseRadio.setChecked(False)
        self.movemouseRadio.setObjectName(_fromUtf8("movemouseRadio"))
        self.buttonGroup_2.addButton(self.movemouseRadio)
        self.gridLayout.addWidget(self.movemouseRadio, 7, 3, 1, 1)
        self.add_quotes = QtGui.QCheckBox(self.gridLayoutWidget)
        self.add_quotes.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.add_quotes.setChecked(True)
        self.add_quotes.setObjectName(_fromUtf8("add_quotes"))
        self.gridLayout.addWidget(self.add_quotes, 10, 2, 1, 1)
        self.text_encrypted = QtGui.QCheckBox(self.gridLayoutWidget)
        self.text_encrypted.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.text_encrypted.setChecked(False)
        self.text_encrypted.setObjectName(_fromUtf8("text_encrypted"))
        self.gridLayout.addWidget(self.text_encrypted, 10, 3, 1, 1)
        self.listWidget = QtGui.QListWidget(self.tab_design)
        self.listWidget.setGeometry(QtCore.QRect(8, 9, 157, 261))
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.listWidget.addItem(item)
        self.widget_2 = QtGui.QWidget(self.tab_design)
        self.widget_2.setGeometry(QtCore.QRect(172, 310, 381, 235))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.widget_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 380, 229))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.roi_y_label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.roi_y_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.roi_y_label.setObjectName(_fromUtf8("roi_y_label"))
        self.gridLayout_2.addWidget(self.roi_y_label, 3, 2, 1, 1)
        self.roi_height_spinbox = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.roi_height_spinbox.setMaximum(9999)
        self.roi_height_spinbox.setObjectName(_fromUtf8("roi_height_spinbox"))
        self.gridLayout_2.addWidget(self.roi_height_spinbox, 4, 3, 1, 1)
        self.line_5 = QtGui.QFrame(self.gridLayoutWidget_2)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout_2.addWidget(self.line_5, 2, 0, 1, 4)
        self.roi_x_spinbox = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.roi_x_spinbox.setMinimum(-9999)
        self.roi_x_spinbox.setMaximum(9999)
        self.roi_x_spinbox.setObjectName(_fromUtf8("roi_x_spinbox"))
        self.gridLayout_2.addWidget(self.roi_x_spinbox, 3, 1, 1, 1)
        self.roi_x_label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.roi_x_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.roi_x_label.setObjectName(_fromUtf8("roi_x_label"))
        self.gridLayout_2.addWidget(self.roi_x_label, 3, 0, 1, 1)
        self.roi_y_spinbox = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.roi_y_spinbox.setMinimum(-9999)
        self.roi_y_spinbox.setMaximum(9999)
        self.roi_y_spinbox.setObjectName(_fromUtf8("roi_y_spinbox"))
        self.gridLayout_2.addWidget(self.roi_y_spinbox, 3, 3, 1, 1)
        self.roi_height_label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.roi_height_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.roi_height_label.setObjectName(_fromUtf8("roi_height_label"))
        self.gridLayout_2.addWidget(self.roi_height_label, 4, 2, 1, 1)
        self.roi_width_spinbox = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.roi_width_spinbox.setMaximum(9999)
        self.roi_width_spinbox.setObjectName(_fromUtf8("roi_width_spinbox"))
        self.gridLayout_2.addWidget(self.roi_width_spinbox, 4, 1, 1, 1)
        self.roi_width_label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.roi_width_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.roi_width_label.setObjectName(_fromUtf8("roi_width_label"))
        self.gridLayout_2.addWidget(self.roi_width_label, 4, 0, 1, 1)
        self.clickRadio_2 = QtGui.QRadioButton(self.gridLayoutWidget_2)
        self.clickRadio_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.clickRadio_2.setObjectName(_fromUtf8("clickRadio_2"))
        self.buttonGroup_4 = QtGui.QButtonGroup(Form)
        self.buttonGroup_4.setObjectName(_fromUtf8("buttonGroup_4"))
        self.buttonGroup_4.addButton(self.clickRadio_2)
        self.gridLayout_2.addWidget(self.clickRadio_2, 6, 0, 1, 1)
        self.doubleclickRadio_2 = QtGui.QRadioButton(self.gridLayoutWidget_2)
        self.doubleclickRadio_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.doubleclickRadio_2.setObjectName(_fromUtf8("doubleclickRadio_2"))
        self.buttonGroup_4.addButton(self.doubleclickRadio_2)
        self.gridLayout_2.addWidget(self.doubleclickRadio_2, 6, 2, 1, 1)
        self.line_7 = QtGui.QFrame(self.gridLayoutWidget_2)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.gridLayout_2.addWidget(self.line_7, 0, 0, 1, 4)
        self.line_9 = QtGui.QFrame(self.gridLayoutWidget_2)
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.gridLayout_2.addWidget(self.line_9, 5, 0, 1, 4)
        self.doubleSpinBoxThreshold_2 = QtGui.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBoxThreshold_2.setMaximum(1.0)
        self.doubleSpinBoxThreshold_2.setSingleStep(0.05)
        self.doubleSpinBoxThreshold_2.setObjectName(_fromUtf8("doubleSpinBoxThreshold_2"))
        self.gridLayout_2.addWidget(self.doubleSpinBoxThreshold_2, 1, 3, 1, 1)
        self.threshold_label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.threshold_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.threshold_label_2.setObjectName(_fromUtf8("threshold_label_2"))
        self.gridLayout_2.addWidget(self.threshold_label_2, 1, 0, 1, 3)
        self.movemouseRadio_2 = QtGui.QRadioButton(self.gridLayoutWidget_2)
        self.movemouseRadio_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.movemouseRadio_2.setChecked(False)
        self.movemouseRadio_2.setObjectName(_fromUtf8("movemouseRadio_2"))
        self.buttonGroup_4.addButton(self.movemouseRadio_2)
        self.gridLayout_2.addWidget(self.movemouseRadio_2, 6, 3, 1, 1)
        self.inserttext_2 = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.inserttext_2.setObjectName(_fromUtf8("inserttext_2"))
        self.gridLayout_2.addWidget(self.inserttext_2, 8, 0, 1, 4)
        self.rightclickRadio_2 = QtGui.QRadioButton(self.gridLayoutWidget_2)
        self.rightclickRadio_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.rightclickRadio_2.setObjectName(_fromUtf8("rightclickRadio_2"))
        self.buttonGroup_4.addButton(self.rightclickRadio_2)
        self.gridLayout_2.addWidget(self.rightclickRadio_2, 6, 1, 1, 1)
        self.dontclickRadio_2 = QtGui.QRadioButton(self.gridLayoutWidget_2)
        self.dontclickRadio_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.dontclickRadio_2.setChecked(True)
        self.dontclickRadio_2.setObjectName(_fromUtf8("dontclickRadio_2"))
        self.buttonGroup_4.addButton(self.dontclickRadio_2)
        self.gridLayout_2.addWidget(self.dontclickRadio_2, 7, 3, 1, 1)
        self.text_encrypted_2 = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.text_encrypted_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.text_encrypted_2.setChecked(False)
        self.text_encrypted_2.setObjectName(_fromUtf8("text_encrypted_2"))
        self.gridLayout_2.addWidget(self.text_encrypted_2, 9, 3, 1, 1)
        self.add_quotes_2 = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.add_quotes_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.add_quotes_2.setChecked(True)
        self.add_quotes_2.setObjectName(_fromUtf8("add_quotes_2"))
        self.gridLayout_2.addWidget(self.add_quotes_2, 9, 2, 1, 1)
        self.tabWidget.addTab(self.tab_design, _fromUtf8(""))
        self.tab_code = QtGui.QWidget()
        self.tab_code.setObjectName(_fromUtf8("tab_code"))
        self.spinBoxArgs = QtGui.QSpinBox(self.tab_code)
        self.spinBoxArgs.setGeometry(QtCore.QRect(68, 245, 60, 22))
        self.spinBoxArgs.setObjectName(_fromUtf8("spinBoxArgs"))
        self.labelArgs = QtGui.QLabel(self.tab_code)
        self.labelArgs.setGeometry(QtCore.QRect(10, 250, 46, 13))
        self.labelArgs.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelArgs.setObjectName(_fromUtf8("labelArgs"))
        self.tabWidget.addTab(self.tab_code, _fromUtf8(""))
        self.tab_customlines = QtGui.QWidget()
        self.tab_customlines.setObjectName(_fromUtf8("tab_customlines"))
        self.listWidgetBlocks = QtGui.QListWidget(self.tab_customlines)
        self.listWidgetBlocks.setGeometry(QtCore.QRect(472, 9, 81, 261))
        self.listWidgetBlocks.setObjectName(_fromUtf8("listWidgetBlocks"))
        self.textEditCustomLines = QtGui.QTextEdit(self.tab_customlines)
        self.textEditCustomLines.setGeometry(QtCore.QRect(8, 9, 456, 221))
        self.textEditCustomLines.setTabStopWidth(80)
        self.textEditCustomLines.setAcceptRichText(False)
        self.textEditCustomLines.setObjectName(_fromUtf8("textEditCustomLines"))
        self.pushButtonAddBlock = QtGui.QPushButton(self.tab_customlines)
        self.pushButtonAddBlock.setGeometry(QtCore.QRect(290, 243, 71, 23))
        self.pushButtonAddBlock.setObjectName(_fromUtf8("pushButtonAddBlock"))
        self.spinBoxLine = QtGui.QSpinBox(self.tab_customlines)
        self.spinBoxLine.setGeometry(QtCore.QRect(160, 243, 121, 22))
        self.spinBoxLine.setMinimum(1)
        self.spinBoxLine.setMaximum(99999)
        self.spinBoxLine.setObjectName(_fromUtf8("spinBoxLine"))
        self.label_line = QtGui.QLabel(self.tab_customlines)
        self.label_line.setGeometry(QtCore.QRect(90, 244, 61, 21))
        self.label_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_line.setObjectName(_fromUtf8("label_line"))
        self.pushButtonRemoveBlock = QtGui.QPushButton(self.tab_customlines)
        self.pushButtonRemoveBlock.setGeometry(QtCore.QRect(370, 243, 91, 23))
        self.pushButtonRemoveBlock.setObjectName(_fromUtf8("pushButtonRemoveBlock"))
        self.tabWidget.addTab(self.tab_customlines, _fromUtf8(""))
        self.tab_perfdata = QtGui.QWidget()
        self.tab_perfdata.setObjectName(_fromUtf8("tab_perfdata"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.tab_perfdata)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(19, 30, 497, 22))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.checkBoxEnablePerformance = QtGui.QCheckBox(self.gridLayoutWidget_3)
        self.checkBoxEnablePerformance.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBoxEnablePerformance.setChecked(True)
        self.checkBoxEnablePerformance.setObjectName(_fromUtf8("checkBoxEnablePerformance"))
        self.gridLayout_3.addWidget(self.checkBoxEnablePerformance, 0, 0, 1, 1)
        self.labelCritical = QtGui.QLabel(self.gridLayoutWidget_3)
        self.labelCritical.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelCritical.setObjectName(_fromUtf8("labelCritical"))
        self.gridLayout_3.addWidget(self.labelCritical, 0, 3, 1, 1)
        self.doubleSpinBoxWarning = QtGui.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.doubleSpinBoxWarning.setMaximum(9999.99)
        self.doubleSpinBoxWarning.setSingleStep(0.05)
        self.doubleSpinBoxWarning.setObjectName(_fromUtf8("doubleSpinBoxWarning"))
        self.gridLayout_3.addWidget(self.doubleSpinBoxWarning, 0, 2, 1, 1)
        self.labelWarning = QtGui.QLabel(self.gridLayoutWidget_3)
        self.labelWarning.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelWarning.setObjectName(_fromUtf8("labelWarning"))
        self.gridLayout_3.addWidget(self.labelWarning, 0, 1, 1, 1)
        self.doubleSpinBoxCritical = QtGui.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.doubleSpinBoxCritical.setMaximum(9999.99)
        self.doubleSpinBoxCritical.setSingleStep(0.05)
        self.doubleSpinBoxCritical.setObjectName(_fromUtf8("doubleSpinBoxCritical"))
        self.gridLayout_3.addWidget(self.doubleSpinBoxCritical, 0, 4, 1, 1)
        self.tabWidget.addTab(self.tab_perfdata, _fromUtf8(""))
        self.pushButtonOk = QtGui.QPushButton(Form)
        self.pushButtonOk.setGeometry(QtCore.QRect(411, 321, 75, 23))
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.pushButtonCancel = QtGui.QPushButton(Form)
        self.pushButtonCancel.setGeometry(QtCore.QRect(494, 321, 75, 23))
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Alyvix - Image Finder", None))
        self.inserttext.setText(_translate("Form", "Insert here the Keystroke to send", None))
        self.clickRadio.setText(_translate("Form", "Click", None))
        self.timeout_label.setText(_translate("Form", "Timeout", None))
        self.wait_radio.setText(_translate("Form", "Wait", None))
        self.find_radio.setText(_translate("Form", "Find", None))
        self.namelineedit.setText(_translate("Form", "Type here the name of the object", None))
        self.threshold_label.setText(_translate("Form", "Threshold", None))
        self.rightclickRadio.setText(_translate("Form", "Right Click", None))
        self.timeout_exception.setText(_translate("Form", "Exception", None))
        self.dontclickRadio.setText(_translate("Form", "Don\'t Click", None))
        self.doubleclickRadio.setText(_translate("Form", "Double Click", None))
        self.movemouseRadio.setText(_translate("Form", "Move", None))
        self.add_quotes.setText(_translate("Form", "Add Quotes", None))
        self.text_encrypted.setText(_translate("Form", "Is Encrypted", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "main_component", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.roi_y_label.setText(_translate("Form", "Roi Y", None))
        self.roi_x_label.setText(_translate("Form", "Roi X", None))
        self.roi_height_label.setText(_translate("Form", "Roi Height", None))
        self.roi_width_label.setText(_translate("Form", "Roi Width", None))
        self.clickRadio_2.setText(_translate("Form", "Click", None))
        self.doubleclickRadio_2.setText(_translate("Form", "Double Click", None))
        self.threshold_label_2.setText(_translate("Form", "Threshold", None))
        self.movemouseRadio_2.setText(_translate("Form", "Move", None))
        self.inserttext_2.setText(_translate("Form", "Insert here the Keystroke to send", None))
        self.rightclickRadio_2.setText(_translate("Form", "Right Click", None))
        self.dontclickRadio_2.setText(_translate("Form", "Don\'t Click", None))
        self.text_encrypted_2.setText(_translate("Form", "Is Encrypted", None))
        self.add_quotes_2.setText(_translate("Form", "Add Quotes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_design), _translate("Form", "Graphic Design", None))
        self.labelArgs.setText(_translate("Form", "Args", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_code), _translate("Form", "Source Code", None))
        self.pushButtonAddBlock.setText(_translate("Form", "Add Block", None))
        self.label_line.setText(_translate("Form", "Begin Line", None))
        self.pushButtonRemoveBlock.setText(_translate("Form", "Remove Block", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_customlines), _translate("Form", "Custom Lines", None))
        self.checkBoxEnablePerformance.setText(_translate("Form", "Enable Performance", None))
        self.labelCritical.setText(_translate("Form", "Critical", None))
        self.labelWarning.setText(_translate("Form", "Warning", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_perfdata), _translate("Form", "Performance Data", None))
        self.pushButtonOk.setText(_translate("Form", "Ok", None))
        self.pushButtonCancel.setText(_translate("Form", "Cancel", None))

