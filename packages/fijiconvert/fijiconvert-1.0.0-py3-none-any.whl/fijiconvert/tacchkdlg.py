from PyQt5.QtWidgets import QMessageBox as QMB
from os.path import basename
import xml.etree.ElementTree as ET

def makedlg(allfound, basic, detail):
    #print(" allfound: " + str(allfound))
    #print(" basic:\n" + basic)
    #print(" detail:\n" + detail)
    msg = QMB()
    #print("    qmb")
    if allfound:
        msg.setIcon(QMB.Information)
        #print("    all: seticon")
        msg.setWindowTitle("SPARC Vocabulary Terms Found")
        #print("    all: setwindowtitle")
    else:
        msg.setIcon(QMB.Critical)
        #print("    not: seticon")
        msg.setWindowTitle("SPARC Vocabulary Terms Missing")
        #print("    not: setwindowtitle")
    msg.setText(basic)
    #print("    settext")
    if not allfound:
        msg.setDetailedText(detail)
        #print("    setdetail")
    msg.setStandardButtons(QMB.Close)
    #print("    setbuttons")
    return msg

def checkelems(root, elemname):
    empty = list()
    for elem in root.findall("./" + elemname):
        if len(elem.findall("./property/[@name=\"TraceAssociation\"]")) < 1:
            empty.append(elem.attrib["name"])
    return empty

def checkfiles(flist):
    #print(flist)
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
        print("contours: " + str(len(fecontours)) + " of " + str(totalc))
        print("markers: " + str(len(femarkers)) + " of " + str(totalf))
        if not cfound:
            allhavecontour = False
        if not mfound:
            allhavemarker = False
        if not (cfound and mfound):
            detail += basename(fpath) + "\n"
            if len(fecontours) > 0:
                detail += " "*4 + "contours:\n"
            for contour in fecontours:
                detail += " "*8 + contour + "\n"
            if len(femarkers) > 0:
                detail += " "*4 + "markers:\n"
            for marker in femarkers:
                detail += " "*8 + marker + "\n"
            detail += "\n"
    if (not allhavecontour) and (not allhavemarker):
        #print("missing both")
        basic = "Missing SPARC Vocabulary Terms for Contours and Markers. Contact sparc@mbfbioscience.com for assistance with curating this data."
    elif not allhavecontour:
        #print("missing contour")
        basic = "Missing SPARC Vocabulary Terms for Contours. Contact sparc@mbfbioscience.com for assistance with curating this data."
    elif not allhavemarker:
        #print("missing marker")
        basic = "Missing SPARC Vocabulary Terms for Markers. Contact sparc@mbfbioscience.com for assistance with curating this data."
    else:
        allfound = True
        basic = "SPARC Vocabulary Terms found for Contours and Markers."
    return makedlg(allfound, basic, detail)

def maketacchkdlg(flist):
    return checkfiles(flist)
