from flask import Flask, jsonify, send_file, Response
import os
import subprocess
from config import WALPAPERS_DIR
from get_walpappers import get_walpappers
from get_pastezip import zip_folder_stream

app = Flask(__name__)
walpapers_dir = WALPAPERS_DIR

def serve_static(file_path):
    try:
        return send_file(file_path)
    except FileNotFoundError:
        return "Arquivo não encontrado", 404

@app.route('/')
def home():
    return serve_static("index.html")

@app.route('/script.js')
def script():
    return serve_static("script.js")

@app.route('/style.css')
def style():
    return serve_static("style.css")

@app.route("/get_wallpapers")
def get_wallpapers():
    return jsonify(get_walpappers())

@app.route("/download_wallpaper/<wallpaper_id>/<filename>")
def download_wallpaper(wallpaper_id, filename):
    if not wallpaper_id.isalnum() or not filename.isalnum():
        return "Parâmetros inválidos", 400
    folder_path = os.path.join(walpapers_dir, wallpaper_id)
    if not os.path.exists(folder_path):
        return "Wallpaper não encontrado", 404
    return zip_folder_stream(folder_path, filename)

@app.route("/preview/<wallpaper_id>/<preview_file>")
def get_preview(wallpaper_id, preview_file):
    file_path = os.path.join(walpapers_dir, wallpaper_id, preview_file)
    if not os.path.exists(file_path):
        return "Arquivo de prévia não encontrado", 404
    return send_file(file_path)

if __name__ == '__main__':
    process = subprocess.Popen(["C:/Users/Micro/devtunnel.exe", "host", "wpp-eng.brs", "--allow-anonymous"])
    app.run(debug=True, host="0.0.0.0", port="5000")