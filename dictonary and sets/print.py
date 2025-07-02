subjects = {
    "name": "Artificial Intelligence",
    "level": "4th sem",
    "batch": 2080,
    "code": "CSC200",
    "is_fun": True,
    "students_marks": 
    {
        "Ram": 99,
        "shyam":44
    }
}

print(subjects)
print(type(subjects))
print(subjects["name"])
print(subjects["students_marks"])
print(subjects["students_marks"]["Ram"])
print(list(subjects.keys()))
print(list(subjects.values()))
print(subjects.items())