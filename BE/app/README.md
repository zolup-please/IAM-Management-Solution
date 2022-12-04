# API 명세

## /api/v1/{api 경로}

### API개요

- fastAPI를 이용한 RESTful API 서버입니다.
- 모든 통신은 application/json 방식으로 data를 주고 받습니다.

### Response templete

```json
{
	"msg":string // status message
	"status":int // status code
	"result":dict // json형식의 결과
}
```

### API 목록

### GET  /api/v1/dashboard

### Description

- dashboard에 필요한 정보를 반환합니다.

### Note

<aside>
💡 현재 반환되는 값은 dummy data입니다.
IAMActivity값은 아직 구현되지 않았습니다.

</aside>

### Query parameters

- None

### Response sample

```json
{
  "RecentReport": {
    "Counts": 2,
    "Reports": [
      {
        "Date": "2022-11-24",
        "Checked": 12,
        "Detected": 4
      },
      {
        "Date": "2022-11-23",
        "Checked": 8,
        "Detected": 0
      }
    ]
  },
  "IAMActivities": {},
  "Changes": {
    "Total": 3,
    "Created": 2,
    "Deleted": 2
  }
}
```

### GET  /api/v1/scanning

### Description

- 스캐닝 항목 리스트 반환

### Query parameters

- None

### Response sample

