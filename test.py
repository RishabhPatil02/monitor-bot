import requests 
import time 
import json
from bs4 import BeautifulSoup
import threading
import randomheaders


def monitor():
    source=requests.get('https://www.vegnonveg.com/',headers = randomheaders.LoadHeader()).text
    soup=BeautifulSoup(source,'lxml')
    webhook = 'https://discordapp.com/channels/@me/803317856019415121/806488604431220737'
    
    for hrefs in soup.find_all('a',class_='gt-product-click'):
        url = hrefs.get('href')
        filename = 'links.txt'

        with open(filename, 'r' ) as rf:
            with open(filename, 'a' ) as af:
                read=rf.read()
                if url not in read:
                    print(url)
                    af.write('\n' + url)
                    data={
                        "username": "VegNonVeg",
                        "content": url
                    }
                    requests.post(webhook, data=data)
                # else:
                #     print("No new links found")
    time.sleep(30)

while True:        
     monitor()
