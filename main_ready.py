import os
from zipfile import ZipFile

#PART 1 Loop through the directory and if there is a file with zip extension unarchive it in the same directory
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
          new_name = file_name+"_archive.zip"
          os.rename(zip_file, new_name)
          with ZipFile(new_name, 'r') as zObject:
            zObject.extractall(path = os.path.dirname(zip_file))
      file_path = os.path.dirname(zip_file)+"/all_html_and_css.txt"
      feedback_file = os.path.dirname(zip_file)+"/feedback.txt"
    try:
      if os.path.exists(file_path):
        os.remove(file_path)
      with open(file_path, 'x') as all_html_and_css:
        all_html_and_css.write("START\n")
    except FileExistsError:
      print(f"The file '{file_path}' already exists.")
    
    entryDirectory = os.scandir(entry)
    for projectDirectory in entryDirectory:
      if projectDirectory.is_file():
        split_tup = os.path.splitext(projectDirectory)
        file_name = split_tup[0]
        file_extension = split_tup[1]
        if(file_extension == ".html" or file_extension == ".css"):
          if projectDirectory.is_file():
            split_tup = os.path.splitext(projectDirectory)
            file_name = split_tup[0]
            file_extension = split_tup[1]
            if(file_extension == ".html" or file_extension == ".css"):
              #os.rename(file_name+file_extension, file_name+".txt")
              f = open(file_name+file_extension, "r")
              with open(file_path, 'a') as all_html_and_css:
                all_html_and_css.write("FILE: "+file_name.upper()+file_extension.upper()+"\n")
                for x in f:
                  all_html_and_css.write(x+"\n")
                  #print(x)
                f.close()
              all_html_and_css.close()
      if projectDirectory.is_dir() and not projectDirectory.path.endswith("__MACOSX"):
        #print("ND:"+projectDirectory.path)
        projectDirectoryObject = os.scandir(projectDirectory)
        for project_file in projectDirectoryObject:
          #print("ALL CONTENT FILE:"+file_path)
          if project_file.is_file():
            split_tup = os.path.splitext(project_file)
            file_name = split_tup[0]
            file_extension = split_tup[1]
            if(file_extension == ".html" or file_extension == ".css"):
              #os.rename(file_name+file_extension, file_name+".txt")
              f = open(file_name+file_extension, "r")
              with open(file_path, 'a') as all_html_and_css:
                all_html_and_css.write("FILE: "+file_name.upper()+file_extension.upper()+"\n")
                for x in f:
                  all_html_and_css.write(x+"\n")
                  #print(x)
                f.close()
              all_html_and_css.close()
          if(project_file.is_dir()):
            project_file_directory_object = os.scandir(project_file)
            for project_file_in_directory in project_file_directory_object:
              #print("ALL CONTENT FILE:"+file_path)
              if(project_file_in_directory.is_file()):
                split_tup = os.path.splitext(project_file_in_directory)
                file_name = split_tup[0]
                file_extension = split_tup[1]
                if(file_extension == ".html" or file_extension == ".css"):
                  #os.rename(file_name+file_extension, file_name+".txt")
                  f = open(file_name+file_extension, "r")
                  with open(file_path, 'a') as all_html_and_css:
                    all_html_and_css.write("FILE: "+file_name.upper()+file_extension.upper()+"\n")
                    for x in f:
                      all_html_and_css.write(x+"\n")
                      #print(x)
                    f.close()
                  all_html_and_css.close()

    print(file_path.upper())
    items_needed = ('<h1', '<h2', '<h3', '<h4', '<h5', '<h6', '<a',
                    '<img', '<!--', '<b', '<strong', '<i', '&lt',
                    '&gt', '&amp', '&nbsp', '&copy', '&quot', '<ul',
                    '<ol', '<li', '<br', '<hr', '<div', '<p', '<span',
                    'font-family', 'font-size', 'color', 'margin', 'padding',
                    'background-color', 'border', 'width', 'height', 'class=')
    items_lack = ""
    #contentFile = os.path.dirname(zip_file)+"/all_html_and_css.txt"    
    line_counter = 0
    for y in items_needed:
      #print(y+ " is being searched\n")
      f = open(file_path, "r")
      found = -1
      for x in f:
        if x.find(y) >= 0:
          found = found + 1
      f.close
      if found < 0:
        #print(y+" NOT FOUND")
        items_lack = items_lack + y + ", "
      #else:
        #print(y+" FOUND")
      number_of_items_lack = len(items_lack.split(", ")) - 1
    if number_of_items_lack > 30:
      print("MORE THAN 30 ITEMS ARE MISSING")
    try:
      if os.path.exists(feedback_file):
        os.remove(feedback_file)
      with open(feedback_file, 'x') as feedback:          
        feedback.write("FEEDBACK START:\n")
        if len(items_lack) > 2:
          feedback.write("There are no following HTML elements:\n")          
        else:
          feedback.write("All HTML elements: are present\n")
        feedback.write(items_lack)
        feedback.write("\nThere are "+str(number_of_items_lack)+" html and/or css items are missing\n")        
    except FileExistsError:
      print(f"The file '{feedback_file}' already exists.")