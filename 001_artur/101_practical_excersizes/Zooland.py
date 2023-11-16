class Animal:
    def __init__(self, name, species):
        self.__name = name
        self.__species = species
    @property
    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species

class Mammal(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color

    def get_fur_color(self):
        return self.fur_color

class Bird(Animal):
    def __init__(self, name, species, wing_span):
        super().__init__(name, species)
        self.wing_span = wing_span

    def get_wing_span(self):
        return self.wing_span

class Reptile(Animal):
    def __init__(self, name, species, scale_type):
        super().__init__(name, species)
        self.scale_type = scale_type

    def get_scale_type(self):
        return self.scale_type


class Zoo:
    def __init__(self):
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)

    def list_animals(self):
        return self.__animals

    def get_animals_by_species(self, species):
        return [animal for animal in self.__animals if animal.get_species() == species]

    def count_animals(self):
        return len(self.__animals)

    def remove_animal(self, name):
        for animal in self.__animals:
            if animal.get_name() == name:
                self.__animals.remove(animal)
                break


    def feed_animals(self):
        for animal in self.__animals:
            if isinstance(animal, Mammal):
                print(
                    f"Feeding {animal.get_name()} the {animal.get_species()} with fur color {animal.get_fur_color()}...")
                # Implement feeding logic for mammals
            elif isinstance(animal, Bird):
                print(
                    f"Feeding {animal.get_name()} the {animal.get_species()} with wing span {animal.get_wing_span()}...")
                # Implement feeding logic for birds
            elif isinstance(animal, Reptile):
                print(
                    f"Feeding {animal.get_name()} the {animal.get_species()} with scale type {animal.get_scale_type()}...")
                # Implement feeding logic for reptiles

if __name__ == '__main__':
    zoo = Zoo()

    lion = Mammal('Simba', 'Lion', 'Golden')
    eagle = Bird('Baldy', 'Eagle', 100.1)
    python = Reptile('Monty', 'Python', 'Diamond')
    python = Reptile('Kaa', 'Python', 'Octagon')
    royal_python = Reptile('Muscle', 'Python', 'Triangle')

    zoo.add_animal(lion)
    zoo.add_animal(eagle)
    zoo.add_animal(python)
    zoo.add_animal(royal_python)


    print('Zooland animals:')
    for animal in zoo.list_animals():
        print(f"{animal.get_name()} ({animal.get_species()})")

    print("\nList of Lions in the Zoo:")
    for lion in zoo.get_animals_by_species("Lion"):
        print(f"{lion.get_name()} ({lion.get_species()})")

    print(f"\nTotal Animals in the Zoo: {zoo.count_animals()}")

    print("\nFeeding the Animals:")
    zoo.feed_animals()