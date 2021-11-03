class Dog:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return 'Woof!'

class Cat:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return 'Meow!'

def get_pet(pet='dog'):
    """factory method"""
    pets =dict(dog=Dog('Hope'),cat=Cat('Peace'))
    return pets[pet]

d = get_pet('cat')

print(d.speak())

c = get_pet()





