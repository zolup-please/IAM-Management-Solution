from .scanner import *

class getScanner:
    d = {
        "1.1.1" : dummy._dummy,
        "1.1.2" : dummy._dummy,
        "1.1.3" : dummy._dummy,
        "1.1.4" : dummy._dummy,
        "1.1.5" : dummy._dummy,
        "1.1.6" : dummy._dummy,
        "1.1.7" : dummy._dummy,
        "1.2.1" : dummy._dummy,
        "1.2.2" : dummy._dummy,
        "1.3.1" : dummy._dummy,
        "1.3.2" : dummy._dummy,
        "1.3.3" : dummy._dummy,
        "1.3.4" : dummy._dummy,
        "1.3.5" : dummy._dummy,
        "1.3.6" : dummy._dummy,
        "1.4.1" : dummy._dummy,
        "1.4.2" : dummy._dummy,
        "2.1.1" : dummy._dummy,
        "2.1.2" : dummy._dummy,
        "2.1.3" : dummy._dummy,
        "2.2.1" : dummy._dummy,
        "2.2.2" : dummy._dummy,
        "2.2.3" : dummy._dummy,
        "2.2.4" : dummy._dummy,
        "2.3.1" : dummy._dummy,
        "2.3.2" : dummy._dummy,
        "2.3.3" : dummy._dummy,
        "2.3.4" : dummy._dummy,
        "2.4.1" : dummy._dummy,
        "2.4.2" : dummy._dummy
    }
    def __init__(self, checked:list):
        self.scannerList = dict()
        for i in checked:
            self.scannerList[i] = self.d[i]