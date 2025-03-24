import os
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

MAINPATH = os.path.join(os.path.dirname(os.path.abspath("consult.py")))

def consulta_mac(mac):
    try:
        URL = "https://" + mac   

        with open(os.path.join(MAINPATH, "config", "token.txt"), 'r') as file:
            token = file.read().strip()

        headers = {
        "Authorization": f"Bearer {token}"
        }
        
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        response = requests.get(URL, headers=headers)
        
        if response.status_code == 200:
            status = response.json()['profile']['status']
            client = response.json()['profile']['name']
            version = response.json()['fw_version']
            
            #print(status, client, version)

            return status, version, client
        else:
            nomac = 10
            return nomac
    except Exception as e:
        print("Error ", e)
