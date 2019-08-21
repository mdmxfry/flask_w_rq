FROM python:3.7

ADD ./app/ /src/app/
WORKDIR /app
RUN pip3 install -r requirements.txt

CMD python app.py