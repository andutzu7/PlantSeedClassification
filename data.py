import os
from PIL import Image

path = r'F:\Code\RobertPlant\data\train'

val_path = r'F:\Code\RobertPlant\data\validation'
categories = []

for filename in os.listdir(path):
    categories.append(filename)

no_photos = 4500
resize_size = (100, 100)


def resize_photos(path):
    for filename in os.listdir(path):
        new_file_name = os.path.join(path, filename)
        img = Image.open(new_file_name)
        resized_image = img.resize(resize_size, Image.ANTIALIAS)
        resized_image.save(new_file_name, 'PNG')


def rename_photos(path, category):
    i = -1
    for file in os.listdir(path):
        i = i + 1
        new_name = f'{category}{i}.png'
        os.rename(path + '/' + file, path + '/' + new_name)


# configuring validation data set

train_path = r'F:\Code\RobertPlant\data\train'


def get_validation_data(path, category, validation_count):
    counter = 0
    for file in os.listdir(train_path + '/' + category):
        new_name = f'{path}/{category}/{category}{counter}.png'
        os.rename(f'{train_path}/{category}/{file}', new_name)
        counter = counter + 1
        if counter >= validation_count:
            break


for weed in categories:
    rename_photos(train_path + '/' + weed, weed)
