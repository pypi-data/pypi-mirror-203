from . reader import ReaderMixin
from . writer import WriterMixin


class Converter(ReaderMixin, WriterMixin):
    
    markers = {
        1: "Dot", 
        2: "OpenCircle", 
        3: "Cross", 
        4: "Plus", 
        5: "OpenUpTriangle", 
        6: "OpenDownTriangle", 
        7: "OpenSquare", 
        8: "Asterisk", 
        9: "OpenDiamond", 
        10: "FilledStar", 
        11: "FilledCircle", 
        12: "FilledUpTriangle", 
        13: "FilledDownTriangle", 
        14: "FilledSquare", 
        15: "FilledDiamond", 
        16: "Flower", 
        17: "OpenStar", 
        18: "DoubleCircle", 
        19: "Circle1", 
        20: "Circle2", 
        21: "Circle3", 
        22: "Circle4", 
        23: "Circle5", 
        24: "Circle6", 
        25: "Circle7", 
        26: "Circle8", 
        27: "Circle9", 
        28: "Flower2", 
        29: "SnowFlake", 
        30: "OpenFinial", 
        31: "FilledFinial", 
        32: "MalteseCross", 
        33: "FilledQuadStar", 
        34: "OpenQuadStar", 
        35: "Flower3", 
        36: "Pinwheel", 
        37: "TexacoStar", 
        38: "ShadedStar", 
        39: "SkiBasket", 
        40: "Clock", 
        41: "ThinArrow", 
        42: "ThickArrow", 
        43: "SquareGunSight", 
        44: "GunSight", 
        45: "TriStar", 
        46: "NinjaStar", 
        47: "KnightsCross", 
        48: "Splat", 
        49: "CircleArrow", 
        50: "CircleCross"
    }
    
    boilerplateXML = {
        'header': ('<?xml version="1.0" encoding="ISO-8859-1"?>\r\n'
                         '<mbf version="4.0" xmlns="http://www.mbfbioscience.com/2007/neurolucida"'
                         ' xmlns:nl="http://www.mbfbioscience.com/2007/neurolucida" appname="Neurolucida"'
                         ' appversion="2018.2.2 (64-bit)">\r\n<description><![CDATA[]]></description>\r\n'
                        ), 
        'footer': '</mbf>\r\n', 
        'contour props': ('  <property name="GUID"><s></s></property>\r\n'
                                     '  <property name="FillDensity"><n>0</n></property>\r\n'
                                     '  <resolution>1.000000</resolution>\r\n'
                                    )
    }
    
    def __init__(self):
        self.files = list()
        self.markerFiles = list()
        self.roiFiles = list()
        self.output = str()
        self.doManyXML = False
        self.do3D = False
        self.doMarkers = False
        self.doROIs = False
        self.scaleX = 1.0
        self.scaleY = 1.0
        self.ZSpacing = 0.0
    
    def propStr(self):
        #holds string
        retstr = str()
        #go through bools
        if self.doManyXML:
            retstr += "XML:\t\t\tto Many\r\n"
        else:
            retstr += "XML:\t\t\tto One\r\n"
        if self.do3D:
            retstr += "Dimensionality:\t\t3D\r\n"
        else:
            retstr += "Dimensionality:\t\t2D\r\n"
        if self.doMarkers:
            retstr += "Markers:\t\t\tYes\r\n"
        else:
            retstr += "Markers:\t\t\tNo\r\n"
        if self.doROIs:
            retstr += "Regions:\t\t\tYes\r\n"
        else:
            retstr += "Regions:\t\t\tNo\r\n"
        #whitespace
        retstr += "\r\n"
        #go through scaling data
        retstr += "X: " + str(self.scaleX) + "\r\n"
        retstr += "Y: " + str(self.scaleY) + "\r\n"
        if self.do3D:
            retstr += "Z: " + str(self.ZSpacing) + "\r\n"
        else:
            retstr += "Z: " + "N/A\r\n"
        #whitespace
        retstr += "\r\n"
        #output path
        retstr += "Output: " + self.output + "\r\n"
        #whitespace
        retstr += "\r\n"
        #input files
        retstr += "Inputs:\r\n"
        for file in self.files:
            retstr += file + "\r\n"
        return retstr

    def _convertMarkers_toMany(self):
        convertedData = list()
        for ind in range(len(self.markerFiles)):
            image = self.readXMLImage(self.markerFiles[ind])
            data = self.readXMLMarkers(self.markerFiles[ind])
            for markerType in list(data.keys()):
                for markerPoint in range(len(data[markerType])):
                    newPoint = (data[markerType][markerPoint][0] * self.scaleX,
                                       data[markerType][markerPoint][1] * self.scaleY * -1.0, 
                                       data[markerType][markerPoint][2] * self.ZSpacing * -1.0)
                    data[markerType][markerPoint] = newPoint
            filefactsStr = self.xmlFilefactsBlock(1)
            imageStr = self.xmlImageBlock([image], (self.scaleX, self.scaleY))
            markerStr = ""
            for markerType in list(data.keys()):
                markerStr += self.xmlMarkerBlock(markerType, data[markerType], self.markers)
            filenameStr = self.output + "/" + self.markerFiles[ind].strip(".xml").rsplit("/", 1)[1] + "_markers.xml"
            bodyStr = self.boilerplateXML["header"] + filefactsStr + imageStr + markerStr + self.boilerplateXML["footer"]
            convertedData.append((filenameStr, bodyStr))
        return convertedData
            
    def _convertMarkers_toOne(self):
        images = list()
        data = dict()
        for ind in range(len(self.markerFiles)):
            images.append(self.readXMLImage(self.markerFiles[ind]))
            data = self.readXMLMarkers(self.markerFiles[ind], data)
            for markerType in list(data.keys()):
                for markerPoint in range(len(data[markerType])):
                    newPoint = (data[markerType][markerPoint][0] * self.scaleX,
                                       data[markerType][markerPoint][1] * self.scaleY * -1.0, 
                                       data[markerType][markerPoint][2] * self.ZSpacing * -1.0)
                    data[markerType][markerPoint] = newPoint                      
        filefactsStr = self.xmlFilefactsBlock(1)
        imageStr = self.xmlImageBlock(images, (self.scaleX, self.scaleY))
        markerStr = ""
        for markerType in list(data.keys()):
                markerStr += self.xmlMarkerBlock(markerType, data[markerType], self.markers)
        filenameStr = self.output + "/" + self.markerFiles[0].strip(".xml").rsplit("/", 1)[1] + "_markers.xml"
        bodyStr = self.boilerplateXML["header"] + filefactsStr + imageStr + markerStr + self.boilerplateXML["footer"]
        return (filenameStr, bodyStr)
    
    def _convertROIs_toMany(self):
        convertedData = list()
        for ind in range(len(self.roiFiles)):
            roi = self.readROI(self.roiFiles[ind])
            for coord in range(len(roi)):
                newPoint = (roi[coord][0] * self.scaleX, 
                                   roi[coord][1] * self.scaleY * -1.0)
                roi[coord] = newPoint
                if self.do3D:
                    roi[coord] = roi[coord] + (ind * self.ZSpacing, ind + 1)
            filenameStr = self.output + "/" + self.roiFiles[ind].strip(".txt").rsplit("/", 1)[1] + "_rois.xml"
            if self.do3D:
                filefactsStr = self.xmlFilefactsBlock(len(self.roiFiles), self.ZSpacing)
            else:
                filefactsStr = self.xmlFilefactsBlock(1)
            roiStr = self.xmlContourBlock(ind + 1, roi, self.boilerplateXML["contour props"])
            bodyStr = self.boilerplateXML["header"] + filefactsStr + roiStr + self.boilerplateXML["footer"]
            convertedData.append((filenameStr, bodyStr))
        return convertedData
    
    def _convertROIs_toOne(self):
        filenameStr = self.output + "/" + self.roiFiles[0].strip(".txt").rsplit("/", 1)[1] + "_rois.xml"
        if self.do3D:
            filefactsStr = self.xmlFilefactsBlock(len(self.roiFiles), self.ZSpacing)
        else:
            filefactsStr = self.xmlFilefactsBlock(1)
        roiStr = ""
        for ind in range(len(self.roiFiles)):
            roi = self.readROI(self.roiFiles[ind])
            for coord in range(len(roi)):
                newPoint = (roi[coord][0] * self.scaleX, 
                                   roi[coord][1] * self.scaleY * -1.0)
                roi[coord] = newPoint
                if self.do3D:
                    roi[coord] = roi[coord] + (ind * self.ZSpacing, ind + 1)
            roiStr += self.xmlContourBlock(ind + 1, roi, self.boilerplateXML["contour props"])
        bodyStr = self.boilerplateXML["header"] + filefactsStr + roiStr + self.boilerplateXML["footer"]
        return (filenameStr, bodyStr)

    def convert(self, saveSettings = False):
        if saveSettings:
            with open(self.output + "\\settings.txt", "w") as file:
                file.write(self.propStr())
        data = list()
        for file in self.files:
            if ".xml" in file:
                self.markerFiles.append(file)
            elif ".txt" in file:
                self.roiFiles.append(file)
        if self.doMarkers:
            if self.doManyXML:
                data.extend(self._convertMarkers_toMany())
            else:
                data.append(self._convertMarkers_toOne())
        if self.doROIs:
            if self.doManyXML:
                data.extend(self._convertROIs_toMany())
            else:
                data.append(self._convertROIs_toOne())
        return data
