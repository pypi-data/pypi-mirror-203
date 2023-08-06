from xml.etree import ElementTree
from csv import reader


class ReaderMixin:
    
    def _verifyXML(self, filename):
        if type(filename) is str and ".xml" in filename:
            return True
        else:
            return False
    
    def readXMLImage(self, filename):
        if self._verifyXML(filename):
            tree = ElementTree.parse(filename)
            root = tree.getroot()
            if root[0][0].tag == 'Image_Filename':
                return root[0][0].text
            else:
                return None
        else:
            return None
    
    def readXMLMarkers(self, filename, append = None):
        if self._verifyXML(filename):
            tree = ElementTree.parse(filename)
            root = tree.getroot()
            data = dict()
            if type(append) is dict:
                data = append
            for ind in range(1, len(root[1])):
                markerType = int(root[1][ind][0].text)
                if markerType not in data:
                    data[markerType] = list()
                for marker in range(1, len(root[1][ind])):
                    coords = (float(root[1][ind][marker][0].text), float(root[1][ind][marker][1].text), float(root[1][ind][marker][2].text))
                    data[markerType].append(coords)
            return data
        else:
            return None
    
    def readROI(self, filename):
        if type(filename) is str and ".txt" in filename:
            roi = list()
            with open(filename, newline="") as csvfile:
                rdr = reader(csvfile, delimiter="\t")
                for row in rdr:
                    coords = list()
                    for coord in row:
                        coords.append(int(coord))
                    roi.append(tuple(coords))
            return roi
        else:
            return None
