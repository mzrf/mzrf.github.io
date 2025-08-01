import sys, os, json
import codecs
from datetime import datetime

def merge_file(src, dst):
    """追加 src 文件内容到 dst 文件"""
    print(f"📎 Merging content from {src} to {dst}")
    with open(src, 'r', encoding='utf-8') as fsrc, open(dst, 'a', encoding='utf-8') as fdst:
        fdst.write(fsrc.read())

# 传入变更文件名，逗号分隔
raw_path = sys.argv[1].strip().strip('"')

# 如果路径中包含类似 \347 这种字节转义，说明需要转码
if '\\' in raw_path:
    try:
        # 将字节形式的字符串转为真正的 UTF-8 中文路径
        corrected_path = codecs.decode(raw_path.encode('latin1'), 'unicode_escape').encode('latin1').decode('utf-8')
        print(f"✅ 修正路径: {corrected_path}")
        files = corrected_path
    except Exception as e:
        print(f"❌ 路径解码失败: {e}")
        files = raw_path  # 回退
else:
    file_path = raw_path

# ✅ 可读日志输出
print(f"🔍 最终处理文件路径: {files}")

# 读取 list.json
with open('list.json', 'r+', encoding='utf-8') as f:
    try:
        data = json.load(f)
        print(f"📖 Loaded list.json with {len(data)} entries")
    except json.JSONDecodeError:
        print("⚠️ list.json is empty or invalid, starting with empty list")
        data = []

    for filepath in files:
        print(f"🔍 Processing file: {filepath}")
        if not filepath.startswith('p/'):
            print(f"⏭️ Skipped non-target file: {filepath}")
            continue

        b = os.path.basename(filepath)
        parts = b.split(']')
        now = datetime.now().strftime('%Y-%m-%d')

        if len(parts) == 1:
            # 无标签，直接更新日期、合并文件
            filename = b
            print(f"📄 Detected untagged file: {filename}")
            found = False
            for item in data:
                if item["1"] == filename:
                    print(f"✅ Updating existing file date: {filename}")
                    item["2"] = now
                    found = True
                    break
            if not found:
                print(f"➕ Adding new untagged file: {filename}")
                data.append({"1": filename, "2": now, "3": []})
            merge_file(filepath, filename)
        else:
            # 含标签
            tag_str = parts[0].lstrip('[')
            tags = [t.strip() for t in tag_str.replace(',', ' ').replace(';', ' ').split()]
            filename = parts[1]
            print(f"🏷️ Tags: {tags}, Filename: {filename}")

            for item in data:
                if item["1"] == filename:
                    print(f"📝 Updating tagged file: {filename}")
                    item["2"] = now
                    item["3"] = sorted(set(item["3"] + tags))
                    break
            else:
                print(f"➕ Adding new tagged file: {filename}")
                data.append({"1": filename, "2": now, "3": tags})

            merge_file(filepath, filename)
            new_path = os.path.join('p', filename)
            print(f"🚚 Renaming {filepath} → {new_path}")
            os.rename(filepath, new_path)

    f.seek(0)
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.truncate()
    print("✅ list.json updated")
