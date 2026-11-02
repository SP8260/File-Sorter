import os

os.makedirs("Sorted Files", exist_ok = True)

os.makedirs("Sorted Files/Images", exist_ok = True)
os.makedirs("Sorted Files/Documents", exist_ok = True)
os.makedirs("Sorted Files/Videos", exist_ok = True)
os.makedirs("Sorted Files/Audio", exist_ok = True)
os.makedirs("Sorted Files/Misc", exist_ok = True)

docs = 0
images = 0
audio = 0
video = 0
misc = 0

user_dir = input("Enter the directory you want to sort: ")

try:
    files_list = os.listdir(user_dir)
except (FileNotFoundError, PermissionError):
    print("This directory is invalid or you do not have permission to access it")
    user_dir = input("Enter the directory you want to sort: ")

for file in os.listdir(user_dir):
    filetype = (file.split(".")[1]).lower()
    if filetype == "pdf" or filetype == "txt":
        os.replace(os.path.join(user_dir, file), os.path.join("Sorted Files/Documents", file))
        docs += 1
    elif filetype == "jpg" or filetype == "jpeg" or filetype == "png" or filetype == "svg":
        os.replace(os.path.join(user_dir, file), os.path.join("Sorted Files/Images", file))
        images += 1
    elif filetype == "mp3":
        os.replace(os.path.join(user_dir, file), os.path.join("Sorted Files/Audio", file))
        audio += 1
    elif filetype == "mp4":
        os.replace(os.path.join(user_dir, file), os.path.join("Sorted Files/Videos", file))
        video += 1
    else:
        os.replace(os.path.join(user_dir, file), os.path.join("Sorted Files/Misc", file)) # safely add other filetypes to misc folder
        misc += 1
        
print(f"Sorting Complete! Moved {docs} files to Documents, {audio} files to Audio, {images} files to Images, {video} files to Videos, and {misc} files to Misc.")