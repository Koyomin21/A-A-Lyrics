import requests
from bs4 import BeautifulSoup
import csv
import lxml
from utils import *
import math

client_id = 'Uzji2Ly8g53CyPb1BGXrA5_kpF6Jas4J4txp9Pi55144c2MkPnMfVD12n34FA1JI'
client_secret = 'T-DSYjEjwRIZzSajBWsPEdCvAlKNZPECrXuDXMxq2dzcq30Y6489E_CJ6H304WQOJGDcJZo9j462L3eMLHe9HQ'
client_access_token = 'blsOYvt4Fv9LqB_hYWSrP_fmkRhoHlfcxMi7NCW_4LGFs1_Vlyi0uKNe4qT9N8I8'

base_api = 'https://api.genius.com/'

def main():
    token = 'Bearer {}'.format(client_access_token)
    headers = {"Authorization": token}  
    r = requests.get('https://api.genius.com/search?q={}'.format(name),headers=headers)
    id_ = get_artist_id(name)
    print(id_)
    

    url = 'https://genius.com/' + 'Xxxtentacion-sad-lyrics'
    r = requests.get(url)

    
    # art = write_json('artists/1421','artist.json')
    # print('Image url: ',art['response']['artist']['image_url'])
    # print(art['response']['artist']['description'])
    name = input()
    url = base_api + 'artists/1421'
    r = requests.get(url,headers=headers)
    print(r)
    artist = r.json()
    with open('artist_infa.json','w',encoding='utf-8') as f:
        json.dump(artist,f,ensure_ascii=False)

    print(artist)
    
    # s1 = write_json('search?q={}'.format(name),'artist_info.json')


    # a1 = write_json('search?q={}'.format(name),'artist_info.json')
    # a2 = write_json(a1['response']['hits'][0]['result']['primary_artist']['api_path'][1:],'artist.json')
    




    # with open('lyrics3.txt','w')as f:
    #     print(lyrics.get_text())
    #     print(type(lyrics))
    #     f.write(lyrics.get_text())


    # with open('lyrics3.txt','w+',encoding='utf-8')as f:
    #     for div in soup.body.find_all('div'):
    #         f.write(div.text)
    #     f.close()
        # f.write(soup.find_all('div',attr={'class':'lyrics'}))
    



if __name__ == '__main__':
    main()
    