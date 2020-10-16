FROM tiangolo/uvicorn-gunicorn:python3.8
RUN python -m pip install --upgrade pip

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN python -m spacy download en

COPY ./app /app

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
