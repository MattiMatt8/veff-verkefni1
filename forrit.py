from bottle import *
import os

@route('/')
def index():
    return '<a href="about">About</a> <a href="bio">Biography</a> <a href="pic">Pictures</a>'
@route('/about')
def about():
    return "Upplýsingar um Bill Gates"
@route('/bio')
def bio():
    return "Biography frá Bill Gates"
@route('/pic')
def pic():
    return "Myndir af Bill Gates"

run(host="0.0.0.0", port=os.environ.get('PORT'))
#run(host="localhost", port=8080)
