employees = [ 
    {"eid": 1, "ename": "Shah Rukh Khan", "gender": "Male", "age": 59}, 
    {"eid": 2, "ename": "Deepika Padukone", "gender": "Female", "age": 38}, 
    {"eid": 3, "ename": "Amitabh Bachchan", "gender": "Male", "age": 82}, 
    {"eid": 4, "ename": "Priyanka Chopra", "gender": "Female", "age": 42}, 
    {"eid": 5, "ename": "Aamir Khan", "gender": "Male", "age": 59}, 
    {"eid": 6, "ename": "Kareena Kapoor", "gender": "Female", "age": 44}, 
    {"eid": 7, "ename": "Salman Khan", "gender": "Male", "age": 59}, 
    {"eid": 8, "ename": "Katrina Kaif", "gender": "Female", "age": 41}, 
    {"eid": 9, "ename": "Hrithik Roshan", "gender": "Male", "age": 50}, 
    {"eid": 10, "ename": "Alia Bhatt", "gender": "Female", "age": 31}, 
    {"eid": 11, "ename": "Akshay Kumar", "gender": "Male", "age": 57}, 
    {"eid": 12, "ename": "Kangana Ranaut", "gender": "Female", "age": 37}, 
    {"eid": 13, "ename": "Ranbir Kapoor", "gender": "Male", "age": 42}, 
    {"eid": 14, "ename": "Vidya Balan", "gender": "Female", "age": 46}, 
    {"eid": 15, "ename": "Ranveer Singh", "gender": "Male", "age": 39}, 
    {"eid": 16, "ename": "Anushka Sharma", "gender": "Female", "age": 36}, 
    {"eid": 17, "ename": "Rajinikanth", "gender": "Male", "age": 74}, 
    {"eid": 18, "ename": "Aishwarya Rai", "gender": "Female", "age": 51}, 
    {"eid": 19, "ename": "Vijay", "gender": "Male", "age": 50}, 
    {"eid": 20, "ename": "Madhuri Dixit", "gender": "Female", "age": 57}
]
"""
   Basic if & for (Beginner)


# print all employee names using a for loop:
for emp in employees:
    print(emp["ename"])

# print employee names whose age is  greater than 50
    for emp in employees: 
        if emp["age"] > 50:
            print(emp["ename"])


# count total number of male employees
     
count = 0
for emp in employees:
    if emp["gender"] == "Male":
        count += 1

print("Total Male Employees:", count)


# count total number of female employees

count = 0
for emp in employees:
    if emp ["gender"] == "female":
        female_count += 1

print("total female employees:",count)

# print employees whose age is exactly 59
for emp in employees:
    if emp["age"] == 59:
        print(emp["ename"])

# print employee names whose age is less than 40        
for emp in employees:
    if emp["age"] < 40:
        print(emp["ename"])


# print employee names whose age is between 30 and 50
for emp in employees:
    if emp["age"] >= 30 and emp["age"] <= 50:
        print(emp["ename"])


# print employee name and age if the employee is female 
for emp in employees:
    if emp["gender"] == "female":
        print(emp["ename"],emp["age"])


# print employee name and age if the employee is male 
for emp in employees:
    if emp["gender"] == "Male":
        print(emp["ename"], emp["age"])


# print emplyees whose name starts with the letter "A"
for emp in employees:
    if emp ["ename"].startswith("A"):
        print(emp["ename"])

      If-else & elif
      
#print "senior employee" or "regular employee"
for emp in employees:
    if emp ["age"] >= 60:
        print(emp["ename"],"-seninor employee")
    else:
        print(emp["ename"],"-regular employee")

# print age category: young /middle-aged /senior
for emp in employees:
    if emp ["age"] < 40:
        print(emp ["ename"],"-young")
    elif emp["age"] >=40 and emp["age"] <= 59:
        print(emp["ename"],"- middle-aged")
    else:
        print(emp["ename"],"-senior")        

#print employees eligible for retirement (age_>60)
for emp in employees:
    if emp ["age"] >= 60:
        print(emp["ename"])
 
# print emploeename if age is above 80
for emp in employees:
    if emp["age"] > 80:
        print(emp["ename"])

# print employee name with label actor/actress
for emp in employees:
    if emp ["gender"] =="male":
        print(emp["ename"],"-actor")
    else:
        print(emp["ename"], "-actress")    

# print employees whose age is an even number
for emp in employees:
    if emp["age"] % 2 == 0:
        print(emp["ename"], emp["age"])


# print employees whose age is an odd number
for emp in employees:
    if emp["age"] % 2 != 0:
        print(emp["ename"], emp["age"])

#print employees with eid divisible by 5
for emp in employees:
    if emp["eid"] % 5 == 0:
        print(emp["ename"], emp["eid"])
      

# print employees whose name length is greater than 12 characters
for emp in employees:
    if len(emp["ename"]) > 12:
        print(emp["ename"])

#print employees whose age ends with digit 7 or 9
for emp in employees:
    if emp["age"] % 10 == 7 or emp["age"] % 10 == 9:
        print(emp["ename"], emp["age"])
"""