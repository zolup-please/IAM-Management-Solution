from datetime import datetime, timedelta
from .getCredentialReport import getCredentialReport

class CheckCredentialRoot(getCredentialReport):
    def __init__(self):
        super().__init__()
        self.check_Root_Using()
    
    # 1.1.1 최근 30일 간 root계정을 사용한적 있는지 판단
    def check_Root_Using(self):
        self.result = dict()
        now = datetime.now()
        datetime_str = self.report[0]['password_last_used'] #Root 패스워드 마지막 시간

        datetime_object = datetime.strptime(datetime_str[:-6], '%Y-%m-%dT%H:%M:%S') # 시간 정형화
        datetime_str1 = now - datetime_object # 현재 시간 - 패스워드 마지막사용시간
        month = timedelta(days=30) #30 days

        # month보다 30일 기준으로 넘었을때 안넘었을때 또는 아예 로그 기록이 존재하지않을때 3가지
        if month > datetime_str1:
            self.result["Detected"] = True
            self.result["Report"] = {"password_last_used" : datetime_str}
        elif(datetime_str == 'N/A'):
            self.result["Detected"]= False
            self.result["Report"] = {"password_last_used" : 'N/A'}
        else:
            self.result["Detected"] = False
            self.result["Report"] = {"password_last_used" : datetime_str}

#1.1.2 Root 계정에 엑세스 키가 활성화 되어있는지 유무판단
class CheckAccessKeyRoot(getCredentialReport):
    def __init__(self):
        super().__init__()
        self.check_Root_Active_AccessKey()

    def check_Root_Active_AccessKey(self):
        self.result = dict()
        #Root 계정의 여러개 엑세스 키중에 하나라도 활성화 되었있으면 True반환
        if self.report[0]['access_key_1_active']=='true' or self.report[0]['access_key_2_active']=='true':
            self.result["Detected"] = True
        else:
            self.result["Detected"] = False

class ExpiredAccessKey(getCredentialReport):
    def __init__(self):
        super().__init__()
        self.scanning()
    
    def scanning(self):
        self.result = dict()
        rootReport = getCredentialReport.rootReport
        report = {}
        Detected = False
        if(rootReport['access_key_1_active'] == 'true'):
            Detected = self._checkRotation(rootReport['access_key_1_last_rotated'])
            if(Detected):
                    report['access_key_1_last_rotated'] = rootReport['access_key_1_last_rotated']

        if(rootReport['access_key_2_active'] == 'true'):
            Detected = self._checkRotation(rootReport['access_key_2_last_rotated'])
            if(Detected):
                    report['access_key_2_last_rotated'] = rootReport['access_key_2_last_rotated']
        
        self.result['Detected'] = Detected
        self.result['Report'] = report

    def _checkRotation(self, date_str):
        date = datetime.strptime(date_str[:-6], '%Y-%m-%dT%H:%M:%S')
        if(datetime.now() - date).days > 30:
            return True
        else:
            return False
    

if __name__ == '__main__':
    check = ExpiredAccessKey()
    print(check.result)