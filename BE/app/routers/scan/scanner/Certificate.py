import boto3
import datetime

class Certificate:
    client = None
    response = None

    def __init__(self):
        if(Certificate.client == None):
            Certificate.client = boto3.client('acm')
            Certificate.response = Certificate.client.list_certificates(
                CertificateStatuses=['ISSUED', 'EXPIRED', 'INACTIVE'],
                MaxItems=1000
            )
    
    def _printResponse(self):
        print(Certificate.response)


class ExpiredCertificate(Certificate):
    def __init__(self):
        super().__init__()
        self.scanning()

    def scanning(self):
        report = []
        self.result = {}
        for cert in Certificate.response['CertificateSummaryList']:
            if cert['Type'] == 'AMAZON_ISSUED':
                if (datetime.datetime.strptime(cert['InUseBy'][0]['NotAfter'], "%Y-%m-%dT%H:%M:%SZ") - datetime.datetime.now()).days < 7:
                    report.append(cert)

        if(not report):
            self.result['Detected'] = False

        else:
            self.result['Detected'] = True
            self.result['Report'] = report


class HeartBleedCertificate(Certificate):
    def __init__(self):
        super().__init__()
        self.scanning()

    def scanning(self):
        report = []
        self.result = {}
        for cert in Certificate.response['CertificateSummaryList']:
            if cert['Type'] == 'AMAZON_ISSUED':
                if datetime.datetime.strptime(cert['InUseBy'][0]['NotBefore'], "%Y-%m-%dT%H:%M:%SZ") < datetime.datetime(2014, 4, 1):
                    report.append(cert)

        if(not report):
            self.result['Detected'] = False

        else:
            self.result['Detected'] = True
            self.result['Report'] = report
        

if __name__=='__main__':
    demo = ExpiredCertificate()
    print(demo.result)
    demo = HeartBleedCertificate()
    print(demo.result)