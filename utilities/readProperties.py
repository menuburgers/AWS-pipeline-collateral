import configparser

config = configparser.RawConfigParser()
config.read(".\\configfiles\\config.ini")

class ReadConfig():
    @staticmethod
    def get_application_url():
        url = config.get('common_info','baseURL')
        return url

    @staticmethod
    def get_application_username():
        username = config.get('common_info','username')
        return username

    @staticmethod
    def get_application_password():
        password = config.get('common_info','password')
        return password