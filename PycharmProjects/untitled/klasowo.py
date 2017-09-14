class Person:
    """
    This class is used to handle Person and its parents
    
    :type __age : int
    :type __surname : str
    :type __name : str    
    :type father : Person
    """
    def __init__(self, name, surname="Piątkowski", age=0):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.mother = None  # type: Person
        self.father = None

    def say_hello(self):
        print("Hello {} {}!".format(self.__name, self.__surname))

    def set_father(self, daddy):
        """        
        :param Person daddy: daddy to be set
        """
        self.father = daddy

    def set_mother(self, mommy):
        """
        Sets new mother
        
        :param Person mommy: mommy to set for this person
        """
        self.mother = mommy

    def get_mother(self) -> Person:
        """
        Returns mother if set
        """
        return self.mother

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_age_in_months(self) -> float:
        """        
        :return: age in months 
        """
        return self.__age * 12

    def set_age(self, new_age: int):
        """        
        :param new_age: sets new pretty age
        """
        if new_age < 0:
            raise Exception
        self.__age = new_age
