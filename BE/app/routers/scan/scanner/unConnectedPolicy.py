import json

import boto3
from botocore.exceptions import ClientError

client = boto3.client('iam')
resource = boto3.resource('iam')

#2_3_4 미연결 IAM POLICY
class unConnectedPolicy:
    def __init__(self):
        self.list_access_service()

    #Policy_ARN 추출
    def list_policies(self, count):
        self.policies = list()
        try:
            self.policies = list(resource.policies.limit(count=count))
        except ClientError:
            raise

    def list_access_service(self):
        #모든 Policy_ARN 가져옴
        self.list_policies(123)

        self.sub = dict()
        self.sub['PolicyName'] = list() 
        countPolicy = 0

        for policy in self.policies:
            #JobID 추출을 위하여 사용
            jobId = client.generate_service_last_accessed_details(
                Arn = policy.arn
            )
            #policy_name을 얻기위해 사용
            policyName = resource.Policy(policy.arn)
            
            # 고객 관리형 Policy_ Arn의 account-id는 aws가 아님을 이용
            if 'aws' != policy.arn[13:16]: # 즉, 고객 관리형이면
                # Entity를 가져와서
                entity = client.get_service_last_accessed_details_with_entities(
                    JobId=jobId['JobId'],
                    ServiceNamespace='iam'
                )

                # EntityDetailsList가 존재하지 않으면 정책 이름과 count 증가
                if not 'EntityDetailsList' in entity:
                    self.sub['PolicyName'].append(policyName.policy_name)
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
    example = unConnectedPolicy()
    #print(example.result)