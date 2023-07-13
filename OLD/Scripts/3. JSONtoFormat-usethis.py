import re
import json
import os
import shutil

x = 4

while x < 1136:
    song_json = '/Users/jobinthomas/VirtualSongbook/assets/songs.json'
    song_number = x
    folder_path = "/NEW/ReadyToUpload"
    file_name = f"{x}.txt"
    if os.path.isfile(os.path.join(folder_path, file_name)):
        notes = {"C": 0, "C#": 1, "Db": 1, "D": 2, "Eb": 3, "D#": 3, "E": 4, "F": 5, "F#": 6, "Gb": 6, "G": 7, "G#": 8, "Ab": 8, "A": 9, "Bb": 10, "A#": 10, "B": 11}

        # open the input file for reading
        with open(f"/NEW/ReadyToUpload/{x}.txt", "r") as f:
            text = f.read()

        # replace letters with numbers using a regular expression
        pattern = r"\|([A-G](#|b)?)(\|)"
        text = re.sub(pattern, lambda match: "|" + str(notes[match.group(1)]) + match.group(3), text)

        # open the output file for writing
        with open(f"/NEW/ReadyToUpload/{x}.txt", "w") as f:
            f.write(text)

        with open(f"/NEW/ReadyToUpload/{x}.txt", 'r') as f:
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

        source_file_path = f"/NEW/ReadyToUpload/{x}.txt"
        destination_folder_path = "/UploadedToDB/"
        shutil.move(source_file_path, destination_folder_path)
        x = x + 1

    else:
        print(f'{x}.txt is not in the queue')
        x = x + 1
