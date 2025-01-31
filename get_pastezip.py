import zipfile
import io
import os

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


# Powered By chatgpt4o