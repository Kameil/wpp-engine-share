import os
import json
from config import WALPAPERS_DIR

# Cache global
wallpapers_cache = None

def get_walpappers():
    global wallpapers_cache
    if wallpapers_cache is None:
        wallpapers_cache = {}
        walpprs = [walpp for walpp in os.listdir(WALPAPERS_DIR) if "." not in walpp]
        for wallpaper_id in walpprs:
            try:
                with open(f"{WALPAPERS_DIR}{wallpaper_id}/project.json", "r", encoding="utf-8") as file:
                    project = json.load(file)
                    wallpapers_cache[wallpaper_id] = {
                        "preview": project.get("preview", ""),
                        "title": project.get("title", ""),
                        "description": project.get("description", ""),
                        "type": project.get("type", ""),
                        "tags": project.get("tags", [])
                    }
            except FileNotFoundError:
                print(f"Arquivo project.json não encontrado para {wallpaper_id}")
            except json.JSONDecodeError:
                print(f"Erro ao decodificar JSON para {wallpaper_id}")
    return wallpapers_cache