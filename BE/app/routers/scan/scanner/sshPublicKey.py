#1.1.6 
import boto3
from botocore.exceptions import ClientError


client = boto3.client('iam')

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
        
if __name__ == '__main__':
    check = check_publickey()
    print(check.result)
    
