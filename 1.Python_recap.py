# Variable 
Name = "Blink"
Age = 19
height = 4.7
is_student = True 






# Lists 
Numbers = [1,2,3,4,5]
Numbers.append(8);
Numbers.remove(3);
print(Numbers);
Squares = [x*x for x in range(1,10,2)]
print(Squares)






# Dictionaries 
Student = {
    "name": "Blink",
    "age": 20,
    "skills": ["python", "js"]    
}
print(Student["name"])
Student["age"] = 21

for (key,value) in Student.items():
    print (key,value);






# Loops 
for i in range(1,10):
    print(i)

# Functions
def greet(name):
    return f"Hello {name}"

print(greet("Blink"))






# Conditionals 
age = 18
if age>=18 :
    print("Adult")
else:
    print("Kid")






# Classes 
class Person:
    def __init__(self,name):
        self.name = name
    def greet(self):
        return f"Hello {self.name}"

p = Person("Blink")
print(p.greet())






# File Handling 
with open("data.txt", "w") as file:
    file.write ("hello world\n") # overwrite

with open("data.txt", "a") as file:
    file.write("New line added\n") #new lines

with open("data.txt", "r") as file:
    content = file.read()
print (content)

with open("data.txt", "r") as file:
    lines = file.readlines()

print(lines) # read all lines into list






# JSON
import json 

data1 = {
    "name": "Blink",
    "age": 20,
    "skills": ["python", "ml"]
}

json_data = json.dumps(data1)

print(json_data)

data2 = {
    "name": "Blink",
    "age": 20
}

with open("user.json", "w") as file:
    json.dump(data2,file)


with open("user.json", "r") as file:
    data = json.load(file)

print(data)
print(data["name"])



json_string = '{"name": "Blink", "age": 20}'
data = json.loads(json_string)

# dump: write to file, dumps: convert to string 


try:
    x = 10 / 0
except ZeroDivisionError:
    print("cannot divide by zero")