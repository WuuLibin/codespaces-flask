import json

# Step 2: Read the JSON File
with open('students.json', 'r') as file:
    data = json.load(file)

# Step 3: Access the Data
students = data['students']

# Step 4: Process the Data
for student in students:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Math Grade: {student['grades']['math']}")
    print(f"Science Grade: {student['grades']['science']}")
    print()