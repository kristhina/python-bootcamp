class ListStats:
    def __init__(self, list_of_numbers):
        self.__list_of_numbers = list_of_numbers
        self.__list_average = None
        self.__max_number = None
        self.__min_number = None
        self.__median = None

    def add_number(self, new_number):
        self.__list_of_numbers.append(new_number)

    def get_list_average(self):
        if not self.__list_of_numbers:
            raise Exception
        self.__list_average = sum(self.__list_of_numbers) / len(self.__list_of_numbers)
        return self.__list_average

    def get_max(self):
        if not self.__list_of_numbers:
            raise Exception
        self.__max_number = self.__list_of_numbers[0]
        for number in self.__list_of_numbers:
            if number >= self.__max_number:
                self.__max_number = number
        return self.__max_number

    def get_min(self):
        if not self.__list_of_numbers:
            raise Exception
        self.__min_number = self.__list_of_numbers[0]
        for number in self.__list_of_numbers:
            if number < self.__min_number:
                self.__min_number = number
        return self.__min_number

    def __sort(self):
        sorted_list = []
        l = len(self.__list_of_numbers)
        list_to_sort = self.__list_of_numbers
        for i in range(l):
            x = min(list_to_sort)
            sorted_list.append(x)
            list_to_sort.remove(x)
        return sorted_list

    def get_median(self):
        if not self.__list_of_numbers:
            raise Exception
        l = len(self.__list_of_numbers)
        sorted_list = self.__sort()
        if l%2 == 1:
            x = l/2 + 0.5
            self.__median = sorted_list[x]
        else:
            x = l/2
            self.__median = (sorted_list[x] + sorted_list[x+1])/2
        return self.__median