```json
{
  "ScanningList": {
    "Credential": [
      {
        "id": "1.1.1",
        "Description": "Root 사용",
        "Detail": "AWS 계정 Root 사용자가 30일 이내에 사용되었습니다."
      },
      {
        "id": "1.1.2",
        "Description": "Root Access Key 활성화",
        "Detail": "AWS 계정 Root 사용자의 활성화된 액세스 키가 존재합니다."
      },
      {
        "id": "1.1.3",
        "Description": "Root Access Key 만료",
        "Detail": "AWS 계정 Root 사용자의 액세스 키가 30일 이내에 재발급되지 않았습니다."
      },
      {
        "id": "1.1.4",
        "Description": "User Access Key 만료",
        "Detail": "IAM 사용자의 액세스 키가 90일 이내에 교체되지 않았습니다."
      },
      {
        "id": "1.1.5",
        "Description": "User Access Key 2개 활성화",
        "Detail": "IAM 사용자의 액세스 키가 2개 이상 활성화되어 있습니다."
      },
      {
        "id": "1.1.6",
        "Description": "User SSH Public Key 2개 활성화",
        "Detail": "2개 이상의 SSH Public Key가 활성화된 IAM 사용자가 존재합니다."
      },
      {
        "id": "1.1.7",
        "Description": "User SSH Public Key 만료",
        "Detail": "SSH Public Key가 90일 이내에 재발급 되지 않았습니다."
      }
    ],
    "MFA": [
      {
        "id": "1.2.1",
        "Description": "Root MFA 비활성화",
        "Detail": "AWS 계정 Root 사용자의 MFA가 비활성화되어 있습니다."
      },
      {
        "id": "1.2.2",
        "Description": "User MFA 비활성화",
        "Detail": "IAM 사용자의 MFA가 비활성화 되어 있습니다."
      }
    ],
    "PW": [
      {
        "id": "1.3.1",
        "Description": "IAM 암호 정책 미사용",
        "Detail": "IAM 암호 정책이 사용되지 않았습니다."
      },
      {
        "id": "1.3.2",
        "Description": "강력한 IAM 암호 정책 설정 오류",
        "Detail": "강력한 IAM 암호 정책을 설정하지 않았습니다."
      },
      {
        "id": "1.3.3",
        "Description": "암호 길이 제한 설정 오류",
        "Detail": "IAM 암호 정책이 14자 이상의 암호를 요구하도록 설정하지 않았습니다."
      },
      {
        "id": "1.3.4",
        "Description": "암호 재사용 설정 오류",
        "Detail": "IAM 암호 정책이 암호 재사용을 방지하도록 설정하지 않았습니다."
      },
      {
        "id": "1.3.5",
        "Description": "암호 만료일 설정 오류",
        "Detail": "IAM 암호 정책이 암호를 90일 이내에 만료하도록 설정하지 않았습니다."
      },
      {
        "id": "1.3.6",
        "Description": "User 암호 만료",
        "Detail": "암호가 만료되거나 만료일이 7일 이내인 IAM 사용자가 존재합니다."
      }
    ],
    "Certificate": [
      {
        "id": "1.4.1",
        "Description": "서버 인증서 만료",
        "Detail": "만료되거나 만료일이 7일 이내인 SSL/TLS 인증서가 존재합니다."
      },
      {
        "id": "1.4.2",
        "Description": "서버 하트블리드 취약점 존재",
        "Detail": "2014년 4월 1일 이전에 업로드 된 SSL/TLS 인증서가 존재합니다."
      }
    ],
    "HistoryBasedPriv": [
      {
        "id": "2.1.1",
        "Description": "과도한 권한 IAM USER",
        "Detail": "IAM USER에게 연결된 서비스"
      },
      {
        "id": "2.1.2",
        "Description": "과도한 권한 IAM GROUP",
        "Detail": "IAM GROUP에게 연결된 서비스"
      },
      {
        "id": "2.1.3",
        "Description": "과도한 권한 IAM ROLE",
        "Detail": "IAM ROLE에게 연결된 서비스"
      }
    ],
    "UnusedIAM": [
      {
        "id": "2.2.1",
        "Description": "미사용 IAM USER",
        "Detail": "90일 이내 액세스 키나 패스워드를 통해 IAM 사용자가 접속한 기록이 없습니다."
      },
      {
        "id": "2.2.2",
        "Description": "미사용 IAM GROUP",
        "Detail": "90일 이내 IAM GROUP을 이용하여 AWS 서비스에서 접근한 기록이 없습니다."
      },
      {
        "id": "2.2.3",
        "Description": "미사용 IAM ROLE",
        "Detail": "90일 이내 IAM ROLE을 사용한 기록이 없습니다."
      },
      {
        "id": "2.2.4",
        "Description": "미사용 IAM POLICY",
        "Detail": "90일 이내 해당 IAM POLICY를 이용하여 AWS 서비스에서 접근한 기록이 없습니다."
      }
    ],
    "UnconnectedIAM": [
      {
        "id": "2.3.1",
        "Description": "미연결 IAM USER",
        "Detail": "IAM USER에 연결된 관리형/인라인 정책이 없습니다."
      },
      {
        "id": "2.3.2",
        "Description": "미연결 IAM GROUP",
        "Detail": "IAM GROUP에 연결된 IAM USER가 없습니다."
      },
      {
        "id": "2.3.3",
        "Description": "미연결 IAM ROLE",
        "Detail": "IAM ROLE에 연결된 관리형/인라인 정책이 없습니다."
      },
      {
        "id": "2.3.4",
        "Description": "미연결 IAM POLICY",
        "Detail": "고객 관리형 IAM POLICY에 연결된 AIM 엔티티가 없습니다."
      }
    ],
    "ExcessivePriv": [
      {
        "id": "2.4.1",
        "Description": "조직도 기반 과도한 권한",
        "Detail": "자신이 해당하는 조직의 조직원들과는 다른 권한이 존재합니다."
      }
    ],
    "Duplicate": [
      {
        "id": "2.4.2",
        "Description": "중복된 정책",
        "Detail": "  기존에 만들어진 정책과 동일한 정책이 생성되었습니다."
      }
    ]
  },
  "Version": "1.0"
}
```

### POST  /api/v1/scanning

### Description

- 스캐닝 트리거
- 스캐닝 완료시 Discord로 notification

### Request body schema

- **checkedCount**  : integer   (required)
    - 체크된 항목 수
- **checkedList**  : list[dict]   ****(required) ****
    - 체크된 항목

### Request sample

