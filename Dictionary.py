student={
  "name": "Aditya",
  "age": 14,
  "subject": ["Maths", "English", "PE", "Geography"], 
  "addr": {"school":"abc",
    "home":"xyz"
  },
  "abc": 5
}

del student["abc"]
print(student["name"])
print(student)
for i in student:
  print(i,student[i])
  
for i in student.values():
  print(i)

student["name"]="Aditya Sengupta"
print(student)
if "age" in student:
  print(student["age"])


print(student["name"])

if "Aditya Sengupta" in student.values():
  print("Yes")

if "abc" in student["addr"].values():
  print("Yes")

studentData={}

for i in range(2):
  name=input("What is your full name?")
  age=input("How old are you?")
  grade=input("What is your grade?")
  studentData[name]={"age":age, "name":name, "grade":grade}
print(studentData)

for i in studentData:
  print(i,studentData[i])