import os
from PIL import Image

image_folder, new_folder = tuple(
    input('Enter image folder and new folder name: ').split(' '))

# check if the new folder exists
if os.path.exists(new_folder) is False:
    os.mkdir(new_folder)


# iterate over files in image folder/directory
if len(os.listdir(image_folder)) > 0:
    for filename in os.listdir(image_folder):
        f = os.path.join(image_folder, filename)
        # checking if it is a file
        if os.path.isfile(f):
            try:
                new_file_name = f.split('/')[1].replace('.jpg', '.png')
                img = Image.open(f)
                img.save(f'{new_folder}{new_file_name}')
            except OSError as error:
                print('Something went wrong', error)
else:
    print(f'{image_folder} is empty')
