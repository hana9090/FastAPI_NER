from pydantic import BaseModel, Field
from fastapi import FastAPI, Query, Path
# Import your ML/DL model
from nlp_model import check_name_entity_recognition

app = FastAPI()

class Text(BaseModel):
    text:str

#API to call NER model
@app.post('/named_entity_recognition/')
async def check_ner(text:Text):
    '''
    - Send your string
    - asdfasdfsadf
    '''
    out = await check_name_entity_recognition(text.text)
    return out

@app.get("/")
def read_root():
    return {"Hello": "World"}
