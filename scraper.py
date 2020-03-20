from requests import get
from bs4 import BeautifulSoup as BS 
from json import loads

def scrape_data(username):
    resp = get(f'https://instagram.com/{username}')
    if resp.status_code == 200:
        soup = BS(resp.text, 'html.parser')
        scripts = soup.find_all('script')

        data_script = scripts[4]

        content = data_script.contents[0]
        data_object = content[content.find('{"config"') : -1]
        data_json = loads(data_object)
        data_json = data_json['entry_data']['ProfilePage'][0]['graphql']['user']

        result = {
            'biography': data_json['biography'],
            'external_url': data_json['external_url'],
            'followers_count': data_json['edge_followed_by'],
            'following_count': data_json['edge_follow'],
            'full_name': data_json['full_name'],
            'is_private': data_json['is_private'],
            'username': data_json['username'],
            'total_posts': data_json['edge_owner_to_timeline_media']['count']
        }
        return result
    return None
