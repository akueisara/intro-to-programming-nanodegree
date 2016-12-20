# Lesson 3.4: Make Classes
# Mini-Project: Draw Turtles

# Sometimes we want to define classes that may have similarities.
# For example, a TVShow class and a Movie class would both have a title attribute.
# To cut down on repitition we can have classes inherit from each other.
# So in our example we could have both TVShow and Movie inherit from a class
# Video which includes all the shared attributes between Movie and TVShow.

class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - " + self.last_name)
        print("Eye Color - " + self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last Name - " + self.last_name)
        print("Eye Color - " + self.eye_color)
        print("Number of toys - " + str(self.number_of_toys))

billy_cyrus = Parent("Cyrus", "blue")
billy_cyrus.show_info()
#print(billy_cyrus.last_name)

miley_cyrus = Child("Cyrus", "Blue", 5)
miley_cyrus.show_info()
#print(miley_cyrus.last_name)
#print(miley_cyrus.number_of_toys)
