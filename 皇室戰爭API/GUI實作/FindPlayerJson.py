import tkinter as tk
import json
import requests

def get_player_data():
    api_key = api_key_entry.get()
    player_tag = player_tag_entry.get()

    headers = {"Authorization": f"Bearer {api_key}"}
    url = f"https://api.clashroyale.com/v1/players/%23{player_tag}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        player_data = response.json()
        player_name = player_data['name']
        # player_trophies = player_data['trophies']
        All_data = response.json()

        with open(player_name+".json", "w", encoding="utf-8") as f:
         json.dump(All_data, f, ensure_ascii=False)

        result_label["text"] = "檔案已儲存於預設路徑內:\n"+"檔名為"+f"{player_name}"+".json"
    except requests.exceptions.RequestException as e:
        result_label["text"] = f"Error: {e}"

root = tk.Tk()
root.title("CR Player Data")


api_key_label = tk.Label(root, text="API Key:")
api_key_entry = tk.Entry(root)

player_tag_label = tk.Label(root, text="Player Tag:")
player_tag_entry = tk.Entry(root)

get_data_button = tk.Button(root, text="Get Data", command=get_player_data)

result_label = tk.Label(root, text="")

api_key_label.grid(row=0, column=0,padx=10,sticky=tk.W)
api_key_entry.grid(row=0, column=1,padx=8,pady=10)

player_tag_label.grid(row=1, column=0,sticky=tk.W)
player_tag_entry.grid(row=1, column=1,pady=10)

get_data_button.grid(row=2,pady=10)
result_label.grid(row=3, columnspan=2)

# 2024/2/25新增
doc = tk.Label(root, text="https://developer.clashroyale.com/#/")
doc.grid(row=4, column=1)

# 介面置中以及大小設置
window_width = root.winfo_screenwidth()    # 取得螢幕寬度
window_height = root.winfo_screenheight()  # 取得螢幕高度

width = 300
height = 200
left = int((window_width - width)/2)       # 計算左上 x 座標
top = int((window_height - height)/2)      # 計算左上 y 座標
root.geometry(f'{width}x{height}+{left}+{top}')
root.mainloop()
