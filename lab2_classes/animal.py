#!/usr/bin/env python3

# https://peps.python.org/pep-0498/#s-r-and-a-are-redundant

# TODO: fill classes below with the required logic
#       to represent human and person (probably with tax number, ...)
# TODO: try to make an Enterprise able to own Pets
# TODO: - add class to represent vaccine
#       - add class to represent generic chip,
#           and separate subclasses for concrete animal ID chips
#       - anything other you want to extend here

# doing only a half of sanity checks because it is bloated already

# Animal -> Human -> Person
#        -> Pet
# Vaccine
# Enterprise
# Chip -> RFIDChip
#      -> GPSChip
# https://www.asiarfid.com/wp-content/uploads/2020/07/pet-id-tags-600x600.jpg

class Enterprise:
    def __init__(self, name):
        self.name = name
        self.pets = list()
    
    def add_pet(self, pet):
        self.pets.append(pet)
        pet.change_owner(self)
        
    def __repr__(self):
        return f'{self.__class__.__name__}: name = {self.name}, owned_pets = {self.pets}'

class Chip:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_size_str(self):
        return f'({self.width} x {self.length}) mm'

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.get_size_str()}'

class RFIDChip(Chip):
    def __init__(self, width, length, frequency):
        super().__init__(width, length)
        self.frequency = frequency

    @property
    def frequency(self):
        return self.__frequency

    @frequency.setter
    def frequency(self, value):
        if value >= 120 and value <= 150:
            self.__frequency = value
        else:
            raise ValueError('frequency must be in range [120-150] kHz')

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.get_size_str()}, frequency = {self.frequency} kHz'

class GPSChip(Chip):
    def __init__(self, width, length, xy):
        super().__init__(width, length)
        self.update_xy(xy)

    def update_xy(self, xy):
        self.x = xy[0]
        self.y = xy[1]

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.get_size_str()}, pos = ({self.x}, {self.y})'

class Vaccine:
    def __init__(self, vac_type, due_in_months):
        self.vac_type = vac_type
        self.due_in_months = due_in_months
    
    @property
    def vac_type(self):
        return self.__vac_type

    @vac_type.setter
    def vac_type(self, value):
        if isinstance(value, str):
            self.__vac_type = value
        else:
            raise ValueError('vac_type must be a string')

    @property
    def due_in_months(self):
        return self.__due_in_months

    @due_in_months.setter
    def due_in_months(self, value):
        if value > 0:
            self.__due_in_months = value
        else:
            raise ValueError('due_in_months must be greater than 0.')

    def __repr__(self):
        return f'{self.__class__.__name__}: type = {self.vac_type}, due_in = {self.due_in_months} month(s)'

class Animal:
    def __init__(self, kind, age):
        self.kind = kind
        self.age = age

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        if isinstance(value, str):
            self.__kind = value
        else:
            raise ValueError('kind must be a string')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            raise ValueError('age must be greater than 0.')

    def __repr__(self):
        return f"{self.__class__.__name__}: kind = {self.kind}"

class Pet(Animal):
    def __init__(self, kind, age, owner):
        super().__init__(kind, age)
        self.owner = owner
        self.vaccine = None
        self.chip = None

    def change_owner(self, new_owner):
        self.owner = new_owner

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if isinstance(value, (Person, Enterprise)):
            self.__owner = value
        else:
            err = f'{value} must be an instance or subclass of Person or Enterprise.'
            raise ValueError(err)

    def add_vaccine(self, vaccine):
        self.vaccine = vaccine

    def add_chip(self, chip):
        self.chip = chip

    def __repr__(self):
        desc = f'{self.__class__.__name__}: kind = {self.kind}, age = {self.age}, owner = {self.owner.name}'
        if self.vaccine:
            desc += f', vaccine = ({self.vaccine})'
        if self.chip:
            desc += f', chip = ({self.chip})'
        return desc

class Human(Animal):
    def __init__(self, name, age):
        super().__init__('human', age)
        self.name = name

class Person(Human):
    def __init__(self, name, age, tax_number):
        super().__init__(name, age)
        self.__tax_number = tax_number

    @property
    def tax_number(self):
        return self.__tax_number

    @tax_number.setter
    def tax_number(self, value):
        if value > 0:
            self.__tax_number = value
        else:
            err = f'tax_number must be greater than 0.'
            raise ValueError(err)

    def __repr__(self):
        return f'{self.__class__.__name__}: name = {self.name}, age = {self.age}, tax = {self.tax_number}'

def main(args):
    rfid = RFIDChip(1.4, 8, 144.4)
    gps = GPSChip(2.12, 12, (1, 1))

    cat_vac = Vaccine('cat vaccine', 6)
    dog_vac = Vaccine('dog vaccine', 3)

    good_person = Person('John Smith', 21, 123456789)
    
    cat = Pet('cat', 5, good_person)
    cat.add_vaccine(cat_vac)
    cat.add_chip(rfid)
    dog = Pet('dog', 2, good_person)
    dog.add_vaccine(dog_vac)
    dog.add_chip(gps)

    print(good_person)
    print(cat)
    print(dog)

    company = Enterprise('Animal Company')

    for i in range(1, 4):
        pet = Pet('cat', i, company)
        company.add_pet(pet)

    print(company)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
