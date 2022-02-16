import PIL.Image
img = PIL.Image.open('gps0.jpg')
exif_data = img._getexif()
print(exif_data)