import json

import boto3
from botocore.exceptions import ClientError

client = boto3.client('iam')
resource = boto3.resource('iam')

#2_3_3 미연결 User
class unConnectedUser:
    def __init__(self):
        self.listUserPolicies()

    def listUsers(self, count):
        self.users = list()
        try:
            self.users = list(resource.users.limit(count=count))
        except ClientError:
            raise

    def listUserPolicies(self):
        self.listUsers(123) #모든 user 가져옴

        #managed와 inline을 나누어 저장
        self.managed = dict()
        self.inline = dict()
        self.managed['Managed_Users'] = list()
        self.inline['Inline_Users'] = list()
        countManaged = 0
        countInline = 0

        # for문으로 모든 유저를 검사
        for user in self.users:
            #관리형 정책
            resManaged = client.list_attached_user_policies(
                UserName=user.name
            )

            #관리형 정책이 없으면 유저를 managed['Managed_Policies']에 저장하고 count 증가
            if len(resManaged['AttachedPolicies']) == 0: 
                self.managed['Managed_Users'].append(user.name)
                countManaged = countManaged + 1
 
            #인라인 정책
            resInline = client.list_user_policies(
                UserName=user.name
            )
            #인라인 정책이 없으면 유저를 inline['Inline_Policies']에 저장하고 count 증가
            if len(resInline['PolicyNames']) == 0: 
                self.inline['Inline_Users'].append(user.name)
                countInline = countInline + 1
           
          

        #result dictionary에 추가
        self.result = dict()
        if (countManaged == 0 and countInline == 0):
            self.result["Detected"] = False
        else:
            self.result["Detected"] = True
            self.result["Report"] = dict()
            self.result["Report"]["ManagedCount"] = countManaged
            self.result["Report"].update(self.managed)
            self.result["Report"]["InlineCount"] = countInline
            self.result["Report"].update(self.inline)

if __name__ == '__main__':
    example = unConnectedUser()
    print(example.result)