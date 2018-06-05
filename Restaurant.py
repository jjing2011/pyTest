class Restaurant():
    """ex9"""

    def __init__(self, name, type):
        """init"""
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0

    def describe_restaurant(self):
        """print restaurant info"""
        print(self.restaurant_name.title())
        print(self.cuisine_type.title())

    def open_restaurant(self):
        """print open"""
        print(self.restaurant_name.title() + " is opening!")

    def set_number_served(self, numbers):
        if numbers > self.number_served:
            self.number_served = numbers
            print(self.number_served)
        else:
            print("Can't roll back the number")

    def increment_number_served(self, increment_number):
        if increment_number > 0:
            self.number_served += increment_number
            print(self.number_served)
        else:
            print("Don't support negative number")
        

restaurant = Restaurant("hard rock", "Thai Food")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

print(restaurant.number_served)
restaurant.set_number_served(12)
restaurant.set_number_served(11)

restaurant.increment_number_served(12)
restaurant.increment_number_served(-23)




class User():
    """user class"""

    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.full_name = self.first_name + ' ' + self.last_name

    def describe_user(self):
        print(self.full_name.title())

    def greet_user(self):
        print("Greetings, " + self.full_name.title())

user = User('Rick', 'Wang')

user.describe_user()
user.greet_user()