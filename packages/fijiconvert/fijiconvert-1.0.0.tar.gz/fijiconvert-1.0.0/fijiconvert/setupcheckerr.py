#used to verify that all needed inputs have been given by the user
class SetupCheckErr:
    def __init__(self):
        self.inputs = False
        self.output = False
        self.XMLChecked = False
        self.dimChecked = False
        self.contentsChecked = False
        self.scaling = False
    
    #returns true if all inputs good
    def check(self):
        if not self.inputs:
            return False
        elif not self.output:
            return False
        elif not self.XMLChecked:
            return False
        elif not self.dimChecked:
            return False
        elif not self.contentsChecked:
            return False
        elif not self.scaling:
            return False
        else:
            return True
    
    #returns string with missing inputs listed
    def getErrors(self):
        reterrs = str()
        if not self.inputs:
            reterrs += "\tInput Files\r\n"
        if not self.output:
            reterrs += "\tOutput Location\r\n"
        if not self.XMLChecked:
            reterrs += "\tXML Option\r\n"
        if not self.dimChecked:
            reterrs += "\tDimensionality\r\n"
        if not self.contentsChecked:
            reterrs += "\tContent Choice\r\n"
        if not self.scaling:
            reterrs +="\tScaling\r\n"
        else:
            reterrs += "\tNone\r\n"
        return reterrs
