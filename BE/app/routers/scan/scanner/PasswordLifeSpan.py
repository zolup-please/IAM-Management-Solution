from datetime import datetime, timedelta

from .getCredentialReport import getCredentialReport
from .PasswordPolicy import getPasswordPolicy

class checkLifeSpan(getCredentialReport):
    def __init__(self):
        self.result = dict()
        pwPolicy = getPasswordPolicy()

        if(not pwPolicy.pw_policy):
            self.result['Detected'] = True
            report = { 'description' : 'Password policy is not defined.' }
            self.result['Report'] = report

        else:
            super().__init__()
            self.scanning()
    
    def scanning(self):
        now = datetime.now()
        oneWeek = timedelta(days=7)
        count = 0
        for user in self.report[1:]:
            # print(user['user']+'\t'+user['password_next_rotation'])
            datetime_str = user['password_next_rotation']
            if(datetime_str == 'N/A'):
                continue

            datetime_object = datetime.strptime(datetime_str[:-6], '%Y-%m-%dT%H:%M:%S')
            passwordLifeSpan = datetime_object - now

            report = {}
            report['count'] = None
            report['users'] = []
            if(passwordLifeSpan < oneWeek):
                count = count + 1
                report['users'].append({ 'user' : user['user'], 'password_next_rotation' : datetime_object})
        
        if(count != 0):
            report['count'] = count
            self.result['Detected'] = True
            self.result['Report'] = report
        
        else:
            self.result['Detected'] = False


if __name__ == '__main__':
    demo = checkLifeSpan()

    print(demo.result)
    