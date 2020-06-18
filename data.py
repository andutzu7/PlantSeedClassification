import os
from PIL import Image

no_photos = 4500
resize_size = (100, 100)
path = r'C:\Users\diana\OneDrive\Desktop\plant-seedlings-classification\data\train'
categories = []

for filename in os.listdir(path):
    categories.append(filename)


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

train_path = r'C:\Users\diana\OneDrive\Desktop\plant-seedlings-classification\data\train'

val_path = r'C:\Users\diana\OneDrive\Desktop\plant-seedlings-classification\data\validation'
for weed in categories:
    rename_photos(train_path+'/'+weed,weed)


def get_validation_data(path, category, validation_count):
    counter = 0
    for file in os.listdir(train_path + '/' + category):
        new_name = f'{path}/{category}/{category}{counter}.png'
        os.rename(f'{train_path}/{category}/{file}', new_name)
        counter = counter + 1
        if counter >= validation_count:
            break


# Data augmentation
'''''
#data_gen= ImageDataGenerator(
      featurewise_center=True,
    samplewise_center=False,
    featurewise_std_normalization=True,
    samplewise_std_normalization=False,
    zca_whitening=False,
    zca_epsilon=1e-06,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    brightness_range=None,
    shear_range=0.0,
    zoom_range=0.0,
    channel_shift_range=0.0,
    fill_mode="nearest",
    cval=0.0,
    horizontal_flip=True,
    vertical_flip=False,
    rescale=None,
    preprocessing_function=None,
    data_format=None,
    validation_split=0.0,
    dtype=None,
)

'''
