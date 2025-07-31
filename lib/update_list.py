# lib/update_list.py
import sys, os, json, shutil
from datetime import datetime

def merge_file(src, dst):
    """追加 src 文件内容到 dst 文件"""
    with open(src, 'r', encoding='utf-8') as fsrc, open(dst, 'a', encoding='utf-8') as fdst:
        fdst.write(fsrc.read())

# 传入变更文件名，逗号分隔
files = sys.argv[1].split(',')

# 读取 list.json
with open('list.json', 'r+', encoding='utf-8') as f:
    try:
        data = json.load(f)
    except json.JSONDecodeError:
        data = []

    for filepath in files:
        if not filepath.startswith('p/'):
            continue

        b = os.path.basename(filepath)
        parts = b.split(']')
        now = datetime.now().strftime('%Y-%m-%d')

        if len(parts) == 1:
            # 无标签，直接更新日期、合并文件
            filename = b
            found = False
            for item in data:
                if item[0] == filename:
                    item[1] = now
                    found = True
                    break
            if not found:
                data.append([filename, now, []])
            merge_file(filepath, f'merged/{filename}')
        else:
            # 含标签
            tag_str = parts[0].lstrip('[')
            tags = [t.strip() for t in tag_str.replace(',', ' ').replace(';', ' ').split()]
            filename = parts[1]

            for item in data:
                if item["1"] == filename:
                    item["2"] = now
                    item["3"] = sorted(set(item[2] + tags))
                    break
            else:
                data.append([filename, now, tags])

            # 合并文件 + 重命名
            merge_file(filepath, f'merged/{filename}')
            os.rename(filepath, os.path.join('p', filename))

    f.seek(0)
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.truncate()
