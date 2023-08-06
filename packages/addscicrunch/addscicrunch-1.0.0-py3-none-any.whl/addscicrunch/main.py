import sys
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom
from os.path import basename
from PySide6.QtWidgets import QWidget, QApplication, QTableView, QLabel, QComboBox, QLineEdit, QFileDialog
from PySide6 import QtCore
from PySide6.QtCore import Signal, Slot, Qt, QObject
from . gui_output import Ui_mdgForm
from . static import StaticData as SD
from . tacchkdlg import maketacchkdlg
from . AgeSelector import AgeSelector

class MainWindow(QWidget):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_mdgForm()
        self.ui.setupUi(self)
        self.tblFiles = self.ui.tblFiles
        self.fpaths = list()
        self.saved = list()
        self.ui.btnAdd.clicked.connect(self.onBtnAdd)
        self.ui.btnRemove.clicked.connect(self.onBtnRemove)
        self.ui.btnSave.clicked.connect(self.onBtnSave)
        self.lsSpecies = SD.subject["species"]
        self.lsSex = SD.subject["sex"]
        self.lsOrgan = SD.atlas["organ"]
        self.dcLabel = SD.atlas["label"]
        self.dcLinkToSpecies = SD.specieslinks["reverse"]
        self.dcSpeciesToLink = SD.specieslinks["forward"]

    #@Slot(int)
    def onWidgetSignal(self):
        wdg = self.sender()
        ind = self.tblFiles.indexAt(wdg.pos())
        if ind.column() == 5:
            self.adjustLabelComboBox(ind.row())
        self.setRowColors(ind.row())
        self.saved[ind.row()] = False

    def onBtnAdd(self):
        caption = "Add XML Files"
        directory = "C:\\"
        filefilt = "XML Files (*.xml)"
        newlist, _ = QFileDialog.getOpenFileNames(caption=caption, dir=directory, filter=filefilt)
        newset = set(newlist)
        curset = set(self.fpaths)
        newset = curset.union(newset)
        newlist = list(newset)
        self.addFiles(newlist)

    def onBtnRemove(self):
        inds = self.tblFiles.selectedIndexes()
        keeprows = set(range(self.tblFiles.rowCount()))
        for ind in inds:
            if ind.row() in keeprows:
                keeprows.remove(ind.row())
        newfpaths = [self.fpaths[x] for x in keeprows]
        self.addFiles(newfpaths)

    def onBtnSave(self):
        changedfiles = list()
        for row in range(self.tblFiles.rowCount()):
            if self.isRowReady(row) and not self.saved[row]:
                fpath = self.fpaths[row]
                root = ET.parse(fpath).getroot()
                sparcdata = root.find("sparcdata")
                subject = None
                atlas = None
                if sparcdata is None:
                    sparcdata = ET.SubElement(root, "sparcdata")
                    subject = ET.SubElement(sparcdata, "subject")
                    atlas = ET.SubElement(sparcdata, "atlas")
                    subject.set("species","")
                    subject.set("subjectid","")
                    subject.set("sex","")
                    subject.set("age","")
                    atlas.set("organ","")
                    atlas.set("label","")
                    atlas.set("rootid","")
                else:
                    subject = sparcdata.find("subject")
                    if subject is None:
                        subject = ET.SubElement(sparcdata, "subject")
                        subject.set("species","")
                        subject.set("subjectid","")
                        subject.set("sex","")
                        subject.set("age","")
                    atlas = sparcdata.find("atlas")
                    if atlas is None:
                        atlas = ET.SubElement(sparcdata, "atlas")
                        atlas.set("organ","")
                        atlas.set("label","")
                        atlas.set("rootid","")
                for col in range(1,self.tblFiles.columnCount()+1):
                    wdg = self.tblFiles.cellWidget(row,col)
                    if col == 1:
                        subject.attrib["species"] = self.dcSpeciesToLink[wdg.currentText()]
                    elif col == 2:
                        subject.attrib["subjectid"] = wdg.text()
                    elif col == 3:
                        subject.attrib["sex"] = wdg.currentText()
                    elif col == 4:
                        subject.attrib["age"] = wdg.getStr()
                    elif col == 5:
                        atlas.attrib["organ"] = wdg.currentText()
                    elif col == 6:
                        atlas.attrib["label"] = wdg.currentText()
                    elif col == 7:
                        organ = atlas.attrib["organ"]
                        dcorganlinks = DS.organlinks[organ]
                        atlas.attrib["rootid"] = dcorganlinks[atlas.attrib["label"]]
                xmlstr = minidom.parseString(ET.tostring(root)).toxml()
                splist = re.split(r"\n( )*",xmlstr)
                xmlstr = ""
                for i in range(len(splist)):
                    if i % 2 == 0:
                        xmlstr += splist[i]
                xmlstr = minidom.parseString(xmlstr).toprettyxml(indent="  ")
                with open(fpath,"w") as f:
                    f.write(xmlstr)
                changedfiles.append(fpath)
                self.setRowSaved(row)
        tacmsgbox = maketacchkdlg(changedfiles)
        _ = tacmsgbox.exec()

    def adjustLabelComboBox(self,row):
        cmbLabel = QComboBox()
        self.setWidgetColor(cmbLabel,"white")
        organ = self.tblFiles.cellWidget(row,5).currentText()
        if organ in self.dcLabel.keys():
            lsLabel = self.dcLabel[organ]
            cmbLabel.addItems(lsLabel)
            label = self.checkXMLLabel(self.fpaths[row])
            if label in lsLabel:
                cmbLabel.setCurrentIndex(lsLabel.index(label))
            else:
                cmbLabel.setCurrentIndex(-1)
        cmbLabel.currentIndexChanged.connect(self.onWidgetSignal)
        self.tblFiles.setCellWidget(row,6,cmbLabel)

    def setWidgetColor(self,wdg,color="white"):
        stylestr = "QWidget{background-color:customcolor}"
        if color in ["palegreen","salmon","palegoldenrod","paleturquoise","white"]:
            stylestr = stylestr.replace("customcolor",color)
        wdg.setStyleSheet(stylestr)

    #  0  Filename  QLabel
    #  1  Species   QComboBox    *
    #  2  ID        QLineEdit
    #  3  Sex       QComboBox    *
    #  4  Age       AgeSelector  *
    #  5  Organ     QComboBox    *
    #  6  Label     QComboBox    *
    def addFiles(self, flist):
        self.fpaths.clear()
        self.saved.clear()
        self.tblFiles.clearContents()
        self.tblFiles.setRowCount(len(flist))
        for row in range(self.tblFiles.rowCount()):

            self.saved.append(False)
            
            #get data from XML file
            rowdata = self.checkXML(flist[row])
            
            #0:Filename
            lblFilename = QLabel(basename(rowdata[0]))
            self.setWidgetColor(lblFilename,"white")
            lblFilename.setTextInteractionFlags(
                Qt.TextBrowserInteraction |
                Qt.TextSelectableByKeyboard
            )
            self.tblFiles.setCellWidget(row,0,lblFilename)
            self.fpaths.append(flist[row])
            
            #1:Species
            cmbSpecies = QComboBox()
            self.setWidgetColor(cmbSpecies,"white")
            cmbSpecies.addItems(self.lsSpecies)
            link = rowdata[1]
            if link in self.dcLinkToSpecies.keys():
                species = self.dcLinkToSpecies[link]
                if species in self.lsSpecies:
                    cmbSpecies.setCurrentIndex(self.lsSpecies.index(species))
                else:
                    cmbSpecies.setCurrentIndex(-1)
            cmbSpecies.currentIndexChanged.connect(self.onWidgetSignal)
            self.tblFiles.setCellWidget(row,1,cmbSpecies)
            
            #2:ID
            ledID = QLineEdit(rowdata[2])
            self.setWidgetColor(ledID,"white")
            ledID.editingFinished.connect(self.onWidgetSignal)
            self.tblFiles.setCellWidget(row,2,ledID)
            
            #3:Sex
            cmbSex = QComboBox()
            self.setWidgetColor(cmbSex,"white")
            cmbSex.addItems(self.lsSex)
            if rowdata[3] in self.lsSex:
                cmbSex.setCurrentIndex(self.lsSex.index(rowdata[3]))
            else:
                cmbSex.setCurrentIndex(-1)
            cmbSex.currentIndexChanged.connect(self.onWidgetSignal)
            self.tblFiles.setCellWidget(row,3,cmbSex)
            
            #4:Age
            agsAge = AgeSelector()
            self.setWidgetColor(agsAge,"white")
            agsAge.setData(rowdata[4])
            agsAge.editingFinished.connect(self.onWidgetSignal)
            self.tblFiles.setCellWidget(row,4,agsAge)
            
            #5:Organ
            cmbOrgan = QComboBox()
            self.setWidgetColor(cmbOrgan,"white")
            cmbOrgan.addItems(self.lsOrgan)
            if rowdata[5] in self.lsOrgan:
                cmbOrgan.setCurrentIndex(self.lsOrgan.index(rowdata[5]))
            else:
                cmbOrgan.setCurrentIndex(-1)
            cmbOrgan.currentIndexChanged.connect(self.onWidgetSignal)
            self.tblFiles.setCellWidget(row,5,cmbOrgan)
            
            #6:Label
            self.adjustLabelComboBox(row)
            self.setRowColors(row)
            
        self.tblFiles.resizeColumnsToContents()

    def checkXML(self, fpath):
        itfound = False
        rlist = [None]*self.tblFiles.columnCount()
        rlist[0] = fpath
        for item in ET.parse(fpath).getroot():
            if item.tag == "sparcdata":
                itfound = True
                sdroot = item
                sdfound = False
                atfound = False
                for child in sdroot:
                    if child.tag == "subject":
                        sdfound = True
                        keyset = set(child.attrib.keys())
                        if "species" in keyset:
                            rlist[1] = child.attrib["species"]
                        if "subjectid" in keyset:
                            rlist[2] = child.attrib["subjectid"]
                        if "sex" in keyset:
                            rlist[3] = child.attrib["sex"]
                        if "age" in keyset:
                            rlist[4] = child.attrib["age"]
                    elif child.tag == "atlas":
                        atfound = True
                        keyset = child.attrib.keys()
                        if "organ" in keyset:
                            rlist[5] = child.attrib["organ"]
                        if "label" in keyset:
                            rlist[6] = child.attrib["label"]
                    if sdfound and atfound:
                        break
        return rlist

    def checkXMLLabel(self, fpath):
        itfound = False
        for item in ET.parse(fpath).getroot():
            if item.tag == "sparcdata":
                for child in item:
                    if child.tag == "atlas":
                        keyset = child.attrib.keys()
                        if "label" in keyset:
                            return child.attrib["label"]
        return None

    def setRowSaved(self, row):
        for col in range(self.tblFiles.columnCount()):
            wdg = self.tblFiles.cellWidget(row,col)
            self.setWidgetColor(wdg,"paleturquoise")
        self.tblFiles.cellWidget(row,4).setSaved()
        self.saved[row] = True

    def setRowColors(self, row):
        hasempty = False
        for col in range(self.tblFiles.columnCount()):
            wdg = self.tblFiles.cellWidget(row,col)
            if col in [1,3,5,6]:
                if wdg.currentIndex() < 0:
                    self.setWidgetColor(wdg,"salmon")
                    hasempty = True
                else:
                    self.setWidgetColor(wdg,"white")
            elif col == 2:
                if wdg.text() == "":
                    self.setWidgetColor(wdg,"palegoldenrod")
                    hasempty = True
                else:
                    self.setWidgetColor(wdg,"white")
            elif col == 4:
                if wdg.isEmpty():
                    self.setWidgetColor(wdg,"salmon")
                    hasempty = True
                else:
                    self.setWidgetColor(wdg,"white")
        if not hasempty:
            for col in range(self.tblFiles.columnCount()):
                wdg = self.tblFiles.cellWidget(row,col)
                if col == 4:
                    if wdg.isBlind():
                        wdg.ledNumber.setStyleSheet("QWidget{background-color:#90c390}")
                    else:
                        wdg.ledNumber.setStyleSheet("QWidget{background-color:palegreen}")
                self.setWidgetColor(wdg,"palegreen")

    def isRowFull(self, row):
        for col in range(self.tblFiles.columnCount()):
            wdg = self.tblFiles.cellWidget(row,col)
            if col in [1,3,5,6]:
                if wdg.currentIndex() < 0:
                    return False
            elif col == 2:
                if wdg.text() == "":
                    return False
            elif col == 4:
                if wdg.isEmpty():
                    return False
        return True

    def isRowReady(self, row):
        for col in [1,3,5,6]:
            wdg = self.tblFiles.cellWidget(row,col)
            if wdg.currentIndex() < 0:
                return False
        ags = self.tblFiles.cellWidget(row,4)
        if ags.isEmpty():
            return False
        return True

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


