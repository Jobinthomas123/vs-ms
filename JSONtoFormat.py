import json

with open('/Users/jobinthomas/VirtualSongbook/assets/songs.json', 'r') as f:
    data = json.load(f)

for d in data:
    if str(d["song_number"]).isdigit():
        d["song_number"] = int(d["song_number"])

with open('/Users/jobinthomas/VirtualSongbook/assets/songs.json', 'w') as f:
    json.dump(data, f, indent=4)
