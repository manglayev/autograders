import os
if __name__ == "__main__":
  path = "/Users/talgatmanglayev/Desktop/CSCI-111/hw-1"
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
                    with open(file, 'r+') as content_file:
                        body = content_file.read()
                        content_file.seek(0)
                        content_file.write('"' + body)
                        content_file = open(file, "r")
                    content_file.close()
                    content_file = open(file, "a")
                    content_file.write('"')
                    content_file.close()                    
  print("COMPLETED")