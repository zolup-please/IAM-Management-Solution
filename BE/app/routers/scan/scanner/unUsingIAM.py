from datetime import datetime, timedelta
from .getCredentialReport import getCredentialReport

class unUsingUsered(getCredentialReport):
    def __init__(self):
        super().__init__()
        self.checkUnsingUser()
    
    def checkUnsingUser(self):
        self.result = dict()
        resultList = list()
        now = datetime.now()
        month = timedelta(days=90) #90 days
        count = 0
        setcount = 0

        for i in self.report:
            datetime_str = self.report[count]['password_last_used']
            if datetime_str != 'N/A' and datetime_str != 'no_information':
                datetime_object = datetime.strptime(datetime_str[:-6], '%Y-%m-%dT%H:%M:%S') # 시간 정형화
                datetime_str1 = now - datetime_object
                if month < datetime_str1:
                    resultList.append(self.report[count]['user'])
            else:
                resultList.append(self.report[count]['user'])
            count = count + 1
            setcount = setcount + 1

        if not resultList:
            self.result["Detected"] = False
        else:
            self.result["Detected"] = True
            self.result["Report"] = {
                'DetectedUserCount': len(resultList),
                'DetectedUser': resultList
            }
            
        
if __name__ == '__main__':
    example = unUsingUsered()
    print(example.result)