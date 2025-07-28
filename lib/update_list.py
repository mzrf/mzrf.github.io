import os 
import json 
from datetime import datetime 
import re # Import the regex module

def update_file_list_with_regex_for_tags(): 
    p_dir = 'p'
    list_json_path = 'list.json'

    # Ensure the 'p' directory exists
    if not os.path.isdir(p_dir):
        print(f"Error: Directory '{p_dir}' not found. Please create it.")
        return

    # Get all .md filenames in p/
    files_in_p = {f for f in os.listdir(p_dir) if f.endswith('.md')}
    
    # Get current timestamp for new files' default date
    current_timestamp = datetime.now().strftime('%Y-%m-%d') 
    
    # Read existing list.json or initialize an empty list
    existing_file_list = []
    if os.path.exists(list_json_path): 
        try:
            with open(list_json_path, 'r', encoding='utf-8') as f: 
                existing_file_list = json.load(f) 
            if not isinstance(existing_file_list, list):
                print(f"Warning: '{list_json_path}' content is not a list. Initializing with empty list.")
                existing_file_list = []
        except json.JSONDecodeError:
            print(f"Warning: '{list_json_path}' is malformed or empty. Initializing with empty list.")
            existing_file_list = []
        except FileNotFoundError:
            pass 

    # Convert existing file list to a dictionary for quick lookup by cleaned filename
    existing_file_map = {}
    for item in existing_file_list:
        if isinstance(item, dict) and "1" in item:
            existing_file_map[item["1"]] = item

    final_file_list = []

    # Iterate through files in p/ directory
    for original_filename in files_in_p:
        cleaned_filename = original_filename
        extracted_tags = []
        file_date = current_timestamp # Default to current timestamp, will try to get modification time

        # --- TAGS EXTRACTION WITH REGEX ---
        # Match pattern: [tags_string]filename.md
        # This regex specifically captures the content INSIDE the brackets for tag processing
        tag_match = re.match(r'^\[([^\]]+)\](.*)$', original_filename)
        
        if tag_match:
            tag_string_raw = tag_match.group(1).strip() # Content inside brackets, e.g., "test1_tag test2_tag"
            cleaned_filename = tag_match.group(2).strip() # Content after brackets, e.g., "1.test.md"
            
            # Now, process the tag_string_raw using regex for more flexible splitting
            # Example: splitting by space, comma, or underscore if needed.
            # For "test1_tag test2_tag", splitting by space is still appropriate.
            # If tags could be "test1,test2", use r'[, ]+'
            # If tags could be "test1_test2", use r'[ _]+'
            # For your example "test1_tag test2_tag", splitting by spaces is fine.
            extracted_tags = [tag.strip() for tag in re.split(r'\s+', tag_string_raw) if tag.strip()]
            
            # Ensure the cleaned_filename ends with .md if it's supposed to
            if not cleaned_filename.endswith('.md'):
                # This handles cases where the regex might capture too much or too little
                # If your filenames consistently end with .md, this might not be strictly necessary
                # but it's a good safeguard.
                print(f"Warning: Cleaned filename '{cleaned_filename}' does not end with .md for '{original_filename}'. Appending .md.")
                # cleaned_filename = cleaned_filename + '.md' # Only append if needed
        else:
            # If no [tags] prefix found, no tags are extracted, and filename remains original.
            extracted_tags = [] # Ensure it's an empty list
            cleaned_filename = original_filename # Keep the original filename

        # --- DATE EXTRACTION (from file modification time) ---
        try:
            mod_timestamp = os.path.getmtime(os.path.join(p_dir, original_filename))
            file_date = datetime.fromtimestamp(mod_timestamp).strftime('%Y-%m-%d')
        except OSError:
            print(f"Warning: Could not get modification date for '{original_filename}'. Using current date.")
            # file_date is already set to current_timestamp as fallback

        # Construct the item for list.json
        new_item_data = {
            "1": cleaned_filename,
            "2": file_date,
            "3": extracted_tags 
        }

        # Check if the cleaned_filename already exists in the old list.json
        if cleaned_filename in existing_file_map:
            # If exists, update its tags and date
            existing_item = existing_file_map[cleaned_filename]
            
            # For this version, we always update date and tags from latest processing
            new_item_data["2"] = file_date 
            new_item_data["3"] = extracted_tags 

            # Remove from map to track processed files
            del existing_file_map[cleaned_filename] 
        
        final_file_list.append(new_item_data)
    
    # Sort the final list by the '1' field (cleaned filename)
    final_file_list.sort(key=lambda x: x.get("1", ""))

    # Save back to list.json 
    try:
        with open(list_json_path, 'w', encoding='utf-8') as f: 
            json.dump(final_file_list, f, indent=4, ensure_ascii=False) 
        print(f"'{list_json_path}' updated successfully using regex for tag extraction.")
    except IOError as e:
        print(f"Error writing to '{list_json_path}': {e}")

if __name__ == "__main__": 
    update_file_list_with_regex_for_tags()
