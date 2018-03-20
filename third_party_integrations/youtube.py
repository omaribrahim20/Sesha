import requests
import json


json_data = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCZtH-W0pLbkTI0q0JEctWHg&maxResults=50&type=video&fields=items%2Fid&key=AIzaSyD4GLthTOLHHaoTKHOLp2hsxrDqo0SCTZA')

data = json.loads(json_data.text)

for n in range(len(data['items'])):
    for k, v in data.items():
            value = v[n]['id']['videoId']
            url = 'https://www.youtube.com/watch?v=' + value
            print(url)



















# #api key = 'AIzaSyD4GLthTOLHHaoTKHOLp2hsxrDqo0SCTZA