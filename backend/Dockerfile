FROM tiangolo/uvicorn-gunicorn:python3.8
RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN python -m spacy download en

COPY ./app /app
RUN pip install --no-cache-dir fastapi