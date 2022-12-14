import json

import boto3
from botocore.exceptions import ClientError

client = boto3.client('iam')
resource = boto3.resource('iam')

#2_3_2 미연결 IAM GROUP
class unConnectedGroup:
    def __init__(self):
        self.list_user_policies()

    def list_groups(self, count):
        self.groups = list()
        try:
            self.groups = list(resource.groups.limit(count))
        except ClientError:
            raise

    def list_user_policies(self):
        self.list_groups(123)       #모든 group 가져옴
        self.sub = dict()  
        self.sub["GroupName"] = list()
        countGroup = 0

        for group in self.groups:
            #Group 정보 dict 가져오기
            response = client.get_group(  
                GroupName=group.name
            )
            #User가 없다면 Group이름을 저장 후 카운트 증가
            if len(response['Users']) == 0:
                self.sub["GroupName"].append(group.name)
                countGroup = countGroup + 1
            
        #result dictionary에 추가
        self.result = dict()
        if countGroup == 0 :
            self.result["Detected"] = False
        else:
            self.result["Detected"] = True
            self.result["Report"] = dict()
            self.result["Report"]["GroupCount"] = countGroup
            self.result["Report"].update(self.sub)    

if __name__ == '__main__':
    example = unConnectedGroup()
    #print(example.result)