import json
from datetime import date, timedelta

import boto3
from botocore.exceptions import ClientError

client = boto3.client('iam')
resource = boto3.resource('iam')

class unUsedRole:
    def __init__(self):
        self.unUsedRoleList() #90일 이상 지났는지 확인

    def list_roles(self, count):
        self.roles = list()

        try:
            self.roles = list(resource.roles.limit(count=count))
        except ClientError:
            raise


    def unUsedRoleList(self):
        #모든 ROLE 가져옴
        self.list_roles(123)
        
        self.sub = dict()
        # 아예 사용 안한 ROLE 리스트와
        self.sub['NoneAccessRoleName'] = list() 
        # 사용했지만 90일이 경과된 리스트
        self.sub['OverDateRoleName'] = list()
        countRole = 0

        # 오늘 날짜 저장        
        today = date.today()

        for role in self.roles:
            response = client.get_role(
                RoleName = role.name
            )
            #LastUsedDate 기록이 있으면
            if 'LastUsedDate' in response["Role"]["RoleLastUsed"] :
                RoleLastUsed = response['Role']['RoleLastUsed']['LastUsedDate'].date()
                How_long = today - RoleLastUsed
                #90일 이상 사용했다면
                if(How_long >= timedelta(days=90)):
                    self.sub['OverDateRoleyName'].append(role.name)
                    countRole = countRole + 1
            else :
                self.sub['NoneAccessRoleName'].append(role.name)
                countRole = countRole + 1

        #result dictionary에 추가
        self.result = dict()
        if (countRole == 0):
            self.result["Detected"] = False
        else:
            self.result["Detected"] = True
            self.result["Report"] = dict()
            self.result["Report"]["RoleCount"] = countRole
            self.result["Report"].update(self.sub)

if __name__ == '__main__':
    example = unUsedRole()
    print(example.result)

