#2_4_2 사용자 친화 레포트 필요
import boto3

from botocore.exceptions import ClientError

client = boto3.client('iam')
resource = boto3.resource('iam')

class DuplicatedPolicy:
    def __init__(self):
        self.list_jungbok_policy()

    def list_jungbok_policy(self):
        self.result = dict()
        response = client.list_policies()
        result_list = list()
        policy_count = 0
        
        for i in response['Policies']:
            result_list.append(i['PolicyId'])
            policy_count = policy_count + 1

        dup = {x for x in result_list if result_list.count(x) > 1}

        if not dup:
            self.result["Detected"] = False
            self.result["Report"] = {"count " : policy_count ,"result_list" : result_list}
        else:
            self.result["Detected"] = True
            self.result["Report"] = {"count " : policy_count , "duplicated_Policy" : dup, "PolicyId" : result_list}

if __name__ == '__main__':
    example = DuplicatedPolicy()
    print(example.result)