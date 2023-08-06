from PySide6.QtWidgets import QMessageBox as QMB
from os.path import basename
import xml.etree.ElementTree as ET

indent = 7

def makedlg(allfound, basic, detail):
    msg = QMB()
    if allfound:
        msg.setIcon(QMB.Information)
        msg.setWindowTitle("SPARC Vocabulary Terms Found")
    else:
        msg.setIcon(QMB.Critical)
        msg.setWindowTitle("SPARC Vocabulary Terms Missing")
    msg.setText(basic)
    if not allfound:
        msg.setDetailedText(detail)
    msg.setStandardButtons(QMB.Close)
    return msg

def checkelems(root, elemname):
    empty = list()
    for elem in root.findall("./" + elemname):
        if len(elem.findall("./property/[@name=\"TraceAssociation\"]")) < 1:
            empty.append(elem.attrib["name"])
    return empty

def checkfiles(flist):
    allhavecontour = True
    allhavemarker = True
    allfound = False
    basic = str()
    detail = str()
    for fpath in flist:
        tree = ET.parse(fpath)
        root = tree.getroot()
        totalc = len(root.findall("./contour"))
        fecontours = checkelems(root, "contour")
        cfound = len(fecontours) < totalc
        totalf = len(root.findall("./marker"))
        femarkers = checkelems(root, "marker")
        mfound = len(femarkers) < totalf
        if not cfound:
            allhavecontour = False
        if not mfound:
            allhavemarker = False
        if not (cfound and mfound):
            detail += basename(fpath) + "\n"
            if len(fecontours) > 0:
                detail += " "*indent + "contours:\n"
            for contour in fecontours:
                detail += " "*indent*2 + contour + "\n"
            if len(femarkers) > 0:
                detail += " "*indent + "markers:\n"
            for marker in femarkers:
                detail += " "*indent*2 + marker + "\n"
            detail += "\n"
    if (not allhavecontour) and (not allhavemarker):
        basic = "Missing SPARC Vocabulary Terms for Contours and Markers. Contact sparc@mbfbioscience.com for assistance with curating this data."
    elif not allhavecontour:
        basic = "Missing SPARC Vocabulary Terms for Contours. Contact sparc@mbfbioscience.com for assistance with curating this data."
    elif not allhavemarker:
        basic = "Missing SPARC Vocabulary Terms for Markers. Contact sparc@mbfbioscience.com for assistance with curating this data."
    else:
        allfound = True
        basic = "SPARC Vocabulary Terms found for Contours and Markers."
    return makedlg(allfound, basic, detail)

def maketacchkdlg(flist):
    return checkfiles(flist)
