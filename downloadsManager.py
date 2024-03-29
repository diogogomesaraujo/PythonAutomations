# To create the Automator follow this steps:

#1. Open "Automator" on your Mac.
#2. Choose "New Document" and select "Folder Action".
#3. Set the folder to watch (e.g., Downloads).
#4. Drag "Run Shell Script" from the actions list to the workflow area.
#5. Choose your shell (e.g., /bin/zsh) from the "Shell" dropdown.
#6. Type your Python script command (e.g., python3 /path/to/script.py).
#7. Save the Automator action with a meaningful name.
#8. Test by adding a file to the folder.

import os
from datetime import datetime

source = "/Users/diogoaraujo/Downloads" # change this to your downloads folder

# Define a dictionary for extension mapping to folder names
extension_mapping = {
    ".pdf": "PDFs",
    ".jpeg": "Imagens", ".jpg": "Imagens", ".png": "Imagens", ".heic": "Imagens", ".gif": "Imagens",
    ".mov": "Videos", ".mp4": "Videos",
    ".zip": "Comprimidos", ".rar": "Comprimidos",
    ".mp3": "Audios", ".wav": "Audios",
    ".py": "Codigos", ".java": "Codigos", ".cpp": "Codigos", ".c": "Codigos", 
    ".h": "Codigos", ".html": "Codigos", ".css": "Codigos", ".js": "Codigos"
}

with os.scandir(source) as files:
    for file in files:
        if file.is_file():  # Check if it's a file and not a directory
            file_extension = os.path.splitext(file.name)[1].lower()
            
            # Determine the target directory based on the file extension
            target_dir = extension_mapping.get(file_extension, "Outros")
            target_folder_path = os.path.join(source, target_dir)
            
            # Ensure the target directory exists
            os.makedirs(target_folder_path, exist_ok=True)
            
            # Create a unique file name if the file already exists
            original_target_path = os.path.join(target_folder_path, file.name)
            unique_target_path = original_target_path
            counter = 1
            while os.path.exists(unique_target_path):
                name, extension = os.path.splitext(original_target_path)
                unique_target_path = f"{name}_{counter}{extension}"
                counter += 1
            
            # Move the file
            os.replace(file.path, unique_target_path)
