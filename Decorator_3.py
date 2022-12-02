from Decorator_2 import logger
import requests

FILE_PATH = 'decoratorlogger.log'

@logger(FILE_PATH)
def get_status(*args, **kwargs):
    url = ''.join(args)
    response = requests.get(url)
    return response.status_code


if __name__ == '__main__':
    get_status('https://vk.com/')
