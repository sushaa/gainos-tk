# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\parai@foxmail.com\github\gainos-tk\tool\gainos-studio\ui\forms\cd_comm.ui'
#
# Created: Sun Jul 14 16:41:39 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_cd_comm(object):
    def setupUi(self, cd_comm):
        cd_comm.setObjectName(_fromUtf8("cd_comm"))
        cd_comm.resize(943, 512)
        cd_comm.setStyleSheet(_fromUtf8("font: 12pt \"Consolas\";"))
        self.groupBox = QtGui.QGroupBox(cd_comm)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 931, 101))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.widget = QtGui.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(31, 31, 851, 56))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.cbxDevErr = QtGui.QCheckBox(self.widget)
        self.cbxDevErr.setObjectName(_fromUtf8("cbxDevErr"))
        self.verticalLayout_6.addWidget(self.cbxDevErr)
        self.cbxNoCommu = QtGui.QCheckBox(self.widget)
        self.cbxNoCommu.setObjectName(_fromUtf8("cbxNoCommu"))
        self.verticalLayout_6.addWidget(self.cbxNoCommu)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.cbxVersionInfoApi = QtGui.QCheckBox(self.widget)
        self.cbxVersionInfoApi.setObjectName(_fromUtf8("cbxVersionInfoApi"))
        self.verticalLayout_7.addWidget(self.cbxVersionInfoApi)
        self.cbxModeLimit = QtGui.QCheckBox(self.widget)
        self.cbxModeLimit.setObjectName(_fromUtf8("cbxModeLimit"))
        self.verticalLayout_7.addWidget(self.cbxModeLimit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.spbxMinTime = QtGui.QSpinBox(self.widget)
        self.spbxMinTime.setMaximum(65535)
        self.spbxMinTime.setObjectName(_fromUtf8("spbxMinTime"))
        self.horizontalLayout.addWidget(self.spbxMinTime)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.groupBox_2 = QtGui.QGroupBox(cd_comm)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 110, 931, 401))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777214, 16777215))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.tabCfg = QtGui.QTabWidget(self.groupBox_2)
        self.tabCfg.setGeometry(QtCore.QRect(390, 10, 541, 381))
        self.tabCfg.setObjectName(_fromUtf8("tabCfg"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.widget1 = QtGui.QWidget(self.tab_3)
        self.widget1.setGeometry(QtCore.QRect(10, 23, 481, 165))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_44 = QtGui.QLabel(self.widget1)
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.horizontalLayout_15.addWidget(self.label_44)
        self.leChanneName = QtGui.QLineEdit(self.widget1)
        self.leChanneName.setText(_fromUtf8(""))
        self.leChanneName.setObjectName(_fromUtf8("leChanneName"))
        self.horizontalLayout_15.addWidget(self.leChanneName)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_32 = QtGui.QLabel(self.widget1)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.horizontalLayout_16.addWidget(self.label_32)
        self.cmbxBusType = QtGui.QComboBox(self.widget1)
        self.cmbxBusType.setMinimumSize(QtCore.QSize(250, 0))
        self.cmbxBusType.setToolTip(_fromUtf8(""))
        self.cmbxBusType.setObjectName(_fromUtf8("cmbxBusType"))
        self.cmbxBusType.addItem(_fromUtf8(""))
        self.cmbxBusType.addItem(_fromUtf8(""))
        self.cmbxBusType.addItem(_fromUtf8(""))
        self.cmbxBusType.addItem(_fromUtf8(""))
        self.horizontalLayout_16.addWidget(self.cmbxBusType)
        self.verticalLayout_2.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.spbxMainFncPeriod = QtGui.QSpinBox(self.widget1)
        self.spbxMainFncPeriod.setMaximum(65535)
        self.spbxMainFncPeriod.setObjectName(_fromUtf8("spbxMainFncPeriod"))
        self.horizontalLayout_3.addWidget(self.spbxMainFncPeriod)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.label_33 = QtGui.QLabel(self.widget1)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.horizontalLayout_17.addWidget(self.label_33)
        self.cmbxNmVariant = QtGui.QComboBox(self.widget1)
        self.cmbxNmVariant.setMinimumSize(QtCore.QSize(250, 0))
        self.cmbxNmVariant.setToolTip(_fromUtf8(""))
        self.cmbxNmVariant.setObjectName(_fromUtf8("cmbxNmVariant"))
        self.cmbxNmVariant.addItem(_fromUtf8(""))
        self.cmbxNmVariant.addItem(_fromUtf8(""))
        self.cmbxNmVariant.addItem(_fromUtf8(""))
        self.cmbxNmVariant.addItem(_fromUtf8(""))
        self.horizontalLayout_17.addWidget(self.cmbxNmVariant)
        self.verticalLayout.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.label_34 = QtGui.QLabel(self.widget1)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.horizontalLayout_18.addWidget(self.label_34)
        self.spbxLightTimeout = QtGui.QSpinBox(self.widget1)
        self.spbxLightTimeout.setMaximum(65535)
        self.spbxLightTimeout.setObjectName(_fromUtf8("spbxLightTimeout"))
        self.horizontalLayout_18.addWidget(self.spbxLightTimeout)
        self.verticalLayout.addLayout(self.horizontalLayout_18)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.widget2 = QtGui.QWidget(self.tab_3)
        self.widget2.setGeometry(QtCore.QRect(10, 210, 481, 62))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget2)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.label_35 = QtGui.QLabel(self.widget2)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.horizontalLayout_19.addWidget(self.label_35)
        self.cmbxNmChannel = QtGui.QComboBox(self.widget2)
        self.cmbxNmChannel.setMinimumSize(QtCore.QSize(250, 0))
        self.cmbxNmChannel.setToolTip(_fromUtf8(""))
        self.cmbxNmChannel.setObjectName(_fromUtf8("cmbxNmChannel"))
        self.horizontalLayout_19.addWidget(self.cmbxNmChannel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.label_36 = QtGui.QLabel(self.widget2)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.horizontalLayout_20.addWidget(self.label_36)
        self.cmbxSmChannel = QtGui.QComboBox(self.widget2)
        self.cmbxSmChannel.setMinimumSize(QtCore.QSize(250, 0))
        self.cmbxSmChannel.setToolTip(_fromUtf8(""))
        self.cmbxSmChannel.setObjectName(_fromUtf8("cmbxSmChannel"))
        self.horizontalLayout_20.addWidget(self.cmbxSmChannel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_20)
        self.tabCfg.addTab(self.tab_3, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.layoutWidget_30 = QtGui.QWidget(self.tab)
        self.layoutWidget_30.setGeometry(QtCore.QRect(250, 100, 41, 62))
        self.layoutWidget_30.setObjectName(_fromUtf8("layoutWidget_30"))
        self.verticalLayout_21 = QtGui.QVBoxLayout(self.layoutWidget_30)
        self.verticalLayout_21.setMargin(0)
        self.verticalLayout_21.setObjectName(_fromUtf8("verticalLayout_21"))
        self.btnAddChl = QtGui.QPushButton(self.layoutWidget_30)
        self.btnAddChl.setMaximumSize(QtCore.QSize(39, 16777215))
        self.btnAddChl.setObjectName(_fromUtf8("btnAddChl"))
        self.verticalLayout_21.addWidget(self.btnAddChl)
        self.btnDelChl = QtGui.QPushButton(self.layoutWidget_30)
        self.btnDelChl.setMaximumSize(QtCore.QSize(39, 16777215))
        self.btnDelChl.setObjectName(_fromUtf8("btnDelChl"))
        self.verticalLayout_21.addWidget(self.btnDelChl)
        self.trChannelDst = QtGui.QTreeWidget(self.tab)
        self.trChannelDst.setGeometry(QtCore.QRect(10, 50, 231, 291))
        self.trChannelDst.setObjectName(_fromUtf8("trChannelDst"))
        self.trChannelSrc = QtGui.QTreeWidget(self.tab)
        self.trChannelSrc.setGeometry(QtCore.QRect(300, 50, 231, 291))
        self.trChannelSrc.setObjectName(_fromUtf8("trChannelSrc"))
        self.trChannelSrc.headerItem().setText(0, _fromUtf8("Avaliable Channel"))
        self.widget3 = QtGui.QWidget(self.tab)
        self.widget3.setGeometry(QtCore.QRect(19, 10, 471, 27))
        self.widget3.setObjectName(_fromUtf8("widget3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_45 = QtGui.QLabel(self.widget3)
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.horizontalLayout_4.addWidget(self.label_45)
        self.leUserName = QtGui.QLineEdit(self.widget3)
        self.leUserName.setText(_fromUtf8(""))
        self.leUserName.setObjectName(_fromUtf8("leUserName"))
        self.horizontalLayout_4.addWidget(self.leUserName)
        self.tabCfg.addTab(self.tab, _fromUtf8(""))
        self.btn1 = QtGui.QPushButton(self.groupBox_2)
        self.btn1.setGeometry(QtCore.QRect(270, 55, 111, 23))
        self.btn1.setObjectName(_fromUtf8("btn1"))
        self.trComMCfg = QtGui.QTreeWidget(self.groupBox_2)
        self.trComMCfg.setGeometry(QtCore.QRect(10, 30, 256, 361))
        self.trComMCfg.setObjectName(_fromUtf8("trComMCfg"))
        item_0 = QtGui.QTreeWidgetItem(self.trComMCfg)
        item_0 = QtGui.QTreeWidgetItem(self.trComMCfg)

        self.retranslateUi(cd_comm)
        self.tabCfg.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(cd_comm)

    def retranslateUi(self, cd_comm):
        cd_comm.setWindowTitle(QtGui.QApplication.translate("cd_comm", "ComM", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("cd_comm", "ComM General", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxDevErr.setText(QtGui.QApplication.translate("cd_comm", "DevErrorDetection", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxNoCommu.setText(QtGui.QApplication.translate("cd_comm", "No Communication", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxVersionInfoApi.setText(QtGui.QApplication.translate("cd_comm", "VersionInfoApi", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxModeLimit.setText(QtGui.QApplication.translate("cd_comm", "Mode Limitation Enable", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("cd_comm", "Min Time In Full\n"
"Communication Mode:", None, QtGui.QApplication.UnicodeUTF8))
        self.spbxMinTime.setToolTip(QtGui.QApplication.translate("cd_comm", "<html><head/><body><p>ms</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("cd_comm", "ComM Entities", None, QtGui.QApplication.UnicodeUTF8))
        self.label_44.setText(QtGui.QApplication.translate("cd_comm", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setText(QtGui.QApplication.translate("cd_comm", "Bus Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxBusType.setItemText(0, QtGui.QApplication.translate("cd_comm", "COMM_BUS_TYPE_CAN", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxBusType.setItemText(1, QtGui.QApplication.translate("cd_comm", "COMM_BUS_TYPE_FR", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxBusType.setItemText(2, QtGui.QApplication.translate("cd_comm", "COMM_BUS_TYPE_INTERNAL", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxBusType.setItemText(3, QtGui.QApplication.translate("cd_comm", "COMM_BUS_TYPE_LIN", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("cd_comm", "Main Function Period(ms):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setText(QtGui.QApplication.translate("cd_comm", "Nm Variant:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxNmVariant.setItemText(0, QtGui.QApplication.translate("cd_comm", "COMM_NM_VARIANT_NONE", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxNmVariant.setItemText(1, QtGui.QApplication.translate("cd_comm", "COMM_NM_VARIANT_LIGHT", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxNmVariant.setItemText(2, QtGui.QApplication.translate("cd_comm", "COMM_NM_VARIANT_PASSIVE", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxNmVariant.setItemText(3, QtGui.QApplication.translate("cd_comm", "COMM_NM_VARIANT_FULL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate("cd_comm", "Light Timeout:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setText(QtGui.QApplication.translate("cd_comm", "Nm Channel Handle:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_36.setText(QtGui.QApplication.translate("cd_comm", "Bus SM Network Handle:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabCfg.setTabText(self.tabCfg.indexOf(self.tab_3), QtGui.QApplication.translate("cd_comm", "Channel", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddChl.setText(QtGui.QApplication.translate("cd_comm", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDelChl.setText(QtGui.QApplication.translate("cd_comm", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.trChannelDst.headerItem().setText(0, QtGui.QApplication.translate("cd_comm", "Channel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_45.setText(QtGui.QApplication.translate("cd_comm", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabCfg.setTabText(self.tabCfg.indexOf(self.tab), QtGui.QApplication.translate("cd_comm", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.btn1.setText(QtGui.QApplication.translate("cd_comm", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.trComMCfg.headerItem().setText(0, QtGui.QApplication.translate("cd_comm", "ComM", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.trComMCfg.isSortingEnabled()
        self.trComMCfg.setSortingEnabled(False)
        self.trComMCfg.topLevelItem(0).setText(0, QtGui.QApplication.translate("cd_comm", "Channels", None, QtGui.QApplication.UnicodeUTF8))
        self.trComMCfg.topLevelItem(1).setText(0, QtGui.QApplication.translate("cd_comm", "Users", None, QtGui.QApplication.UnicodeUTF8))
        self.trComMCfg.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    cd_comm = QtGui.QDialog()
    ui = Ui_cd_comm()
    ui.setupUi(cd_comm)
    cd_comm.show()
    sys.exit(app.exec_())

