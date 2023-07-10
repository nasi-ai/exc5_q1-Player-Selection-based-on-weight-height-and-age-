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

    # Check if a value is positive integer / can convert to integer or not
    @staticmethod
    def _check_integer(value):
        try:
            if not int(value) < 0:
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
        # try:
        #     age = Participant._check_integer(value)
        # except ValueError:
        #     raise InvalidAgeException('Age is not valid')
        # else:
        #     if not (15 <= age <= 35):
        #         raise InvalidAgeException('Age out of range.\nThis person is not allowed to register.')
        #
        # self._age = age

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

participant = Participant()

# try:
#     participant.weight = input('Enter weight : ')
# except InvalidWeightException as error:
#     print(error)

# participant.age = '35'
try:
    c= Participant._check_integer('36')
except ValueError as error:
    print(error)
else:
    print(c)