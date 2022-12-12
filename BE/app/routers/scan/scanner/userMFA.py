from .getCredentialReport import getCredentialReport

class check_IAM_User_MFA(getCredentialReport):
    def __init__(self):
        super().__init__()
        self.scanning()

    def scanning(self): 
        self.result = {}
        count = 0
        detectedUser = []
        for r in self.report[1:]:
            if(r['mfa_active'].lower()=='false'):
                count = count + 1
                detectedUser.append(r['user'])
        if(count == 0):
            self.result["Detected"] = False
        else:
            self.result["Detected"] = True
            self.result["Report"] = { "count": count, "DisabledMfaUser": detectedUser }


if __name__ == '__main__':
    demo = check_IAM_User_MFA()
    print(demo.result)
