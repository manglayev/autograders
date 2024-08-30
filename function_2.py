#create all_html_and_css.txt and feedback.txt files in each student directories
import os
path = "/Users/talgatmanglayev/Desktop/CSCI-111/hw-1_test"
directoryObject = os.scandir(path)
file_path = ""
feedback_file = ""
#print("Files and Directories in '% s':" % path)
for studentDirectory in directoryObject:
  if studentDirectory.is_dir():
    file_path = os.path.dirname(studentDirectory)+"/all_html_and_css.txt"
    feedback_file = os.path.dirname(studentDirectory)+"/feedback.txt"
    try:
      if os.path.exists(file_path):
        os.remove(file_path)
      with open(file_path, 'x') as all_html_and_css:
        all_html_and_css.write("START\n")
    except FileExistsError:
      print(f"The file '{file_path}' already exists.")