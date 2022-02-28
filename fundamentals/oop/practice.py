# ********************** ASSIGNMENT: FOR LOOPS: BASIC I *******************************************************

# 1
# for x in range(150):
#     print(x)

# 2
# for x in range(5,1000,5):
#     print(x)

# 3 
# for x in range(1,100):
#     if(x % 5 == 0):
#         print("Coding")
#     if(x % 10 == 0):
#         print("Coding Dojo")
#     else:
#         print(x)

# 4
# sum = 0
# for x in range(0,500000):
#     if(x % 2 != 0):
#         sum += x
# print(sum)

# 5
# for x in range(2018,0,-4):
#     print(x)

# 6
# lowNum = 30
# highNum = 404
# mult = 23
# for x in range(lowNum,highNum):
#     if(x % mult == 0):  
#         print(x)



# **************************** Assignment: Functions Basic II *******************************************************

# 1 
x = [ [5,2,3], [10,8,9] ]
x[1][0] = 15
# print(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]["last_name"] = "Bryant"
# print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory["soccer"][0] = "Andres"
# print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0]["y"]=30
# print(z)


# 2
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


# def iterateDictionary(students):
    # for x in range(0,len(students)):

    #     print(f"{students[x]['first_name']}  {students[x]['last_name']}")

    
        
#     for x in range(0,len(students)):
#         string = ""
#         for z in students[0]:
#             if z == "first_name":
#                 string += f"{z} - {students[x][z]}, "
#             else:
#                 string += f"{z} - {students[x][z]} "
#         print(string)
# iterateDictionary(students)


# 3 Get Values From a List of Dictionaries
# for y in range(0,len(students)):
#     for x in students[y]:
#         if(x == "first_name"):
#             print(students[y][x])

# for y in range(0,len(students)):
#     for x in students[y]:
#         if(x == "last_name"):
#             print(students[y][x])

# 4 
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

for x in dojo:
    print(f"{len(x)} {x.upper()}")
    for y in range(0,len(dojo[x])):
        print(dojo[x][y])
    print("\n")