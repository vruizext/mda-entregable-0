FROM python:3.9
RUN mkdir home/bart && mkdir home/bart/app
COPY app home/bart/app
WORKDIR "home/bart/app"
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]