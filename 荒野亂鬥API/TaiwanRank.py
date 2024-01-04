import json
import requests
import openpyxl
import datetime

# Set the API key and headers
API_KEY = ""
headers = {
    "Authorization": "Bearer {}".format(API_KEY)
}

# Make the request
response = requests.get(
    "https://api.brawlstars.com/v1/rankings/TW/players",
    headers=headers,
)

# Load the existing Excel workbook
wb = openpyxl.Workbook() 

# Create a new worksheet
ws = wb.active

# Write the header row
# ws.cell(row=1, column=1).value = "Rank"
ws.cell(row=1, column=1).value = "tag"
ws.cell(row=1, column=2).value = "name"
ws.cell(row=1, column=2).value = "trophies"
ws.cell(row=1, column=2).value = "rank"

now = datetime.datetime.now()
now_str = now.strftime("%Y-%m-%d %H:%M:%S")
ws["F1"] = "執行時間"
ws["F2"] = now_str

# Write the player data
row_number = 2
for player in response.json()["items"]:
    # ws.cell(row=row_number, column=1).value = player["rank"]
    ws.cell(row=row_number, column=1).value = player["tag"]
    ws.cell(row=row_number, column=2).value = player["name"]
    ws.cell(row=row_number, column=3).value = player["trophies"]
    ws.cell(row=row_number, column=4).value = player["rank"]
    row_number += 1

# Save the existing Excel workbook
wb.save("TaiwanRank.xlsx")
print("執行完成")