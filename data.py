import os
from PIL import Image

no_photos = 4500
resize_size = (100, 100)
path = r'C:\Users\diana\OneDrive\Desktop\plant-seedlings-classification\train'
categories=[]
for filename in os.listdir(path):
    if filename=='Black-grass':
        continue
    categories.append(filename)

def resize_photos(path):
    for filename in os.listdir(path):
        new_file_name= os.path.join(path, filename)
        img=Image.open(new_file_name)
        resized_image = img.resize(resize_size, Image.ANTIALIAS)
        resized_image.save(new_file_name, 'PNG')


def rename_photos(path,category):
    i=-1
    for file in os.listdir(path):
        i=i+1
        new_name=f'{category}{i}.png'
        os.rename(path + '/' + file, path + '/' + new_name)

for weed in categories:
    resize_photos(path+'/'+weed)
    rename_photos(path+'/'+weed,weed)

