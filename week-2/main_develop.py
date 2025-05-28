"""
This program requires:
 - Download homework-1 of all students from Moodle as a zip archive
 - Paste here the path of the zip file
 - Download all participants of the course as csv file
"""
import os
from zipfile import ZipFile

#PART 1 Loop through the directory and if there is a file with zip extension unarchive it in the same directory
#MacOS path
#path = "/Users/talgatmanglayev/Desktop/CSCI-111
#Ubuntu path
path = "C:/Users/user/Downloads/homework2"
directoryObject = os.scandir(path)
file_path = ""
feedback_file = ""
#students = []
student_info = {}
grade_1 = 5
import csv
file_result = "C:/Users/user/Downloads/results_hw2.csv"
with open(file_result, mode='w') as csv_file:
    fieldnames = ["first_name", "last_name", "id", "grade-2", "grade-1", "grade", "feedback"] # grade-2 autograder+ TODO things, grade-1 is Grade-1 in homework-2 pdf file (range 0-5)
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    #writer.writerow({"first_name": 'John', "last_name": 'Smith', "id": '123456', "grade-1":'5', "grade-2":'4', "grade":'4.5', "feedback":'Nice'})
#print("Files and Directories are in '% s':" % path)
for entry in directoryObject:
  if entry.is_dir():
    first_name = entry.name[0:entry.name.find(' ')]
    last_name = entry.name[entry.name.find(' ')+1:entry.name.find('_')]
    student_info = {"first_name":first_name, "last_name":last_name, "id":"", "grade_1":"", "feedback_text":""}
    #students.append(student_info)
    #print("FN:"+first_name)
    #print("LN:"+last_name)
    #print(student_info)
    """
    Prepare CSV file with following columns:
    First Name, Last Name, ID, Grade-1, Grade-2, Feedback
    Parse first name and last name from directory name,
    Parse first name and last name from csv file downloaded from moodle
    if there is match, then append first name, last name and id (taken from csv),
    grade 1, grade 2 as 0 and Feedback into a new CSV file
    """
    import csv
    file_participants = "C:/Users/user/Downloads/courseid_15122_participants(1).csv"
    with open(file_participants, newline='') as csvfile:
      path_participants = csv.reader(csvfile, delimiter=' ', quotechar='|')
      for row in path_participants:
        ', '.join(row)
        #for student in students:
        if student_info["first_name"] in row[0] and student_info["last_name"] in row[0]:
            student_info["id"] = row[0].split(',')[2]
            #print("2 FN:"+student["first_name"]+"; LN:"+student["last_name"]+"; id:"+student["id"]+";")
    #Continue entering the directory
    entryDirectory = os.scandir(entry)
    for zip_file in entryDirectory:
      if zip_file.is_file():
        split_tup = os.path.splitext(zip_file)
        # extract the file name and extension
        file_name = split_tup[0]
        file_extension = split_tup[1]
        if file_extension == ".zip":
          print(file_name+file_extension)
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

    #print(file_path.upper())
    items_needed = (':hover', ':active', ':visited', ':first-child', ':last-child', '::before', '::after','border',
                  'overflow', 'box-sizing','block', 'inline', 'inline-block',
                  'margin', 'padding', 'auto', 'scroll', 'hidden', 'with',
                  'without', 'float', 'clear:', 'static', 'relative', 'absolute', 'fixed', 'sticky')
    flex_items_needed = ('flex-container', 'flex-direction')
    # 'flex-container', 'flex-direction' each 0.35 TODO: DONE
    # manually check for nav bar (or menu) (0.6%) TODO
    # check manually Combine selectors to style elements more precisely (0.4%) TODO
    # check manually for hild selectors to style immediate children of a parent element (0.4%) ( div > li ) TODO
    # Manually: Adjacent sibling selectors to style elements that come immediately after another element (0.4%) (div + li) TODO
    # Alua Akhmolda TODO: DONE
    # Ayazhan Zhora
    # Daniya Mukusheva
    # Mukhsin Assetov           - they've used non-english characters, so I'll check 'em manually
    items_lack = ""
    flex_items_lack = ""
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
    #if number_of_items_lack > 30:
    #  print("MORE THAN 30 ITEMS ARE MISSING")

    for y in flex_items_needed:
      f = open(file_path, "r")
      found = -1
      for x in f:
        if x.find(y) >= 0:
          found = found + 1
      f.close()
      if found < 0:
        flex_items_lack = flex_items_lack + y + ", "

    number_of_flex_items_lack = len(flex_items_lack.split(", ")) - 1

    feedback_text = ""
    # print(items_lack)
    """
    try:
      if os.path.exists(feedback_file):
        os.remove(feedback_file)
      with open(feedback_file, 'x') as feedback:          
        feedback.write("FEEDBACK START:\n")
        if len(items_lack) > 2:
          feedback.write("Grade 1./nMissing HTML and/or CSS elements: ")
          feedback.write(items_lack)
          feedback_text = feedback_text + "Grade 1./nMissing HTML and/or CSS elements: "
          feedback_text = feedback_text + items_lack
          #print(items_lack)
        else:
          feedback.write("All HTML and CSS elements: are present\n")
          feedback_text = feedback_text + "All HTML and CSS elements: are present\n"
        #feedback.write(items_lack)
        #print(feedback_text)
        feedback.write(". Number of missing HTML and/or CSS items: "+str(number_of_items_lack))
        #feedback.write(items_lack)
        #feedback_text = feedback_text + items_lack + "\n"
        feedback_text = feedback_text + ". Number of missing HTML and/or CSS items: "+str(number_of_items_lack)
        #print(feedback_text)
        feedback_text = feedback_text + "/n; Grade 2: "
        grade_1 = 3.2 - number_of_items_lack*0.1
    except FileExistsError:
      print(f"The file '{feedback_file}' already exists.")
    """
    if len(items_lack) > 2:
      feedback_text = feedback_text + "Grade 2.\nMissing HTML and/or CSS elements: "
      feedback_text = feedback_text + items_lack
      feedback_text = feedback_text + ". Number of missing HTML and/or CSS items: "+str(number_of_items_lack)
      #print(items_lack)
    if len(flex_items_lack) > 2:
      feedback_text += "\nMissing Flexbox elements: " + flex_items_lack
      feedback_text += ". Number of missing Flexbox items: " + str(number_of_flex_items_lack)
    if len(items_lack) <= 2 and len(flex_items_lack) <= 2:
      feedback_text += "All HTML and CSS elements are present.\n"

    feedback_text = feedback_text + "\nGrade 1: "
    grade_1 = 3.2 - number_of_items_lack * 0.1 - (number_of_flex_items_lack * 0.35)

    file_result = "C:/Users/user/Downloads/results_hw2.csv"
    with open(file_result, mode='a') as csv_file:
      fieldnames = ["first_name", "last_name", "id", "grade-1", "grade-2", "grade", "feedback"]
      writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
      #writer.writeheader()
      writer.writerow({"first_name": student_info["first_name"], "last_name": student_info["last_name"], "id": student_info["id"], "grade-1":grade_1, "grade-2":0, "grade":0, "feedback":feedback_text})