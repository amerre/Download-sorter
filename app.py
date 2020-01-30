import os
import shutil
from os import path

# ------------------------------
# Create directories
def create_dir(directory, parent_directory = "/Users/Adrien/dev/python"):
    try:
        path = os.path.join(parent_directory, directory)
        os.mkdir(path)
        print("Directory "+ directory +" has been created!")
    except FileExistsError:
        print("Files already exist")
# ------------------------------

# Files
files = [f for f in os.listdir() if path.isfile(f)]
# Directories
dir = [d for d in os.listdir() if path.isdir(d)]

# Array where files are gonna be dispatched
filesList = {
    "videos": [],
    "documents": [],
    "compressed": [],
    "photos": [],
    "executables": []
}

# Where we distinguish files between themselves
for file in files:
    extension = file.split(".",1)[1]
    # Vidéos (avi, mkv, mp4...)
    if  extension == "avi" or "mkv" or "mp4" or "mov":
        filesList["video"].append(file)
    # Text based documents (pdf, doc, txt...)
    elif  extension == "pdf" or "doc" or "txt" or "odf":
        filesList["documents"].append(file)
    # Compressed documents (zip, rar...)
    elif  extension == "zip" or "rar":
        filesList["compressed"].append(file)

print(filesList)
    