FROM python:3.8.5-alpine

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "src/MainScores.py"]
