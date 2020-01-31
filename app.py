import os
from os import path

# -----------Functions-----------
# Create directories
def create_dir(directory, parent_directory = "/Users/Adrien/dev/python/Download-organizer"):
    try:
        path = os.path.join(parent_directory, directory)
        os.mkdir(path)
        print("Directory '" + directory + "' has been created!")
    except FileExistsError:
        print("Files already exist")
# ------------------------------


# Files
files = [f for f in os.listdir() if path.isfile(f)]
# Directories
directories = [d for d in os.listdir() if path.isdir(d)]

# Array where files are gonna be dispatched
filesList = {
    "videos": [],
    "documents": [],
    "compressed": [],
    "photos": [],
    "executables": []
}

# Where we distinguish files between themselves and sort them in the array
for file in files:
    extension = file.split(".",1)[1]
    # Vidéos (avi, mkv, mp4...)
    if extension == "avi" or extension == "mkv" or extension == "mp4" or extension == "mov":
        filesList["videos"].append(file)
    # Text based documents (pdf, doc, txt...)
    elif extension == "pdf" or extension == "doc" or extension == "txt" or extension == "odf":
        filesList["documents"].append(file)
    # Compressed documents (zip, rar...)
    elif  extension == "zip" or extension == "rar":
        filesList["compressed"].append(file)
    # Executables (exe...)
    elif  extension == "png" or extension == "jpg":
        filesList["photos"].append(file)
    # Executables (exe...)
    elif  extension == "exe":
        filesList["executables"].append(file)

# Created directories that we need in function or the files
for fileType in filesList:
    if filesList[fileType]:
        create_dir(fileType)
        for file in filesList[fileType]:
            os.rename("/Users/Adrien/dev/python/Download-organizer/" + file, "/Users/Adrien/dev/python/Download-organizer/" + fileType + "/" + file)
            print(file + " has been sorted in the " + fileType + " directory")
