import json
import requests
import openpyxl
import datetime
from tqdm import tqdm
# Set the API key and headers
API_KEY = ""
headers = {
    "Authorization": "Bearer {}".format(API_KEY)
}

# Make the request
response = requests.get(
    "https://api.clashroyale.com/v1/locations/57000228/pathoflegend/players",
    headers=headers,
)

now = datetime.datetime.now()
now_str = now.strftime("%Y-%m-%d")

wb = openpyxl.Workbook() 
ws = wb.active

ws.cell(row=1, column=1).value = "ID"
ws.cell(row=1, column=2).value = "Name"
ws.cell(row=1, column=3).value = "Rating"

row_number = 2
for player in tqdm(response.json()["items"]):
    ws.cell(row=row_number, column=1).value = player["tag"]
    ws.cell(row=row_number, column=2).value = player["name"]
    ws.cell(row=row_number, column=3).value = player["eloRating"]
    row_number += 1

wb.save(now_str+".xlsx")
print("執行完成")
