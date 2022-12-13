from datetime import datetime, timedelta

from .getCredentialReport import getCredentialReport


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
    demo = SecondKeyActivated()
    print(demo.result)