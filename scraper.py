from requests import get
from bs4 import BeautifulSoup as BS
from json import loads


url = 'https://instagram.com'
def scrape_data(username):
    resp = get(f'{url}/{username}')
    if resp.status_code == 200:
        soup = BS(resp.text, 'html.parser')
        script_tags = soup.find_all('script')
        data_script = script_tags[4]
        data_json = loads(data_script.contents[0][21:-1])
        user_data = data_json['entry_data']['ProfilePage'][0]['graphql']['user']
        result = {
            'biography': user_data['biography'],
            'external_url': user_data['external_url'],
            'followers_count': user_data['edge_followed_by'],
            'following_count': user_data['edge_follow'],
            'full_name': user_data['full_name'],
            'is_private': user_data['is_private'],
            'username': user_data['username'],
            'total_posts': user_data['edge_owner_to_timeline_media']['count']
        }
        
        return result

    return None

