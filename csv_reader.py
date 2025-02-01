"""
Prepare CSV file with following columns:
First Name, Last Name, ID, Grade-1, Grade-2, Feedback
Parse first name and last name from directory name,
Parse first name and last name from csv file downloaded from moodle
if there is match, then append first name, last name and id (taken from csv),
grade 1, grade 2 as 0 and Feedback into a new CSV file
"""
import csv
file_participants = "/home/talgat/Desktop/111/111-participants.csv"
with open(file_participants, newline='') as csvfile:
    path_participants = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in path_participants:
        print(', '.join(row))