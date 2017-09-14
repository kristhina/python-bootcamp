class Vector:
    """
    Vector Class that is used to count many different statistics for a list of numbers (vector)
    
    :type list_of_numbers: List
    :type __Vector: List 
    """

    def __init__(self, list_of_numbers):
        self.__Vector = list_of_numbers
        self.__sorted_list = sorted(list_of_numbers)

    def get_min(self):
        """
        Method used to count minimal value for our list of numbers (vector)
        :return: minimal value for the vector of numbers
        """
        l = len(self.__Vector)
        minimal_value = self.__Vector[0]
        for i in range(l):
            if self.__Vector[i] < minimal_value:
                minimal_value = self.__Vector[i]
        return minimal_value

    def get_max(self):
        """
        Method used to count maximal value for our list of numbers (vector)
        :return: maximal value for the vector of numbers
        """
        l = len(self.__Vector)
        maximal_value = self.__Vector[0]
        for i in range(l):
            if self.__Vector[i] > maximal_value:
                maximal_value = self.__Vector[i]
        return maximal_value

    def get_average(self):
        """
        Method used to count the mean of the list of numbers
        :return: arithmetical mean
        """
        l = len(self.__Vector)
        s = 0
        for i in range(l):
            s += self.__Vector[i]
        average = s/l
        return average

    def get_median(self):
        """
        Method used to count the median of the list of numbers (vector)
        :return: median
        """
        l = len(self.__Vector)
        if l % 2 == 1:
            middle = int(l/2 - 1/2)
            median = self.__sorted_list[middle]
            return median
        else:
            m1 = int(l/2-1)
            m2 = int(l/2)
            median = (self.__sorted_list[m1]+self.__sorted_list[m2])/2
            return median

    def get_std(self):
        """
        Method used to count the standard deviation for the list of numbers (vector)
        :return: standard deviation
        """
        




