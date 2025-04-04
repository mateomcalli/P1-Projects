from pakuri import Pakuri

class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.tally = 0
        self.species = []
    def get_size(self):
        return self.tally
    def get_capacity(self):
        return self.capacity
    def get_species_array(self):
        if self.species:
            dummy = []
            for pakuri in self.species:
                dummy.append(pakuri.species)
            return dummy
        else: return None
    def get_stats(self, species):
        for pakuri in self.species:
            if pakuri.get_species() == species:
                return [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]
        else: return None
    def sort_pakuri(self):
        unsorted = []
        for pakuri in self.species:
            unsorted.append(pakuri.species)
        unsorted.sort()
        return unsorted
    def add_pakuri(self, species):
        for pakuri in self.species:
            if pakuri.get_species() == species:
                return False
        if self.tally < self.capacity:
            self.tally += 1
            self.species.append(Pakuri(species))
            return True
    def evolve_species(self, species):
        for pakuri in self.species:
            if pakuri.get_species() == species:
                return pakuri.evolve()
        else: return False

