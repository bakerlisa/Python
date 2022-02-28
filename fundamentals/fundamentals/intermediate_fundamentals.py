# 1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
# HERE
x[1][0] = 15

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
# HERE
students[0]["last_name"] = "Bryant"

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
# HERE
sports_directory["soccer"][0] = "Andres"

z = [ {'x': 10, 'y': 20} ]
# HERE
z[0]['y'] = 30


# 2. Iterate Through a List of Dictionaries
activities = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"}
]
def iterateDictionary(activities):
    for m in range(0,len(activities)):
        items = list(activities[m])
        message = ""
        counter = 0
        for n in items:
            if(len(items) - 1 == counter):
                message += f"{n} - {activities[m][n]} "
            else:
                message += f"{n} - {activities[m][n]}, "
                counter+=1
        print(message)

iterateDictionary(activities)


# 3. Get Values From a List of Dictionaries

students = [
    {"name": "Michael", "last_name": "Jordan"},
    {"name": "John", "last_name": "Rosales"},
    {"name": "Mark", "last_name": "Guillen"},
    {"name": "KB", "last_name": "Tonel"}
]

def iterateDictionary2(key,values):
    for x in range(len(values)):
        print(values[x][key])

iterateDictionary2("name",students)
iterateDictionary2("last_name",students)


# 4. Iterate Through a Dictionary with List Values

travel = {
    "Cities": ["Rome","London","Istanbul","Venice","Vienna","Barcelona","Egypt"],
    "Countries": ["Australia", "New Zealand", "Iceland", "Antarctica"]
}

def traveling(travel):
    counter = 0
    for v in travel:
        print(f"\n{len(travel[v])} {v.upper()}")
        for u in travel[v]:
            print(u)
    counter += 1

traveling(travel)