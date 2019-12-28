from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello flask!!!!"

@app.route("/about")
def about():
    return "<form> <input name='Sum' type='text' /> <button name='submit'>sum method called in flask!!!!</form>"

#@app.route("/login")
#def login():
 #   return " login page in flask"

@app.route("/login")
def login():
    mydict = request.args
    return mydict['a']

if __name__ == "__main__":
    app.run(port=80)