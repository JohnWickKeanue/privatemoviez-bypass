import time
import cloudscraper
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from requests import get, head

url = "https://privatemoviez.buzz/secret?data=QUt2THUwcVVHLzg0MWF3L0xuSjNvMXo4UlRaSThxWm5UQ2NvaUMwYktVcFU0MExmU1VjZDJGODR5aU00cDd2bDo6CM_s_fxBjF6WuEjrvBCXz4VA_e__e_"

def private(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    r = client.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    test= soup.text
    param = test.split('console.log("')[-1]
    url = param.split('");')[0]       
    param = url.split("/")[-1]     
    DOMAIN = "https://go.kinemaster.cc"
    final_url = f"{DOMAIN}/{param}"
    resp = client.get(final_url)
    soup = BeautifulSoup(resp.content, "html.parser")    
    try: inputs = soup.find(id="go-link").find_all(name="input")
    except: return "Incorrect Link"
    data = { input.get('name'): input.get('value') for input in inputs }
    h = { "x-requested-with": "XMLHttpRequest" }
    time.sleep(10)
    r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
    try:
        return r.json()['url']
    except: return "Something went wrong :("
print(private(url))
