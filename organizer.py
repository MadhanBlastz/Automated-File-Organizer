import os
import shutil

# Categories and their file extensions
EXTENSIONS = {
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z", ".iso"],
    "Code": [".py", ".html", ".css", ".js", ".java", ".cpp", ".json"],
    "Installers": [".exe", ".msi"]
}

def organize_folder(folder_path):
    # Validate if folder exists
    if not os.path.exists(folder_path):
        print(f"❌ Error: The path '{folder_path}' does not exist.")
        return

    if not os.path.isdir(folder_path):
        print(f"❌ Error: '{folder_path}' is a file, not a folder.")
        return

    print(f"\n📂 Organizing folder: {folder_path}\n")

    moved_count = 0
    skipped_count = 0

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        # Skip folders (including existing subfolders)
        if os.path.isdir(item_path):
            continue

        _, ext = os.path.splitext(item)
        ext = ext.lower()

        # Find target category
        dest_folder_name = "Others"
        for folder_name, ext_list in EXTENSIONS.items():
            if ext in ext_list:
                dest_folder_name = folder_name
                break

        # Move the file with error handling
        try:
            destination_dir = os.path.join(folder_path, dest_folder_name)
            os.makedirs(destination_dir, exist_ok=True)
            shutil.move(item_path, os.path.join(destination_dir, item))
            print(f"✅ Moved: {item} -> {dest_folder_name}/")
            moved_count += 1
        except PermissionError:
            print(f"⚠️ Skipped (In use): {item}")
            skipped_count += 1
        except Exception as e:
            print(f"⚠️ Error moving {item}: {e}")
            skipped_count += 1

    print(f"\n🎉 Done! {moved_count} files organized, {skipped_count} skipped.")

if __name__ == "__main__":
    # Get path from user and clean any extra quotes (e.g. if dragged and dropped)
    user_path = input("Enter the folder path to organize: ").strip().strip('"').strip("'")
    
    if user_path:
        organize_folder(user_path)
    else:
        print("❌ No path entered. Exiting.")

