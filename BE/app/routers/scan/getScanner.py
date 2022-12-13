from .scanner import *

class getScanner:
    d = {
        "1.1.1" : credentialRoot.CheckCredentialRoot,
        "1.1.2" : credentialRoot.CheckAccessKeyRoot,
        "1.1.3" : credentialRoot.ExpiredAccessKey,
        "1.1.4" : credentialIAM._dummy,
        "1.1.5" : credentialIAM._dummy,
        "1.1.6" : sshPublicKey.check_publickey,
        "1.1.7" : dummy._dummy,
        "1.2.1" : MFA.check_Root_User_MFA,
        "1.2.2" : MFA.check_IAM_User_MFA,
        "1.3.1" : PasswordPolicy.PolicyPresence,
        "1.3.2" : PasswordPolicy.HardExpiry,
        "1.3.3" : PasswordPolicy.MinPasswordLength,
        "1.3.4" : PasswordPolicy.PasswordReusePrevention,
        "1.3.5" : PasswordPolicy.MaxPasswordAge,
        "1.3.6" : PasswordLifeSpan.checkLifeSpan,
        "1.4.1" : Certificate.ExpiredCertificate,
        "1.4.2" : Certificate.HeartBleedCertificate,
        "2.1.1" : dummy._dummy,
        "2.1.2" : dummy._dummy,
        "2.1.3" : dummy._dummy,
        "2.2.1" : dummy._dummy,
        "2.2.2" : dummy._dummy,
        "2.2.3" : dummy._dummy,
        "2.2.4" : dummy._dummy,
        "2.3.1" : dummy._dummy,
        "2.3.2" : dummy._dummy,
        "2.3.3" : dummy._dummy,
        "2.3.4" : dummy._dummy,
        "2.4.1" : dummy._dummy,
        "2.4.2" : duplicationPolicy.DuplicatedPolicy
    }
    def __init__(self, checked:list):
        self.scannerList = dict()
        for i in checked:
            self.scannerList[i] = self.d[i]