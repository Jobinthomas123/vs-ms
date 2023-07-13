import os
import shutil

folder_path = "/NEW/Review"
x = 4

while x < 1136:
    file_name = f"{x}.txt"
    if os.path.isfile(os.path.join(folder_path, file_name)):
        file_path = f"/NEW/Review/{x}.txt"
        with open(file_path, 'r') as file:
            file_contents = file.read()
            if '|' in file_contents:
                source_file_path = f"/NEW/Review/{x}.txt"
                destination_folder_path = "/NEW/ReadyToUpload/"
                shutil.move(source_file_path, destination_folder_path)
                x = x + 1
            else:
                print(f'{x}.txt still needs to be reviewed')
                x = x + 1

    else:
        x = x + 1
