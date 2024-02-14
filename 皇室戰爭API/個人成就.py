import openpyxl
import requests
import json
import re
import time
start_time = time.time()
API_KEY = ""
headers = {
    "Authorization": "Bearer {}".format(API_KEY)
}

player_tags = []
              
wb = openpyxl.Workbook()
ws = wb.active

ws["A1"] = "遊戲ID"
ws["B1"] = "經典挑戰12勝次數"
ws["C1"] = "終極挑戰12勝次數"
ws["D1"] = "遊玩時間"
ws["E1"] = "表情收集次數"
ws["F1"] = "戰旗收集次數"
ws["G1"] = "星光點數"
ws["H1"] = "全部經驗值"

def clean_result(result):
    if result is None:
        return ""
    return result[result.rfind(" ") + 1:].split("}")[0]


def keep_numbers(string):
  
  filtered_string = filter(str.isdigit, string)
  return "".join(filtered_string)

def get_numbers_by_position_and_delete(variable, start_position, end_position):

  numbers = str(variable)[start_position:end_position]
  filtered_numbers = filter(str.isdigit, numbers)
  return "".join(filtered_numbers)

x=0




for player_tag in player_tags:
    response = requests.get(f"https://api.clashroyale.com/v1/players/{player_tag}", headers=headers)
    
    player_data = response.json()
    best = json.dumps(player_data.get("bestPathOfLegendSeasonResult"))
    last = json.dumps(player_data.get("lastPathOfLegendSeasonResult"))

    best2 = clean_result(best)
    last2= clean_result(last)

    best3 = get_numbers_by_position_and_delete(keep_numbers(best), 2, 6)
    last3 = get_numbers_by_position_and_delete(keep_numbers(last), 2, 6)

    y=player_data["tag"]

    Classic12WinsCout =0 
    Grand12WinsCout = 0

    starPoints = player_data["starPoints"]

    totalExpPoints = player_data["totalExpPoints"]
    
    for Classic12Wins in player_data["badges"]:
       if Classic12Wins["name"] == "Classic12Wins":
        Classic12WinsCout = Classic12Wins["progress"]

    for Grand12Wins in player_data["badges"]:
       if Grand12Wins["name"] == "Grand12Wins":
        Grand12WinsCout = Grand12Wins["progress"]

    for YearsPlayed in player_data["badges"]:
       if YearsPlayed["name"] == "YearsPlayed":
        YearsPlayedCout = YearsPlayed["progress"]

    for EmoteCollection in player_data["badges"]:
       if EmoteCollection["name"] == "EmoteCollection":
        EmoteCollectionCout = EmoteCollection["progress"]

    for BannerCollection in player_data["badges"]:
       if BannerCollection["name"] == "BannerCollection":
        BannerCollectionCout = BannerCollection["progress"]


    # for PracticewithFriendsCout in player_data["achievements"]:
    #   if PracticewithFriendsCout["name"] == "Practice with Friends":
    #     PracticewithFriendsCoutCout = PracticewithFriendsCout["value"]





    ws.append([
    player_data["name"],Classic12WinsCout,Grand12WinsCout,YearsPlayedCout,EmoteCollectionCout,BannerCollectionCout,starPoints,totalExpPoints])

    x+=1
    print(x)
wb.save("TCRS.xlsx")

end_time = time.time()
print(f"執行時間：{end_time - start_time}")