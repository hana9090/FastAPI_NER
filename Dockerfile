FROM tiangolo/uvicorn-gunicorn:python3.8
RUN python -m pip install --upgrade pip
RUN pip install python-multipart

RUN pip install -U spacy
RUN python -m spacy download en 

COPY ./app /app
RUN pip install --no-cache-dir fastapi