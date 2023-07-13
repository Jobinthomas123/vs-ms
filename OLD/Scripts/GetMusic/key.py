import json

# Open the songs.json file and load the JSON data
with open('songs.json') as f:
    songs = json.load(f)

# Open the music.json file and load the JSON data
with open('music.json') as f:
    music = json.load(f)

# Iterate through each object in the music.json file
for obj in music:
    # Get the song number from the current object
    song_number = obj['song_number']

    # Find the corresponding song in the songs.json file
    for song in songs:
        if song['song_number'] == song_number:
            # Replace the key in the current object with the key from the songs.json file
            obj['key'] = song['key']
            break

# Write the updated music.json data back to the file
with open('music.json', 'w') as f:
    json.dump(music, f, indent=4)
