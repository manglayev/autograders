import os
if __name__ == "__main__":
  path = "/Users/talgatmanglayev/Desktop/CSCI-111/hw-1_test_2"
  pathObject = os.scandir(path)
  for directory in pathObject:
    if directory.is_dir():
        files = os.scandir(directory)
        for file in files:
            if file.is_file():
                split_tup = os.path.splitext(file)
                file_name = split_tup[0]                
                file_extension = split_tup[1]
                if file_name.endswith("feedback") and file_extension == ".txt":                    
                    f = open(file, "r")
                    for x in f:
                        x.strip()
  print("COMPLETED")