import os
import sys
import json
from datetime import datetime
import re

def load_list(path='list.json'):
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data if isinstance(data, list) else [data]

def save_list(data, path='list.json'):
    # 按日期降序排序（字段 "2"）
    data.sort(key=lambda x: x.get("2", ""), reverse=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def extract_tag_and_filename(basename):
    match = re.match(r'^\[(.*?)\](.+\.md)$', basename)
    if match:
        tag = match.group(1).strip()
        filename = match.group(2).strip()
        return tag, filename
    else:
        return None, basename

def process(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    dir_name, basename = os.path.split(file_path)
    tag, new_name = extract_tag_and_filename(basename)
    current_date = datetime.today().strftime('%Y-%m-%d')

    list_data = load_list()

    # Check if renaming needed
    if tag:
        new_path = os.path.join(dir_name, new_name)
        os.rename(file_path, new_path)
        file_path = new_path
        basename = new_name
        print(f"🔁 Renamed to: {basename}")

    found = False
    for item in list_data:
        if item["1"] == basename:
            found = True
            item["2"] = current_date
            if tag and tag not in item["3"]:
                item["3"].append(tag)
            print(f"✅ Updated existing entry: {basename}")
            break

    if not found:
        entry = {
            "1": basename,
            "2": current_date,
            "3": [tag] if tag else []
        }
        list_data.append(entry)
        print(f"➕ Added new entry: {basename}")

    save_list(list_data)
    print(f"💾 list.json updated and sorted.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python update_list.py <path/to/file.md>")
        sys.exit(1)
    process(sys.argv[1])
