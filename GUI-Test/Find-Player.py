import tkinter as tk
import json
import requests

def get_player_data():
    api_key = api_key_entry.get()
    player_tag = player_tag_entry.get()

    headers = {"Authorization": f"Bearer {api_key}"}
    url = f"https://api.clashroyale.com/v1/players/{player_tag}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        player_data = response.json()
        player_name = player_data['name']
        # player_trophies = player_data['trophies']
        All_data = response.json()

        with open(player_name+".json", "w", encoding="utf-8") as f:
         json.dump(All_data, f, ensure_ascii=False)

        result_label["text"] = f"Player Name: {player_name}\n"
    except requests.exceptions.RequestException as e:
        result_label["text"] = f"Error: {e}"

root = tk.Tk()
root.title("Clash Royale Player Data")

api_key_label = tk.Label(root, text="API Key:")
api_key_entry = tk.Entry(root)

player_tag_label = tk.Label(root, text="Player Tag:")
player_tag_entry = tk.Entry(root)

get_data_button = tk.Button(root, text="Get Data", command=get_player_data)

result_label = tk.Label(root, text="")

api_key_label.grid(row=0, column=0)
api_key_entry.grid(row=0, column=1)

player_tag_label.grid(row=1, column=0)
player_tag_entry.grid(row=1, column=1)

get_data_button.grid(row=2, columnspan=2)
result_label.grid(row=3, columnspan=2)

root.mainloop()
