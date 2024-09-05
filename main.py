import os
from zipfile import ZipFile
def unArchiveProjects(path):
  directoryObject = os.scandir(path)
  for entry in directoryObject:
    if entry.is_dir():
      entryDirectory = os.scandir(entry)
      for zip_file in entryDirectory:
        if zip_file.is_file():
          # extract the file name and extension
          split_tup = os.path.splitext(zip_file)
          file_name = split_tup[0]
          file_extension = split_tup[1]
          if file_extension == ".zip":
            #print(file_name+file_extension)
            new_name = file_name+"_archive.zip"
            os.rename(zip_file, new_name)
            with ZipFile(new_name, 'r') as zObject:
              zObject.extractall(path = os.path.dirname(zip_file))
          else:
            print(zip_file.path)              

def createContentAndFeedbackFiles(pathToFiles):  
  #create content file to contain all html and css of the site
  content_file = pathToFiles+"/all_html_and_css.txt"
  try:
    if os.path.exists(content_file):
      os.remove(content_file)
    with open(content_file, 'x') as all_html_and_css:
      all_html_and_css.write("START CONTENT\n")
  except FileExistsError:
    print(f"The file '{content_file}' already exists.")
    
  #create feedback file
  feedback_file = pathToFiles+"/feedback.txt"
  try:
    if os.path.exists(feedback_file):
      os.remove(feedback_file)
    with open(feedback_file, 'x') as feedback:
      feedback.write("START FEEDBACK\n")
  except FileExistsError:
    print(f"The file '{feedback_file}' already exists.")
  return [content_file, feedback_file]
    
def ConcatenateHTMLandCSS(input_file, content_file):
  split_tup = os.path.splitext(input_file)
  file_name = split_tup[0]
  file_extension = split_tup[1]
  if(file_extension == ".html" or file_extension == ".css"):
    f = open(input_file, "r")
    with open(content_file, 'a') as content_file:
      content_file.write("FILE: "+file_name.upper()+file_extension.upper()+"\n")
      for x in f:
        content_file.write(x+"\n")
      f.close()
    content_file.close()

def checkContent(content_file, feedback_file):  
  items_needed = ('<h1', '<h2', '<h3', '<h4', '<h5', '<h6', '<a',
                    '<img', '<!--', '<b', '<strong', '<i', '&lt',
                    '&gt', '&amp', '&nbsp', '&copy', '&quot', '<ul',
                    '<ol', '<li', '<br', '<hr', '<div', '<p', '<span',
                    'font-family', 'font-size', 'color', 'margin',
                    'padding', 'background-color', 'border', 'width',
                    'height', 'class=', '.css', '[')
  items_lack = ""   
  line_counter = 0
  for y in items_needed:    
    f = open(content_file, "r")
    found = -1
    for x in f:
      if x.find(y) >= 0:
        found = found + 1
    f.close
    if found < 0:      
      items_lack = items_lack + y + ", "
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
  
if __name__ == "__main__":
  #print("Please enter the path to directory:")
  #path = input()
  path = "/Users/talgatmanglayev/Desktop/CSCI-111/hw-1_test"
  unArchiveProjects(path)  
  pathObject = os.scandir(path)
  for directory in pathObject:
    if directory.is_dir():      
      [content_file, feedback_file] = createContentAndFeedbackFiles(directory.path)
      studentDirectory = os.scandir(directory)
      for site in studentDirectory:
        if site.is_file():
          ConcatenateHTMLandCSS(site, content_file)
        if site.is_dir() and not site.path.endswith("__MACOSX"):
          siteDirectory = os.scandir(site)
          for siteObject in siteDirectory:
            if siteObject.is_file():
              ConcatenateHTMLandCSS(siteObject, content_file)
            if siteObject.is_dir():
              siteFiles = os.scandir(siteObject)
              for siteFile in siteFiles:
                ConcatenateHTMLandCSS(siteFile, content_file)
      checkContent(content_file, feedback_file)