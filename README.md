## Deploy Named Entity Recognition using FastAPI

* My goal to deploy any ML/DL model using FastAPI and prepare a Docker to containerized the API.

![](https://github.com/hana9090/FastAPI_NER/blob/main/resources/template.jpg?raw=true)

## Named Entity Recognition


Named entity recognition (NER) is one of the key information extraction tasks, which is able to identify the key elements in a text, like names of people, places, brands and more. Extracting entities from text helps in detecting the import information from unstractured data as an information extraction task.

![img](https://miro.medium.com/max/1000/1*0BuSAIQOLNQGVWJIxZhFuA.png)

 [image source](https://mc.ai/everything-you-need-to-know-about-named-entity-recognition/)




### Spacy
spaCy is a free open-source library for Natural Language Processing in Python. It provides multiple NLP sevices such as NER, POS tagging, word vectors and more. 

## FastAPI
FastAPI is a python web framework for building APIs and it features as a fast framework.
![img](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

## Docker
Docker is a tool helps developers to easily deploy and run their applications using container. Container helps in packaging the application with all dependencies of libraries to get it running. 
![im](https://www.docker.com/sites/default/files/d8/styles/role_icon/public/2019-07/Docker-Logo-White-RGB_Horizontal.png?itok=cFIHFZiP)


## How to run the app?

### Local
* cd inside the app directory and run the unicorn server
`cd app`
`uvicorn main:app --reload`

* Go to FastAPI Swagger UI http://127.0.0.1:8000/docs to access your API

![im](https://github.com/hana9090/FastAPI_NER/blob/main/resources/image1.png?raw=true)

![im](https://github.com/hana9090/FastAPI_NER/blob/main/resources/image2.png?raw=true)

### Docker

* Cd into the project directory
* Build the docker file to create the image
`docker build -t fastapi_ner_image .`
* Create and run the container
`docker run -dit --name fastapi_ner_container  -p 80:80 fastapi_ner_image`

* Now visit the new url for the API from the running container
* * You can find it by listing the running containers with their information, such as port:
`docker container ls -a `

| CONTAINER ID         | IMAGE           | PORTS  | NAMES  |
| -------------------- |:---------------:| ------:|--------------:|
| ccf287c57675    | right-fastapi_ner_image |0.0.0.0:80->80/tcp | fastapi_ner_container|

* In my case it is  http://0.0.0.0:80/docs Go there and test the API 


## Teaser video

[video](https://dms.licdn.com/playlist/C4D05AQG9jTvvDumKVg/mp4-720p-30fp-crf28/0?e=1602428400&v=beta&t=iLBzvbhCP67q9bLYY5T_MtCtkyijiyRoS84ZbLrJ-ws)

