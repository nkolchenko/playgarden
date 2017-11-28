# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
# Create your views here.

from flask import Flask
from redis import Redis
from django.http import HttpResponse

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
#def hello():
#    count = redis.incr('hits')
#    return 'Hello World od Docker! I have been seen {} times.\n'.format(count)

#if __name__ == "__main__":
#    app.run(host="0.0.0.0", debug=True)


#from django.http import HttpResponse
def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
     count = redis.incr('hits')
     return HttpResponse('Hello World od Docker! I have been seen {} times.\n'.format(count))
