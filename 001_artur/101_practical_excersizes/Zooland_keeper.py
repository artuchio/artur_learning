import csv

class Animal:
    def __init__(self, name, species):
        self.__name = name
        self.__species = species

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

    def remove_animal(self, name):
        for animal in self.__animals:
            if animal.get_name() == name:
                self.__animals.remove(animal)
                break

    def count_animals(self):
        return len(self.__animals)

    def feed_animals(self):
        for animal in self.__animals:
            if isinstance(animal, Mammal):
                print(f"Feeding {animal.get_name()} the {animal.get_species()} with fur color {animal.get_fur_color()}...")
            elif isinstance(animal, Bird):
                print(f"Feeding {animal.get_name()} the {animal.get_species()} with wing span {animal.get_wing_span()}...")
            elif isinstance(animal, Reptile):
                print(f"Feeding {animal.get_name()} the {animal.get_species()} with scale type {animal.get_scale_type()}...")

def main():
    zoo = Zoo()

    while True:
        print("\nZoo Management System")
        print("1. Add Animal")
        print("2. Remove Animal")
        print("3. List Animals")
        print("4. Feed Animals")
        print("5. Save Data to CSV")
        print("6. Load Data from CSV")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the animal's name: ").capitalize()
            species = input("Enter the animal's species: ").capitalize()
            animal_type = input("Enter the animal type (Mammal/Bird/Reptile): ").capitalize()
            if animal_type not in ["Mammal", "Bird", "Reptile"]:
                print("Invalid animal type. Choose from Mammal, Bird, or Reptile.")
                continue

            if animal_type == "Mammal":
                fur_color = input("Enter fur color: ").capitalize()
                animal = Mammal(name, species, fur_color)
            elif animal_type == "Bird":
                wing_span = float(input("Enter wing span: "))
                animal = Bird(name, species, wing_span)
            else:
                scale_type = input("Enter scale type: ").capitalize()
                animal = Reptile(name, species, scale_type)

            zoo.add_animal(animal)
            print(f"{name} the {species} has been added to the zoo.")

        elif choice == "2":
            name = input("Enter the name of the animal to remove: ").capitalize()
            zoo.remove_animal(name)
            print(f"{name} has been removed from the zoo.")

        elif choice == "3":
            print("\nList of Animals in the Zoo:")
            for animal in zoo.list_animals():
                print(f"{animal.get_name()} ({animal.get_species()})")

        elif choice == "4":
            print("\nFeeding the Animals:")
            zoo.feed_animals()

        elif choice == "5":
            with open("zoo_data.csv", mode="w", newline="") as file:
                writer = csv.writer(file)
                for animal in zoo.list_animals():
                    if isinstance(animal, Mammal):
                        writer.writerow(["Mammal", animal.get_name(), animal.get_species(), animal.get_fur_color()])
                    elif isinstance(animal, Bird):
                        writer.writerow(["Bird", animal.get_name(), animal.get_species(), animal.get_wing_span()])
                    elif isinstance(animal, Reptile):
                        writer.writerow(["Reptile", animal.get_name(), animal.get_species(), animal.get_scale_type()])

            print("Zoo data has been saved to zoo_data.csv.")

        elif choice == "6":
            try:
                with open("zoo_data.csv", mode="r") as file:
                    reader = csv.reader(file)
                    for row in reader:
                        animal_type, name, species, attribute = row
                        if animal_type == "Mammal":
                            animal = Mammal(name, species, attribute)
                        elif animal_type == "Bird":
                            animal = Bird(name, species, float(attribute))
                        elif animal_type == "Reptile":
                            animal = Reptile(name, species, attribute)
                        zoo.add_animal(animal)

                print("Zoo data has been loaded from zoo_data.csv.")
            except FileNotFoundError:
                print("No saved data found.")

        elif choice == "7":
            break

if __name__ == "__main__":
    main()
