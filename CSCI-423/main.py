'''
This program:
 - starts a new file
 - enters the directory
    - reads a file in the directory
    - copies text from a file
    - writes to a new file what is in the buffer
    - loops through all files in the directory
'''
import os
import csv

def split_by_space(text: str):
    """Splits a string into two parts at the first space."""
    parts = text.split(" ", 1)
    return parts if len(parts) == 2 else (parts[0], "")

def get_first_and_last_names(directory):
    """Extracts first and last names from the directory name."""
    last_directory = os.path.basename(directory)
    full_student_name = last_directory.split("_")[0]  # Extract name before _
    first_name, last_name = split_by_space(full_student_name)    
    return first_name, last_name

def get_student_id(file_path, first_name, last_name):
    student_info = {"first_name": first_name, "last_name": last_name, "student_id": ""}
    with open(file_path, newline='') as csvfile:
        #print("INSIDE 1: " + file_path)
        path_participants = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in path_participants:
            #print("INSIDE 2: " + row[0])
            if student_info["first_name"] in row[0] and student_info["last_name"] in row[0]:
                parts = row[0].split(',')
                if len(parts) >= 3:
                    student_info["student_id"] = parts[2]
    return student_info["student_id"]

if __name__ == "__main__":

    path_to_directory = "/home/talgat/Desktop/423/Lab_2.2"
    participants_file = "/home/talgat/Desktop/423/participants.csv"
    file_result = "/home/talgat/Desktop/423/results_lab_2.2.csv"
    # === CSV HEADER ===
    with open(file_result, mode='w') as csv_file:
        fieldnames=["first_name", "last_name", "student_id", "link", "grade"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

    for directory in os.scandir(path_to_directory):
        #print("INSIDE: " + directory.path)
        first, last = get_first_and_last_names(directory.path)
        student_id = str(get_student_id(participants_file, first, last))
        #print("FIRST: " + first +"; LAST: " + last + "; Student_id: " + student_id)
        for entry in os.scandir(directory.path):
            #print("ENTRY: " + entry.path)
            if entry.is_file():
                try:
                    with open(entry, "r") as src:
                        content = src.read().strip()+"#"
                        print("CONTENT: " + content)
                        grade = 2
                        if len(content) < 10:
                            content = "No link provided"
                            grade = 0
                except Exception as e:
                    print(f"Error processing file {entry}: {e}")

        # === Save results ===
        with open(file_result, mode='a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["first_name", "last_name", "student_id", "link", "grade"])
            writer.writerow({
                "first_name": first,
                "last_name": last,
                "student_id": student_id,
                "link": content,
                "grade": grade
            })