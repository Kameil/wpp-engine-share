from flask import Flask
from flask import jsonify
from flask import send_file
import os
import json
import zipfile
import io
app = Flask(__name__)

walpapers_dir = "C:/Program Files (x86)/Steam/steamapps/workshop/content/431960/"


def zip_folder_in_memory(folder_path):
    # Cria um arquivo ZIP em memória
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Adiciona ao arquivo ZIP, preservando a estrutura de diretórios
                zipf.write(file_path, os.path.relpath(file_path, folder_path))

    zip_buffer.seek(0)  # Volta para o início do buffer para envio
    return zip_buffer


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

@app.route("/download_walpaper/<walpaper_id>")
def dowwappp(walpaper_id):
    folder_path = f"{walpapers_dir}{walpaper_id}"
    zip_buffer = zip_folder_in_memory(folder_path)
    return send_file(zip_buffer, as_attachment=True, download_name='arquivo.zip', mimetype='application/zip')
    
    

if __name__ == '__main__':
    app.run(debug=True)