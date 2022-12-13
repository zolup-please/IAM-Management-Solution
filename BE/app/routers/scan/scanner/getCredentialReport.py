import logging
import copy

import boto3

from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
iam = boto3.resource('iam')
client = boto3.client('iam')

class getCredentialReport:
    rootReport = None
    userReport = None
    def __init__(self):
        response = client.generate_credential_report()
        self.report = self.get_report()
        if(getCredentialReport.rootReport == None):
            getCredentialReport.rootReport = self.report[0]
            getCredentialReport.userReport = self.report[1:]

    def get_credential_report(self):
        try:
            response = iam.meta.client.get_credential_report()
            logger.debug(response['Content'])
        except ClientError:
            logger.exception("Couldn't get credentials report.")
            raise
        else:
            return response['Content']

    def get_report(self):
        cred_report = self.get_credential_report()
        col_count = 22
        cred_lines = [line.split(',')[:col_count] for line
                      in cred_report.decode('utf-8').split('\n')]

        ret = list()
        dic = dict()
        col_name = cred_lines[0]
        for i in cred_lines[1:]:
            for j in range(col_count):
                dic[col_name[j]] = i[j]
            dic_copy = copy.deepcopy(dic)
            ret.append(dic_copy)
            dic.clear()
        return ret

if __name__ == '__main__':
    credentialReport = getCredentialReport()
    print('Report - Root User')
    print(credentialReport.report[0])
    print('Report - IAM User')
    print(credentialReport.report[1:])
