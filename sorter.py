import os
import shutil

try:
    from PIL import Image
    import pillow_heif
    pillow_heif.register_heif_opener()
    HAS_CONVERTER = True
except ImportError:
    HAS_CONVERTER = False

def organize_photos(source_dir, output_dir, extensions=None, keywords=None, convert_to=None):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created folder: {output_dir}")


    files = os.listdir(source_dir)
    count = 0

    for file_name in files:
        name, ext = os.path.splitext(file_name)
        ext = ext.lower()

        match_ext = extensions and ext in extensions
        match_key = False
        if keywords:
            for k in keywords:
                if k in name.lower():
                    match_key = True
                    break

        if match_ext or match_key:
            source_path = os.path.join(source_dir, file_name)
            
            if convert_to and ext in ['.heic', '.heif']:
                if not HAS_CONVERTER:
                    print(f"Cannot convert {file_name}. Missing required packages. Run: pip install pillow pillow-heif")
                    dest_path = os.path.join(output_dir, file_name)
                    shutil.copy2(source_path, dest_path)
                    print(f"Copied without conversion: {file_name}")
                    count += 1
                    continue
                
                new_file_name = f"{name}{convert_to}"
                dest_path = os.path.join(output_dir, new_file_name)
                try:
                    image = Image.open(source_path)
                    if convert_to == '.jpg':
                        # Convert to RGB to save as JPG
                        image = image.convert("RGB")
                        image.save(dest_path, "JPEG")
                    elif convert_to == '.png':
                        image.save(dest_path, "PNG")
                    print(f"Converted and Copied: {file_name} -> {new_file_name}")
                    count += 1
                except Exception as e:
                    print(f"Failed to convert {file_name}: {e}")
            else:
                dest_path = os.path.join(output_dir, file_name)
                shutil.copy2(source_path, dest_path)
                print(f"Copied: {file_name}")
                count += 1

    print(f"\nTask Complete! {count} files processed to {output_dir}")

while True:
    print("\n--- New Task ---")
    SOURCE = input("Enter the source dest (or type 'exit' to quit): ").strip()
    if SOURCE.lower() == 'exit':
        break
        
    DESTINATION = input("Enter the output dest: ").strip()
    raw_input = input("Enter the extension with a comma sepertaion (.jpg, .png): ")
    TARGET_EXTENSIONS = [
        f".{ext.strip().lstrip('.')}".lower() 
        for ext in raw_input.split(',') 
        if ext.strip()
    ]
    raw_keyword = input("Enter keywords to search for, comma separated (or leave empty): ").strip()
    TARGET_KEYWORDS = [k.strip().lower() for k in raw_keyword.split(',') if k.strip()] if raw_keyword else None

    CONVERT_TO = input("Convert .heif/.heic files to (.jpg, .png) or leave empty to skip: ").strip().lower()
    if CONVERT_TO and not CONVERT_TO.startswith('.'):
        CONVERT_TO = f".{CONVERT_TO}"
    if CONVERT_TO not in [".jpg", ".png", ""]:
        print("Invalid format. Skipping conversion.")
        CONVERT_TO = None
    elif CONVERT_TO == "":
        CONVERT_TO = None

    organize_photos(SOURCE, DESTINATION, TARGET_EXTENSIONS, TARGET_KEYWORDS, CONVERT_TO)