class Account:
    def __init__(self, username, password, debug):
        self.__username = username
        self.__password = password
        self.__debug = debug

    def __str__(self):
        return f"Username: {self.__username}, Password: {self.__password}, Debug: {self.__debug}"

if __name__ == "__main__":
    config = {}
    with open("user_data.txt", 'r') as txtFile:
        for line in txtFile:
            line = line.strip() # loại bỏ khoảng trắng và xuống dòng
            if line and "=" in line:
                key, value = line.split("=")
                config[key.strip()] = value.strip()

    account = Account(config['username'], config['password'], config['debug'])
    print(account)


