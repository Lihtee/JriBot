FROM python:3.9

ADD bot2.py .
ADD config.py .
ADD requirements.txt .

RUN pip install -r ./requirements.txt

CMD ["python", "./bot2.py"]
