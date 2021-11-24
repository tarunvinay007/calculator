"""This is our calculation base class"""
class Calculation:
    # pylint: disable=too-few-public-methods
    """class constructor"""
    def __init__(self,value_a, value_b):
        """self references the instantiated object of the class"""
        self.value_a = value_a
        self.value_b = value_b
    @classmethod
    def create(cls, value_a, value_b):
        """class"""
        return cls(value_a,value_b)
