# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fijiconvertdialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from os import path
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from . setupcheckerr import SetupCheckErr
from . converter import Converter
from . xml_gui import Ui_mdgForm

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName("MainDialog")
        MainDialog.resize(648, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainDialog.sizePolicy().hasHeightForWidth())
        MainDialog.setSizePolicy(sizePolicy)
        MainDialog.setMinimumSize(QtCore.QSize(0, 450))
        MainDialog.setMaximumSize(QtCore.QSize(16777215, 450))
        self.mdlayout = QtWidgets.QVBoxLayout(MainDialog)
        self.mdlayout.setObjectName("mdlayout")
        self.MainDialogLayout = QtWidgets.QVBoxLayout()
        self.MainDialogLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.MainDialogLayout.setContentsMargins(0, -1, -1, -1)
        self.MainDialogLayout.setObjectName("MainDialogLayout")
        self.FileIOWidget = QtWidgets.QWidget(MainDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FileIOWidget.sizePolicy().hasHeightForWidth())
        self.FileIOWidget.setSizePolicy(sizePolicy)
        self.FileIOWidget.setObjectName("FileIOWidget")
        self.fiolayout = QtWidgets.QVBoxLayout(self.FileIOWidget)
        self.fiolayout.setContentsMargins(0, 0, 0, 0)
        self.fiolayout.setObjectName("fiolayout")
        self.FileIOLayout = QtWidgets.QVBoxLayout()
        self.FileIOLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.FileIOLayout.setSpacing(1)
        self.FileIOLayout.setObjectName("FileIOLayout")
        self.ListLabel = QtWidgets.QLabel(self.FileIOWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ListLabel.sizePolicy().hasHeightForWidth())
        self.ListLabel.setSizePolicy(sizePolicy)
        self.ListLabel.setObjectName("ListLabel")
        self.FileIOLayout.addWidget(self.ListLabel)
        self.FileListWidget = QtWidgets.QListWidget(self.FileIOWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FileListWidget.sizePolicy().hasHeightForWidth())
        self.FileListWidget.setSizePolicy(sizePolicy)
        self.FileListWidget.setObjectName("FileListWidget")
        self.FileListWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.FileIOLayout.addWidget(self.FileListWidget)
        self.ButtonsWidget = QtWidgets.QWidget(self.FileIOWidget)
        self.ButtonsWidget.setObjectName("ButtonsWidget")
        self.bwlayout = QtWidgets.QHBoxLayout(self.ButtonsWidget)
        self.bwlayout.setObjectName("bwlayout")
        self.AddButton = QtWidgets.QPushButton(self.ButtonsWidget)
        self.AddButton.setObjectName("AddButton")
        self.bwlayout.addWidget(self.AddButton)
        self.RemoveButton = QtWidgets.QPushButton(self.ButtonsWidget)
        self.RemoveButton.setObjectName("RemoveButton")
        self.bwlayout.addWidget(self.RemoveButton)
        self.OutputLabel = QtWidgets.QLabel(self.ButtonsWidget)
        self.OutputLabel.setObjectName("OutputLabel")
        self.bwlayout.addWidget(self.OutputLabel)
        self.OutputLine = QtWidgets.QLineEdit(self.ButtonsWidget)
        self.OutputLine.setObjectName("OutputLine")
        self.bwlayout.addWidget(self.OutputLine)
        self.BrowseButton = QtWidgets.QToolButton(self.ButtonsWidget)
        self.BrowseButton.setObjectName("BrowseButton")
        self.bwlayout.addWidget(self.BrowseButton)
        self.FileIOLayout.addWidget(self.ButtonsWidget)
        self.fiolayout.addLayout(self.FileIOLayout)
        self.MainDialogLayout.addWidget(self.FileIOWidget)
        self.TopLine = QtWidgets.QFrame(MainDialog)
        self.TopLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.TopLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.TopLine.setObjectName("TopLine")
        self.MainDialogLayout.addWidget(self.TopLine)
        self.OpsWidget = QtWidgets.QWidget(MainDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpsWidget.sizePolicy().hasHeightForWidth())
        self.OpsWidget.setSizePolicy(sizePolicy)
        self.OpsWidget.setObjectName("OpsWidget")
        self.owlayout = QtWidgets.QHBoxLayout(self.OpsWidget)
        self.owlayout.setContentsMargins(0, 0, 0, 0)
        self.owlayout.setObjectName("owlayout")
        self.XMLWidget = QtWidgets.QWidget(self.OpsWidget)
        self.XMLWidget.setObjectName("XMLWidget")
        self.xwlayout = QtWidgets.QVBoxLayout(self.XMLWidget)
        self.xwlayout.setContentsMargins(0, 0, 0, 0)
        self.xwlayout.setSpacing(1)
        self.xwlayout.setObjectName("xwlayout")
        self.XMLLabel = QtWidgets.QLabel(self.XMLWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.XMLLabel.sizePolicy().hasHeightForWidth())
        self.XMLLabel.setSizePolicy(sizePolicy)
        self.XMLLabel.setObjectName("XMLLabel")
        self.xwlayout.addWidget(self.XMLLabel)
        self.XMLLayout = QtWidgets.QVBoxLayout()
        self.XMLLayout.setSpacing(1)
        self.XMLLayout.setObjectName("XMLLayout")
        self.RbManyToMany = QtWidgets.QRadioButton(self.XMLWidget)
        self.RbManyToMany.setObjectName("RbManyToMany")
        self.XMLLayout.addWidget(self.RbManyToMany)
        self.RbManyToOne = QtWidgets.QRadioButton(self.XMLWidget)
        self.RbManyToOne.setObjectName("RbManyToOne")
        self.XMLLayout.addWidget(self.RbManyToOne)
        self.xwlayout.addLayout(self.XMLLayout)
        self.owlayout.addWidget(self.XMLWidget)
        self.LeftLine = QtWidgets.QFrame(self.OpsWidget)
        self.LeftLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.LeftLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LeftLine.setObjectName("LeftLine")
        self.owlayout.addWidget(self.LeftLine)
        self.DimWidget = QtWidgets.QWidget(self.OpsWidget)
        self.DimWidget.setObjectName("DimWidget")
        self.dwlayout = QtWidgets.QVBoxLayout(self.DimWidget)
        self.dwlayout.setContentsMargins(0, 0, 0, 0)
        self.dwlayout.setSpacing(1)
        self.dwlayout.setObjectName("dwlayout")
        self.DimLabel = QtWidgets.QLabel(self.DimWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DimLabel.sizePolicy().hasHeightForWidth())
        self.DimLabel.setSizePolicy(sizePolicy)
        self.DimLabel.setObjectName("DimLabel")
        self.dwlayout.addWidget(self.DimLabel)
        self.DimWidgetLayout = QtWidgets.QVBoxLayout()
        self.DimWidgetLayout.setObjectName("DimWidgetLayout")
        self.Rb2D = QtWidgets.QRadioButton(self.DimWidget)
        self.Rb2D.setObjectName("Rb2D")
        self.DimWidgetLayout.addWidget(self.Rb2D)
        self.Rb3D = QtWidgets.QRadioButton(self.DimWidget)
        self.Rb3D.setObjectName("Rb3D")
        self.DimWidgetLayout.addWidget(self.Rb3D)
        self.dwlayout.addLayout(self.DimWidgetLayout)
        self.owlayout.addWidget(self.DimWidget)
        self.MiddleLine = QtWidgets.QFrame(self.OpsWidget)
        self.MiddleLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.MiddleLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.MiddleLine.setObjectName("MiddleLine")
        self.owlayout.addWidget(self.MiddleLine)
        self.ContentWidget = QtWidgets.QWidget(self.OpsWidget)
        self.ContentWidget.setObjectName("ContentWidget")
        self.cwlayout = QtWidgets.QVBoxLayout(self.ContentWidget)
        self.cwlayout.setContentsMargins(0, 0, 0, 0)
        self.cwlayout.setSpacing(1)
        self.cwlayout.setObjectName("cwlayout")
        self.ContentsLabel = QtWidgets.QLabel(self.ContentWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ContentsLabel.sizePolicy().hasHeightForWidth())
        self.ContentsLabel.setSizePolicy(sizePolicy)
        self.ContentsLabel.setObjectName("ContentsLabel")
        self.cwlayout.addWidget(self.ContentsLabel)
        self.ContentWidgetLayout = QtWidgets.QVBoxLayout()
        self.ContentWidgetLayout.setObjectName("ContentWidgetLayout")
        self.RbMarkers = QtWidgets.QRadioButton(self.ContentWidget)
        self.RbMarkers.setObjectName("RbMarkers")
        self.ContentWidgetLayout.addWidget(self.RbMarkers)
        self.RbROIs = QtWidgets.QRadioButton(self.ContentWidget)
        self.RbROIs.setObjectName("RbROIs")
        self.ContentWidgetLayout.addWidget(self.RbROIs)
        self.RbMarkersAndROIs = QtWidgets.QRadioButton(self.ContentWidget)
        self.RbMarkersAndROIs.setObjectName("RbMarkersAndROIs")
        self.ContentWidgetLayout.addWidget(self.RbMarkersAndROIs)
        self.cwlayout.addLayout(self.ContentWidgetLayout)
        self.owlayout.addWidget(self.ContentWidget)
        self.RightLine = QtWidgets.QFrame(self.OpsWidget)
        self.RightLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.RightLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.RightLine.setObjectName("RightLine")
        self.owlayout.addWidget(self.RightLine)
        self.ScalingWidget = QtWidgets.QWidget(self.OpsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScalingWidget.sizePolicy().hasHeightForWidth())
        self.ScalingWidget.setSizePolicy(sizePolicy)
        self.ScalingWidget.setObjectName("ScalingWidget")
        self.swlayout = QtWidgets.QVBoxLayout(self.ScalingWidget)
        self.swlayout.setContentsMargins(0, 0, 0, 0)
        self.swlayout.setSpacing(1)
        self.swlayout.setObjectName("swlayout")
        self.ScalingLabel = QtWidgets.QLabel(self.ScalingWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScalingLabel.sizePolicy().hasHeightForWidth())
        self.ScalingLabel.setSizePolicy(sizePolicy)
        self.ScalingLabel.setObjectName("ScalingLabel")
        self.swlayout.addWidget(self.ScalingLabel)
        self.ScalingLayout = QtWidgets.QFormLayout()
        self.ScalingLayout.setHorizontalSpacing(1)
        self.ScalingLayout.setObjectName("ScalingLayout")
        self.XLabel = QtWidgets.QLabel(self.ScalingWidget)
        self.XLabel.setObjectName("XLabel")
        self.ScalingLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.XLabel)
        self.YLabel = QtWidgets.QLabel(self.ScalingWidget)
        self.YLabel.setObjectName("YLabel")
        self.ScalingLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.YLabel)
        self.ZLabel = QtWidgets.QLabel(self.ScalingWidget)
        self.ZLabel.setObjectName("ZLabel")
        self.ScalingLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ZLabel)
        self.XLine = QtWidgets.QLineEdit(self.ScalingWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.XLine.sizePolicy().hasHeightForWidth())
        self.XLine.setSizePolicy(sizePolicy)
        self.XLine.setMaximumSize(QtCore.QSize(80, 16777215))
        self.XLine.setObjectName("XLine")
        self.ScalingLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.XLine)
        self.YLine = QtWidgets.QLineEdit(self.ScalingWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.YLine.sizePolicy().hasHeightForWidth())
        self.YLine.setSizePolicy(sizePolicy)
        self.YLine.setMaximumSize(QtCore.QSize(80, 16777215))
        self.YLine.setObjectName("YLine")
        self.ScalingLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.YLine)
        self.ZLine = QtWidgets.QLineEdit(self.ScalingWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ZLine.sizePolicy().hasHeightForWidth())
        self.ZLine.setSizePolicy(sizePolicy)
        self.ZLine.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ZLine.setObjectName("ZLine")
        self.ScalingLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ZLine)
        self.swlayout.addLayout(self.ScalingLayout)
        self.owlayout.addWidget(self.ScalingWidget)
        self.MainDialogLayout.addWidget(self.OpsWidget)
        self.BottomLine = QtWidgets.QFrame(MainDialog)
        self.BottomLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.BottomLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.BottomLine.setObjectName("BottomLine")
        self.MainDialogLayout.addWidget(self.BottomLine)
        self.ConvertButton = QtWidgets.QPushButton(MainDialog)
        self.ConvertButton.setObjectName("ConvertButton")
        self.MainDialogLayout.addWidget(self.ConvertButton)
        self.mdlayout.addLayout(self.MainDialogLayout)

        self.retranslateUi(MainDialog)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)
        self.makeConnections()

    def retranslateUi(self, MainDialog):
        _translate = QtCore.QCoreApplication.translate
        MainDialog.setWindowTitle(_translate("MainDialog", "FIJI Data Converter"))
        self.ListLabel.setText(_translate("MainDialog", "Input Files:"))
        self.AddButton.setText(_translate("MainDialog", "Add..."))
        self.RemoveButton.setText(_translate("MainDialog", "Remove"))
        self.OutputLabel.setText(_translate("MainDialog", "Output Location:"))
        self.BrowseButton.setText(_translate("MainDialog", "..."))
        self.XMLLabel.setText(_translate("MainDialog", "XML Collation:"))
        self.RbManyToMany.setText(_translate("MainDialog", "Many to Many"))
        self.RbManyToOne.setText(_translate("MainDialog", "Many to One"))
        self.DimLabel.setText(_translate("MainDialog", "Dimensionality:"))
        self.Rb2D.setText(_translate("MainDialog", "2D"))
        self.Rb3D.setText(_translate("MainDialog", "3D"))
        self.ContentsLabel.setText(_translate("MainDialog", "Contents:"))
        self.RbMarkers.setText(_translate("MainDialog", "Markers"))
        self.RbROIs.setText(_translate("MainDialog", "Regions"))
        self.RbMarkersAndROIs.setText(_translate("MainDialog", "Markers and Regions"))
        self.ScalingLabel.setText(_translate("MainDialog", "Scaling (\u03BCm/px):"))
        self.XLabel.setText(_translate("MainDialog", "X:"))
        self.YLabel.setText(_translate("MainDialog", "Y:"))
        self.ZLabel.setText(_translate("MainDialog", "Z:"))
        self.ConvertButton.setText(_translate("MainDialog", "Convert"))

	#adds items to the FileListWidget
    def on_AddButton_clicked(self):
        #make a file dialog
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.ExistingFiles)
        filters = list()
        filters.append("Marker files (*.xml)")
        filters.append("Exported ROI data (*.txt)")
        dlg.setNameFilters(filters)
        
        if dlg.exec_():
            #get unique list of selected files
            selected = list()
            selected = dlg.selectedFiles()
            selected = list(set(selected))
            #get list of files already in list widget
            existing = list()
            for ind in range(self.FileListWidget.count()):
                existing.append(self.FileListWidget.item(ind).text())
            #remove files already in list widget from list of selected files
            for item in existing:
                if item in selected:
                    selected.remove(item)
            #add new items
            self.FileListWidget.addItems(selected)
    
    #removes an item from the FileListWidget
    def on_RemoveButton_clicked(self):
        removeThese = self.FileListWidget.selectedItems()
        for item in removeThese:
            self.FileListWidget.takeItem(self.FileListWidget.row(item))
    
    #opens a file explorer dialog to let the user select a folder
    def on_BrowseButton_clicked(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.DirectoryOnly)
        filenames = list()
        
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            self.OutputLine.setText(filenames[0])
    
    #disables ZLine when checked
    def on_Rb2D_selected(self, selected):
        if selected:
            palette = QPalette()
            palette.setColor(QPalette.Base, Qt.gray)
            palette.setColor(QPalette.Text, Qt.darkGray)
            self.ZLine.setPalette(palette)
            self.ZLine.setReadOnly(True)
    
    #enables ZLine when checked
    def on_Rb3D_selected(self, selected):
        if selected:
            palette = QPalette()
            palette.setColor(QPalette.Base, Qt.white)
            palette.setColor(QPalette.Text, Qt.black)
            self.ZLine.setPalette(palette)
            self.ZLine.setReadOnly(False)
    
    #performs conversion
    def on_ConvertButton_clicked(self):
        #check all inputs are given
        chkr = self.checkSetup()
        opaths = list()
        if not chkr.check():
            #MessageBox to inform user of missing inputs
            msg = "Please choose settings for:\r\n\r\n"
            msg += chkr.getErrors()
            errMsg = QMessageBox()
            errMsg.setIcon(QMessageBox.Critical)
            errMsg.setText(msg)
            errMsg.setWindowTitle("Invalid Settings")
            errMsg.exec_()
            
        else:
            #put data from inputs into converter object
            files = list()
            for ind in range(self.FileListWidget.count()):
                files.append(self.FileListWidget.item(ind).text())
            convertops = Converter()
            convertops.files = files
            convertops.output = self.OutputLine.text()
            convertops.doManyXML = self.RbManyToMany.isChecked()
            convertops.do3D = self.Rb3D.isChecked()
            if self.RbMarkersAndROIs.isChecked():
                convertops.doMarkers = True
                convertops.doROIs = True
            elif self.RbMarkers.isChecked():
                convertops.doMarkers = True
            else:
                convertops.doROIs = True
            convertops.scaleX = float(self.XLine.text())
            convertops.scaleY = float(self.YLine.text())
            if convertops.do3D:
                convertops.ZSpacing = float(self.ZLine.text())
            #do the conversion
            self.ConvertButton.setText("Converting data...")
            self.dialogDisabled(True)
            data = convertops.convert()
            for datum in data:
                opaths.append(datum[0])
                if path.exists(datum[0]):
                    overwriteBox = QMessageBox()
                    overwriteBox.setIcon(QMessageBox.Warning)
                    overwriteBox.setText(datum[0] + " already exists. Overwrite?")
                    overwriteBox.setWindowTitle("File Already Exists")
                    overwriteBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                    if overwriteBox.exec_() == QMessageBox.Yes:
                        convertops.writeFile(datum[0], datum[1])
                else:
                    convertops.writeFile(datum[0], datum[1])
            doneBox = QMessageBox()
            doneBox.setIcon(QMessageBox.Information)
            doneBox.setText("Conversion complete")
            doneBox.setStandardButtons(QMessageBox.Ok)
            doneBox.exec_()
            ui = Ui_mdgForm()
            tacmsgbox = QtWidgets.QDialog()
            ui.setupUi(tacmsgbox)
            ui.addfromlist(opaths)
            _ = tacmsgbox.exec_()
            self.FileListWidget.clear()
            self.OutputLine.clear()
            self.ConvertButton.setText("Convert")
            self.dialogDisabled(False)

    
    def makeConnections(self):
        self.AddButton.clicked.connect(self.on_AddButton_clicked)
        self.RemoveButton.clicked.connect(self.on_RemoveButton_clicked)
        self.BrowseButton.clicked.connect(self.on_BrowseButton_clicked)
        self.Rb2D.toggled.connect(self.on_Rb2D_selected)
        self.Rb3D.toggled.connect(self.on_Rb3D_selected)
        self.ConvertButton.clicked.connect(self.on_ConvertButton_clicked)
    
    def checkSetup(self):
        #make object to hold check info
        chkr = SetupCheckErr()
        #must have at least one input file
        if self.FileListWidget.count() >= 1:
            chkr.inputs = True
        #must have an output location
        if len(self.OutputLine.text()) >= 1:
            chkr.output = True
        #must have XML option selected
        xmlBool = (
            self.RbManyToMany.isChecked()
            or self.RbManyToOne.isChecked()
        )
        if xmlBool:
            chkr.XMLChecked = True
        #must have dimension selected
        dimBool = (
            self.Rb2D.isChecked()
            or self.Rb3D.isChecked()
        )
        if dimBool:
            chkr.dimChecked = True
        #must have contents selected
        contentBool = (
            self.RbMarkers.isChecked()
            or self.RbROIs.isChecked()
            or self.RbMarkersAndROIs.isChecked()
        )
        if contentBool:
            chkr.contentsChecked = True
        #must have scaling entered
        scalingBool = (
            len(self.XLine.text()) > 0
            and len(self.YLine.text()) > 0
        )
        if self.Rb3D.isChecked():
            scalingBool = scalingBool and len(self.ZLine.text()) > 0
        if scalingBool:
            chkr.scaling = True
        return chkr

    def dialogDisabled(self, disabled):
        self.FileIOWidget.setDisabled(disabled)
        self.OpsWidget.setDisabled(disabled)
        self.ConvertButton.setDisabled(disabled)
