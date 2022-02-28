#book mark the read more list stuff

# differences don't have to decarle var types, no semi colones, and no {}
x = 10
name = "lisa"
gorceries = ('bananas','pineapple','mango')
gorceries = gorceries + ("domestic",)
gorceries = gorceries[:3] + ("man's best friend",) + gorceries[4:]
    # can't be changed?
    # you're only manipulating the data not changing it. Most of these methods are 

# print(gorceries + ("domestic",))
# print(gorceries)

# print(f"hello {name}")
# print("Good mringin {}".format(name))

# for x in 'Hello':
#    print(x)

my_list = ["abc", 123, "xzy", "890"]
my_dic = {"map": "google", True: "Lisa", "address": "5115"}


# AFTERNNO LESSON

def addition(x = 0,y = 40):
    return x + y

# print(addition( y = 20))

# context = {
#     'questions': [
#         { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
#         { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
#         { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
#         { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
#     ]
# }

# def contextStuff(stuff):
#     for x in range(0,len(context["questions"])):
#         print(context["questions"][x][stuff])

# contextStuff('content')


context = {
    'questions':[
        {"id": 1, "content": "This is content"},
        {"id" : 2, "content": "this is  context"},
        {"id": 3, "content": "This is a python string"},
        {"id": 4, "content": "This is not the right I've no idea what do I write"},
    ]
}


for x in range(0,len(context["questions"])):
    print(context["questions"][x]["content"])

# for k in context["questions"]:
#     print(context["questions"])
