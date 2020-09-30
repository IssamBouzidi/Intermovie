import requests
import zipfile
import os 




def download_file (url):
    if not os.path.exists('../../data.zip'):
        r = requests.get(url)
        with open('../../data.zip','wb') as f:
            f.write(r.content)
    else:
        print("data.zip existe déja")

    if not os.path.exists('../../data'):
         with zipfile.ZipFile('../../data.zip', 'r') as data_zip:
            data_zip.extractall('../../data')
    else:
        print("data existe déja")
    











