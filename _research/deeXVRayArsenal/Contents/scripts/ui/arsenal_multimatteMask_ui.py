from PySide import QtCore, QtGui

class Ui_arsenal_multimatteMask(object):

    def setupUi(self, arsenal_multimatteMask):
        arsenal_multimatteMask.setObjectName('arsenal_multimatteMask')
        arsenal_multimatteMask.resize(375, 183)
        self.verticalLayout = QtGui.QVBoxLayout(arsenal_multimatteMask)
        self.verticalLayout.setObjectName('verticalLayout')
        self.arsenal_multimatteMaskWidget = QtGui.QWidget(arsenal_multimatteMask)
        self.arsenal_multimatteMaskWidget.setObjectName('arsenal_multimatteMaskWidget')
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.arsenal_multimatteMaskWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName('verticalLayout_3')
        self.arsenal_multimatteMaskGroupBox = QtGui.QGroupBox(self.arsenal_multimatteMaskWidget)
        self.arsenal_multimatteMaskGroupBox.setObjectName('arsenal_multimatteMaskGroupBox')
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.arsenal_multimatteMaskGroupBox)
        self.verticalLayout_2.setObjectName('verticalLayout_2')
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.label = QtGui.QLabel(self.arsenal_multimatteMaskGroupBox)
        self.label.setObjectName('label')
        self.horizontalLayout.addWidget(self.label)
        self.arsenal_multimatteMaskName = QtGui.QLineEdit(self.arsenal_multimatteMaskGroupBox)
        self.arsenal_multimatteMaskName.setObjectName('arsenal_multimatteMaskName')
        self.horizontalLayout.addWidget(self.arsenal_multimatteMaskName)
        self.arsenal_multimatteMaskRemoveGroupe = QtGui.QPushButton(self.arsenal_multimatteMaskGroupBox)
        self.arsenal_multimatteMaskRemoveGroupe.setObjectName('arsenal_multimatteMaskRemoveGroupe')
        self.horizontalLayout.addWidget(self.arsenal_multimatteMaskRemoveGroupe)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.arsenal_multimatteMaskButtonsGroup = QtGui.QWidget(self.arsenal_multimatteMaskGroupBox)
        self.arsenal_multimatteMaskButtonsGroup.setEnabled(False)
        self.arsenal_multimatteMaskButtonsGroup.setObjectName('arsenal_multimatteMaskButtonsGroup')
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.arsenal_multimatteMaskButtonsGroup)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName('verticalLayout_4')
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName('gridLayout_2')
        self.arsenal_multimatteMaskaddInRed = QtGui.QPushButton(self.arsenal_multimatteMaskButtonsGroup)
        self.arsenal_multimatteMaskaddInRed.setObjectName('arsenal_multimatteMaskaddInRed')
        self.gridLayout_2.addWidget(self.arsenal_multimatteMaskaddInRed, 0, 0, 1, 1)
        self.arsenal_multimatteMaskremoveInRed = QtGui.QPushButton(self.arsenal_multimatteMaskButtonsGroup)
        self.arsenal_multimatteMaskremoveInRed.setObjectName('arsenal_multimatteMaskremoveInRed')
        self.gridLayout_2.addWidget(self.arsenal_multimatteMaskremoveInRed, 0, 1, 1, 1)
        self.arsenal_multimatteMaskselectInRed = QtGui.QPushButton(self.arsenal_multimatteMaskButtonsGroup)
        self.arsenal_multimatteMaskselectInRed.setObjectName('arsenal_multimatteMaskselectInRed')
        self.gridLayout_2.addWidget(self.arsenal_multimatteMaskselectInRed, 0, 2, 1, 1)
        self.arsenal_multimatteMaskaddInGreen = QtGui.QPushButton(self.arsenal_multimatteMaskButtonsGroup)
        self.arsenal_multimatteMaskaddInGreen.setObjectName('arsenal_multimatteMaskaddInGreen')
        self.gridLayout_2.addWidget(self.arsenal_multimatteMaskaddInGreen, 1, 0, 1, 1)
        self.arsenal_multimatteMaskremoveInGreen = QtGui.QPushButton(self.arsenal_multimatteMaskButtonsGroup)
        self.arsenal_multimatteMaskremoveInGreen.setObjectName('arsenal_multimatteMaskremoveInGreen')
        self.gridLayout_2.addWidget(self.arsenal_multimatteMaskremoveInGreen, 1, 1, 1, 1)
        self.arsenal_multimatteMaskselectInGreen = QtGui.QPushButton(self.arsenal_multimatteMaskButtonsGroup)
        self.arsenal_multimatteMaskselectInGreen.setObjectName('arsenal_multimatteMaskselectInGreen')
        self.gridLayout_2.addWidget(self.arsenal_multimatteMaskselectInGreen, 1, 2, 1, 1)
        self.arsenal_multimatteMaskaddInBlue = QtGui.QPushButton(self.arsenal_multimatteMaskButtonsGroup)
        self.arsenal_multimatteMaskaddInBlue.setObjectName('arsenal_multimatteMaskaddInBlue')
        self.gridLayout_2.addWidget(self.arsenal_multimatteMaskaddInBlue, 2, 0, 1, 1)
        self.arsenal_multimatteMaskremoveInBlue = QtGui.QPushButton(self.arsenal_multimatteMaskButtonsGroup)
        self.arsenal_multimatteMaskremoveInBlue.setObjectName('arsenal_multimatteMaskremoveInBlue')
        self.gridLayout_2.addWidget(self.arsenal_multimatteMaskremoveInBlue, 2, 1, 1, 1)
        self.arsenal_multimatteMaskselectInBlue = QtGui.QPushButton(self.arsenal_multimatteMaskButtonsGroup)
        self.arsenal_multimatteMaskselectInBlue.setObjectName('arsenal_multimatteMaskselectInBlue')
        self.gridLayout_2.addWidget(self.arsenal_multimatteMaskselectInBlue, 2, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addWidget(self.arsenal_multimatteMaskButtonsGroup)
        self.verticalLayout_3.addWidget(self.arsenal_multimatteMaskGroupBox)
        self.verticalLayout.addWidget(self.arsenal_multimatteMaskWidget)
        self.retranslateUi(arsenal_multimatteMask)
        QtCore.QMetaObject.connectSlotsByName(arsenal_multimatteMask)



    def retranslateUi(self, arsenal_multimatteMask):
        arsenal_multimatteMask.setWindowTitle(QtGui.QApplication.translate('arsenal_multimatteMask', 'VRay Arsenal', None, QtGui.QApplication.UnicodeUTF8))
        self.arsenal_multimatteMaskGroupBox.setTitle(QtGui.QApplication.translate('arsenal_multimatteMask', 'Groupe 1', None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate('arsenal_multimatteMask', 'Mask name :', None, QtGui.QApplication.UnicodeUTF8))
        self.arsenal_multimatteMaskRemoveGroupe.setStyleSheet(QtGui.QApplication.translate('arsenal_multimatteMask', 'background-color: rgb(150, 0, 0);', None, QtGui.QApplication.UnicodeUTF8))
        self.arsenal_multimatteMaskRemoveGroupe.setText(QtGui.QApplication.translate('arsenal_multimatteMask', 'remove', None, QtGui.QApplication.UnicodeUTF8))
        self.arsenal_multimatteMaskaddInRed.setText(QtGui.QApplication.translate('arsenal_multimatteMask', 'add in red', None, QtGui.QApplication.UnicodeUTF8))
        self.arsenal_multimatteMaskremoveInRed.setText(QtGui.QApplication.translate('arsenal_multimatteMask', 'remove', None, QtGui.QApplication.UnicodeUTF8))
        self.arsenal_multimatteMaskselectInRed.setText(QtGui.QApplication.translate('arsenal_multimatteMask', 'select', None, QtGui.QApplication.UnicodeUTF8))
        self.arsenal_multimatteMaskaddInGreen.setText(QtGui.QApplication.translate('arsenal_multimatteMask', 'add in green', None, QtGui.QApplication.UnicodeUTF8))
        self.arsenal_multimatteMaskremoveInGreen.setText(QtGui.QApplication.translate('arsenal_multimatteMask', 'remove', None, QtGui.QApplication.UnicodeUTF8))
        self.arsenal_multimatteMaskselectInGreen.setText(QtGui.QApplication.translate('arsenal_multimatteMask', 'select', None, QtGui.QApplication.UnicodeUTF8))
        self.arsenal_multimatteMaskaddInBlue.setText(QtGui.QApplication.translate('arsenal_multimatteMask', 'add in blue', None, QtGui.QApplication.UnicodeUTF8))
        self.arsenal_multimatteMaskremoveInBlue.setText(QtGui.QApplication.translate('arsenal_multimatteMask', 'remove', None, QtGui.QApplication.UnicodeUTF8))
        self.arsenal_multimatteMaskselectInBlue.setText(QtGui.QApplication.translate('arsenal_multimatteMask', 'select', None, QtGui.QApplication.UnicodeUTF8))



