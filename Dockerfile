from python:slim-bookworm 

COPY ./src ./app
WORKDIR ./app
RUN pip install -r ./requirements.txt --no-cache-dir

ENTRYPOINT ["python", "./main.py"]
