# let's practice the os module:
import os
from datetime import datetime
import pandas as pd
print(os.getcwd())
# os.makedirs("D:/BIOINFORMATICS/smart/Envelope")
print(os.getcwd())
# getting information about a file: size, last time modified etc
# ----------------------------------------------------------------------------------------
info = os.stat("current.txt")
last_modified = info.st_mtime
print("Last Modidified : ", datetime.fromtimestamp(last_modified))
file_size = info.st_size
print("file size :", file_size ,"bytes")
# ----------------------------------------------------------------------------------------
# loop throught the folders and files in the directory
sizes = []
file_name = []
modified = []
is_dir = []
for file in os.listdir("D:/BIOINFORMATICS/Gene_files"):
    # creates an absolute file path for each item:
    path = f"D:/BIOINFORMATICS/Gene_files/{file}"
    # checks if it is a directory
    type = os.path.isdir(path)
    file_info = os.stat(path)
    # let's query the information of each file
    size = file_info.st_size
    last_modified = datetime.fromtimestamp(file_info.st_mtime)
    # appending information into a list
    file_name.append(file)
    sizes.append(size)
    is_dir.append(type)
    modified.append(last_modified)
files_info = pd.DataFrame(
    {
        "Filename": file_name,
        "File_Size": sizes,
        "Directory": is_dir,
        "Last_Modified":modified
    }
)
print(files_info)