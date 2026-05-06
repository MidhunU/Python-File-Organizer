import os
import shutil

def organize_photos(source_dir, output_dir, extensions=None, keyword=None):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created folder: {output_dir}")


    files = os.listdir(source_dir)
    count = 0

    for file_name in files:
        name, ext = os.path.splitext(file_name)
        ext = ext.lower()

        match_ext = extensions and ext in extensions
        match_key = keyword and keyword.lower() in name.lower()

        if match_ext or match_key:
            source_path = os.path.join(source_dir, file_name)
            dest_path = os.path.join(output_dir, file_name)

            shutil.copy2(source_path, dest_path)
            print(f"Copied: {file_name}")
            count += 1

    print(f"\nTask Complete! {count} files moved to {output_dir}")

SOURCE = input("Enter the source dest: ").strip()
DESTINATION = input("Enter the output dest: ").strip()
raw_input = input("Enter the extension with a comma sepertaion (.jpg, .png): ")
TARGET_EXTENSIONS = [
    f".{ext.strip().lstrip('.')}".lower() 
    for ext in raw_input.split(',') 
    if ext.strip()
]
TARGET_KEYWORD = input("Enter a keyword to search for (or leave empty): ").strip()
if TARGET_KEYWORD == "":
    TARGET_KEYWORD = None
organize_photos(SOURCE, DESTINATION, TARGET_EXTENSIONS, TARGET_KEYWORD)