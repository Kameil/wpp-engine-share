import zipfile
import os
import io
from flask import Response

def zip_folder_stream(folder_path, filename):
    def generate():
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, folder_path))
        zip_buffer.seek(0)
        yield from zip_buffer
    return Response(generate(), mimetype='application/zip', headers={"Content-Disposition": f"attachment; filename={filename}.zip"})