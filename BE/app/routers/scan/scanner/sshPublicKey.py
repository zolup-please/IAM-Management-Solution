import boto3
from botocore.exceptions import ClientError
from datetime import datetime, timedelta

client = boto3.client('iam')
#1.1.6 
class check_publickey:
    def __init__(self):
        self.list_public_key()

    def list_public_key(self): # ssh_public_key list
        self.result = dict()
        response = client.list_ssh_public_keys()
        result_list = list()
        ssh_public_key_count = 0

        for i in response['SSHPublicKeys']:
            result_list.append(i['UserName'])
            ssh_public_key_count = ssh_public_key_count + 1

        dup = {x for x in result_list if result_list.count(x) > 1}

        if not dup:
            self.result["Detected"] = False
            self.result["Report"] = {"count" : ssh_public_key_count, "sshPubilcKey" : result_list}
        else:
            self.result["Detected"] = True
            self.result["Report"] = {"count" : ssh_public_key_count, "sshPubilcKey" : result_list, "2_access_key_User" : dup}

#1.1.7 SSH Public Key가 90일 이내에 재발급 되지 않았습니다.
class SshPublicKeyExpiration:
    def __init__(self):
        self.ListPublicKey()

    def ListPublicKey(self): # ssh_public_key list
        self.result = dict()
        value = list()
        now = datetime.now()
        result_list = list()

        response = client.list_ssh_public_keys()

        month = timedelta(days=90) #90 days

        for i in response['SSHPublicKeys']:
            result_list.append(i['UploadDate'])
            datetime_object = datetime.strptime(result_list[:-6], '%Y-%m-%dT%H:%M:%S') # 시간 정형화
            datetime_str1 = now - datetime_object
            if month < datetime_str1:
                value.append(i)

        if not value:
            self.result["Detected"] = False
        else:
            self.result["Detected"] = True
            self.result["Report"] = value

if __name__ == '__main__':
    check = check_publickey()
    print(check.result)
    check = SshPublicKeyExpiration()
    print(check.result)
    
