from art import tprint
import requests
from rich import print as rprint
tprint ("checkhost","amcaaa01")
rprint ("'создано при проекте *Python для чайников*'")



url = input('URL: ')


def valio(url):
        try:
                if 'http://' in url or 'https://' in url:
                        response = requests.get(url)
                else:
                        response = requests.get(f'https://{url}')

                return (str(response.status_code))

        except:
                print ('ошибка')
print (valio(url))
