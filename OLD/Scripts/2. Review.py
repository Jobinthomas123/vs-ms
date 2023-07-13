import os
import shutil

folder_path = "/without *"
review_path = "/NEW/Review"
rtu_path = "/NEW/ReadyToUpload"
uploaded_path = "/UploadedToDB"
complete_path = '/NEW/COMPLETED'
x = 4

while x < 1136:
    file_name = f"{x}.txt"
    if os.path.isfile(os.path.join(folder_path, file_name)):
        if os.path.isfile(os.path.join(complete_path, file_name)) and os.path.isfile(os.path.join(review_path, file_name)):
            print(f'{x}.txt is in review')
            delete_file = f'/NEW/COMPLETED/{x}.txt'
            os.remove(delete_file)
            x = x + 1
            print(x)

        elif os.path.isfile(os.path.join(complete_path, file_name)) and os.path.isfile(os.path.join(rtu_path, file_name)):
            print(f'{x}.txt is ready for upload')
            delete_file = f'/NEW/COMPLETED/{x}.txt'
            os.remove(delete_file)
            x = x + 1
            print(x)

        elif os.path.isfile(os.path.join(complete_path, file_name)) and os.path.isfile(os.path.join(uploaded_path, file_name)):
            print(f'{x}.txt has already been uploaded')
            delete_file = f'/NEW/COMPLETED/{x}.txt'
            os.remove(delete_file)
            x = x + 1
            print(x)

        elif os.path.isfile(os.path.join(complete_path, file_name)):
            file_path = f"/NEW/COMPLETED/{x}.txt"
            with open(file_path, 'r') as file:
                file_contents = file.read()
                if '|' in file_contents:
                    source_file_path = f"/NEW/without */{x}.txt"
                    destination_folder_path = "/NEW/ReadyToUpload/"
                    shutil.move(source_file_path, destination_folder_path)
                    x = x + 1
                    print(x)
                else:
                    source_file_path = f"/NEW/without */{x}.txt"
                    destination_folder_path = "/NEW/Review/"
                    shutil.move(source_file_path, destination_folder_path)
                    x = x + 1
                    print(x)
    else:
        x = x + 1
        print(x)