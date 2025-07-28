import os
import json
from datetime import datetime
import re # Import the regular expression module

def update_file_list_simple_leading_brackets():
    p_dir = 'p'
    list_json_path = 'list.json'

    # Ensure the 'p' directory exists
    if not os.path.isdir(p_dir):
        print(f"Error: Directory '{p_dir}' not found. Please create it.")
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
            print(f"Warning: '{list_json_path}' not found, creating a new one.")
            file_list_from_json = []
    
    # Convert existing file list to a dictionary for easy lookup by the *cleaned* filename.
    existing_file_map = {}
    for item in file_list_from_json:
        if isinstance(item, dict) and "1" in item:
            existing_file_map[item["1"]] = item

    final_file_list = []

    # Iterate through current original .md filenames from the 'p' directory
    for original_filename in original_md_filenames:
        
        # Initialize tags and a cleaned filename
        tags = []
        cleaned_filename = original_filename # Default to original filename if no match

        # --- SIMPLIFIED TAG EXTRACTION AND FILENAME CLEANING ---
        # Pattern: ^\[([^\]]+)\](.*)$
        # This will match filenames starting with `[tag]` and capture the tag and the rest of the name.
        # It assumes the `.md` extension is part of the second captured group.
        # Example: "[tag1]1.RF基础.md" -> Group 1: "tag1", Group 2: "1.RF基础.md"
        match = re.match(r'^\[([^\]]+)\](.*)$', original_filename)
        
        if match:
            extracted_tag_string = match.group(1) # e.g., "tag1"
            remaining_filename = match.group(2)   # e.g., "1.RF基础.md"
            
            # Tags processing
            tags = [t.strip() for t in extracted_tag_string.replace(',', ' ').split() if t.strip()]
            if not tags: tags = [] 

            # Cleaned filename is simply the remaining_filename
            cleaned_filename = remaining_filename
        else:
            # If the filename does NOT start with `[tag]`, then `cleaned_filename` remains
            # `original_filename`, and `tags` remains an empty list.
            pass
        # --- END SIMPLIFIED TAG EXTRACTION AND FILENAME CLEANING ---
        
        # --- DUPLICATE CHECK AND ITEM CREATION ---
        new_item = {}
        new_item["1"] = cleaned_filename 
        new_item["3"] = tags 

        if cleaned_filename in existing_file_map:
            existing_item = existing_file_map[cleaned_filename]
            new_item["2"] = existing_item.get("2", timestamp) 
            del existing_file_map[cleaned_filename]
        else:
            new_item["2"] = timestamp
        
        final_file_list.append(new_item)
    
    # Sort the final list for consistent output (optional)
    final_file_list.sort(key=lambda x: x.get("1", ""))

    # Save back to list.json
    try:
        with open(list_json_path, 'w', encoding='utf-8') as f:
            json.dump(final_file_list, f, indent=4, ensure_ascii=False)
        print(f"'{list_json_path}' updated successfully (simple leading bracket logic).")
    except IOError as e:
        print(f"Error writing to '{list_json_path}': {e}")

if __name__ == "__main__":
    update_file_list_simple_leading_brackets()
