
# config File in testGit
class Config:

    def __init__(self, username, password, database):
        self.__username = username
        self.__password = password
        self.__database = database

    def __str__(self):
        return f'{self.__username} - {self.__password} - {self.__database}'

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username):
        self.__username = username

    def to_dict(self):
        return {
            'username': self.__username,
            'password': self.__password,
            'database': self.__database,
        }

# add some comment to use status