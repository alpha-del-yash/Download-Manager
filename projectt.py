import os
from pathlib import Path
import time
import shutil

def count_files_in_folder(folder_path):
    try:
        path=Path(folder_path) #when entering the path write it as (r"path").
        count = 0
        # os.scandir is an iterator, making it very fast for large folders
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    count += 1
        return count
    except FileNotFoundError:
        return "Path not found"
    except PermissionError:
        return "Permission denied"

def sorting_files(folder_path):
    sort={".pdf": r"C:\Users\alluy\Downloads\documents", ".png": r"C:\Users\alluy\Downloads\images", 
          ".jpeg": r"C:\Users\alluy\Downloads\images", ".jpg": r"C:\Users\alluy\Downloads\images", 
          ".exe": r"C:\Users\alluy\Downloads\apps", ".tmp": r"C:\Users\alluy\Downloads\temperory",
          ".docx": r"C:\Users\alluy\Downloads\documents", ".txt": r"C:\Users\alluy\Downloads\documents",
          ".mp3": r"C:\Users\alluy\Downloads\audios", ".mp4": r"C:\Users\alluy\Downloads\videos"} 
    # dictionary used to map the file extensions to respective folders
    for file in folder_path.iterdir():
        if file.is_file():  # Ensure it's a file, not a subfolder
            name=file.name
            ext=file.suffix
            print(f"sorting {name}")
            if ext in sort.keys(): #check if the extension is in the dictionary
                dest = Path(sort[ext])
                dest_file = dest / name
                if dest_file.exists():
                    print(f"File {name} already exists in {dest}, skipping")
                else:
                    shutil.move(str(file), dest) #moves to the respective folder
            else: 
                #if not present, then moves to a seperate folder called "others"
                others = Path(r"C:\Users\alluy\Downloads\others")
                others_file = others / name
                if others_file.exists():
                    print(f"File {name} already exists in {others}, skipping")
                else:
                    shutil.move(str(file), others)
            print(f"\nsorted {name}")
 
def sort_folder(folder_path, interval_seconds=30):
    try:
        while True:
            file_count = count_files_in_folder(folder_path)
            if file_count > 0:
                sorting_files(folder_path)
            time.sleep(interval_seconds) #runs this function recursively

    except KeyboardInterrupt: #if needed to stop
        print("\nMonitoring stopped by user.")

def monitor_sorting_folder(folder_path, interval_seconds=30):
    try:
        while True:
            file_count = count_files_in_folder(folder_path)
            if file_count > 0:
                sorting_files(folder_path)
            time.sleep(interval_seconds) #runs this function recursively
    except KeyboardInterrupt: #if needed to stop
        print("\nMonitoring stopped by user.")

m=input("do you want to sort any folder other than downloads folder?(Y/N): ")
if m=="Y" or m=="y":
    folder_path1 = input("enter the path of the folder you want to sort: ").strip().strip('"')
    print(folder_path1)
    folder_path2 = Path(folder_path1)
    if folder_path2.is_dir():
        sort_folder(folder_path2)
    else:
        print(f"Folder not found: {folder_path2}")
else:
    folder_path = Path(r"C:\Users\alluy\Downloads") #enter the path of your downloads folder
    count= count_files_in_folder(folder_path)
    monitor_sorting_folder(folder_path) 