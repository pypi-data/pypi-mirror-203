import os
import sys
from pathlib import Path
import requests  
import zipfile

downloadLink = 'https://github.com/eng-aomar/ts/raw/main/my_data.pickle'
# downloadLink = 'https://github.com/eng-aomar/ts/raw/main/500.json'
# #downloadLink = 'https://www.deq.state.mi.us/gis-data/downloads/waterwells/Alcona_WaterWells.zip'
def _get_appdatadir():
    home = Path.home()


    if sys.platform == 'win32':
        return Path(home, 'AppData/Roaming/nlptools')
    else:
        return Path(home, '.nlptools')


def download_file(url, dest_path):
    filename = os.path.basename(url)
    file_path = os.path.join(dest_path, filename)
    
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                if chunk: 
                    f.write(chunk)
    
    # Extract zip file if downloaded file is a zip
    if zipfile.is_zipfile(file_path):
        extracted_folder_name = os.path.splitext(file_path)[0]
        with zipfile.ZipFile(file_path, 'r') as zip_file:
            zip_file.extractall(extracted_folder_name)
        os.remove(file_path)
    
    return file_path






#download_file(downloadLink ,_get_appdatadir())