import json

notes = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "G#", "A", "Bb", "B"]

song_json = '/Users/jobinthomas/VirtualSongbook/assets/songs.json'

song_number = input('Enter song number: ')

with open('song.txt', 'r') as f:
    lines = [line.rstrip('\n').lstrip() for line in f.readlines()]

song_string = '\n'.join(lines)  # join the lines with the string "\\n"

for i in range(len(notes)):
    song_string = song_string.replace('|' + notes[i], '|' + str(i))

# load the song data from the json file
with open(song_json, 'r') as f:
    songs = json.load(f)

# find the song with the given song number
for song in songs:
    if song['song_number'] == int(song_number):
        # update the lyrics field with the parsed song_string
        song['lyrics'] = song_string

# save the updated song data back to the json file
with open(song_json, 'w') as f:
    json.dump(songs, f, indent=4)
