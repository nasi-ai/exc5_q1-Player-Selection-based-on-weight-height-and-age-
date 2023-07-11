import random


# class MyExceptionHandling(Exception):
#     def __init__(self, message):
#         super().__init__(message)

class InvalidWeightException(Exception):
    'Raised when the input value is less than 18'
    pass


class InvalidAgeException(Exception):
    'Raised when the input value is less than 18'
    pass


class Participant:

    def __init__(self, name, lastname, age, height, weight):
        self._participant_code = self._make_participant_code()
        self._name = name
        self._lastname = lastname
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return f'{self._participant_code}' \
               f'{self._name}' \
               f'{self._lastname}' \
               f'{self._age}' \
               f'{self._height}' \
               f'{self._weight}'

    @staticmethod
    def _make_participant_code():
        rnd = random.randint(1000, 2000)
        return rnd

    # Check if a value is positive integer / can convert to integer or not
    @staticmethod
    def _is_integer(value):
        try:
            v = int(value)
            if v < 0:
                return False
            return True
        except ValueError:
            return False

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
    def age(self, value):
        if not Participant._is_integer(value):
            raise InvalidAgeException('Age is not valid')
        else:
            if not (15 <= int(value) <= 35):
                raise InvalidAgeException('Age out of range.\nThis person is not allowed to register.')

        self._age = int(value)

    @property
    def height(self):
        return 
    
    @height.setter
    def height(self, value):
        if not (170 <= value <= 190):
            raise ValueError('Height out of range.\nThis person is not allowed to register.')
        self._height = value

    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, value):
        try:
            value = float(value)

        except ValueError:
            raise InvalidWeightException('Weight is not valid!')

        else:
            if not (50 <= value <= 80):
                raise InvalidWeightException('Weight out of range!\nThis person is not allowed to register.')

            self._weight = float(value)



# ----------------------------------------------


try:
    name = input('Enter name : ')
    lastname = input('Enter lastname : ')
    weight = input('Enter weight : ')
    height = input('Enter height : ')
    age = input('Enter age : ')
    participant = Participant(name=name, lastname=lastname, age=age, weight=weight, height=height)

except InvalidWeightException as error:
    print(error)
except InvalidAgeException as error:
    print(error)
# except InvalidHeightException as error:
#     print(error)
else:
    print(participant)