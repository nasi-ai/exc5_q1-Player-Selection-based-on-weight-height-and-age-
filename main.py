import random


class MyExceptionHandling(Exception):
    def __init__(self, message):
        super().__init__(message)

# class InvalidWeightException(Exception):
#     'Raised when the input value is less than 18'
#     pass
#
#
# class InvalidAgeException(Exception):
#     'Raised when the input value is '
#     pass
#
#
# class InvalidHeightException(Exception):
#     'Raised when the input value is not integer or not between 170 and 190'
#     pass


class Participant:

    def __init__(self, v_name, v_lastname, v_age, v_height, v_weight):
        self._participant_code = self._generate_participant_code()
        self._name = v_name
        self._lastname = v_lastname
        self.age = v_age
        self.height = v_height
        self.weight = v_weight

    def __str__(self):
        return f'{self._participant_code}' \
               f'{self._name}' \
               f'{self._lastname}' \
               f'{self._age}' \
               f'{self._height}' \
               f'{self._weight}'

    @staticmethod
    def _generate_participant_code():
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

    @staticmethod
    def _is_float(value):
        try:
            v = float(value)
            if v < 0:
                return False
            return True
        except ValueError:
            return False

    def validate_weight(self, value):
        # if age is not entered, raise an Error.
        if self.age is None:
            raise MyExceptionHandling('Age is not entered, first enter the age, then continue...')

        if not Participant._is_float(value):
            raise MyExceptionHandling('weight is not valid!')

        weight_value = float(value)
        if 15 <= self.age < 25:
            if not (60 <= weight_value <= 80):
                raise MyExceptionHandling('Weight out of range! This person is not allowed to register.')
        else:
            if not (50 <= weight_value <= 75):
                raise MyExceptionHandling('Weight out of range! This person is not allowed to register.')

        return weight_value

    @staticmethod
    def validate_height(value):
        if not Participant._is_integer(value):
            raise MyExceptionHandling('Height is not valid!')
        else:
            height_value = int(value)
            if not (170 <= height_value <= 190):
                raise MyExceptionHandling('Height out of range.\nThis person is not allowed to register.')

        return height_value

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
        if value is None:
            age_value = None
        else:
            if not Participant._is_integer(value):
                raise MyExceptionHandling('Age is not valid')
            else:
                age_value = int(value)
                if not (15 <= age_value <= 35):
                    raise MyExceptionHandling('Age out of range.\nThis person is not allowed to register.')

        self._age = age_value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value is None:
            height_value = None
        else:
            height_value = self.validate_height(value)

        self._height = height_value

    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, value):
        if value is not None:
            self._weight = self.validate_weight(value)
        else:
            self._weight = None

# ----------------------------------------------


try:
    name = input('Enter name : ')
    if not name.isalpha():
        raise MyExceptionHandling('Invalid name! Name should only contain alphabetic characters.')

    lastname = input('Enter lastname : ')
    if not lastname.isalpha():
        raise MyExceptionHandling('Invalid Lastname! Lastname should only contain alphabetic characters.')

    participant = Participant(v_name=name, v_lastname=lastname, v_age=None, v_weight=None, v_height=None)

    participant.age = input('Enter age : ')
    participant.weight = input('Enter weight : ')
    participant.height = input('Enter height : ')

except MyExceptionHandling as error:
    print(error)

else:
    print(participant)