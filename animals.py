class Dog():
    def __init__(self, breed, color, age):
        self._breed = breed
        self._color = color
        self._age = age

    

    def set_breed(self, breed):
        self._breed = breed

    def set_color(self, color):
        self._color = color

    def set_age(self, age):
        self._age = age


        
    def get_breed(self):
        return self._breed
    
    def get_color(self):
        return self._color
    
    def get_age(self):
        return self._age

    def __eq__(self, other):
            if self.get_breed() == other.get_breed() and \
               self.get_color() == other.get_color() and \
               self.get_age() == other.get_age():
                return True
            else:
                return False