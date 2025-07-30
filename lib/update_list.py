import sys
import os
import json
import shutil
import re
from datetime import datetime

def extract_tags_and_newname(filename):
    """从文件名中提取标签和新文件名"""
    match = re.match(r"^\[(.*?)\](.+)$", filename)
    if not match:
        return [], filename
    raw_tags = match.group(1)
    clean_name = match.group(2).strip()
    tags = re.split(r"[,\s;，；]+", raw_tags.strip())
    tags = [tag for tag in tags if tag]
    return tags, clean_name

def load_list(path="list.json"):
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_list(data, path="list.json"):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    if len(sys.argv) < 2:
        print("请提供上传的文件路径")
        sys.exit(1)

    uploaded_path = sys.argv[1]
    if not os.path.exists(uploaded_path):
        print(f"文件不存在: {uploaded_path}")
        sys.exit(1)

    # 提取原始文件名
    folder = os.path.dirname(uploaded_path)
    old_filename = os.path.basename(uploaded_path)
    tags, new_filename = extract_tags_and_newname(old_filename)
    new_path = os.path.join(folder, new_filename)

    # 如果新文件名不同且目标不存在，就重命名
    if old_filename != new_filename:
        if os.path.exists(new_path):
            print(f"目标文件 {new_filename} 已存在，将覆盖内容")
            shutil.copyfile(uploaded_path, new_path)
            os.remove(uploaded_path)
        else:
            os.rename(uploaded_path, new_path)

    # 处理 list.json
    data = load_list()
    today = datetime.today().strftime('%Y-%m-%d')

    updated = False
    for item in data:
        if item[0] == new_filename:
            item[1] = today  # 更新日期
            item_tags = set(item[2:] if len(item) > 2 else [])
            item_tags.update(tags)
            item[:] = [new_filename, today] + sorted(item_tags)
            updated = True
            break

    if not updated:
        data.append([new_filename, today] + sorted(set(tags)))

    save_list(data)
    print(f"处理完成: {new_filename}")

if __name__ == "__main__":
    main()
