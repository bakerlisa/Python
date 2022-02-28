num1 = 42# varaialbe and number initilization: Data Types -> Primitive -> number 
num2 = 2.3 # varaialbe and double initilization: Data Types -> float
boolean = True # boolean set to true: Data Types 
string = 'Hello World' # variable set to a string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # list varaialbe with initialized values (looks like a JS array)
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable set to Dictionaries with initialized values  (looks like a JS object)
fruit = ('blueberry', 'strawberry', 'banana') #varaialbe set to a Tuple with initialized values 
print(type(fruit)) # printing to the console/termianl var fruit's type which would be a tuple
print(pizza_toppings[1]) # going to access the value in the 1 index in the   dictonaries named pizza_toppings.  answer =Sausage
pizza_toppings.append('Mushrooms') # going to add the value  Mushrooms to the end of pizza_toppings dictonaries
print(person['name']) # going to consolelog/print to the terminal the Name John from the list person.
person['name'] = 'George' # change the value of name (John) in the Dictionaries to George
person['eye_color'] = 'blue' # going to add the value eye_color set to 'bule to the person Dictionaries
print(fruit[2]) # Going to access the list varable named fruit and print the 2 indexed (or 3 value) value. Answer = banana

if num1 > 45: #if statment and condtional. If var num1 is greater than 45
    print("It's greater") # what to print is the conditional is true
else: #else statmet to do if the if statment is false 
    print("It's lower") #printe to the screen "It's lower"

if len(string) < 5: # if statement set checking the length of the varialbe strong and if its less than five
    print("It's a short word!") #It will print this line printing to the screen It's a short word!
elif len(string) > 15: #this is an else if statement. So if the if statment is false it will next go to thie statement. It is also checing the length of the variable string and if its greater than 15
    print("It's a long word!") #It prints to the screen It's a long word
else: #else, if non of the if statements vaildate to true this is the default action. 
    print("Just right!") #which prints the word Just right!

for x in range(5): #For loop, using the range function from 0..5
    print(x) # then printing those values 0..5 to the screen
for x in range(2,5): #for loop using the range function to loop through the numbers 2-5. 2 is the start and 5 is the stop int
    print(x) #printing the numbers 2-5 to the screen
for x in range(2,10,3): #For loop using a range function with a start int at 2 and stop int at 10 and increment by 3 each loop (so the loop will ++3 each loop)
    print(x) # var x to the screen each loop: answer 2,5,8
x = 0 # varaiable declartion set to the int 0
while(x < 5): #while lopp checking to see if x li less than 5
    print(x) #If the above is true, then print to the screen value x: answer 0,1,2,3,4
    x += 1 #this increments the value of x by 1 each iteration of the while loop

pizza_toppings.pop() # removes the last item from the list and returns the value
pizza_toppings.pop(1) # removes the index 1 from the pizza toppings list and returns the value. answer ['Pepperoni', 'Jalepenos', 'Cheese', 'Olives']

print(person) #prints the Dictionaries person to the screen: answer: {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, eye_color: 'blue'}
person.pop('eye_color') #removes the eye_color var from the person Dictionaries and prints it to the screen. answer: blue
print(person) #prints the Dictionaries to the screne. (since we poped eye color the Dictionaries will be {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False})

for topping in pizza_toppings: #for loop, looping through the values in the list var. temportry setting each value to the var topping
    if topping == 'Pepperoni': #if statmemnt checking to see if the item in the sequence == Pepperoni
        continue #if it does it skips over and goes to the next item in the sequence
    print('After 1st if statement') #if topping == 'Pepperoni' then the string is printed to the screen 
    if topping == 'Olives': # if statement chekcin to see if this item in the sequence olives
        break #this is a break statement. When it hits here if breks out of the for lopp completely, no matter where it is in the iteration 

def print_hello_ten_times(): #function declaration  named print_hello_ten_times
    for num in range(10): #for loop set to the range fuction 
        print('Hello') # with each iteration of the loop hello is printed to the screen

print_hello_ten_times() #function call 

def print_hello_x_times(x): #function declaration with an parameters/arguments named x 
    for num in range(x): #for loop with the range of the parameter x
        print('Hello') #for each iteation of the loop, hello is printed to the screen

print_hello_x_times(4) #function call with the parameters/arguments 4 passed in the call

def print_hello_x_or_ten_times(x = 10): #function declaration with the parameters/arguments x defualt setting as 10 (so if no parameters/arguments get passed x wil = 10) 
    for num in range(x): #range loop that loops through x number of interantion based on the value of the parameters/arguments x
        print('Hello') #for that many iterations hello will be printed to the screen

print_hello_x_or_ten_times() # fucntion call. Since there is no parameters/arguments being passed x=10
print_hello_x_or_ten_times(4) # functnio call with a parameters/arguments, so x=4 in this call


"""
Bonus section
"""
# num3 = 72 #needs to be here
# print(num3) # we need to declare the var before we make the call

# fruit[0] = 'cranberry' #tuple's can't be changed once they are set. 
#person[favorite_team] = "NFL Rams";
# print(person['favorite_team']) # we have not set this item in the  Dictionaries 
# print(pizza_toppings[7]) #there is no list item set at index of 7 
#   print(boolean) #indented where no indent is needed
# fruit.append('raspberry') #Tuple can't be added to they're static
# fruit.pop(1) #again Tuple can't be changed, added to or deleted