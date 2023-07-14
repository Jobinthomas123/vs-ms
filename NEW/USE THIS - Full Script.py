import shutil
import os
import re
import json

completed = '/Users/jobinthomas/PycharmProjects/Virtual Songbook Microservices/NEW/COMPLETED'
review = '/Users/jobinthomas/PycharmProjects/Virtual Songbook Microservices/NEW/Review'
ready = '/Users/jobinthomas/PycharmProjects/Virtual Songbook Microservices/NEW/ReadyToUpload'
uploaded = '/Users/jobinthomas/PycharmProjects/Virtual Songbook Microservices/NEW/UploadedToDB'
with_astrick = '/Users/jobinthomas/PycharmProjects/Virtual Songbook Microservices/NEW/with *'
without = '/Users/jobinthomas/PycharmProjects/Virtual Songbook Microservices/NEW/without *'
song_json = '/Users/jobinthomas/VirtualSongbook/assets/songs.json'


# Path to the source folder containing the text files
source_folder = completed

# Path to the destination folder to move files without '|'
destination_folder_review = review

# Iterate through each file in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith('.txt'):  # Consider only text files
        file_path = os.path.join(source_folder, filename)
        with open(file_path, 'r') as file:
            content = file.read()
            count = content.count('|')
            if count % 2 != 0:  # Check if the count is an even number
                # Move the file to the destination folder
                shutil.move(file_path, os.path.join(destination_folder_review, filename))
                print(f"Moved {filename} to the review folder.")


# Specify the source and destination folders
source_folder = completed
destination_folder = with_astrick

# Get a list of all text files in the source folder
text_files = [f for f in os.listdir(source_folder) if f.endswith('.txt')]

# Copy each text file from the source folder to the destination folder
for file in text_files:
    source_file = os.path.join(source_folder, file)
    destination_file = os.path.join(destination_folder, file)
    shutil.copy(source_file, destination_file)

print("Files with * copied successfully.")


# Specify the source and destination folders
source_folder = completed
destination_folder_two = without

# Get a list of all text files in the source folder
text_files = [f for f in os.listdir(source_folder) if f.endswith('.txt')]

# Copy and modify each text file
for file in text_files:
    source_file = os.path.join(source_folder, file)
    destination_file = os.path.join(destination_folder_two, file)  # Use destination_folder_two here
    # Read the source file
    with open(source_file, 'r') as f:
        content = f.read()

    # Remove "*" from the content
    modified_content = content.replace('*', '')

    # Write the modified content to the destination file
    with open(destination_file, 'w') as f:  # Use destination_file here
        f.write(modified_content)

print("Removed * and copied files successfully.")


choice = input('Would you like to upload with or without *? 1 - With 2 - Without ')


if choice == '1':
    notes = {"C": 0, "C#": 1, "Db": 1, "D": 2, "Eb": 3, "D#": 3, "E": 4, "F": 5, "F#": 6, "Gb": 6, "G": 7, "G#": 8,
             "Ab": 8, "A": 9, "Bb": 10, "A#": 10, "B": 11}

    folder_path = with_astrick

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r") as file:
                lines = file.readlines()

            modified_lines = []  # Store the modified lines

            for line in lines:
                matches = re.findall(r"\|(.*?)\|", line)
                if matches:
                    for match in matches:
                        notes_str = match.strip()
                        notes_list = notes_str.split()
                        converted_notes = []
                        for note in notes_list:
                            if note in notes:
                                converted_notes.append(str(notes[note]))
                            else:
                                converted_notes.append(note)
                        converted_notes_str = " ".join(converted_notes)
                        line = line.replace("|" + notes_str + "|", "|" + converted_notes_str + "|")

                modified_lines.append(line)  # Append the modified line to the list

            # Write the modified lines back to the file
            with open(file_path, "w") as file:
                file.writelines(modified_lines)

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):  # Consider only text files
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r") as file:
                file_contents = file.read().replace("\n", "\n")
                print(file_contents)

                song_number = filename[:-4]
                song_number = int(song_number)

                # load the song data from the json file
                with open(song_json, 'r') as f:
                    songs = json.load(f)

                # find the song with the given song number
                for song in songs:
                    if song['song_number'] == int(song_number):
                        # update the lyrics field with the parsed song_string
                        song['lyrics'] = file_contents

                # save the updated song data back to the json file
                with open(song_json, 'w') as f:
                    json.dump(songs, f, indent=4)


elif choice == '2':
    notes = {"C": 0, "C#": 1, "Db": 1, "D": 2, "Eb": 3, "D#": 3, "E": 4, "F": 5, "F#": 6, "Gb": 6, "G": 7, "G#": 8,
             "Ab": 8, "A": 9, "Bb": 10, "A#": 10, "B": 11}

    folder_path = without

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r") as file:
                lines = file.readlines()

            modified_lines = []  # Store the modified lines

            for line in lines:
                matches = re.findall(r"\|(.*?)\|", line)
                if matches:
                    for match in matches:
                        notes_str = match.strip()
                        notes_list = notes_str.split()
                        converted_notes = []
                        for note in notes_list:
                            if note in notes:
                                converted_notes.append(str(notes[note]))
                            else:
                                converted_notes.append(note)
                        converted_notes_str = " ".join(converted_notes)
                        line = line.replace("|" + notes_str + "|", "|" + converted_notes_str + "|")

                modified_lines.append(line)  # Append the modified line to the list

            # Write the modified lines back to the file
            with open(file_path, "w") as file:
                file.writelines(modified_lines)

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):  # Consider only text files
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r") as file:
                file_contents = file.read().replace("\n", "\n")
                print(file_contents)

                song_number = filename[:-4]
                song_number = int(song_number)

                # load the song data from the json file
                with open(song_json, 'r') as f:
                    songs = json.load(f)

                # find the song with the given song number
                for song in songs:
                    if song['song_number'] == int(song_number):
                        # update the lyrics field with the parsed song_string
                        song['lyrics'] = file_contents

                # save the updated song data back to the json file
                with open(song_json, 'w') as f:
                    json.dump(songs, f, indent=4)

else:
    print('Invalid choice')
