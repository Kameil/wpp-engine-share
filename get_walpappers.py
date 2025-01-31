import os
import json


def get_walpappers():
    walpapper_dir = "C:/Program Files (x86)/Steam/steamapps/workshop/content/431960/"
    walpparers = {}
    walpprs = [walpp for walpp in os.listdir(walpapper_dir) if "." not in walpp]
    for walppr_id in walpprs:
        with open(f"{walpapper_dir}{walppr_id}/project.json", "r", encoding="utf-8") as file:
            project = json.loads(file.read())
            if str(walppr_id) not in walpparers:
                walpparers[str(walppr_id)] = {}
            walpparers[str(walppr_id)]["preview"] = project["preview"]
            walpparers[str(walppr_id)]["title"] = project["title"]
    return walpparers

if __name__ == "__main__":
    walprs = get_walpappers()
    print(walprs)
