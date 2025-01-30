from flask import Flask
from flask import jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    with open("index.html", "r") as file:
        return file.read()
@app.route('/script.js')
def script():
    with open("script.js", "r") as file:
        return file.read()
@app.route('/style.css')
def style():
    with open("style.css", "r") as file:
        return file.read()

@app.route("/get_walpapers")
def getwalpp():
    walpprs = os.listdir("C:/Program Files (x86)/Steam/steamapps/workshop/content/431960/")
    for walpp in walpprs:
        
    

if __name__ == '__main__':
    app.run(debug=True)