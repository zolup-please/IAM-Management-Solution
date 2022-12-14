import json

import boto3
from botocore.exceptions import ClientError

client = boto3.client('iam')
resource = boto3.resource('iam')

#2_3_3 미연결 ROLE
class unConnectedRole:
    def __init__(self):
        self.list_policies()

    def list_roles(self, count):
        self.roles = list()
        try:
            self.roles = list(resource.roles.limit(count=count))
        except ClientError:
            raise

    def list_policies(self):
        self.list_roles(123) #모든 ROLE 가져옴

        #managed와 inline을 나누어 저장
        self.managed = dict()
        self.inline = dict()
        self.managed['Managed_Roles'] = list()
        self.inline['Inline_Roles'] = list()
        countManaged = 0
        countInline = 0


        for role in self.roles:
            #관리형 정책
            resManaged = client.list_attached_role_policies(
                RoleName=role.name
            )
            #관리형 정책이 없으면 유저를 managed['Managed_Policies']에 저장하고 count 증가
            if len(resManaged['AttachedPolicies']) == 0: 
                self.managed['Managed_Roles'].append(role.name)
                countManaged = countManaged + 1
           
           #인라인 정책
            resInline = client.list_role_policies(
                RoleName=role.name
            )
            #인라인 정책이 없으면 유저를 inline['Inline_Policies']에 저장하고 count 증가
            if len(resInline['PolicyNames']) == 0: 
                self.inline['Inline_Roles'].append(role.name)
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
    example = unConnectedRole()
    print(example.result)