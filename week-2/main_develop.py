import os
from zipfile import ZipFile
import csv

# === PATHS (adjust as needed) ===
path = "week-2/CSCI111"
file_result = "week-2/CSCI111/results_hw2.csv"
file_participants = "week-2/CSCI111/participants.csv"

# === CSV HEADER ===
with open(file_result, mode='w') as csv_file:
    fieldnames = ["first_name", "last_name", "id", "grade-1", "grade-2", "grade", "feedback"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

# === REQUIREMENTS ===
# Grade 1 (6%)
grade1_items = {
    "bio_page": ("biography", 2.0),   # short biography/overview
    "hobby": ("hobby", 2.0),          # hobby (art/sport/volunteering etc.)
    "nav_menu": ("<nav", 1.0),        # navigation menu
    "flexbox": ("flex", 1.0),         # flexbox usage
}

# Grade 2 (6%)
grade2_items = {
    # I. Selectors
    "child_selector": (">", 0.4),
    "adjacent_selector": ("+", 0.4),
    "hover": (":hover", 0.2),
    "active": (":active", 0.2),
    "visited": (":visited", 0.2),
    "first_child": (":first-child", 0.1),
    "last_child": (":last-child", 0.1),
    "before": ("::before", 0.2),
    "after": ("::after", 0.2),

    # II. Position
    "margin": ("margin", 0.2),
    "padding": ("padding", 0.2),
    "border": ("border", 0.2),
    "overflow": ("overflow", 0.3),
    "box-sizing": ("box-sizing", 0.1),
    "display": ("display", 0.3),
    "float": ("float", 0.1),
    "clear": ("clear", 0.1),
    "static": ("static", 0.1),
    "relative": ("relative", 0.1),
    "absolute": ("absolute", 0.1),
    "fixed": ("fixed", 0.1),
    "sticky": ("sticky", 0.1),

    # III. Self-study
    "flexbox": ("flex", 2.0),
}

# === PROCESS SUBMISSIONS ===
directoryObject = os.scandir(path)

for entry in directoryObject:
    if not entry.is_dir():
        continue

    # Extract student names from folder name
    first_name = entry.name[0:entry.name.find(' ')]
    last_name = entry.name[entry.name.find(' ') + 1:entry.name.find('_')]
    student_info = {"first_name": first_name, "last_name": last_name, "id": ""}

    # Match ID from participants.csv
    with open(file_participants, newline='') as csvfile:
        path_participants = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in path_participants:
            if student_info["first_name"] in row[0] and student_info["last_name"] in row[0]:
                parts = row[0].split(',')
                if len(parts) >= 3:
                    student_info["id"] = parts[2]

    # === Unpack zip files ===
    entryDirectory = os.scandir(entry)
    for zip_file in entryDirectory:
        if zip_file.is_file():
            file_name, file_extension = os.path.splitext(zip_file)
            if file_extension == ".zip":
                new_name = file_name + "_archive.zip"
                os.rename(zip_file, new_name)
                with ZipFile(new_name, 'r') as zObject:
                    zObject.extractall(path=os.path.dirname(zip_file))

    # === Collect all .html and .css into one text file ===
    file_path = os.path.join(entry.path, "all_html_and_css.txt")
    if os.path.exists(file_path):
        os.remove(file_path)

    with open(file_path, 'w') as all_html_and_css:
        for root, dirs, files in os.walk(entry.path):
            for f in files:
                if f.endswith(".html") or f.endswith(".css"):
                    try:
                        with open(os.path.join(root, f), "r", errors="ignore") as source:
                            all_html_and_css.write(f"FILE: {f}\n")
                            all_html_and_css.write(source.read() + "\n")
                    except Exception:
                        pass

    # === Analyze features ===
    with open(file_path, "r") as f:
        content = f.read().lower()

    missing_g1 = []
    missing_g2 = []
    grade1_score = 0
    grade2_score = 0

    for key, (token, weight) in grade1_items.items():
        if token in content:
            grade1_score += weight
        else:
            missing_g1.append(key)

    for key, (token, weight) in grade2_items.items():
        if token in content:
            grade2_score += weight
        else:
            missing_g2.append(key)

    # raw total (out of 12)
    raw_total = grade1_score + grade2_score

    # normalize to max 6
    total_grade = raw_total / 12 * 6

    # === Feedback ===
    feedback_text = ""
    if missing_g1:
        feedback_text += f"Missing Grade-1 items: {', '.join(missing_g1)}\n"
    if missing_g2:
        feedback_text += f"Missing Grade-2 items: {', '.join(missing_g2)}\n"
    if not missing_g1 and not missing_g2:
        feedback_text = "All requirements satisfied.\n"

    # === Save results ===
    with open(file_result, mode='a') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["first_name", "last_name", "id", "grade-1", "grade-2", "grade", "feedback"])
        writer.writerow({
            "first_name": student_info["first_name"],
            "last_name": student_info["last_name"],
            "id": student_info["id"],
            "grade-1": grade1_score,
            "grade-2": grade2_score,
            "grade": total_grade,
            "feedback": feedback_text
        })

print("✅ Grading completed. Results saved to", file_result)