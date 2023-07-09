import random


class Participant:
    def __init__(self):
        self._participant_code = self._make_participant_code()
        self._name = None
        self._lastname = None
        self._age = -1
        self._height = -1
        self._weight = -1
# def __init__(self, name, lastname, age, height, weight):
#         self._participant_code = self._make_participant_code()
#         self._name = name
#         self._lastname = lastname
#         self._age = age
#         self._height = height
#         self._weight = weight

    @staticmethod
    def _make_participant_code():
        rnd = random.randint(1000, 2000)
        return rnd
    
    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def lastname(self):
        return self.lastname
    
    @lastname.setter
    def lastname(self, value):
        self._lastname = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise TypeError('Age must be an integer.')
        if not (15 <= age <= 35):
            raise ValueError('Age must be between 15 and 35.')
        self._age = age

    @property
    def height(self):
        return 
    
    @height.setter
    def height(self, value):
        pass

    @property
    def weight(self):
        return 
    
    @weight.setter
    def weight(self, value):
        pass




o = Participant()
o.age = 35
