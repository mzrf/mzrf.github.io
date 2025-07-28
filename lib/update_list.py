import os
import json
from datetime import datetime

def update_file_list_and_clean_filename_for_github_actions():
    p_dir = 'p'
    list_json_path = 'list.json'

    # Ensure the 'p' directory exists
    if not os.path.isdir(p_dir):
        print(f"Error: Directory '{p_dir}' not found. Please create it.")
        # In GitHub Actions, exiting here might fail the job, which is often desired.
        return

    # Get all .md filenames in p/ (these are the original filenames)
    original_md_filenames = {f for f in os.listdir(p_dir) if f.endswith('.md')}

    # Get current timestamp for new files
    timestamp = datetime.now().strftime('%Y-%m-%d')

    # Read existing list.json or initialize an empty list
    file_list_from_json = []
    if os.path.exists(list_json_path):
        try:
            with open(list_json_path, 'r', encoding='utf-8') as f:
                file_list_from_json = json.load(f)
        except json.JSONDecodeError:
            print(f"Warning: '{list_json_path}' is malformed. Initializing with empty list.")
            file_list_from_json = []
        except FileNotFoundError:
            # This should ideally not happen if os.path.exists is true, but good practice.
            print(f"Warning: '{list_json_path}' not found, creating a new one.")
            file_list_from_json = []
    
    # Convert existing file list to a dictionary for easy lookup by the *cleaned* filename.
    # This is crucial for checking for duplicates based on the cleaned filename.
    existing_file_map = {}
    for item in file_list_from_json:
        if isinstance(item, dict) and "1" in item:
            existing_file_map[item["1"]] = item

    final_file_list = []

    # Iterate through current original .md filenames from the 'p' directory
    for original_filename in original_md_filenames:
        
        # Initialize tags and a cleaned filename
        tags = []
        # Default cleaned_filename to original, in case no backtick is found.
        cleaned_filename = original_filename 

        # Extract tags and modify filename
        first_backtick_index = original_filename.find('`')
        if first_backtick_index != -1:
            second_backtick_index = original_filename.find('`', first_backtick_index + 1)
            
            if second_backtick_index != -1:
                # Extract the tag string between backticks
                tag_string = original_filename[first_backtick_index + 1 : second_backtick_index]
                # Split tag string by comma or space into a list of tags
                tags = [t.strip() for t in tag_string.replace(',', ' ').split() if t.strip()]
                
                # --- CORE CHANGE FOR FILENAME CLEANING ---
                # Clean the filename by taking only the part BEFORE the first backtick.
                # This removes `content` and everything after it.
                cleaned_filename = original_filename[:first_backtick_index]
                # --- END CORE CHANGE ---
                
                if not tags: # Ensure tags is an empty list if no valid tags were extracted
                    tags = []
            else:
                # Case: only one backtick found, meaning it's unmatched.
                # As per requirement, treat it as no tags extracted and no cleaning done.
                pass 
        
        # --- DUPLICATE CHECK AND ITEM CREATION ---
        # Create a new item dictionary for the final list
        new_item = {}
        new_item["1"] = cleaned_filename # Store the thoroughly cleaned filename
        new_item["3"] = tags # Store the extracted tags

        if cleaned_filename in existing_file_map:
            # If the cleaned file already exists in our map:
            # 1. Update its tags.
            # 2. Preserve its original creation date.
            existing_item = existing_file_map[cleaned_filename]
            new_item["2"] = existing_item.get("2", timestamp) # Preserve old date, or use current if missing
            
            # Remove from map to track deleted files from original list.
            del existing_file_map[cleaned_filename]
        else:
            # If it's a new (cleaned) file not previously in list.json, add current timestamp.
            new_item["2"] = timestamp
        
        final_file_list.append(new_item)
    
    # Sort the final list for consistent output (optional)
    # Sorting by filename (value of key "1")
    final_file_list.sort(key=lambda x: x.get("1", ""))

    # Save back to list.json
    try:
        with open(list_json_path, 'w', encoding='utf-8') as f:
            # ensure_ascii=False for proper display of Chinese characters
            json.dump(final_file_list, f, indent=4, ensure_ascii=False)
        print(f"'{list_json_path}' updated successfully with thoroughly cleaned filenames.")
    except IOError as e:
        print(f"Error writing to '{list_json_path}': {e}")

if __name__ == "__main__":
    update_file_list_and_clean_filename_for_github_actions()

# import os
# import json
# from datetime import datetime

# def update_file_list():
#     # 获取 p/ 目录下的所有 .md 文件
#     files = [f for f in os.listdir('p') if f.endswith('.md')]
    
#     # 获取当前时间戳
#     timestamp = datetime.now().strftime('%Y-%m-%d')
# #  timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     # 读取现有的 list.json 文件
#     if os.path.exists('list.json'):
#         with open('list.json', 'r') as f:
#             file_list = json.load(f)
#     else:
#         file_list = []

#     # 更新文件列表
#     for file in files:
#         # 如果该文件还没有在 list.json 中，则添加
#         if not any(f[0] == file for f in file_list):
#             file_list.append([file, timestamp])

#     # 保存回 list.json
#     with open('list.json', 'w') as f:
#         json.dump(file_list, f, indent=4)

# if __name__ == "__main__":
#     update_file_list()
