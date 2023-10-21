import os
import shutil

directory_path = "C:\\Users\\Mihajlo Popovic\\OneDrive\\Desktop\\downloads proba"
dest_path =""
def get_list_of_ext(directory_path):
    ext = []
    with os.scandir(directory_path) as entries:
        for entry in entries:
            parts = entry.name.rsplit('.', 1)
            if len(parts) > 1:
                ext.append(parts[-1])
            else:
                ext.append(entry.name) 
    return ext

def create_folders(names):
    # Get the path to the directory
    desktop_path = os.path.join(os.path.expanduser("C:\\Users\\Mihajlo Popovic\\OneDrive\\Desktop\\"), "dest folder")
    global dest_path
    dest_path = desktop_path
    print("DEST PATH JEEEEEEE: ", dest_path)
    for name in names:
        # Create a folder with the specified name on the desktop
        folder_path = os.path.join(desktop_path, name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Folder '{name}' has been created.")
        else:
            print(f"Folder '{name}' already exists.")

def get_substring_after_last_period(string):
    last_period_index = string.rfind('.')

    # Check if a period was found
    if last_period_index != -1:
        # Extract the substring after the last period
        substring = string[last_period_index + 1:]
        return substring
    else:
        # If no period is found, return the entire string
        return string

def find_folder_path(directory_path, folder_name):
    for root, dirs, files in os.walk(directory_path):
        if folder_name in dirs:
            folder_path = os.path.join(root, folder_name)
            return folder_path
    return None



def move_objects(directory_path):
    global dest_path
    print("Path: ",dest_path)
    with os.scandir(directory_path) as entries:
        for entry in entries:
            ext = get_substring_after_last_period(entry.name)
            src = entry.path
            folder_name = f"{ext}"
            try:
                dest = find_folder_path(dest_path, folder_name)
                print("Destionation is: ",dest)
                shutil.move(src, dest)
            except FileNotFoundError:
                 print("The source or destination path does not exist.")
            except OSError as e:
                 print(f"An error occurred while renaming the file: {e}")




directory_path = "C:\\Users\\Mihajlo Popovic\\OneDrive\\Desktop\\downloads proba"
list_of_ext = get_list_of_ext(directory_path)
print("Substrings behind the last period in the directory:", list_of_ext)
create_folders(list_of_ext)
move_objects(directory_path)
print("Success!")