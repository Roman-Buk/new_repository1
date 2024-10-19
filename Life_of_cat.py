import random

cat_names = ["Whiskers", "Mittens", "Shadow", "Socks", "Fluffy"]
cat_breeds = ["Persian", "Siamese", "Maine Coon", "Bengal", "Sphynx"]

class Pet:
    def __init__(self, species, age, name):
        self.hunger = 100
        self.happiness = 50
        self.age = age
        self.species = species
        self.name = name

    def feed(self, food_amount):
        if self.hunger <= 20:
            self.happiness += 10
        self.hunger = max(self.hunger - food_amount, 40)
        self.happiness = min(self.happiness + food_amount / 8, 100)

    def play(self):
        self.happiness = min(self.happiness + 2, 100)
        self.hunger = max(self.hunger - 10, 0)

    def adjust_happiness(self):
        if random.random() < 0.2:
            self.happiness = max(self.happiness - random.randint(1, 5), 0)

    def status(self):
        return (f"{self.name} is a {self.species} ({self.breed}), "
                f"age: {self.age}, "
                f"happiness: {self.happiness}, "
                f"hunger: {self.hunger}")

    def grow(self):
        self.age += 1

class Cat(Pet):
    def __init__(self):
        name = random.choice(cat_names)
        breed = random.choice(cat_breeds)
        species = "cat"
        age = 0
        super().__init__(species, age, name)
        self.breed = breed

    def breed_get(self):
        return self.breed

def random_actions(cat):
    for _ in range(30):
        action = random.choice(['feed', 'play'])
        if action == 'feed':
            cat.feed(15)
            print(f"Fed {cat.name}.")
        else:
            cat.play()
            print(f"Played with {cat.name}.")
        cat.adjust_happiness()
        cat.grow()
        print(cat.status())

def cat_print():
    my_cat = Cat()
    print(my_cat.status())
    random_actions(my_cat)

cat_print()








