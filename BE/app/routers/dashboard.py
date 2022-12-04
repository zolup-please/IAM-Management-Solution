from fastapi import APIRouter

router = APIRouter(prefix="/dashboard")

fake_response = {
    "RecentReport": {
        # 0개에서 최대 5개까지
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
    "IAMActivities": {
        #흠... 시간대 별로 드리면 되나용?
    },
    "Changes": {
        # 금일 변동 사항
        "Total": 3,
        "Created": 2,
        "Deleted": 2
    }
}

@router.get("/")
async def dashboard():
    return fake_response