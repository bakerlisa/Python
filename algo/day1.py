# 1. Reverse the string
def reverse(element):
    backwards = ""
    for x in range((len(element)-1),-1,-1):
        backwards += element[x]
    return backwards
print(reverse('broadhead'))

# 2. Anacrymn
def acronym(element):
    acr = ""
    print(len(element))
    for x in range(0,len(element)):
        if(x == 0):
            acr+= element[0]
        elif(element[x] == " " and element[x +1] != "-"):
            acr += element[x + 1]
    return acr
print(acronym("There is no such thing - as a free lunch"))