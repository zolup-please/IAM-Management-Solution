import boto3
from datetime import datetime, timedelta

client = boto3.client('iam')

class test:
    def __init__(self, dd):
        self.result = dict()
        self.countUser()
        self.compareUser(dd)
    
    def compareUser(self, dd):
        now = datetime.now()
        
        response = client.list_users()
        mongoData = dd # 이부분을 mongo 파일로 변경하면됨 yUserList에 있는 변수명 바꿔야함
        yUserList = list()
        userList = list()


        for user in response['Users']:
            userList.append(user['UserName'])

        yUserList = mongoData['Users']

        deleteUser = [x for x in yUserList if x not in userList] # 없어진 유저
        addUser = [x for x in userList if x not in yUserList] # 새로생긴 유저
        #elf.result["Create"] = addUser
        #self.result["IAM_delUser"] = deleteUser

    def countUser(self):
        response = client.list_users()
        mongoData = {
            'Date':  [2022, 12, 14, 20, 20, 8, 668456],
            'Users': ['CT_admin', 'groupA_0', 'groupA_1', 'groupA_2', 'groupA_3', 'groupA_4', 'groupB_0', 'groupB_1', 'groupB_2', 'groupB_3', 'groupB_4', 'groupC_0', 'groupC_1', 'groupC_2', 'groupC_3', 'groupC_4', 'groupD_0', 'groupD_1', 'groupD_2', 'groupD_3', 'groupD_4', 'groupE_0', 'groupE_1', 'groupE_2', 'groupE_3', 'groupE_4', 'user0', 'user1', 'user2', 'yeonghae', 'yeonghae1', 'yeonghae2', 'yeonghae3']
        } # 이부분을 mongo 파일로 변경하면됨 yUserList에 있는 변수명 바꿔야함
        yUserList = list()
        userList = list()
        del_count = 0
        add_count = 0
        


        for user in response['Users']:
            userList.append(user['UserName'])

        for user in response['Users']:
            userList.append(user['UserName'])

        yUserList = mongoData['Users']

        deleteUser = [x for x in yUserList if x not in userList] # 없어진 유저
        addUser = [x for x in userList if x not in yUserList] # 새로생긴 유저
        del_count = len(deleteUser)
        add_count = len(addUser)
        

        user_count = len(userList) #현재 총 계정수

        self.result["Total"] = user_count
        self.result["Created"] = add_count
        self. result["Deleted"] = del_count

'''
if __name__ == '__main__':
    dd = {'Date': [2022, 12, 14, 20, 20, 8, 668456], 'Users': ['CT_admin', 'groupA_0', 'groupA_1', 'groupA_2', 'groupA_3', 'groupA_4', 'groupB_0', 'groupB_1', 'groupB_2', 'groupB_3', 'groupB_4', 'groupC_0', 'groupC_1', 'groupC_2', 'groupC_3', 'groupC_4', 'groupD_0', 'groupD_1', 'groupD_2', 'groupD_3', 'groupD_4', 'groupE_0', 'groupE_1', 'groupE_2', 'groupE_3', 'groupE_4', 'user0', 'user1', 'user2', 'yeonghae', 'yeonghae1', 'yeonghae2', 'yeonghae3']}
    example = test(dd)
    print(example.result)
'''