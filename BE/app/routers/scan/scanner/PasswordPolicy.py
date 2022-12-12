import logging
import boto3

from botocore.exceptions import ClientError


logger = logging.getLogger(__name__)

class getPasswordPolicy:
    def __init__(self):
        self.pw_policy = self.load_password_policy()

    def load_password_policy(self):
        iam = boto3.resource('iam')
        try:
            pw_policy = iam.AccountPasswordPolicy()

            ret = dict()
            ret['hard_expiry'] = pw_policy.hard_expiry
            ret['max_password_age'] = pw_policy.max_password_age
            ret['minimum_password_length'] = pw_policy.minimum_password_length
            ret['password_reuse_prevention'] = pw_policy.password_reuse_prevention 
            return ret

        except ClientError as error:
            if error.response['Error']['Code'] == 'NoSuchEntity':
                # 1.3.1 False는 IAM 암호 정책이 사용되지 않았음을 의미
                return False
            else:
                logger.exception("Couldn't get account password policy.")
                raise
        else:
            return ret


class PolicyPresence(getPasswordPolicy):
    def __init__(self):
        super().__init__()
        self.scanning()

    def scanning(self):
        self.result = {}
        if(not self.pw_policy):
            self.result['Detected'] = True
            report = { 'description' : 'Password policy is not defined.' }
            self.result['Report'] = report
        else:
            self.result['Detected'] = False

class HardExpiry(getPasswordPolicy):
    def __init__(self):
        super().__init__()
        self.scanning()
    
    def scanning(self):
        self.result = dict()
        if(not self.pw_policy):
            self.result['Detected'] = True
            report = { 'description' : 'Password policy is not defined.' }
            self.result['Report'] = report
        
        elif(self.pw_policy['hard_expiry'] == None or self.pw_policy['hard_expiry'] == False):
            self.result['Detected'] = True
            report = { 'description' : 'Hard expirie is not set.' }
            self.result['Report'] = report
        else:
            self.result['Detected'] = False

class MinPasswordLength(getPasswordPolicy):
    def __init__(self):
        super().__init__()
        self.scanning()
        
    def scanning(self):
        self.result = dict()
        if(not self.pw_policy):
            self.result['Detected'] = True
            report = { 'description' : 'Password policy is not defined.' }
            self.result['Report'] = report

        elif(self.pw_policy['minimum_password_length'] < 14):
            self.result['Detected'] = True
            report = { 'description' : 'The current setting of "minimum_password_length" is ' + chr(self.pw_policy['minimum_password_length']) + ' and less than 14.' } 
            self.result['Report'] = report
        else :
            self.result['Detected'] = False

class PasswordReusePrevention(getPasswordPolicy):
    def __init__(self):
        super().__init__()
        self.scanning()
    
    def scanning(self):
        self.result = dict()
        if(not self.pw_policy):
            self.result['Detected'] = True
            report = { 'description' : 'Password policy is not defined.' }
            self.result['Report'] = report
        
        elif(self.pw_policy['password_reuse_prevention'] == None):
            self.result['Detected'] = True
            report = { 'description' : '"password_reuse_prevention" is not set.' }
            self.result['Report'] = report
        else :
            self.result['Detected'] = False

class MaxPasswordAge(getPasswordPolicy):
    def __init__(self):
        super().__init__()
        self.scanning()
    
    def scanning(self):
        self.result = dict()
        if(not self.pw_policy):
            self.result['Detected'] = True
            report = { 'description' : 'Password policy is not defined.' }
            self.result['Report'] = report

        elif(self.pw_policy['max_password_age'] == None): # 수정 필요
            self.result['Detected'] = True
            report = { 'description' : '"max_password_age" is not set.' }
            self.result['Report'] = report
        elif(self.pw_policy['max_password_age'] > 90):
            self.result['Detected'] = True
            report = { 'description' : 'The current setting of "max_password_age" is ' + chr(self.pw_policy['max_password_age']) + ' and larger than 90.' }
            self.result['Report'] = report
        else :
            self.result['Detected'] = False



if __name__=='__main__':
    demo = HardExpiry()
    print(demo.result)
    
    demo = PasswordReusePrevention()
    print(demo.result)
    
    demo = MinPasswordLength()
    print(demo.result)
    
    demo = MaxPasswordAge()
    print(demo.result)