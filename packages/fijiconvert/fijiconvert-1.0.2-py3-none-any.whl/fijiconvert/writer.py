class WriterMixin:
    #write a single XML string containing a point
    def xmlPointStr(self, coords):
        if len(coords) > 1:
            retstr = '<point x="'
            retstr += '{0:.2f}'.format(coords[0])
            retstr += '" y="'
            retstr += '{0:.2f}'.format(coords[1])
            retstr += '" z="'
            if len(coords) > 2:
                retstr += '{0:.2f}'.format(coords[2])
            else:
                retstr += '0.00'
            retstr += '" d="'
            if len(coords) == 5:
                retstr += '{0:.2f}'.format(coords[4])
            else:
                retstr += '1.00'
            retstr += '" sid="'
            if len(coords) > 3:
                retstr += 'S' + str(coords[3])
            else:
                retstr += 'S1'
            retstr += '"/>'
            return retstr
        else:
            return ""
            
    #write a single XML string containing a marker
    def xmlMarkerStr(self, number, markerRef):
        if (type(markerRef) is dict and
             number >= 1 and
             number < len(markerRef)):
            retstr = '<marker type="'
            retstr += markerRef[number]
            retstr += '" color="#FFFFFF" name="Marker '
            retstr += str(number)
            retstr += '" varicosity="false">'
            return retstr
        else:
            return ""
    
    #write a single XML string containing a contour
    def xmlContourStr(self, number, closed = True):
        if number >= 0:
            retstr = '<contour name="Contour Name '
            retstr += str(number)
            retstr += '" color="#FFFFFF" closed="'
            if closed:
                retstr += 'true'
            else:
                retstr += 'false'
            retstr += '" shape="Contour">'
            return retstr
        else:
            return ""
    
    def xmlSectionStr(self, number, spacing = 1, cut = None):
        if type(cut) is None:
            cut = spacing
        if number >= 1:
            retstr = '<section sid="S'
            retstr += str(number)
            retstr += '" name="Section '
            retstr += str(number)
            retstr += '" top="'
            retstr += str((number - 1) * spacing)
            retstr += '" cutthickness="'
            retstr += str(spacing)
            retstr += '" mountedthickness="'
            retstr += str(spacing)
            retstr += '"/>'
            return retstr
        else:
            return "" 
    
    def xmlMarkerBlock(self, number, points, markerRef):
        if (number > 0 and
             type(points) is list and
             len(points) > 0 and
             type(points[0]) is tuple):
            retstr = self.xmlMarkerStr(number, markerRef)
            retstr += '\r\n'
            for point in points:
                retstr += '  '
                retstr += self.xmlPointStr(point)
                retstr += '\r\n'
            retstr += '</marker>\r\n'
            return retstr
        else:
            return ""
    
    def xmlContourBlock(self, number, points, boilerplate):
        if (number > 0 and
             type(points) is list and
             type(points[0]) is tuple):
            retstr = self.xmlContourStr(number)
            retstr += '\r\n'
            retstr += boilerplate
            for point in points:
                retstr += '  '
                retstr += self.xmlPointStr(point)
                retstr += '\r\n'
            retstr += '</contour>\r\n'
            return retstr
        else:
            return ""
    
    def xmlFilefactsBlock(self, sections = 0, spacing = 1, cut = None):
        if type(cut) is None:
            cut = spacing
        if sections > 0:
            retstr = '<filefacts>\r\n'
            for section in range(1, sections + 1):
                retstr += '  '
                retstr += self.xmlSectionStr(section, spacing, cut)
                retstr += '\r\n'
            retstr += '</filefacts>\r\n'
            return retstr
        else:
            return ""
    
    def xmlImageBlock(self, filenames, scaling, spacing = 0.0):
        if (type(filenames) is list and
             type(filenames[0]) is str and
             type(scaling) is tuple):
            retstr = '<images>\r\n'
            for ind in range(len(filenames)):
                retstr += '  <image>\r\n'
                retstr += '    <filename>'
                retstr += filenames[ind]
                retstr += '</filename>\r\n'
                retstr += '    <scale x="'
                retstr += '{0:.5f}'.format(scaling[0])
                retstr += '" y="'
                retstr += '{0:.5f}'.format(scaling[1])
                retstr += '"/>\r\n'
                retstr += '    <coord x="0.00000" y="0.00000" z="'
                retstr += '{0:.5f}'.format(ind * spacing)
                retstr += '"/>\r\n'
                retstr += '  </image>\r\n'
            retstr += '</images>\r\n'
            return retstr
        else:
            return ""
    
    def writeFile(self, filename, body):
        with open(filename, mode='w', newline='') as file:
            file.write(body)
