import os
import shutil

folder_path = "/songtext"
review_path = "/NEW/Review"
rtu_path = "/NEW/ReadyToUpload"
uploaded_path = "/UploadedToDB"
x = 4

while x < 1136:
    file_name = f"{x}.txt"
    if os.path.isfile(os.path.join(folder_path, file_name)):
        if os.path.isfile(os.path.join(review_path, file_name)):
            print(f'{x}.txt is in review')
            x = x + 1

        elif os.path.isfile(os.path.join(rtu_path, file_name)):
            print(f'{x}.txt is ready for upload')
            x = x + 1

        elif os.path.isfile(os.path.join(uploaded_path, file_name)):
            print(f'{x}.txt has already been uploaded')
            x = x + 1

        else:
            source_folder_path = "/songtext"
            destination_folder_path = "/TO-DO"
            file_name = f"{x}.txt"
            if os.path.isfile(os.path.join(source_folder_path, file_name)):
                source_file_path = os.path.join(source_folder_path, file_name)
                destination_file_path = os.path.join(destination_folder_path, file_name)
                shutil.copy(source_file_path, destination_file_path)
                print(f"{x}.txt has been copied to the destination folder.")
                x = x + 1
            else:
                # File not found
                print(f"{x}.txt does not exist in the source folder.")
                x = x + 1
