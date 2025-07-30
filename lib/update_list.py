import os
import sys
import json
from datetime import datetime

def extract_tags_and_newname(filename):
    if ']' in filename and filename.startswith('['):
        tag_part, new_name = filename.split(']', 1)
        tags = [t.strip() for t in re.split(r'[;, ]+', tag_part[1:]) if t.strip()]
        return tags, new_name.strip()
    else:
        return [], filename

def load_list(path):
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_list(data, path):
    # 按时间倒序排序
    data.sort(key=lambda x: x["2"], reverse=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def update_entry(entries, filename, tags):
    today = datetime.today().strftime('%Y-%m-%d')
    for entry in entries:
        if entry["1"] == filename:
            entry["2"] = today
            entry["3"] = list(set(entry["3"] + tags))
            return
    entries.append({"1": filename, "2": today, "3": tags})

def main():
    import re
    if len(sys.argv) < 2:
        print("Usage: python update_list.py <filename>")
        return

    original_path = sys.argv[1]
    original_name = os.path.basename(original_path)
    folder = os.path.dirname(original_path)

    tags, new_name = extract_tags_and_newname(original_name)
    new_path = os.path.join(folder, new_name)

    if new_name != original_name:
        os.rename(original_path, new_path)
        print(f"Renamed: {original_name} → {new_name}")
    else:
        new_path = original_path

    entries = load_list('list.json')
    update_entry(entries, new_name, tags)
    save_list(entries, 'list.json')

if __name__ == '__main__':
    main()
