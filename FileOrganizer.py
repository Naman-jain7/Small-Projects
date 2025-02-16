import shutil
import os

file_types = {
    "Images":[".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"]
}

def organize_files(unorganized_folder):
    if not os.path.exists(unorganized_folder):
        print(f"Error: {unorganized_folder} does not exist")
        return
    files = os.listdir(unorganized_folder)
    if not files:
        print(f"No files found in {unorganized_folder}")
        return
    for file in files:
        file_path = os.path.join(unorganized_folder, file)
        # skip if it is a dir
        if os.path.isdir(file_path):
            continue
        
        _, extension = os.path.splitext(file)
        category = "Others"
        for folder, extensions in file_types.items():
            if extension.lower() in extensions:
                category = folder
                break
            
        # create the folder if doesn't exist
        category_folder = os.path.join(unorganized_folder, category)
        os.makedirs(category_folder, exist_ok=True)
        
        try:
            shutil.move(file_path, os.path.join(category_folder, file))
            print(f"Moved {file} -> {category}/")
        except Exception as e:
            print(f"Error moving the file: {e}")