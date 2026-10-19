
import os
import shutil

# File extension categories
file_types = {
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".py": "Code",
    ".java": "Code",
    ".html": "Code",
    ".css": "Code",
    ".js": "Code"
}

def organize_folder(folder_path):
    moved = 0
    skipped = 0

    if not os.path.isdir(folder_path):
        print("Error: Folder does not exist!")
        return

    for entry in os.scandir(folder_path):
        if not entry.is_file():
            continue

        extension = os.path.splitext(entry.name)[1].lower()
        category = file_types.get(extension)

        if category is None:
            continue

        destination_folder = os.path.join(folder_path, category)

        try:
            os.makedirs(destination_folder, exist_ok=True)

            destination = os.path.join(destination_folder, entry.name)

            # Prevent overwriting existing files
            if os.path.exists(destination):
                name, ext = os.path.splitext(entry.name)
                count = 1

                while os.path.exists(destination):
                    new_name = f"{name}_{count}{ext}"
                    destination = os.path.join(destination_folder, new_name)
                    count += 1

            shutil.move(entry.path, destination)
            moved += 1

            print(f"Moved: {entry.name} -> {category}")

        except (PermissionError, FileExistsError, OSError) as error:
            skipped += 1
            print(f"Skipped: {entry.name} - {error}")

    print("\n========== ORGANIZATION SUMMARY ==========")
    print(f"Total files relocated: {moved}")
    print(f"Total files skipped: {skipped}")
    print("Organization completed!")


if __name__ == "__main__":
    test_folder = input("Enter folder path to organize: ")
    organize_folder(test_folder)
