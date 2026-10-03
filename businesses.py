class Rescue():
    def __init__(self):
        self.inventory = []
        self.capacity = 0

    def add_dog(self, dog):
        if len(self.inventory) < self.capacity:
            self.inventory.append(dog)
        else:
            print("inventory full.")