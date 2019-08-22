FROM python:3.7

ADD ./app/ /src/app/
RUN pip3 install -r requirements.txt
WORKDIR /src/app/

CMD gunicorn -w 4 -b 127.0.0.1:5000 wsgi:app