
class User:

    def __init__(self, id, username, email, firstName, lastName, gender, image, accessToken, refreshToken):
        self.__id = id
        self.__username = username
        self.__email = email
        self.__firstName = firstName
        self.__lastName = lastName
        self.__gender = gender
        self.__image = image
        self.__accessToken = accessToken
        self.__refreshToken = refreshToken

    def __str__(self):
        return (f'Id: {self.__id}\n'
                f'Username: {self.__username}\n'
                f'Email: {self.__email}\n'
                f'First Name: {self.__firstName}\n'
                f'Last Name: {self.__lastName}\n'
                f'Gender: {self.__gender}\n'
                f'Image: {self.__image}')

    @property
    def accessToken(self):
        return self.__accessToken
    @accessToken.setter
    def accessToken(self, accessToken):
        self.__accessToken = accessToken

    @property
    def refreshToken(self):
        return self.__refreshToken
    @refreshToken.setter
    def refreshToken(self, refreshToken):
        self.__refreshToken = refreshToken