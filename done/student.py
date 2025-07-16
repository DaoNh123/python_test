class Student:
    def __init__(self, name, branch, year, cgpa):
        self.__name = name
        self.__branch = branch
        self.__year = year
        self.__cgpa = cgpa

    @property
    def branch(self):
        return self.__branch

    @branch.setter
    def branch(self, value):
        self.__branch = value
    def __str__(self):
        return f'{self.__name}: {self.__branch} - {self.__year} - {self.__cgpa}'


if __name__ == '__main__':
    pass