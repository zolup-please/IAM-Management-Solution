import json
from datetime import date, timedelta

import boto3
from botocore.exceptions import ClientError

client = boto3.client('iam')
resource = boto3.resource('iam')

#2_1_3 과도한 권한 IAM Role
class overAuthorityRole:
    def __init__(self):
        self.list_access_service()

    def list_roles(self, count):
        self.roles = list()
        try:
            self.roles = list(resource.roles.limit(count=count))
        except ClientError:
            raise

    def list_access_service(self):
        #모든 Role 가져옴
        self.list_roles(123)

        self.sub = dict()
        # 아예 사용 안한 사용자 리스트와
        self.sub['NotExistServiceRole'] = list() 
        # 사용했지만 90일이 경과된 리스트
        self.sub['OverDateServiceName'] = list()
        countRole = 0

        # 오늘 날짜 저장
        today = date.today()

        for role in self.roles:
            #JobID 추출을 위하여 사용
            jobId = client.generate_service_last_accessed_details(
                Arn = role.arn
            )
            #추출한 JobID로 Role Detail 추출
            entity = client.get_service_last_accessed_details(
                JobId=jobId['JobId']
            )
            #print(entity)
            #ServicesLastAccessed가 없다면 RoleName을 NoneAccessRoleName에 저장 후 카운트 증가
            if not 'ServicesLastAccessed' in entity:
                self.sub['NotExistServiceRole'].append(role.name)
                countRole = countRole + 1
            else :
                #ServicesLastAccessed 안에 있는 리스트 중에
                for i in entity['ServicesLastAccessed']:
                    #마지막 인증 날짜 정보를 가져와
                    if "LastAuthenticated" in i :
                        RoleLastUsed = i['LastAuthenticated'].date()
                        How_long = today - RoleLastUsed
                        #90일이 넘었다면 ServiceName 저장
                        if(How_long >= timedelta(days=90)):
                            self.sub['OverDateServiceName'].append(i['ServiceName'])
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
    example = overAuthorityRole()
    print(example.result)