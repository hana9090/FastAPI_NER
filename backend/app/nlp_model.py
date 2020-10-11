import spacy
import en_core_web_sm
from pydantic import BaseModel

#Class represent the returned structure from ner 
class Structure_Ner(BaseModel):
    word:str
    entity:str
    entity_loc:str

#explanation on the returned location of the entity
entity_loc_dict = {'B': 'BEGIN (first token in multi-token entity)', 'I': 'INNER (inner token of a multi-token entity)', 'L': 'LAST token multi-token entity', 'U': 'uint (single token entity)', 'O': 'Out entity token'}

#explanation on the names of entities
entity_dict = {
    'PERSON':'PERSON',
    'NORP': 'Nationalities or religious or political groups.',
    'FAC': 'Buildings, airports, highways, bridges, etc.',
    'ORG':	'Companies, agencies, institutions, etc.',
    'GPE':	'Countries, cities, states.',
    'LOC':	'Non-GPE locations, mountain ranges, bodies of water.',
    'PRODUCT':	'Objects, vehicles, foods, etc. (Not services.)',
    'EVENT':	'Named hurricanes, battles, wars, sports events, etc.',
    'WORK_OF_ART':	'Titles of books, songs, etc.',
    'LAW':	'Named documents made into laws.',
    'LANGUAGE':	'Any named language.',
    'DATE':	'Absolute or relative dates or periods.',
    'TIME':	'Times smaller than a day.',
    'PERCENT':	'Percentage, including ”%“.',
    'MONEY':	'Monetary values, including unit.',
    'QUANTITY':	'Measurements, as of weight or distance.',
    'ORDINAL':	'“first”, “second”, etc.',
    'CARDINAL':	'Numerals that do not fall under another type.'
}


async def check_name_entity_recognition(text):
    '''
    Recognize name entity in the text
    Args:
        text (string): input text
    Return:
        list of Structure_Ner objects, each object contains (word, entity, entity_location)
    '''
    nlp = en_core_web_sm.load()
    doc = nlp(text)
    
    ner = [Structure_Ner(word= str(X), entity_loc= entity_loc_dict[str(X.ent_iob_)], entity= entity_dict[str(X.ent_type_)]) for X in doc if X.ent_type_]

    return ner

