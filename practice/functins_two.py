# 1
# def countdown(max):
#     newList = []
#     for x in range(0,max + 1):
#         newList.append(x)
#     return newList
# print(countdown(50))

# 2
# def print_return(val1,val2):
#     print(val1)
#     return val2
# print(print_return(2,20))

# 3
# def first_plus_length(list):
#     sum = list[0] + len(list)
#     return sum
# print(first_plus_length([12,34,46,78,95,1]))

# 4 
# def vals_great_sec(list):
#     new_list = []
#     for x in range(0,len(list)):
#         if(list[x] > list[x-1] or x == 0):
#             new_list.append(list[x])
#     return new_list

# print(vals_great_sec([5,2,3,2,1,4]))

# 5
def first_plus_length(size,value):
    new_list = []
    for x in range(0,size):
        new_list.append(value)
    return new_list
print(first_plus_length(2,7))



