import requests

def process(text):
    response = requests.post('http://host.docker.internal:8080/named_entity_recognition/', json=text)
    return response.json()