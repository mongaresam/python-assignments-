class Animal:
    def move(self):
        print("Animal moves in some way...")

class Dog(Animal):
    def move(self):
        print("Running 🐕")

class Bird(Animal):
    def move(self):
        print("Flying 🐦")

class Fish(Animal):
    def move(self):
        print("Swimming 🐠")

# Example usage
animals = [Dog(), Bird(), Fish()]

for a in animals:
    a.move()   # Each one behaves differently
