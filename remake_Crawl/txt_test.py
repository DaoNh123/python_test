from remake_Crawl.config import Config

if __name__ == '__main__':
    config = Config('username1', 'password1', 'url1')

    with open('config.txt', 'w', encoding="utf-8") as txt_file:
        for key, value in config.to_dict().items():
            txt_file.write(f'{key}={value}\n')

    data = {}
    with open('config.txt', 'r', encoding="utf-8") as txt_file:
        config = {}
        with open("config.txt", 'r') as txtFile:
            for line in txtFile:
                line = line.strip()  # loại bỏ khoảng trắng và xuống dòng
                if line and "=" in line:
                    key, value = line.split("=")
                    data[key.strip()] = value.strip()

    print(data)
    config2 = Config(**data)
    print(config2)