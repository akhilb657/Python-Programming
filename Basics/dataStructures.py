students = {"Akhil": ["Python", "JavaScript", "Angular"],
            "Ranga": ["Java", "Spring"],
            "Reddy": ["Django", "DRF"]}

keys = students.keys()

for eachKey in keys:
    print("Courses taken by ",eachKey, "are: ")
    for eachCourse in students[eachKey]:
        print(eachCourse)
