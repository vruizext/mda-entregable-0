FROM python:3.9
RUN mkdir /app && mkdir /app/general && mkdir app/lisa && mkdir app/homer
COPY app /app
WORKDIR "/app"
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]