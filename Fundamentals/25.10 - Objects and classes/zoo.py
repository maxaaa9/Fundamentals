class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species) -> str:
        self.species = ""
        if species == "mammal":
            self.species = f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            self.species = f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            self.species = f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        return self.species


name_of_zoo = Zoo(input())
number = int(input())
for n in range(number):
    command = input().split()
    species_command = command[0]
    name_of_animal = command[1]
    name_of_zoo.add_animal(species_command, name_of_animal)

species_type = input()
print(name_of_zoo.get_info(species_type))


