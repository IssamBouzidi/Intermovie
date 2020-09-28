import requests
import zipfile

url = 'https://stdatalake005.blob.core.windows.net/public/movies_dataset.zip'


def download_file (url):
    
    r = requests.get(url)
    with open('data.zip','wb') as f:
        f.write(r.content)

    with zipfile.ZipFile('data.zip', 'r') as data_zip:
        data_zip.extractall('data')

download_file(url)








