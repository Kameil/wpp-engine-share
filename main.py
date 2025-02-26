from flask import Flask
from flask import jsonify
from flask import send_file
import os
import json
import zipfile
import io
import subprocess
app = Flask(__name__)

walpapers_dir = "C:/Program Files (x86)/Steam/steamapps/workshop/content/431960/"





@app.route('/')
def home():
    with open("index.html", "r", encoding="utf-8") as file:
        return file.read()
@app.route('/script.js')
def script():
    with open("script.js", "r") as file:
        return send_file("script.js")
@app.route('/style.css')
def style():
    with open("style.css", "r") as file:
        return send_file("style.css")





from get_walpappers import get_walpappers

@app.route("/get_walpapers")
def getwalpp():
    return jsonify(get_walpappers())

from get_pastezip import zip_folder_in_memory

@app.route("/download_walpaper/<walpaper_id>/<filename>")
def dowwappp(walpaper_id, filename):
    folder_path = f"{walpapers_dir}{walpaper_id}"
    zip_buffer = zip_folder_in_memory(folder_path)
    return send_file(zip_buffer, as_attachment=True, download_name=f'{filename}.zip', mimetype='application/zip')
#getpreview    

@app.route("/preview/<walpaper_id>/<preview_file>")
def getpreview(walpaper_id, preview_file):
    return send_file(f"{walpapers_dir}{walpaper_id}/{preview_file}")


if __name__ == '__main__':
    process = subprocess.Popen(["C:/Users/Micro/devtunnel.exe", "host", "wpp-eng.brs", "--allow-anonymous"])
    app.run(debug=True, host="0.0.0.0", port="5000")