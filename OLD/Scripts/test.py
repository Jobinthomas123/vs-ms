import os
import shutil

file_name = f"455.txt"
folder_path = "/UploadedToDB"
if not os.path.isfile(os.path.join(folder_path, file_name)):
    print('it is not in there')
else:
    print('it is in there')
