#1
# predict: 5, Answer: 5
# def number_of_food_groups():
#     return 5
# print(number_of_food_groups())

#2
# predict: error, Answer: error
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

# 3
# predict: 5, Answer: 5
# def number_of_books_on_hold():
#     return 5
#     return 10
# print(number_of_books_on_hold())

#4
# predict: 5, Answer: 5
# def number_of_fingers():
#     return 5
#     print(10)
# print(number_of_fingers())

#5
# predict: 5, Answer: 5, none
# def number_of_great_lakes():
#     print(5)
# x = number_of_great_lakes()
# print(f" {x}")

#6
# predict: 8, Answer: 3,5, error
# have to return the vaule of the addintion to get 8, otherise we get an error
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))

#7
# predict: 25, Answer: nothing
# # unindent the print statment then we'd get 25
# def concatenate(b,c):
#     return str(b)+str(c)
#     print(concatenate(2,5))

#8
# predict: error beause of the indentation, Answer: correct
# fix indentation: 100, error
# fix thoes errors: 100, 10
# def number_of_oceans_or_fingers_or_continents():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(number_of_oceans_or_fingers_or_continents())

#9
# predict: 7,14, 21 , Answer: correct
# def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

#10
# predict: 8 , Answer: correct
# def addition(b,c):
#     return b+c
#     return 10
# print(addition(3,5))

#11
# predict: 500,500,300,500, Answer: correct
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
# print(b)
# foobar()
# print(b)

#12
# predict: 500,500,300,500 Answer: correct
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# foobar()
# print(b)

#13
# predict: 500,500,300,300 Answer: correct
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=foobar()
# print(b)

#14
# predict: 1,3,2 Answer: correct
# def foo():
#     print(1)
#     bar()
#     print(2)
# def bar():
#     print(3)
# foo()

#15
# predict: 1,3,5,10 Answer: correct
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

