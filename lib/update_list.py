import sys
import os
import json
import re
from datetime import datetime

uploaded_path = sys.argv[1]
folder, filename = os.path.split(uploaded_path)

if "]" in filename:
    tag_part, new_filename = filename.split("]", 1)
    tags = [tag.strip() for tag in re.split(r"[ ,;]+", tag_part.strip("["))]
    new_path = os.path.join(folder, new_filename)
    os.replace(uploaded_path, new_path)
else:
    new_filename = filename
    tags = []
    new_path = uploaded_path

date_str = datetime.now().strftime("%Y-%m-%d")

list_path = "list.json"
data = []
if os.path.exists(list_path):
    with open(list_path, "r", encoding="utf-8") as f:
        data = json.load(f)

found = False
for item in data:
    if item["1"] == new_filename:
        item["2"] = date_str
        if tags:
            item["3"] = sorted(list(set(item.get("3", []) + tags)))
        found = True
        break

if not found:
    data.append({
        "1": new_filename,
        "2": date_str,
        "3": tags
    })

# ✅ 按日期升序排序（最新在后）
data.sort(key=lambda x: x["2"])

with open(list_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
