FROM docker.io/python:3.10-alpine
ADD ./service.py /service.py
ADD ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ENTRYPOINT python3 /service.py
