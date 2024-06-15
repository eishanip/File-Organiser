import os
import shutil

#Define the desktop directory (edit accordingly for any other directory)
directory = os.path.join(os.path.expanduser("~"), "Desktop")

#Define the extensions and their corresponding folder names
extensions = {
    ".jpg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".docx": "Documents",
    ".doc": "Documents",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".rtf": "Documents",
    ".mp3": "Music",
    ".wav": "Music",
}

#Loop through the files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    #Check if the item is a file
    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower() #Extract the file extension

        #Check if the extension is in the dictionary
        if extension in extensions:
            folder_name = extensions[extension]

            #Create the folder if it doesn't exist
            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            destination_path = os.path.join(folder_path, filename) #Define the destination path

            try:
                #Move the file
                shutil.move(file_path, destination_path)
                print(f"Moved {filename} to {folder_name} folder.")
            except Exception as e:
                print(f"Error moving {filename}: {e}")
        else:
            print(f"Skipped {filename}. Unknown file extension.")
    else:
        print(f"Skipped {filename}. Not a file.")
