import sys, os, json, codecs
from datetime import datetime

def merge_file(src, dst):
    """追加 src 文件内容到 dst 文件"""
    print(f"📎 Merging content from {src} to {dst}")
    with open(src, 'r', encoding='utf-8') as fsrc, open(dst, 'a', encoding='utf-8') as fdst:
        fdst.write(fsrc.read())

# 解析参数（路径）
raw_path = sys.argv[1].strip().strip('"')

# 解码 GitHub Actions 传入的可能带转义符的路径
if '\\' in raw_path:
    try:
        corrected_path = codecs.decode(raw_path.encode('latin1'), 'unicode_escape').encode('latin1').decode('utf-8')
        filepath = corrected_path
        print(f"✅ 修正路径: {filepath}")
    except Exception as e:
        print(f"❌ 路径解码失败: {e}")
        filepath = raw_path
else:
    filepath = raw_path

print(f"🔍 最终处理文件路径: {filepath}")

# ⛔ 仅处理 p/*.md 文件
if not (filepath.startswith('p/') and filepath.endswith('.md')):
    print(f"⏭️ 文件不符合处理条件（需以 p/ 开头，.md 结尾）: {filepath}")
    sys.exit(0)

# 加载 list.json
with open('list.json', 'r+', encoding='utf-8') as f:
    try:
        data = json.load(f)
        print(f"📖 已载入 list.json，共 {len(data)} 项")
    except json.JSONDecodeError:
        print("⚠️ list.json 内容无效或为空，初始化为空列表")
        data = []

    b = os.path.basename(filepath)
    parts = b.split(']')
    now = datetime.now().strftime('%Y-%m-%d')

    if len(parts) == 1:
        # 无标签格式
        filename = b
        print(f"📄 未包含标签的文件: {filename}")
        found = False
        for item in data:
            if item["1"] == filename:
                item["2"] = now
                found = True
                break
        if not found:
            data.append({"1": filename, "2": now, "3": []})
        merge_file(filepath, filename)
    else:
        # 有标签
        tag_str = parts[0].lstrip('[')
        tags = [t.strip() for t in tag_str.replace(',', ' ').replace(';', ' ').split()]
        filename = parts[1]
        print(f"🏷️ 提取标签: {tags}, 文件名: {filename}")

        for item in data:
            if item["1"] == filename:
                item["2"] = now
                item["3"] = sorted(set(item["3"] + tags))
                break
        else:
            data.append({"1": filename, "2": now, "3": tags})

        merge_file(filepath, filename)

        # 移动文件以清理命名空间
        new_path = os.path.join('p', filename)
        print(f"🚚 重命名 {filepath} → {new_path}")
        os.rename(filepath, new_path)

    # 保存 list.json
    f.seek(0)
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.truncate()
    print("✅ list.json 更新完毕")
