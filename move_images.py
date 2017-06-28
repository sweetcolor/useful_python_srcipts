# Move all images in directory and subdirectories in new images folder
# and rename all in accordance subdirectory names


import os
import sys


path = sys.argv[1]
if not os.path.isdir(path):
    sys.exit(1)


def create_folder(path_):
    if not os.path.exists(path_):
        os.mkdir(path_)

os.chdir(path)
images_folder = os.path.join(path, 'images')
create_folder(images_folder)
only_subdir = {f: os.listdir(f) for f in os.listdir('.') if os.path.isdir(f)}
count = 0
for dir_name, files in only_subdir.items():
    for file in files:
        if file.endswith(('.jpg', '.jpeg', '.gif', '.png')):
            count += 1
            destination_folder = os.path.join(images_folder, os.path.basename(dir_name))
            create_folder(destination_folder)
            print(os.path.join(dir_name, file), '->', os.path.join(destination_folder, file))
            os.rename(os.path.join(dir_name, file), os.path.join(destination_folder, file))
print(count)
