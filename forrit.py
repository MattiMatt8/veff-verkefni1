from bottle import *

@route('/')
def index():
    return '<a href="about">About</a> <a href="bio">Biography</a> <a href="pic">Pictures</a>'
@route('/about')
def index():
    return "Upplýsingar um Bill Gates"
@route('/bio')
def index():
    return "Biography frá Bill Gates"
@route('/pic')
def index():
    return "Myndir af Bill Gates"

run(host="127.0.0.1", port=8080)