```json
{
    "checkedCount": 0,
    "checkedList": [
        {
            "1.1.1": true,
            "1.1.2": true,
            "1.1.3": true,
            "1.1.4": true,
            "1.1.5": true,
            "1.1.6": true,
            "1.1.7": true
        },
        {
            "1.2.1": true,
            "1.2.2": true
        },
        {
            "1.3.1": true,
            "1.3.2": true,
            "1.3.3": true,
            "1.3.4": true,
            "1.3.5": true,
            "1.3.6": true
        },
        {
            "1.4.1": true,
            "1.4.2": true
        },
        {
            "2.1.1": true,
            "2.1.2": true,
            "2.1.3": true
        },
        {
            "2.2.1": true,
            "2.2.2": true,
            "2.2.3": true,
            "2.2.4": true
        },
        {
            "2.3.1": true,
            "2.3.2": true,
            "2.3.3": true,
            "2.3.4": true
        },
        {
            "2.4.1": true,
            "2.4.2": true
        }
    ]
  }
```

### Response sample

```json

```

### GET  ~~/api/v1/scanning/recent~~ (수정중)

### Description

- 

### Query parameters

- 

### Response sample

```json

```

### GET  /api/v1/monitoring

### Description

- 모니터링 항목 리스트 반환

### Note

<aside>
💡 현재의 Demo 버전 monitoring api는 **항목 리스트만** 반환합니다.
추 후 **항목별 체크 여부**가 추가 될 예정입니다.

</aside>

### Query parameters

- None

### Response sample

```json
{
  "MonitoringList": {
    "IAM": [
      {
        "id": "3.1.1",
        "Description": "권한 확대",
        "Detail": "기존에 존재하지 않은 권한이 생겼습니다"
      },
      {
        "id": "3.1.2",
        "Description": "조직도 기반 과도한 권한",
        "Detail": "자신이 해당하는 조직의 조직원들과는 다른 권한이 존재합니다."
      },
      {
        "id": "3.1.3",
        "Description": "인라인 정책 사용",
        "Detail": "IAM 리소스에 연결된 인라인 정책이 존재합니다"
      },
      {
        "id": "3.1.4",
        "Description": "Administrator 정책 사용",
        "Detail": "IAM 리소스에 모든 서비스를 이용할 수 있는 관리자급 권한의 AdministratorAccess 정책을 사용합니다."
      },
      {
        "id": "3.1.5",
        "Description": "AWSCloudTrail_FullAccess 정책 사용",
        "Detail": "IAM 리소스가 CloudTrail을 비활성화하거나 재구성할 수 있는 'AWSCloudTrail_FullAccess' 정책을 사용합니다."
      },
      {
        "id": "3.2.1",
        "Description": "IAM Policy 권한에 '*'' 사용",
        "Detail": "IAM POLICY에서 Effect:Allow 와 'Action' 조합을 사용하면서 모든 서비스 또는 액션을 표현하는 '*'을 사용했습니다."
      },
      {
        "id": "3.2.2",
        "Description": "IAM Policy 리소스에 '*'' 사용",
        "Detail": "IAM POLICY에서 Effect:Allow 와 'Action' 조합을 사용하면서 모든 리소스를 표현하는 '*'을 사용했습니다."
      },
      {
        "id": "3.2.4",
        "Description": "IAM Policy Deny 암묵적 표현",
        "Detail": "IAM POLICY에 Deny를 명시적으로 작성하지 않았습니다."
      },
      {
        "id": "3.2.5",
        "Description": "IAM Policy Effect Allow 와 NotAction 조합 사용",
        "Detail": "IAM POlicy에서 Effect:Allow 와 'NOTAction' 조합을 사용했다. 명시적으로 작성하지 않은 서비스 리소스를 사용할 수 있기에 의도한것보다 많은 권한을 부여할 수 있습니다."
      }
    ],
    "Services": [
      {
        "id": "3.3.1",
        "Description": "미사용 활동 리전",
        "Detail": "평소 활동하지 않던 리전에서 활동이 발생했습니다."
      },
      {
        "id": "3.3.2",
        "Description": "미사용 권한/리소스 접근",
        "Detail": "평소 사용하지 않던 권한/리소스를 사용했습니다."
      },
      {
        "id": "3.3.3",
        "Description": "미접속 IP 접근",
        "Detail": "평소 접속하지 않던 IP를 이용한 접속이 발생했습니다."
      },
      {
        "id": "3.3.4",
        "Description": "로그인 연속 실패",
        "Detail": "로그인 시도 연속 5회 실패했습니다."
      },
      {
        "id": "3.3.5",
        "Description": "Root 사용",
        "Detail": "Root 계정을 사용했습니다."
      }
    ]
  },
  "Version": "1.0"
}
```

