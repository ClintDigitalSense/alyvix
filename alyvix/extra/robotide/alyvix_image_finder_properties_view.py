# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alyvix_image_finder_properties_view.ui'
#
# Created: Mon May 14 15:22:31 2018
#      by: PyQt4 UI code generator 4.10
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
        Form.resize(564, 499)
        self.pushButtonCancel = QtGui.QPushButton(Form)
        self.pushButtonCancel.setGeometry(QtCore.QRect(481, 470, 75, 23))
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.pushButtonOk = QtGui.QPushButton(Form)
        self.pushButtonOk.setGeometry(QtCore.QRect(398, 470, 75, 23))
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.label_line = QtGui.QLabel(Form)
        self.label_line.setGeometry(QtCore.QRect(100, 10000, 61, 21))
        self.label_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_line.setObjectName(_fromUtf8("label_line"))
        self.listWidgetBlocks = QtGui.QListWidget(Form)
        self.listWidgetBlocks.setGeometry(QtCore.QRect(482, 10000, 81, 261))
        self.listWidgetBlocks.setObjectName(_fromUtf8("listWidgetBlocks"))
        self.pushButtonAddBlock = QtGui.QPushButton(Form)
        self.pushButtonAddBlock.setGeometry(QtCore.QRect(300, 10000, 71, 23))
        self.pushButtonAddBlock.setObjectName(_fromUtf8("pushButtonAddBlock"))
        self.textEditCustomLines = QtGui.QTextEdit(Form)
        self.textEditCustomLines.setGeometry(QtCore.QRect(18, 10000, 456, 221))
        self.textEditCustomLines.setTabStopWidth(80)
        self.textEditCustomLines.setAcceptRichText(False)
        self.textEditCustomLines.setObjectName(_fromUtf8("textEditCustomLines"))
        self.pushButtonRemoveBlock = QtGui.QPushButton(Form)
        self.pushButtonRemoveBlock.setGeometry(QtCore.QRect(380, 10000, 91, 23))
        self.pushButtonRemoveBlock.setObjectName(_fromUtf8("pushButtonRemoveBlock"))
        self.spinBoxLine = QtGui.QSpinBox(Form)
        self.spinBoxLine.setGeometry(QtCore.QRect(170, 10000, 121, 22))
        self.spinBoxLine.setMinimum(1)
        self.spinBoxLine.setMaximum(99999)
        self.spinBoxLine.setObjectName(_fromUtf8("spinBoxLine"))
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(9, 9, 157, 419))
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.listWidget.addItem(item)
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(173, 9, 381, 451))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayoutWidget = QtGui.QWidget(self.widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 380, 441))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line_10 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.gridLayout.addWidget(self.line_10, 10, 0, 1, 4)
        self.threshold_label = QtGui.QLabel(self.gridLayoutWidget)
        self.threshold_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.threshold_label.setObjectName(_fromUtf8("threshold_label"))
        self.gridLayout.addWidget(self.threshold_label, 4, 0, 1, 3)
        self.wait_disapp_radio = QtGui.QRadioButton(self.gridLayoutWidget)
        self.wait_disapp_radio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.wait_disapp_radio.setChecked(False)
        self.wait_disapp_radio.setObjectName(_fromUtf8("wait_disapp_radio"))
        self.buttonGroup_5 = QtGui.QButtonGroup(Form)
        self.buttonGroup_5.setObjectName(_fromUtf8("buttonGroup_5"))
        self.buttonGroup_5.addButton(self.wait_disapp_radio)
        self.gridLayout.addWidget(self.wait_disapp_radio, 6, 3, 1, 1)
        self.checkBoxEnablePerformance = QtGui.QCheckBox(self.gridLayoutWidget)
        self.checkBoxEnablePerformance.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBoxEnablePerformance.setChecked(True)
        self.checkBoxEnablePerformance.setObjectName(_fromUtf8("checkBoxEnablePerformance"))
        self.gridLayout.addWidget(self.checkBoxEnablePerformance, 9, 2, 1, 2)
        self.timeout_spinbox = QtGui.QSpinBox(self.gridLayoutWidget)
        self.timeout_spinbox.setMaximum(999999)
        self.timeout_spinbox.setObjectName(_fromUtf8("timeout_spinbox"))
        self.gridLayout.addWidget(self.timeout_spinbox, 8, 3, 1, 1)
        self.timeout_label = QtGui.QLabel(self.gridLayoutWidget)
        self.timeout_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.timeout_label.setObjectName(_fromUtf8("timeout_label"))
        self.gridLayout.addWidget(self.timeout_label, 8, 2, 1, 1)
        self.clickRadio = QtGui.QRadioButton(self.gridLayoutWidget)
        self.clickRadio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.clickRadio.setObjectName(_fromUtf8("clickRadio"))
        self.buttonGroup_2 = QtGui.QButtonGroup(Form)
        self.buttonGroup_2.setObjectName(_fromUtf8("buttonGroup_2"))
        self.buttonGroup_2.addButton(self.clickRadio)
        self.gridLayout.addWidget(self.clickRadio, 11, 0, 1, 1)
        self.holdreleaseSpinBox = QtGui.QSpinBox(self.gridLayoutWidget)
        self.holdreleaseSpinBox.setEnabled(False)
        self.holdreleaseSpinBox.setMinimum(1)
        self.holdreleaseSpinBox.setMaximum(9999)
        self.holdreleaseSpinBox.setObjectName(_fromUtf8("holdreleaseSpinBox"))
        self.gridLayout.addWidget(self.holdreleaseSpinBox, 14, 3, 1, 1)
        self.labelClickDelay = QtGui.QLabel(self.gridLayoutWidget)
        self.labelClickDelay.setEnabled(False)
        self.labelClickDelay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelClickDelay.setObjectName(_fromUtf8("labelClickDelay"))
        self.gridLayout.addWidget(self.labelClickDelay, 13, 2, 1, 1)
        self.labelCritical = QtGui.QLabel(self.gridLayoutWidget)
        self.labelCritical.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelCritical.setObjectName(_fromUtf8("labelCritical"))
        self.gridLayout.addWidget(self.labelCritical, 7, 2, 1, 1)
        self.movemouseRadio = QtGui.QRadioButton(self.gridLayoutWidget)
        self.movemouseRadio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.movemouseRadio.setChecked(False)
        self.movemouseRadio.setObjectName(_fromUtf8("movemouseRadio"))
        self.buttonGroup_2.addButton(self.movemouseRadio)
        self.gridLayout.addWidget(self.movemouseRadio, 11, 2, 1, 1)
        self.wait_radio = QtGui.QRadioButton(self.gridLayoutWidget)
        self.wait_radio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.wait_radio.setChecked(True)
        self.wait_radio.setObjectName(_fromUtf8("wait_radio"))
        self.buttonGroup_5.addButton(self.wait_radio)
        self.gridLayout.addWidget(self.wait_radio, 6, 0, 1, 3)
        self.spinBoxArgs = QtGui.QSpinBox(self.gridLayoutWidget)
        self.spinBoxArgs.setObjectName(_fromUtf8("spinBoxArgs"))
        self.gridLayout.addWidget(self.spinBoxArgs, 1, 3, 1, 1)
        self.labelArgs = QtGui.QLabel(self.gridLayoutWidget)
        self.labelArgs.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelArgs.setObjectName(_fromUtf8("labelArgs"))
        self.gridLayout.addWidget(self.labelArgs, 1, 2, 1, 1)
        self.pushButtonXYoffset = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButtonXYoffset.setEnabled(False)
        self.pushButtonXYoffset.setObjectName(_fromUtf8("pushButtonXYoffset"))
        self.gridLayout.addWidget(self.pushButtonXYoffset, 12, 1, 2, 1)
        self.line_3 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 2, 0, 1, 4)
        self.namelineedit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.namelineedit.setObjectName(_fromUtf8("namelineedit"))
        self.gridLayout.addWidget(self.namelineedit, 0, 1, 1, 3)
        self.inserttext = QtGui.QLineEdit(self.gridLayoutWidget)
        self.inserttext.setObjectName(_fromUtf8("inserttext"))
        self.gridLayout.addWidget(self.inserttext, 15, 0, 1, 4)
        self.rightclickRadio = QtGui.QRadioButton(self.gridLayoutWidget)
        self.rightclickRadio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.rightclickRadio.setObjectName(_fromUtf8("rightclickRadio"))
        self.buttonGroup_2.addButton(self.rightclickRadio)
        self.gridLayout.addWidget(self.rightclickRadio, 11, 1, 1, 1)
        self.labelName = QtGui.QLabel(self.gridLayoutWidget)
        self.labelName.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelName.setObjectName(_fromUtf8("labelName"))
        self.gridLayout.addWidget(self.labelName, 0, 0, 1, 1)
        self.doubleSpinBoxCritical = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBoxCritical.setMaximum(9999.99)
        self.doubleSpinBoxCritical.setSingleStep(1.0)
        self.doubleSpinBoxCritical.setObjectName(_fromUtf8("doubleSpinBoxCritical"))
        self.gridLayout.addWidget(self.doubleSpinBoxCritical, 7, 3, 1, 1)
        self.doubleSpinBoxThreshold = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBoxThreshold.setMaximum(1.0)
        self.doubleSpinBoxThreshold.setSingleStep(0.05)
        self.doubleSpinBoxThreshold.setObjectName(_fromUtf8("doubleSpinBoxThreshold"))
        self.gridLayout.addWidget(self.doubleSpinBoxThreshold, 4, 3, 1, 1)
        self.clicknumber_spinbox = QtGui.QSpinBox(self.gridLayoutWidget)
        self.clicknumber_spinbox.setEnabled(False)
        self.clicknumber_spinbox.setMinimum(1)
        self.clicknumber_spinbox.setObjectName(_fromUtf8("clicknumber_spinbox"))
        self.gridLayout.addWidget(self.clicknumber_spinbox, 12, 3, 1, 1)
        self.labelSendKeysDelay = QtGui.QLabel(self.gridLayoutWidget)
        self.labelSendKeysDelay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelSendKeysDelay.setObjectName(_fromUtf8("labelSendKeysDelay"))
        self.gridLayout.addWidget(self.labelSendKeysDelay, 16, 0, 1, 1)
        self.labelWarning = QtGui.QLabel(self.gridLayoutWidget)
        self.labelWarning.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelWarning.setObjectName(_fromUtf8("labelWarning"))
        self.gridLayout.addWidget(self.labelWarning, 7, 0, 1, 1)
        self.timeout_exception = QtGui.QCheckBox(self.gridLayoutWidget)
        self.timeout_exception.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.timeout_exception.setChecked(True)
        self.timeout_exception.setObjectName(_fromUtf8("timeout_exception"))
        self.gridLayout.addWidget(self.timeout_exception, 9, 0, 1, 2)
        self.line_8 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.gridLayout.addWidget(self.line_8, 5, 0, 1, 4)
        self.dontclickRadio = QtGui.QRadioButton(self.gridLayoutWidget)
        self.dontclickRadio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.dontclickRadio.setChecked(True)
        self.dontclickRadio.setObjectName(_fromUtf8("dontclickRadio"))
        self.buttonGroup_2.addButton(self.dontclickRadio)
        self.gridLayout.addWidget(self.dontclickRadio, 11, 3, 1, 1)
        self.labelSendKeysDuration = QtGui.QLabel(self.gridLayoutWidget)
        self.labelSendKeysDuration.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelSendKeysDuration.setObjectName(_fromUtf8("labelSendKeysDuration"))
        self.gridLayout.addWidget(self.labelSendKeysDuration, 16, 2, 1, 1)
        self.add_quotes = QtGui.QCheckBox(self.gridLayoutWidget)
        self.add_quotes.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.add_quotes.setChecked(True)
        self.add_quotes.setObjectName(_fromUtf8("add_quotes"))
        self.gridLayout.addWidget(self.add_quotes, 17, 2, 1, 1)
        self.spinBoxSendKeysDelay = QtGui.QSpinBox(self.gridLayoutWidget)
        self.spinBoxSendKeysDelay.setMaximum(60000)
        self.spinBoxSendKeysDelay.setProperty("value", 15)
        self.spinBoxSendKeysDelay.setObjectName(_fromUtf8("spinBoxSendKeysDelay"))
        self.gridLayout.addWidget(self.spinBoxSendKeysDelay, 16, 1, 1, 1)
        self.text_encrypted = QtGui.QCheckBox(self.gridLayoutWidget)
        self.text_encrypted.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.text_encrypted.setChecked(False)
        self.text_encrypted.setObjectName(_fromUtf8("text_encrypted"))
        self.gridLayout.addWidget(self.text_encrypted, 17, 3, 1, 1)
        self.doubleSpinBoxWarning = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBoxWarning.setMaximum(9999.99)
        self.doubleSpinBoxWarning.setSingleStep(1.0)
        self.doubleSpinBoxWarning.setObjectName(_fromUtf8("doubleSpinBoxWarning"))
        self.gridLayout.addWidget(self.doubleSpinBoxWarning, 7, 1, 1, 1)
        self.labelClickNumber = QtGui.QLabel(self.gridLayoutWidget)
        self.labelClickNumber.setEnabled(False)
        self.labelClickNumber.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelClickNumber.setObjectName(_fromUtf8("labelClickNumber"))
        self.gridLayout.addWidget(self.labelClickNumber, 12, 2, 1, 1)
        self.clickdelay_spinbox = QtGui.QSpinBox(self.gridLayoutWidget)
        self.clickdelay_spinbox.setEnabled(False)
        self.clickdelay_spinbox.setMinimum(1)
        self.clickdelay_spinbox.setMaximum(60000)
        self.clickdelay_spinbox.setProperty("value", 10)
        self.clickdelay_spinbox.setObjectName(_fromUtf8("clickdelay_spinbox"))
        self.gridLayout.addWidget(self.clickdelay_spinbox, 13, 3, 1, 1)
        self.spinBoxSendKeysDuration = QtGui.QSpinBox(self.gridLayoutWidget)
        self.spinBoxSendKeysDuration.setMaximum(60000)
        self.spinBoxSendKeysDuration.setProperty("value", 15)
        self.spinBoxSendKeysDuration.setObjectName(_fromUtf8("spinBoxSendKeysDuration"))
        self.gridLayout.addWidget(self.spinBoxSendKeysDuration, 16, 3, 1, 1)
        self.checkBoxMatchColors = QtGui.QCheckBox(self.gridLayoutWidget)
        self.checkBoxMatchColors.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBoxMatchColors.setChecked(True)
        self.checkBoxMatchColors.setObjectName(_fromUtf8("checkBoxMatchColors"))
        self.gridLayout.addWidget(self.checkBoxMatchColors, 3, 2, 1, 2)
        self.holdreleaseRadio = QtGui.QRadioButton(self.gridLayoutWidget)
        self.holdreleaseRadio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.holdreleaseRadio.setObjectName(_fromUtf8("holdreleaseRadio"))
        self.buttonGroup_2.addButton(self.holdreleaseRadio)
        self.gridLayout.addWidget(self.holdreleaseRadio, 14, 0, 1, 1)
        self.labelPixels = QtGui.QLabel(self.gridLayoutWidget)
        self.labelPixels.setEnabled(False)
        self.labelPixels.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPixels.setObjectName(_fromUtf8("labelPixels"))
        self.gridLayout.addWidget(self.labelPixels, 14, 2, 1, 1)
        self.holdreleaseComboBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.holdreleaseComboBox.setEnabled(False)
        self.holdreleaseComboBox.setObjectName(_fromUtf8("holdreleaseComboBox"))
        self.holdreleaseComboBox.addItem(_fromUtf8(""))
        self.holdreleaseComboBox.addItem(_fromUtf8(""))
        self.holdreleaseComboBox.addItem(_fromUtf8(""))
        self.holdreleaseComboBox.addItem(_fromUtf8(""))
        self.holdreleaseComboBox.addItem(_fromUtf8(""))
        self.holdreleaseComboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.holdreleaseComboBox, 14, 1, 1, 1)
        self.widget_2 = QtGui.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(173, 9000, 381, 301))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.widget_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 380, 291))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.dontclickRadio_2 = QtGui.QRadioButton(self.gridLayoutWidget_2)
        self.dontclickRadio_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.dontclickRadio_2.setChecked(True)
        self.dontclickRadio_2.setObjectName(_fromUtf8("dontclickRadio_2"))
        self.buttonGroup_4 = QtGui.QButtonGroup(Form)
        self.buttonGroup_4.setObjectName(_fromUtf8("buttonGroup_4"))
        self.buttonGroup_4.addButton(self.dontclickRadio_2)
        self.gridLayout_2.addWidget(self.dontclickRadio_2, 3, 3, 1, 1)
        self.doubleSpinBoxThreshold_2 = QtGui.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBoxThreshold_2.setMaximum(1.0)
        self.doubleSpinBoxThreshold_2.setSingleStep(0.05)
        self.doubleSpinBoxThreshold_2.setObjectName(_fromUtf8("doubleSpinBoxThreshold_2"))
        self.gridLayout_2.addWidget(self.doubleSpinBoxThreshold_2, 1, 3, 1, 1)
        self.labelSendKeysDuration_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.labelSendKeysDuration_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelSendKeysDuration_2.setObjectName(_fromUtf8("labelSendKeysDuration_2"))
        self.gridLayout_2.addWidget(self.labelSendKeysDuration_2, 8, 2, 1, 1)
        self.spinBoxSendKeysDuration_2 = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.spinBoxSendKeysDuration_2.setMaximum(60000)
        self.spinBoxSendKeysDuration_2.setProperty("value", 15)
        self.spinBoxSendKeysDuration_2.setObjectName(_fromUtf8("spinBoxSendKeysDuration_2"))
        self.gridLayout_2.addWidget(self.spinBoxSendKeysDuration_2, 8, 3, 1, 1)
        self.clicknumber_spinbox_2 = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.clicknumber_spinbox_2.setEnabled(False)
        self.clicknumber_spinbox_2.setMinimum(1)
        self.clicknumber_spinbox_2.setObjectName(_fromUtf8("clicknumber_spinbox_2"))
        self.gridLayout_2.addWidget(self.clicknumber_spinbox_2, 4, 3, 1, 1)
        self.clickRadio_2 = QtGui.QRadioButton(self.gridLayoutWidget_2)
        self.clickRadio_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.clickRadio_2.setObjectName(_fromUtf8("clickRadio_2"))
        self.buttonGroup_4.addButton(self.clickRadio_2)
        self.gridLayout_2.addWidget(self.clickRadio_2, 3, 0, 1, 1)
        self.labelClickDelay_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.labelClickDelay_2.setEnabled(False)
        self.labelClickDelay_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelClickDelay_2.setObjectName(_fromUtf8("labelClickDelay_2"))
        self.gridLayout_2.addWidget(self.labelClickDelay_2, 5, 2, 1, 1)
        self.holdreleaseSpinBox_2 = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.holdreleaseSpinBox_2.setEnabled(False)
        self.holdreleaseSpinBox_2.setMinimum(1)
        self.holdreleaseSpinBox_2.setMaximum(9999)
        self.holdreleaseSpinBox_2.setObjectName(_fromUtf8("holdreleaseSpinBox_2"))
        self.gridLayout_2.addWidget(self.holdreleaseSpinBox_2, 6, 3, 1, 1)
        self.add_quotes_2 = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.add_quotes_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.add_quotes_2.setChecked(True)
        self.add_quotes_2.setObjectName(_fromUtf8("add_quotes_2"))
        self.gridLayout_2.addWidget(self.add_quotes_2, 9, 2, 1, 1)
        self.pushButtonXYoffset_2 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.pushButtonXYoffset_2.setEnabled(False)
        self.pushButtonXYoffset_2.setObjectName(_fromUtf8("pushButtonXYoffset_2"))
        self.gridLayout_2.addWidget(self.pushButtonXYoffset_2, 4, 1, 2, 1)
        self.spinBoxSendKeysDelay_2 = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.spinBoxSendKeysDelay_2.setMaximum(60000)
        self.spinBoxSendKeysDelay_2.setProperty("value", 15)
        self.spinBoxSendKeysDelay_2.setObjectName(_fromUtf8("spinBoxSendKeysDelay_2"))
        self.gridLayout_2.addWidget(self.spinBoxSendKeysDelay_2, 8, 1, 1, 1)
        self.threshold_label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.threshold_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.threshold_label_2.setObjectName(_fromUtf8("threshold_label_2"))
        self.gridLayout_2.addWidget(self.threshold_label_2, 1, 0, 1, 3)
        self.text_encrypted_2 = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.text_encrypted_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.text_encrypted_2.setChecked(False)
        self.text_encrypted_2.setObjectName(_fromUtf8("text_encrypted_2"))
        self.gridLayout_2.addWidget(self.text_encrypted_2, 9, 3, 1, 1)
        self.line_5 = QtGui.QFrame(self.gridLayoutWidget_2)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout_2.addWidget(self.line_5, 2, 0, 1, 4)
        self.clickdelay_spinbox_2 = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.clickdelay_spinbox_2.setEnabled(False)
        self.clickdelay_spinbox_2.setMinimum(1)
        self.clickdelay_spinbox_2.setMaximum(60000)
        self.clickdelay_spinbox_2.setProperty("value", 10)
        self.clickdelay_spinbox_2.setObjectName(_fromUtf8("clickdelay_spinbox_2"))
        self.gridLayout_2.addWidget(self.clickdelay_spinbox_2, 5, 3, 1, 1)
        self.movemouseRadio_2 = QtGui.QRadioButton(self.gridLayoutWidget_2)
        self.movemouseRadio_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.movemouseRadio_2.setChecked(False)
        self.movemouseRadio_2.setObjectName(_fromUtf8("movemouseRadio_2"))
        self.buttonGroup_4.addButton(self.movemouseRadio_2)
        self.gridLayout_2.addWidget(self.movemouseRadio_2, 3, 2, 1, 1)
        self.inserttext_2 = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.inserttext_2.setObjectName(_fromUtf8("inserttext_2"))
        self.gridLayout_2.addWidget(self.inserttext_2, 7, 0, 1, 4)
        self.labelClickNumber_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.labelClickNumber_2.setEnabled(False)
        self.labelClickNumber_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelClickNumber_2.setObjectName(_fromUtf8("labelClickNumber_2"))
        self.gridLayout_2.addWidget(self.labelClickNumber_2, 4, 2, 1, 1)
        self.labelSendKeysDelay_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.labelSendKeysDelay_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelSendKeysDelay_2.setObjectName(_fromUtf8("labelSendKeysDelay_2"))
        self.gridLayout_2.addWidget(self.labelSendKeysDelay_2, 8, 0, 1, 1)
        self.checkBoxMatchColors_2 = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.checkBoxMatchColors_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBoxMatchColors_2.setChecked(True)
        self.checkBoxMatchColors_2.setObjectName(_fromUtf8("checkBoxMatchColors_2"))
        self.gridLayout_2.addWidget(self.checkBoxMatchColors_2, 0, 2, 1, 2)
        self.rightclickRadio_2 = QtGui.QRadioButton(self.gridLayoutWidget_2)
        self.rightclickRadio_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.rightclickRadio_2.setObjectName(_fromUtf8("rightclickRadio_2"))
        self.buttonGroup_4.addButton(self.rightclickRadio_2)
        self.gridLayout_2.addWidget(self.rightclickRadio_2, 3, 1, 1, 1)
        self.holdreleaseRadio_2 = QtGui.QRadioButton(self.gridLayoutWidget_2)
        self.holdreleaseRadio_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.holdreleaseRadio_2.setObjectName(_fromUtf8("holdreleaseRadio_2"))
        self.buttonGroup_4.addButton(self.holdreleaseRadio_2)
        self.gridLayout_2.addWidget(self.holdreleaseRadio_2, 6, 0, 1, 1)
        self.holdreleaseComboBox_2 = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.holdreleaseComboBox_2.setEnabled(False)
        self.holdreleaseComboBox_2.setObjectName(_fromUtf8("holdreleaseComboBox_2"))
        self.holdreleaseComboBox_2.addItem(_fromUtf8(""))
        self.holdreleaseComboBox_2.addItem(_fromUtf8(""))
        self.holdreleaseComboBox_2.addItem(_fromUtf8(""))
        self.holdreleaseComboBox_2.addItem(_fromUtf8(""))
        self.holdreleaseComboBox_2.addItem(_fromUtf8(""))
        self.holdreleaseComboBox_2.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.holdreleaseComboBox_2, 6, 1, 1, 1)
        self.labelPixels_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.labelPixels_2.setEnabled(False)
        self.labelPixels_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPixels_2.setObjectName(_fromUtf8("labelPixels_2"))
        self.gridLayout_2.addWidget(self.labelPixels_2, 6, 2, 1, 1)
        self.roi_width_label = QtGui.QLabel(Form)
        self.roi_width_label.setGeometry(QtCore.QRect(138, 10000, 89, 20))
        self.roi_width_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.roi_width_label.setObjectName(_fromUtf8("roi_width_label"))
        self.roi_height_label = QtGui.QLabel(Form)
        self.roi_height_label.setGeometry(QtCore.QRect(327, 10000, 94, 20))
        self.roi_height_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.roi_height_label.setObjectName(_fromUtf8("roi_height_label"))
        self.line_9 = QtGui.QFrame(Form)
        self.line_9.setGeometry(QtCore.QRect(138, 10000, 378, 3))
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.roi_height_spinbox = QtGui.QSpinBox(Form)
        self.roi_height_spinbox.setGeometry(QtCore.QRect(427, 10000, 89, 20))
        self.roi_height_spinbox.setMaximum(9999)
        self.roi_height_spinbox.setObjectName(_fromUtf8("roi_height_spinbox"))
        self.roi_y_spinbox = QtGui.QSpinBox(Form)
        self.roi_y_spinbox.setGeometry(QtCore.QRect(427, 10000, 89, 20))
        self.roi_y_spinbox.setMinimum(-9999)
        self.roi_y_spinbox.setMaximum(9999)
        self.roi_y_spinbox.setObjectName(_fromUtf8("roi_y_spinbox"))
        self.roi_width_spinbox = QtGui.QSpinBox(Form)
        self.roi_width_spinbox.setGeometry(QtCore.QRect(233, 10000, 88, 20))
        self.roi_width_spinbox.setMaximum(9999)
        self.roi_width_spinbox.setObjectName(_fromUtf8("roi_width_spinbox"))
        self.roi_y_label = QtGui.QLabel(Form)
        self.roi_y_label.setGeometry(QtCore.QRect(327, 10000, 94, 20))
        self.roi_y_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.roi_y_label.setObjectName(_fromUtf8("roi_y_label"))
        self.roi_x_spinbox = QtGui.QSpinBox(Form)
        self.roi_x_spinbox.setGeometry(QtCore.QRect(233, 10000, 88, 20))
        self.roi_x_spinbox.setMinimum(-9999)
        self.roi_x_spinbox.setMaximum(9999)
        self.roi_x_spinbox.setObjectName(_fromUtf8("roi_x_spinbox"))
        self.roi_x_label = QtGui.QLabel(Form)
        self.roi_x_label.setGeometry(QtCore.QRect(138, 10000, 89, 20))
        self.roi_x_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.roi_x_label.setObjectName(_fromUtf8("roi_x_label"))
        self.find_radio = QtGui.QRadioButton(Form)
        self.find_radio.setGeometry(QtCore.QRect(80, 7800, 88, 17))
        self.find_radio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.find_radio.setObjectName(_fromUtf8("find_radio"))
        self.buttonGroup_5.addButton(self.find_radio)
        self.gridLayoutWidget_3 = QtGui.QWidget(Form)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(9, 436, 158, 61))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButtonSelAll = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButtonSelAll.setObjectName(_fromUtf8("pushButtonSelAll"))
        self.gridLayout_3.addWidget(self.pushButtonSelAll, 0, 0, 1, 1)
        self.pushButtonDesAll = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButtonDesAll.setObjectName(_fromUtf8("pushButtonDesAll"))
        self.gridLayout_3.addWidget(self.pushButtonDesAll, 0, 1, 1, 1)
        self.pushButtonDelete = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButtonDelete.setObjectName(_fromUtf8("pushButtonDelete"))
        self.gridLayout_3.addWidget(self.pushButtonDelete, 1, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Alyvix - Image Finder", None))
        self.pushButtonCancel.setText(_translate("Form", "Cancel", None))
        self.pushButtonOk.setText(_translate("Form", "Ok", None))
        self.label_line.setText(_translate("Form", "Begin Line", None))
        self.pushButtonAddBlock.setText(_translate("Form", "Add Block", None))
        self.pushButtonRemoveBlock.setText(_translate("Form", "Remove Block", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "main_component", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.threshold_label.setText(_translate("Form", "Threshold", None))
        self.wait_disapp_radio.setText(_translate("Form", "Disappeared", None))
        self.checkBoxEnablePerformance.setText(_translate("Form", "Performance", None))
        self.timeout_label.setText(_translate("Form", "Timeout", None))
        self.clickRadio.setText(_translate("Form", "Click", None))
        self.labelClickDelay.setText(_translate("Form", "Delays [ms]", None))
        self.labelCritical.setText(_translate("Form", "Critical", None))
        self.movemouseRadio.setText(_translate("Form", "Move", None))
        self.wait_radio.setText(_translate("Form", "Appeared", None))
        self.labelArgs.setText(_translate("Form", "Arguments", None))
        self.pushButtonXYoffset.setText(_translate("Form", "Interaction\n"
"Point", None))
        self.namelineedit.setText(_translate("Form", "Type the keyword name", None))
        self.inserttext.setText(_translate("Form", "Type text strings and shortcuts", None))
        self.rightclickRadio.setText(_translate("Form", "Right Click", None))
        self.labelName.setText(_translate("Form", "Name", None))
        self.labelSendKeysDelay.setText(_translate("Form", "Delays [ms] ", None))
        self.labelWarning.setText(_translate("Form", "Warning", None))
        self.timeout_exception.setText(_translate("Form", "Break", None))
        self.dontclickRadio.setText(_translate("Form", "None", None))
        self.labelSendKeysDuration.setText(_translate("Form", "Duration [ms] ", None))
        self.add_quotes.setText(_translate("Form", "Quotes", None))
        self.text_encrypted.setText(_translate("Form", " Encrypted", None))
        self.labelClickNumber.setText(_translate("Form", "Clicks", None))
        self.checkBoxMatchColors.setText(_translate("Form", "Colors", None))
        self.holdreleaseRadio.setText(_translate("Form", "Hold\'n\'Release", None))
        self.labelPixels.setText(_translate("Form", "Pixels [px]", None))
        self.holdreleaseComboBox.setItemText(0, _translate("Form", "Hold", None))
        self.holdreleaseComboBox.setItemText(1, _translate("Form", "Release", None))
        self.holdreleaseComboBox.setItemText(2, _translate("Form", "Release Up", None))
        self.holdreleaseComboBox.setItemText(3, _translate("Form", "Release Down", None))
        self.holdreleaseComboBox.setItemText(4, _translate("Form", "Release Left", None))
        self.holdreleaseComboBox.setItemText(5, _translate("Form", "Release Right", None))
        self.dontclickRadio_2.setText(_translate("Form", "None", None))
        self.labelSendKeysDuration_2.setText(_translate("Form", "Duration [ms] ", None))
        self.clickRadio_2.setText(_translate("Form", "Click", None))
        self.labelClickDelay_2.setText(_translate("Form", "Delays [ms]", None))
        self.add_quotes_2.setText(_translate("Form", "Quotes", None))
        self.pushButtonXYoffset_2.setText(_translate("Form", "Interaction\n"
"Point", None))
        self.threshold_label_2.setText(_translate("Form", "Threshold", None))
        self.text_encrypted_2.setText(_translate("Form", "Encrypted", None))
        self.movemouseRadio_2.setText(_translate("Form", "Move", None))
        self.inserttext_2.setText(_translate("Form", "Type text strings and shortcuts", None))
        self.labelClickNumber_2.setText(_translate("Form", "Clicks", None))
        self.labelSendKeysDelay_2.setText(_translate("Form", "Delays [ms] ", None))
        self.checkBoxMatchColors_2.setText(_translate("Form", "Colors", None))
        self.rightclickRadio_2.setText(_translate("Form", "Right Click", None))
        self.holdreleaseRadio_2.setText(_translate("Form", "Hold\'n\'Release", None))
        self.holdreleaseComboBox_2.setItemText(0, _translate("Form", "Hold", None))
        self.holdreleaseComboBox_2.setItemText(1, _translate("Form", "Release", None))
        self.holdreleaseComboBox_2.setItemText(2, _translate("Form", "Release Up", None))
        self.holdreleaseComboBox_2.setItemText(3, _translate("Form", "Release Down", None))
        self.holdreleaseComboBox_2.setItemText(4, _translate("Form", "Release Left", None))
        self.holdreleaseComboBox_2.setItemText(5, _translate("Form", "Release Right", None))
        self.labelPixels_2.setText(_translate("Form", "Pixels [px]", None))
        self.roi_width_label.setText(_translate("Form", "Roi Width", None))
        self.roi_height_label.setText(_translate("Form", "Roi Height", None))
        self.roi_y_label.setText(_translate("Form", "Roi Y", None))
        self.roi_x_label.setText(_translate("Form", "Roi X", None))
        self.find_radio.setText(_translate("Form", "Find", None))
        self.pushButtonSelAll.setText(_translate("Form", "Select All", None))
        self.pushButtonDesAll.setText(_translate("Form", "Deselect All", None))
        self.pushButtonDelete.setText(_translate("Form", "Remove", None))

