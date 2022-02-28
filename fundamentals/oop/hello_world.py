print('hello world!')
x=4
print(x)
y=43
print(y)

# 1
print("Hello World")

# 2
name = "lisa"
print("Hello", name)

# 3
name = "lisa"
print("Hello " + name)

# 4 - can't concatinate a string and a var
number = "11"
print("Hello " + number)

# 5 
num  = 100000000000
print("hello, you just won $", num)
print(f"hello, you just won ${num} ")

# 6 
favfood = "Brownies"
favfood2 = "Pizza"
print("I love {} and {}!! Woot woot".format(favfood,favfood2))

# 7
favfood3 = "Ice Cream"
favFood4 = "Candy"
print(f"I love {favfood3} and {favFood4}!! Woot woot")

# 8
twisters = "Peter pepper PIPEr pepper PICked A pecK of PICKLED pEppErs pepper"
# print(twisters.casefold())
# print(twisters.count)
# x = twisters.count("pepper") Noice
# x = twisters.encode()
phrase = "h\te\tl\tl\to"
x = phrase.expandtabs(20)
print(x)

