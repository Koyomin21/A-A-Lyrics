import json
import requests
from bs4 import BeautifulSoup
import lxml.html
from lxml import etree
import config

client_id = config.CLIENT_ID
client_secret = config.CLIENT_SECRET
client_access_token = client_access_tokens

base_api = 'https://api.genius.com/'


def write_json(url=None,file_name='answer.json',params=None,headers=None):
    '''Send request and get response in json format.'''
    # Generate request URL
    url = base_api+ url
    token = "Bearer {}".format(client_access_token)

    if headers:
        headers['Authorization'] = token
    else:
        headers = {"Authorization": token}

    # Get response object from querying genius api
    response = requests.get(url=url, params=params, headers=headers)
    print(response)
    with open(file_name,'w',encoding='utf-8')as f:
        json.dump(response.json(),f,ensure_ascii=False,indent=4)
        f.close()
    
    return dict(response.json())

def get_artist_id(artist_name=None):
    """
    param artist_name: имя(псевдоним) артиста
    return False: если артиста с таким именем не существует
    return id: возвращает идентификатор артиста
    """
    r = 'search?q={}'.format(artist_name)
    file = write_json(r,'artist_id.json')
    
    if file['response']['hits'][0]['result']['primary_artist']['id']:
        return file['response']['hits'][0]['result']['primary_artist']['id']
    else:
        return False
   


def get_lyrics_path(song_id):
    r = write_json('songs/{}'.format(song_id))
    path = r['response']['song']['path']

    return path

 


def get_name(name):
    return name.replace(' ','-').lower()


def quick_search(artist_name,song_name):
    artist_name = get_name(artist_name)
    song_name = get_name(song_name)

    url = 'https://genius.com/{}'.format(artist_name+'-'+song_name)+'-lyrics'
    r = requests.get(url)
    print(url)


    
    soup = BeautifulSoup(r.text,'lxml')
    lyrics = soup.find('div', class_='lyrics')
    loop = 0
    while type(lyrics)==type(None):
        if loop == 7:
            return False
            break

        r = requests.get(url)
        soup = BeautifulSoup(r.text,'lxml')
        lyrics = soup.find('div', class_='lyrics')
        print(loop)
        loop+=1


    return lyrics.get_text()



def get_artist_info(artist_id=None,artist_name=None):

    if artist_id is None:
        artist_id = get_artist_id(artist_name)

    token = "Bearer {}".format(client_access_token)
    headers = {"Authorization": token}
    params = {'text_format':'plain'}

    r = requests.get(base_api + 'artists/{}'.format(artist_id),headers=headers,params=params)

    js = json.loads(r.text)
    
    return js
        
def get_song_info(song_name=None):
    info = write_json('search?q={}'.format(song_name))
    return info

def get_lyric(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    lyrics = soup.find('div', class_='lyrics')
    loop = 0
    while type(lyrics)==type(None):
        if loop == 7:
            return False
            break

        r = requests.get(url)
        soup = BeautifulSoup(r.text,'lxml')
        lyrics = soup.find('div', class_='lyrics')
        print(loop)
        loop+=1


    return lyrics.get_text()



def check_artist(artist_id,artists):
    for artist in artists:
        if artist_id == artist_id:
            return True
    return False




    



