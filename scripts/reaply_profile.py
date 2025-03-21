import os
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

MAINPATH = os.path.join(os.path.dirname(os.path.abspath("consult.py")))

def reaply_profile(mac):
    try:
        URL = "https://helpdesk.remotize.intelbras.com.br/api/devices/" + mac + "/profile/status/reaply"

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
        response = requests.put(URL, headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print("Error ", e)

reaply_profile("30e1f1cfaa81")