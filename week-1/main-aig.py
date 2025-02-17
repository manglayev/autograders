import os
from zipfile import ZipFile
import pandas as pd

def unArchiveProjects(path):
  directoryObject = os.scandir(path) #we can iterate this dir

  for entry in directoryObject:
    if entry.is_dir():#if dir
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
              zObject.extractall(path = os.path.dirname(zip_file)) #extracts all dirs
          else:
            print(zip_file.path)    #print the path of the non-archived dirs          


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
  # print("TESTING3: " + input_file.path)
  split_tup = os.path.splitext(input_file)
  file_name = split_tup[0]
  file_extension = split_tup[1]
  if(file_extension == ".html" or file_extension == ".css"):
    f = open(input_file, "r")
    # print("TESTING4: " + f)
    with open(content_file, 'a') as content_file:
      #in the file put first the "FILE: " + path of that file
      content_file.write("FILE: "+file_name.upper()+file_extension.upper()+"\n")
      for x in f: #each line in this file.
        # print("TESTING 5: "+x )
        content_file.write(x+"\n")#eaach line inserted to the all_html_and_css.txt
      f.close()
    content_file.close()

def checkContent(content_file, feedback_file):  
  items_needed = ('<h1', '<h2', '<h3', '<h4', '<h5', '<h6', '<a','_blank',
                    '_self','<img', 'alt=','<!--', '<b', '<strong', '<i', '&lt',
                    '&gt', '&amp', '&nbsp', '&copy', '&quot', '<ul',
                    '<ol', '<li', '<br', '<hr', '<div', '<p', '<span', '<video', 
                    '<title','<iframe', '<table',
                    'font-family', 'font-size', 'color', 'margin',
                    'padding', 'background-color', 'border', 'width',
                    'height', 'class=', 'id=', 'style=', '<style', '.css', '[')
  items_lack = ""   
  line_counter = 0
  for item in items_needed:    
    f = open(content_file, "r")
    found = -1
    for x in f:
      if x.find(item) >= 0:
        found = found + 1
    f.close
    if found < 0:      
      items_lack = '' + items_lack + item + ', '
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
      feedback.write("OVERALL PERFORMANCE:\n")
      feedback.write("TOTAL:\n")
  except FileExistsError:
    print(f"The file '{feedback_file}' already exists.")

def process_directory(directory, content_file):
    """Recursively processes all files in the given directory."""
    for entry in os.scandir(directory):
        if entry.is_file():
            ConcatenateHTMLandCSS(entry, content_file)
        elif entry.is_dir() and not entry.path.endswith("__MACOSX"):
            process_directory(entry.path, content_file)  # Recursive call

def split_by_space(text: str):
    """Splits a string into two parts at the first space."""
    parts = text.split(" ", 1)
    return parts if len(parts) == 2 else (parts[0], "")


def process_student_folder_name(directory):
    """Extracts first and second name from the directory name."""
    last_directory = os.path.basename(directory.path)
    full_student_name = last_directory.split("_")[0]  # Extract name before _
    
    first_name, second_name = split_by_space(full_student_name)
    
    return first_name, second_name

def find_xlsx_file(directory):
    """Finds the first .xlsx file in the directory."""
    for entry in os.scandir(directory):
        if entry.is_file() and entry.path.endswith(".xlsx"):
            return entry.path  # Return the path of the first .xlsx file found
    return None  # No .xlsx file found

def get_student_id_from_xlsx(file_path, first_name, second_name):
    """Searches for the student’s ID in the Excel file."""
    df = pd.read_excel(file_path)  # Read the xlsx file
    for _, row in df.iterrows():
        # Check if both first and second names match in any row
        if str(row.get("First Name", "")).strip() == first_name and str(row.get("Last Name", "")).strip() == second_name:
            return row.get("ID", None)  # Return the student ID if found
    return None  # Return None if ID is not found

if __name__ == "__main__":
  #print("Please enter the path to directory:")
  #path = input()
  path = "/Users/aigera/Downloads/CSCI111-L1"
  # unArchiveProjects(path)  #unarchives the submissions inside of each students' folders
  
  pathObject = os.scandir(path)
  print("PATHHHH: " +path)
  xlsx_file = find_xlsx_file(path)
  print("XLSX: " + xlsx_file)

  for directory in pathObject:
    # print("INSIDE: " + os.path.basename(directory.path))
    first, second = process_student_folder_name(directory)
    print("FIRST: " + first)
    print("SECOND: " + second)
    id = get_student_id_from_xlsx(xlsx_file, first, second)
    print("ID: "+id)
    if directory.is_dir():#each iterator - is one student
      #generates two empty txt files for the content and feedback
      [content_file, feedback_file] = createContentAndFeedbackFiles(directory.path) #going through every submition
      
      #fills the all_html_and_css.txt file
      process_directory(directory.path, content_file)
      
      #fills feedback.txt file
      checkContent(content_file, feedback_file)

