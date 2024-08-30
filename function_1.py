import os
from zipfile import ZipFile
#Loop through the directory and identify:
#if there are files with zip extension and unarchive them
path = "/Users/talgatmanglayev/Desktop/CSCI-111/hw-1_test"
#directoryObject = os.scandir()
directoryObject = os.scandir(path)
file_path = ""
feedback_file = ""
#print("Files and Directories in '% s':" % path)
for entry in directoryObject:
  if entry.is_dir():
    entryDirectory = os.scandir(entry)
    for zip_file in entryDirectory:
      if zip_file.is_file():
        split_tup = os.path.splitext(zip_file)
        # extract the file name and extension
        file_name = split_tup[0]
        file_extension = split_tup[1]
        if file_extension == ".zip":
          #print(file_name+file_extension)
          os.rename(zip_file, file_name+"_archive.zip")
          with ZipFile(zip_file, 'r') as zObject:
            zObject.extractall(path = os.path.dirname(zip_file))      