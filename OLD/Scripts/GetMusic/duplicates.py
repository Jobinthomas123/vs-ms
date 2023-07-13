import json

with open('music.json') as f:
    data = json.load(f)

song_numbers = []
duplicates = []

for item in data:
    if item['song_number'] in song_numbers:
        duplicates.append(item['song_number'])
    else:
        song_numbers.append(item['song_number'])

if len(duplicates) > 0:
    print("Duplicate song numbers found: ")
    print(duplicates)
else:
    print("No duplicates found.")
