import os
import shutil

# ============================
# CONFIGURATION
# ============================
# Folder to organize
source_folder = os.path.join(os.path.dirname(__file__), "examples/sample_files")
DEST_FOLDER = source_folder  # You can change to a different folder if needed

# File categories and their extensions
FILE_TYPES = {
    "Images": ["jpg", "jpeg", "png", "gif", "bmp", "psd", "tiff", "webp"],
    "Documents": ["pdf", "doc", "docx", "txt", "xls", "xlsx", "ppt", "pptx", "odt", "epub"],
    "Videos": ["mp4", "mkv", "avi", "mov", "flv", "wmv", "webm"],
    "Software": ["exe", "msi", "apk", "bat", "sh"],
    "Archives": ["zip", "rar", "7z", "tar", "gz"],
}

# ============================
# ORGANIZER FUNCTION
# ============================
def organize_files(source_folder):
    if not os.path.exists(source_folder):
        print(f"Source folder does not exist: {source_folder}")
        return

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        ext = filename.split(".")[-1].lower()
        moved = False

        # Check categories
        for category, extensions in FILE_TYPES.items():
            if ext in extensions:
                category_folder = os.path.join(DEST_FOLDER, category)
                os.makedirs(category_folder, exist_ok=True)

                ext_folder = os.path.join(category_folder, ext.upper())
                os.makedirs(ext_folder, exist_ok=True)

                shutil.move(file_path, os.path.join(ext_folder, filename))
                print(f"Moved {filename} → {ext_folder}")
                moved = True
                break

        # If no match, move to Other
        if not moved:
            other_folder = os.path.join(DEST_FOLDER, "Other")
            os.makedirs(other_folder, exist_ok=True)

            ext_folder = os.path.join(other_folder, ext.upper())
            os.makedirs(ext_folder, exist_ok=True)

            shutil.move(file_path, os.path.join(ext_folder, filename))
            print(f"Moved {filename} → {ext_folder} (Other)")

    print("✅ File organization complete!")

# ============================
# MAIN
# ============================
if __name__ == "__main__":
    organize_files(source_folder)
