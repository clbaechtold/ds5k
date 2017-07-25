class Person(object):
    def __init__(self, age=20, gender='male', friends=[]):
        self.age = age
        self.gender = gender
        self.friends = friends

    def print_stats(self):
        print('Age: ', self.age)
        print('Gender: ', self.gender)
        print('Friends: ', self.friends)

class Building(object):
    avg_sqft = 12500
    avg_bedrooms = 3
    avg_bathroom = 2

    def describe_building(self):
        print('Avg Beds: ', self.avg_bedrooms)
        print('Avg Baths: ' , self.avg_bathroom)
        print('Avg. Square Footage: ', self.avg_sqft)

    def get_avg_price(self):
        price = self.avg_sqft*5 + self.avg_bedrooms*15000 + self.avg_bathroom*15000
        return price

class Mansion(Building):
    avg_sqft = 125000
    avg_bedrooms = 8
    avg_bathroom = 10
