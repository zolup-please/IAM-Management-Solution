from .getCredentialReport import getCredentialReport

class check_Root_User_MFA(getCredentialReport):
    def __init__(self):
        super().__init__()
        self.scanning()

    def scanning(self):
        self.result = {}
        if(self.report[0]['mfa_active'].lower()=='false'):
            self.result["Detected"] = True
        else:
            self.result["Detected"] = False

if __name__ == '__main__':
    demo = check_Root_User_MFA()
    print(demo.result)