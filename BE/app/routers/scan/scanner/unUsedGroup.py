import json
from datetime import date, timedelta

import boto3
from botocore.exceptions import ClientError

client = boto3.client('iam')
resource = boto3.resource('iam')

#2_2_2 미사용 IAM Group
class unUsedGroup:
    def __init__(self):
        self.list_access_service()

    def list_groups(self, count):
        self.groups = list()
        try:
            self.groups = list(resource.groups.limit(count=count))
        except ClientError:
            raise

    def list_access_service(self):
        #모든 Group 가져옴
        self.list_groups(123)
        
        self.sub = dict()
        # 아예 사용 안한 사용자 리스트와
        self.sub['NoneAccessGroupName'] = list() 
        # 사용했지만 90일이 경과된 리스트
        self.sub['OverDateGroupName'] = list()
        countGroup = 0

        # 오늘 날짜 저장
        today = date.today()

        for group in self.groups:
            #JobID 추출을 위하여 사용
            jobId = client.generate_service_last_accessed_details(
                Arn = group.arn
            )
            #추출한 JobID로 Group Detail 추출
            entity = client.get_service_last_accessed_details(
                JobId=jobId['JobId']
            )
            #ServicesLastAccessed가 없다면 GroupName을 NoneAccessGroupName에 저장 후 카운트 증가
            if not 'ServicesLastAccessed' in entity:
                self.sub['NoneAccessGroupName'].append(group.name)
                countGroup = countGroup + 1
            else :
                #ServicesLastAccessed 안에 있는 리스트 중에
                for i in entity['ServicesLastAccessed']:
                    #마지막 인증 날짜 정보를 가져와
                    if "LastAuthenticated" in i :
                        GroupLastUsed = i['LastAuthenticated'].date()
                        How_long = today - GroupLastUsed
                        #90일이 넘었다면 GroupName 저장
                        if(How_long >= timedelta(days=90)):
                            self.sub['OverDateGroupName'].append(group.name)
                            countGroup = countGroup + 1
            
            
        #result dictionary에 추가
        self.result = dict()
        if (countGroup == 0):
            self.result["Detected"] = False
        else:
            self.result["Detected"] = True
            self.result["Report"] = dict()
            self.result["Report"]["GroupCount"] = countGroup
            self.result["Report"].update(self.sub)


if __name__ == '__main__':
    example = unUsedGroup()
    print(example.result)