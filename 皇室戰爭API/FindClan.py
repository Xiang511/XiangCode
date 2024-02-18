import requests
import pandas as pd
import time

#計算起始時間
start_time = time.time()

# 設定 API 金鑰
# 前往 https://developer.clashroyale.com/#/ 取得

API_KEY = ""
headers = {
    "Authorization": "Bearer {}".format(API_KEY)
}

# 取得部落標籤
#ex: %23QCRY22P8

clan_tag = "%23QCRY22P8"

# 建立請求
url = "https://api.clashroyale.com/v1/clans/{}".format(clan_tag)
response = requests.get(url, headers=headers)

# 處理回應
try:
    if response.status_code == 200:
        clan = response.json()

        df = pd.DataFrame(clan["memberList"])
        df.to_excel("FindClan.xlsx")

        #計算結束時間
        end_time = time.time()
        
        print(f"執行時間：{end_time - start_time}")
    else:
        print(response.status_code)
except Exception as e:
    print(e)