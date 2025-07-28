import os
import json
from datetime import datetime
import re # Import the regular expression module

def update_file_list_and_clean_filename_with_brackets():
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
        cleaned_filename = original_filename # Start with original

        # --- TAG EXTRACTION AND FILENAME CLEANING USING REGEX ---
        # Regex pattern to find [tags] in the filename, then capture the part before it.
        # It also handles .md extension potentially being before the tags.
        match = re.search(r'^(.*?)(?:\[([^\]]+)\])?(.*?)(\.md)$', original_filename)
        
        if match:
            # Group 1: Part before [tags]
            # Group 2: The tags content inside []
            # Group 3: Part after [tags] but before .md (if any)
            # Group 4: The .md extension
            
            base_name_before_tags = match.group(1)
            extracted_tag_string = match.group(2)
            # part_after_tags_before_md = match.group(3) # Not used for cleaned filename or tags
            
            # Construct cleaned_filename: part before tags + .md extension
            # This ensures "my_file[tag]suffix.md" becomes "my_file.md"
            cleaned_filename = base_name_before_tags + ".md"

            if extracted_tag_string:
                # Split tag string by comma or space into a list of tags
                tags = [t.strip() for t in extracted_tag_string.replace(',', ' ').split() if t.strip()]
            
            if not tags: # Ensure tags is an empty list if no valid tags were extracted
                tags = []
        else:
            # If no match (e.g., no [tags] found or not a .md file structure as expected)
            # Then the filename remains original, and tags remain empty.
            pass # cleaned_filename remains original_filename, tags remain empty list.
        # --- END TAG EXTRACTION AND FILENAME CLEANING ---
        
        # --- DUPLICATE CHECK AND ITEM CREATION ---
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
    final_file_list.sort(key=lambda x: x.get("1", ""))

    # Save back to list.json
    try:
        with open(list_json_path, 'w', encoding='utf-8') as f:
            json.dump(final_file_list, f, indent=4, ensure_ascii=False)
        print(f"'{list_json_path}' updated successfully with cleaned filenames using brackets.")
    except IOError as e:
        print(f"Error writing to '{list_json_path}': {e}")

if __name__ == "__main__":
    update_file_list_and_clean_filename_with_brackets()
