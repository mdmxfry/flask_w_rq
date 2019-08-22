#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import os
import time

from flask import Flask
from celery import Celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://redis:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://redis:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@app.route('/')
def hello_world():
    task = load.delay('test')
    return 'Started task'


@celery.task
def load(arg1):
    time.sleep(10)
    return arg1