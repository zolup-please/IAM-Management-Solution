import json
from datetime import date, timedelta

import boto3
from botocore.exceptions import ClientError

client = boto3.client('iam')
resource = boto3.resource('iam')

#2_2_4 미사용 IAM POLICY
class unUsedPolicy:
    def __init__(self):
        self.list_access_service()

    def list_policies(self, count):
        self.policies = list()
        try:
            self.policies = list(resource.policies.limit(count=count))
        except ClientError:
            raise

    def list_access_service(self):
        #모든 Policy 가져옴
        self.list_policies(123)

        self.sub = dict()
        # 아예 사용 안한 사용자 리스트와
        self.sub['NoneAccessPolicyName'] = list() 
        # 사용했지만 90일이 경과된 리스트
        self.sub['OverDatePolicyName'] = list()
        countPolicy = 0

        # 오늘 날짜 저장
        today = date.today()

        for policy in self.policies:
            #JobID 추출을 위하여 사용
            jobId = client.generate_service_last_accessed_details(
                Arn = policy.arn
            )
            
            #policy_name을 얻기위해 사용
            policyName = resource.Policy(policy.arn)

            #추출한 JobID로 Policy Detail 추출
            entity = client.get_service_last_accessed_details(
                JobId=jobId['JobId']
            )
            #print(entity)
            
            #ServicesLastAccessed가 없다면 PolicyName을 NoneAccessPolicyName에 저장 후 카운트 증가
            if not 'ServicesLastAccessed' in entity:
                self.sub['NoneAccessPolicyName'].append(policyName.policy_name)
                countPolicy = countPolicy + 1
            else :
                #ServicesLastAccessed 안에 있는 리스트 중에
                for i in entity['ServicesLastAccessed']:
                    #마지막 인증 날짜 정보를 가져와
                    if "LastAuthenticated" in i :
                        PolicyLastUsed = i['LastAuthenticated'].date()
                        How_long = today - PolicyLastUsed
                        #90일이 넘었다면 PolicyName 저장
                        if(How_long >= timedelta(days=90)):
                            self.sub['OverDatePolicyName'].append(policyName.policy_name)
                            countPolicy = countPolicy + 1
            
            
        #result dictionary에 추가
        self.result = dict()
        if (countPolicy == 0):
            self.result["Detected"] = False
        else:
            self.result["Detected"] = True
            self.result["Report"] = dict()
            self.result["Report"]["PolicyCount"] = countPolicy
            self.result["Report"].update(self.sub)


if __name__ == '__main__':
    example = unUsedPolicy()
    print(example.result)