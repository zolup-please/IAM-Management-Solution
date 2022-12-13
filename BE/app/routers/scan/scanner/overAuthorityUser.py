import json
from datetime import date, timedelta

import boto3
from botocore.exceptions import ClientError

client = boto3.client('iam')
resource = boto3.resource('iam')

#2_1_1 과도한 권한 IAM User
class overAuthorityUser:
    def __init__(self):
        self.list_access_service()

    def list_users(self, count):
        self.users = list()
        try:
            self.users = list(resource.users.limit(count=count))
        except ClientError:
            raise

    def list_access_service(self):
        #모든 user 가져옴
        self.list_users(123)

        self.sub = dict()
        # 아예 사용 안한 사용자 리스트와
        self.sub['NotExistServiceUser'] = list() 
        # 사용했지만 90일이 경과된 리스트
        self.sub['OverDateServiceName'] = list()
        countUser = 0

        # 오늘 날짜 저장
        today = date.today()

        for user in self.users:
            #JobID 추출을 위하여 사용
            jobId = client.generate_service_last_accessed_details(
                Arn = user.arn
            )
            #추출한 JobID로 User Detail 추출
            entity = client.get_service_last_accessed_details(
                JobId=jobId['JobId']
            )
            #print(entity)
            #ServicesLastAccessed가 없다면 UserName을 NoneAccessUserName에 저장 후 카운트 증가
            if not 'ServicesLastAccessed' in entity:
                self.sub['NotExistServiceUser'].append(user.name)
                countUser = countUser + 1
            else :
                #ServicesLastAccessed 안에 있는 리스트 중에
                for i in entity['ServicesLastAccessed']:
                    #마지막 인증 날짜 정보를 가져와
                    if "LastAuthenticated" in i :
                        UserLastUsed = i['LastAuthenticated'].date()
                        How_long = today - UserLastUsed
                        #90일이 넘었다면 ServiceName 저장
                        if(How_long >= timedelta(days=90)):
                            self.sub['OverDateServiceName'].append(i['ServiceName'])
                            countUser = countUser + 1
            
            
        #result dictionary에 추가
        self.result = dict()
        if (countUser == 0):
            self.result["Detected"] = False
        else:
            self.result["Detected"] = True
        self.result["Report"] = dict()
        self.result["Report"]["UserCount"] = countUser
        self.result["Report"].update(self.sub)


if __name__ == '__main__':
    example = overAuthorityUser()
    print(example.result)