from datetime import datetime, timedelta
from .getCredentialReport import getCredentialReport

class CheckCredentialRoot(getCredentialReport):
    def __init__(self):
        super().__init__()
        self.check_Root_Using()
    
    # 1.1.1 credential
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
if __name__ == '__main__':
    check = CheckCredentialRoot()
    print(check.result)
