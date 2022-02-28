# ********************** READING NOTES **********************

# We'll use the Person class to demonstrate polymorphism
# in which multiple classes inherit from the same class but behave in different ways
class Person:
  def pay_bill(self):
      raise NotImplementedError
# Millionaire inherits from Person
class Millionaire(Person):
  def pay_bill(self):
      print("Here you go! Keep the change!")
# Grad Student also inherits from the Person class
class GradStudent(Person):
  def pay_bill(self):
      print("Can I owe you ten bucks or do the dishes?")

# Raise - use it if yo're going to override or you're in "debug / building mode"

# ********************** LECTURE NOTES **********************
#  superhero folder

# 4 pillars
# 1. encapulation - grouping 
# 2. inheritance - get from ancestor
# 3. Polymorphism - many forms (room can be office, wo room, guest room ect.)
# 4. abstraction - hide things we don't need

# associations - two unlike things that can't be each other but need to talk or be connected. Dogs amd wolves are similar and can talk but they are very differeny things
  #   - pet can't be an owner
# sub class - more specifis of a class: dog is mamal -> carnivor -> canidea ->canis -> lupus ->familiaris 


# questions to ask ourselves: Whats the relationship between the things we're about to make and what we're doing

# from richtech import RichTech
# from [file] improt [class]



# ******************** READING NOTES: FLASK **********************
