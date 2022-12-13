from datetime import datetime
from .getScanner import getScanner


def executeScanning(scanRequest: dict):
    checkedList = scanRequest['checkedList']
    
    # 체크된 항목 추리기
    checked = []
    for i in checkedList:
        for j in i:
            if(i[j] == True):
                checked.append(j)

    # 체크된 항목에 대한 스캐너 클래스 가져오기
    g = getScanner(checked)
    scannerList = g.scannerList

    # 레포트 생성 및 스캔 실행
    report = {}
    report['Date'] = datetime.now()
    report['Checked'] = len(checked)
    report['Detected'] = 0
    report['checkedList'] = checked
    report['report'] = {}
    for _id, scanner in scannerList.items():
        instance = scanner()
        report['report'][_id] = instance.result

        if(instance.result['Detected'] == True):
            report['Detected'] = report['Detected'] + 1

    return report

def demo():
    import json
    with open('request.json') as f:
        request = json.load(f)
    executeScanning(request)


if __name__ == '__main__':
    demo()
