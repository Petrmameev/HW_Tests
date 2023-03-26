import requests
from Token import TOKEN_YA

def get_headers():
    return {'Content-Type': 'application/json', 'Authorization': f'OAuth {TOKEN_YA}'}

def create_folder():
    folder = 'HW'
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = get_headers()
    res = requests.put(f'{url}?path={folder}', headers=headers).status_code
    return res

if __name__ == '__main__':
    create_folder()