import os
import sys
import json
from datetime import datetime
import re

LIST_PATH = "list.json"

def load_list():
    if os.path.exists(LIST_PATH):
        with open(LIST_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_list(data):
    data.sort(key=lambda x: x[1], reverse=True)
    with open(LIST_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def extract_info(filename):
    print(f"[DEBUG] 正在解析文件名: {filename}")
    match = re.match(r"p/\[([^\]]+)\](.+\.md)", filename)
    if not match:
        print("[DEBUG] 文件名不包含标签结构，无需重命名")
        return [], filename
    tag_str, new_name = match.groups()
    tags = [t.strip() for t in tag_str.split(",")]
    new_path = os.path.join("p", new_name)
    print(f"[DEBUG] 提取到标签: {tags}")
    print(f"[DEBUG] 新文件路径应为: {new_path}")
    return tags, new_path

def update_list(entry_list, filepath, tags):
    today = datetime.now().strftime("%Y-%m-%d")
    for entry in entry_list:
        if entry[0] == filepath:
            print(f"[DEBUG] 文件已存在 list.json 中，更新日期和标签: {filepath}")
            entry[1] = today
            entry[2] = list(set(entry[2] + tags))
            return
    print(f"[DEBUG] 新增文件记录到 list.json: {filepath}")
    entry_list.append([filepath, today, tags])

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 update_list.py <filepath>")
        return

    original_path = sys.argv[1]
    print(f"[DEBUG] 接收到参数: {original_path}")

    tags, new_path = extract_info(original_path)

    if original_path != new_path:
        if not os.path.exists(original_path):
            print(f"❌ 文件不存在: {original_path}")
            return
        os.rename(original_path, new_path)
        print(f"✅ 文件已重命名: {original_path} -> {new_path}")
    else:
        print(f"📎 文件名无需修改: {original_path}")

    data = load_list()
    update_list(data, new_path, tags)
    save_list(data)
    print(f"✅ list.json 更新完成，对象数: {len(data)}")

if __name__ == "__main__":
    main()
