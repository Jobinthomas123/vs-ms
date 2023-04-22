import re
import json
x = 4

while x < 27:
    song_json = '/Users/jobinthomas/VirtualSongbook/assets/songs.json'
    song_number = x

    notes = {"C": 0, "C#": 1, "D": 2, "Eb": 3, "E": 4, "F": 5, "F#": 6, "G": 7, "G#": 8, "A": 9, "Bb": 10, "B": 11}

    # open the input file for reading
    with open(f"songtext/{x}.txt", "r") as f:
        text = f.read()

    # replace letters with numbers using a regular expression
    pattern = r"\|([A-G](#|b)?)(\|)"
    text = re.sub(pattern, lambda match: "|" + str(notes[match.group(1)]) + match.group(3), text)

    # open the output file for writing
    with open(f"songtext/{x}.txt", "w") as f:
        f.write(text)

    with open(f"songtext/{x}.txt", 'r') as f:
        lines = f.readlines()
        one_line = ''.join([line.rstrip('\n') + '\n' for line in lines])

    # load the song data from the json file
    with open(song_json, 'r') as f:
        songs = json.load(f)

    # find the song with the given song number
    for song in songs:
        if song['song_number'] == int(song_number):
            # update the lyrics field with the parsed song_string
            song['lyrics'] = one_line

    # save the updated song data back to the json file
    with open(song_json, 'w') as f:
        json.dump(songs, f, indent=4)

    x = x + 1
