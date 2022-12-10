from .scanner import *

class _dummy:
    
    def __init__(self):
        self.result = {"dummy": "report"}

class getScanner:
    d = {
        "1.1.1" : _dummy,
        "1.1.2" : _dummy,
        "1.1.3" : _dummy,
        "1.1.4" : _dummy,
        "1.1.5" : _dummy,
        "1.1.6" : _dummy,
        "1.1.7" : _dummy,
        "1.2.1" : _dummy,
        "1.2.2" : _dummy,
        "1.3.1" : _dummy,
        "1.3.2" : _dummy,
        "1.3.3" : _dummy,
        "1.3.4" : _dummy,
        "1.3.5" : _dummy,
        "1.3.6" : _dummy,
        "1.4.1" : _dummy,
        "1.4.2" : _dummy,
        "2.1.1" : _dummy,
        "2.1.2" : _dummy,
        "2.1.3" : _dummy,
        "2.2.1" : _dummy,
        "2.2.2" : _dummy,
        "2.2.3" : _dummy,
        "2.2.4" : _dummy,
        "2.3.1" : _dummy,
        "2.3.2" : _dummy,
        "2.3.3" : _dummy,
        "2.3.4" : _dummy,
        "2.4.1" : _dummy,
        "2.4.2" : _dummy
    }
    def __init__(self, checked:list):
        self.scannerList = dict()
        for i in checked:
            self.scannerList[i] = self.d[i]