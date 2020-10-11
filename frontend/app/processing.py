import requests

def process(text):
    response = requests.post('http://ner-backend.heychef.net:8080/named_entity_recognition/', json=text)
    return response.json()