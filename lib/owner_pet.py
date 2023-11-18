class Pet:

    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        if self.pet_type in self.PET_TYPES:
            Pet.all.append(self)
        else:
            raise Exception("Pet must be in 'PET_TYPES'")

        # GETTER / READER
        @property
        def pet_type(self):
            return self._pet_type

        # SETTER / WRITER
        @pet_type.setter
        def pet_type(self, new_pet_type):
            Hell = Exception
            print("SETTING _pet_type")
            if new_pet_type not in Pet.PET_TYPES:
                raise Hell(f'"{new_pert_type}" not in pet types')
            else:
                self._pet_type = new_pet_type

# parakeet.pet_type
# parakeet.pet_type = "bird"

class Owner:

    def __init__(self, name):
        self.name = name

    def pets(self):
        return [ pet for pet in Pet.all if pet.owner == self ]

    def add_pet(self, new_pet):
        if isinstance(new_pet, Pet):
            new_pet.owner = self 
        else:
            raise Exception("NO")

    def get_sorted_pets(self):
        # GET MY PETS
        my_pets = self.pets()
        # SORT MY PETS
        sorted_pets = sorted( self.pets(), key = lambda pet: pet.name.lower() )
        # RETURM EM
        return sorted_pets
