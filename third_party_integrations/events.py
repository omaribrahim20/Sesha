import urllib3, facebook, requests


# token = "EAACOb2qk4m8BAJeSIGReeZAn18Ti8ka09ttpUqpfbpGQ7RMAcjw7sojzdlr0yOMVSNu7mwVM024KYZArquVbxjmuyAL9SprZA3aUtcZAZBJ9rosPlgNpC9Kuy7CoDJWasrPoVEsq4PFTBprG4OvZAa1xOFpa0aEJgjB8n1LugxSVAPJoBZBSiSh3dABGSxK5qNVUTgjBZBmVUiRyNhnRW6V6page_id:422630314545023"

token = '807270556132033|o9cdClVOGwyeNHk6cX_tKs7uuI0'

graph = facebook.GraphAPI(access_token=token, version=2.7)
events = graph.request('/422630314545023/events')
print(events)

