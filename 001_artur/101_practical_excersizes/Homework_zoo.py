class Animal:
    def __init__(self, name, species):
        self.__name = name
        self.__species = species
    @property
    def name(self):
        return self.__name

    @property
    def species(self):
        return self.__species

class Mammal(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.__fur_color = fur_color

    def fur_color(self):
        return self.__fur_color

class Bird(Animal):
    def __init__(self, name, species, wing_span):
        super().__init__(name, species)
        self.__wing_span = wing_span

    def wing_span(self):
        return self.__wing_span

class Reptile(Animal):
    def __init__(self, name, species, scale_type):
        super().__init__(name, species)
        self.__scale_type = scale_type

    def get_scale_type(self):
        return self.__scale_type


class Zoo:
    def __init__(self):
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)

    def list_animals(self):
        for animal in self.__animals:
            print(f'{animal.name} ({animal.species})')

    def count_animals(self):
        return len(self.__animals)

    def get_animals_by_species(self, species):
        species_list = []
        for animal in self.__animals:
            if animal.species == species:
                species_list.append(animal)
        return species_list


    def remove_animal(self, name):
        for animal in self.__animals:
            if animal.name() == name:
                self.__animals.remove(animal)
                return #break razryvaet raboty programmy
        print('Animal with {name} is not in Zoo')

    def feed_animals(self):
        for animal in self.__animals:
            if isinstance(animal, Mammal):
                print(
                    f"Feeding {animal.name()} the {animal.species()} with fur color {animal.fur_color()}...")
                # Implement feeding logic for mammals
            elif isinstance(animal, Bird):
                print(
                    f"Feeding {animal.name()} the {animal.species()} with wing span {animal.wing_span()}...")
                # Implement feeding logic for birds
            elif isinstance(animal, Reptile):
                print(
                    f"Feeding {animal.name()} the {animal.species()} with scale type {animal.scale_type()}...")
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
    zoo.list_animals()
    # for animal in Zoo.list_animals():
    #     print(f"{animal.name()} ({animal.species()})")


    print(f"\nTotal Animals in the Zoo: {zoo.count_animals()}")

    print("\nFeeding the Animals:")
    zoo.feed_animals()