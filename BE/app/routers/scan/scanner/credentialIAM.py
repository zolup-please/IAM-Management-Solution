from datetime import datetime, timedelta

from .getCredentialReport import getCredentialReport

class ExpiredAccessKey(getCredentialReport):
    def __init__(self):
        super().__init__()
        self.scanning()

    
    def scanning(self):
        self.result = dict()
        userReport = getCredentialReport.userReport
        report = []
        Detected = False

        for item in userReport:
            d = self._checkKeys(item)
            if(d):
                report.append(d)

        if(report):
            self.result['Detected'] = True
            self.result['Report'] = {
                'DetectedCount': len(report),
                'DetectedUserInfo': report
            }
        else:
            self.result['Detected'] = False


    def _checkKeys(self, item):
        Detected1 = False
        Detected2 = False

        report = dict()
        if(item['access_key_1_active'] == 'true'):
            Detected1 = self._checkRotation(item['access_key_1_last_rotated'])

        if(item['access_key_2_active'] == 'true'):
            Detected2 = self._checkRotation(item['access_key_2_last_rotated'])

        if(Detected1 or Detected2):
            report['user'] = item['user']

        if(Detected1):
            report['access_key_1_last_rotated'] = item['access_key_1_last_rotated']

        if(Detected2):
            report['access_key_2_last_rotated'] = item['access_key_2_last_rotated']

        return report


    def _checkRotation(self, date_str):
        date = datetime.strptime(date_str[:-6], '%Y-%m-%dT%H:%M:%S')
        if(datetime.now() - date).days > 90:
            return True
        else:
            return False

class SecondKeyActivated(getCredentialReport):
    def __init__(self):
        super().__init__()
        self.userReport = getCredentialReport.userReport
        self.scanning()

    def scanning(self):
        self.result = dict()
        detectedUser = list()

        for item in self.userReport:
            if( item['access_key_1_active'] == 'true' 
            and item['access_key_2_active'] == 'true'):
                detectedUser.append(item['user'])

        if(not detectedUser):
            self.result['Detected'] = False
        else:
            self.result['Detected'] = True
            self.result['Report'] = {
                'DetectedUserCount': len(detectedUser),
                'DetectedUser': detectedUser
            }
            

if __name__=='__main__':
    demo = ExpiredAccessKey()
    print(demo.result)