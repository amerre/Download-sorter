import os
from os import path

# -----------Functions-----------
# Create directories
def create_dir(directory, parent_directory = os.getcwd()):
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
toSort = {
    "videos": [],
    "documents": [],
    "compressed": [],
    "photos": [],
    "executables": [],
    "directories": []
}

# Where we distinguish files between themselves and sort them in the array
for file in files:
    extension = file.rsplit(".",1)[1]
    # Vidéos (avi, mkv, mp4...)
    if extension == "avi" or extension == "mkv" or extension == "mp4" or extension == "mov":
        toSort["videos"].append(file)
    # Text based documents (pdf, doc, txt...)
    elif extension == "pdf" or extension == "doc" or extension == "txt" or extension == "odf" or extension == "docx":
        toSort["documents"].append(file)
    # Compressed documents (zip, rar...)
    elif  extension == "zip" or extension == "rar":
        toSort["compressed"].append(file)
    # Executables (exe...)
    elif  extension == "png" or extension == "jpg":
        toSort["photos"].append(file)
    # Executables (exe...)
    elif  extension == "exe" or extension == "dmg":
        toSort["executables"].append(file)

# Where we distinguish directories and sort them in the array
for directory in directories:
    if directory != "testing_files" and directory != ".git" and directory != "videos" and directory != "documents" and directory != "compressed" and directory != "photos" and directory != "executables" and directory != "directories":
        toSort["directories"].append(directory)


# Created directories that we need in function or the files
for fileType in toSort:
    if toSort[fileType]:
        create_dir(fileType)
        for file in toSort[fileType]:
            os.rename(os.getcwd() + "/" + file, os.getcwd() + "/" + fileType + "/" + file)
            print(os.getcwd() + "/" + file)
            print(file + " has been sorted in the " + fileType + " directory")


