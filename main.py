from flask import Flask
from flask import jsonify
from flask import send_file
import os
import json
import zipfile
import io
app = Flask(__name__)

walpapers_dir = "C:/Program Files (x86)/Steam/steamapps/workshop/content/431960/"





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





from get_walpappers import get_walpappers

@app.route("/get_walpapers")
def getwalpp():
    return jsonify(get_walpappers())

from get_pastezip import zip_folder_in_memory

@app.route("/download_walpaper/<walpaper_id>")
def dowwappp(walpaper_id):
    folder_path = f"{walpapers_dir}{walpaper_id}"
    zip_buffer = zip_folder_in_memory(folder_path)
    return send_file(zip_buffer, as_attachment=True, download_name='arquivo.zip', mimetype='application/zip')
#getpreview    

@app.route("/preview/<walpaper_id>/<preview_file>")
def getpreview(walpaper_id, preview_file):
    return send_file(f"{walpapers_dir}{walpaper_id}/{preview_file}")


if __name__ == '__main__':
    app.run(debug=True)