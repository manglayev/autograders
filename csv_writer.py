import csv
file_result = "/home/talgat/Desktop/111/111-results.csv"
with open(file_result, mode='w') as csv_file:
    fieldnames = ["first_name", "last_name", "id", "grade-1", "grade-2", "grade", "feedback"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({"first_name": 'John', "last_name": 'Smith', "id": '123456', "grade-1":'5', "grade-2":'4', "grade":'4.5', "feedback":'Nice'})
    writer.writerow({"first_name": 'Another', "last_name": 'Last Name', "id": '456789', "grade-1":'4', "grade-2":'3', "grade":'3.5', "feedback":'Good'})    