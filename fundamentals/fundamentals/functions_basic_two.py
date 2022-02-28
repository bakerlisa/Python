# 1. Countdown
def countdown(num):
    for x in range(num,-1,-1):
        print(x)

countdown(46)

# 2. Print and Return
def printReturn(list):
    for x in range(0,len(list)):
        print(list[0])
        return list[x+1]

print(printReturn([11,21,31,41,51]))

# 3. First Plus Length
def first_plus_length(list):
    sum = len(list) + list[0]
    return sum

print(first_plus_length([33,55,44,77,66]))

# 4. Values greater than second
def greater_than(list):
    newNum = []
    for w in range(0,len(list)):
        if(w+1 < len(list)):
            if(list[w] > list[w+1]):
                newNum.append(list[w])
    return newNum;

print(greater_than([786,234,85,23,965,24]))

# 5. This length that value
def len_val(size, value):
    newVals = []
    for b in range(0,size):
        newVals.append(value)
    return newVals

print(len_val(3,10))
