import shutil
import os

folder_path = "/NEW/COMPLETED"

x = 4
while x < 1136:
    file_name = f"{x}.txt"
    if os.path.isfile(os.path.join(folder_path, file_name)):
        source_file = f'/NEW/COMPLETED/{x}.txt'
        destination_folder = '/Users/jobinthomas/PycharmProjects/Virtual Songbook Microservices/with *'
        shutil.copy(source_file, destination_folder)


        source_file = f'/NEW/COMPLETED/{x}.txt'
        destination_folder = '/Users/jobinthomas/PycharmProjects/Virtual Songbook Microservices/without *'
        shutil.copy(source_file, destination_folder)

        filename = f"/NEW/without */{x}.txt"
        with open(filename, 'r') as file:
            file_contents = file.read()
        modified_contents = file_contents.replace('*', '')
        with open(filename, 'w') as file:
            file.write(modified_contents)

        x = x + 1

    else:
        x = x + 1

determineDB = input('Would you like to use the songs with *\'s? 1 = Yes, 2 = No ')

if determineDB == "YES":
    x = 4
    while x < 1136:
        file_name = f"{x}.txt"
        if os.path.isfile(os.path.join(folder_path, file_name)):
            source_file = f'/NEW/with */{x}.txt'
            destination_folder = '/Users/jobinthomas/PycharmProjects/Virtual Songbook Microservices/COMPLETED'
            shutil.copy(source_file, destination_folder)
            x = x + 1
        else:
            x = x + 1
elif determineDB == "NO":
    x = 4
    while x < 1136:
        file_name = f"{x}.txt"
        if os.path.isfile(os.path.join(folder_path, file_name)):
            source_file = f'/NEW/without */{x}.txt'
            destination_folder = '/Users/jobinthomas/PycharmProjects/Virtual Songbook Microservices/COMPLETED'
            shutil.copy(source_file, destination_folder)
            x = x + 1
        else:
            x = x + 1
