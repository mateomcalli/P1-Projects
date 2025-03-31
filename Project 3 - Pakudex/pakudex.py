import pakuri
class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.current = None
        self.stats = None
    def get_size(self):
        return self.current
    def get_capacity(self):
        return self.capacity
    def get_species_array(self):
        pass
    def get_stats(self, species):
        self.stats.append(pakuri.get_attack())