### PUT  ~~/api/v1/monitoring~~ (수정중)

### Description

- 모니터링 항목 업데이트

### Note

<aside>
💡 현재의 Demo 버전 monitoring api는 **항목 리스트만** 반환합니다.
추 후 **항목별 체크 여부**가 추가 될 예정입니다.

</aside>

### Query parameters

- None

### Response sample

```json
{
  "MonitoringList": {
    "IAM": [
      {
        "id": "3.1.1",
        "Description": "권한 확대",
        "Detail": "기존에 존재하지 않은 권한이 생겼습니다"
      },
      {
        "id": "3.1.2",
        "Description": "조직도 기반 과도한 권한",
        "Detail": "자신이 해당하는 조직의 조직원들과는 다른 권한이 존재합니다."
      },
      {
        "id": "3.1.3",
        "Description": "인라인 정책 사용",
        "Detail": "IAM 리소스에 연결된 인라인 정책이 존재합니다"
      },
      {
        "id": "3.1.4",
        "Description": "Administrator 정책 사용",
        "Detail": "IAM 리소스에 모든 서비스를 이용할 수 있는 관리자급 권한의 AdministratorAccess 정책을 사용합니다."
      },
      {
        "id": "3.1.5",
        "Description": "AWSCloudTrail_FullAccess 정책 사용",
        "Detail": "IAM 리소스가 CloudTrail을 비활성화하거나 재구성할 수 있는 'AWSCloudTrail_FullAccess' 정책을 사용합니다."
      },
      {
        "id": "3.2.1",
        "Description": "IAM Policy 권한에 '*'' 사용",
        "Detail": "IAM POLICY에서 Effect:Allow 와 'Action' 조합을 사용하면서 모든 서비스 또는 액션을 표현하는 '*'을 사용했습니다."
      },
      {
        "id": "3.2.2",
        "Description": "IAM Policy 리소스에 '*'' 사용",
        "Detail": "IAM POLICY에서 Effect:Allow 와 'Action' 조합을 사용하면서 모든 리소스를 표현하는 '*'을 사용했습니다."
      },
      {
        "id": "3.2.4",
        "Description": "IAM Policy Deny 암묵적 표현",
        "Detail": "IAM POLICY에 Deny를 명시적으로 작성하지 않았습니다."
      },
      {
        "id": "3.2.5",
        "Description": "IAM Policy Effect Allow 와 NotAction 조합 사용",
        "Detail": "IAM POlicy에서 Effect:Allow 와 'NOTAction' 조합을 사용했다. 명시적으로 작성하지 않은 서비스 리소스를 사용할 수 있기에 의도한것보다 많은 권한을 부여할 수 있습니다."
      }
    ],
    "Services": [
      {
        "id": "3.3.1",
        "Description": "미사용 활동 리전",
        "Detail": "평소 활동하지 않던 리전에서 활동이 발생했습니다."
      },
      {
        "id": "3.3.2",
        "Description": "미사용 권한/리소스 접근",
        "Detail": "평소 사용하지 않던 권한/리소스를 사용했습니다."
      },
      {
        "id": "3.3.3",
        "Description": "미접속 IP 접근",
        "Detail": "평소 접속하지 않던 IP를 이용한 접속이 발생했습니다."
      },
      {
        "id": "3.3.4",
        "Description": "로그인 연속 실패",
        "Detail": "로그인 시도 연속 5회 실패했습니다."
      },
      {
        "id": "3.3.5",
        "Description": "Root 사용",
        "Detail": "Root 계정을 사용했습니다."
      }
    ]
  },
  "Version": "1.0"
}
```