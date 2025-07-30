import os
import json
import re
from datetime import datetime

def update_list_json_by_new_files():
    p_dir = 'p'
    list_json_path = 'list.json'

    if not os.path.isdir(p_dir):
        print(f"❌ Error: Directory '{p_dir}' not found.")
        return

    files_in_p = [f for f in os.listdir(p_dir) if f.endswith('.md') and not f.startswith('.')]

    # 获取当前日期
    current_date = datetime.now().strftime('%Y-%m-%d')

    # 加载原始 list.json 数据
    existing_file_list = []
    if os.path.exists(list_json_path):
        try:
            with open(list_json_path, 'r', encoding='utf-8') as f:
                existing_file_list = json.load(f)
        except Exception as e:
            print(f"⚠️ 读取 list.json 出错：{e}")
            existing_file_list = []

    # 构建 filename => item 映射
    file_map = {item["1"]: item for item in existing_file_list if isinstance(item, dict) and "1" in item}

    for original_filename in files_in_p:
        # --- 提取标签和清理后的文件名 ---
        tag_match = re.match(r'^\[([^\]]+)\](.*)$', original_filename)
        if tag_match:
            tag_str = tag_match.group(1).strip()
            cleaned_filename = tag_match.group(2).strip()
            tags = [tag.strip() for tag in re.split(r'\s+', tag_str) if tag.strip()]
        else:
            cleaned_filename = original_filename
            tags = []

        # 获取文件修改时间作为更新日期
        try:
            mod_timestamp = os.path.getmtime(os.path.join(p_dir, original_filename))
            file_date = datetime.fromtimestamp(mod_timestamp).strftime('%Y-%m-%d')
        except OSError:
            file_date = current_date

        if cleaned_filename in file_map:
            # 修改旧文件记录：更新日期，合并标签（去重）
            existing_tags = set(file_map[cleaned_filename].get("3", []))
            updated_tags = list(existing_tags.union(tags))
            file_map[cleaned_filename]["2"] = file_date
            file_map[cleaned_filename]["3"] = updated_tags
            print(f"📝 修改文件: {cleaned_filename} → 更新日期，合并标签")
        else:
            # 新文件，添加新记录
            file_map[cleaned_filename] = {
                "1": cleaned_filename,
                "2": file_date,
                "3": tags
            }
            print(f"➕ 新增文件: {cleaned_filename}")

    # 转为列表并按文件名排序
    final_list = list(file_map.values())
    final_list.sort(key=lambda x: x.get("1", ""))

    # 保存更新后的 list.json
    try:
        with open(list_json_path, 'w', encoding='utf-8') as f:
            json.dump(final_list, f, indent=4, ensure_ascii=False)
        print(f"✅ '{list_json_path}' 已更新完毕")
    except Exception as e:
        print(f"❌ 写入失败: {e}")

if __name__ == "__main__":
    update_list_json_by_new_files()
