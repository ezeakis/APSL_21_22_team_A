import PIL.Image
img = PIL.Image.open('gps0.jpg')
exif_data = img._getexif()
print(exif_data)




from PIL import Image, ExifTags

img = Image.open("gps0.jpg")
img_exif = img.getexif()
print(type(img_exif))
# <class 'PIL.Image.Exif'>

if img_exif is None:
    print('Sorry, image has no exif data.')
else:
    for key, val in img_exif.items():
        if key in ExifTags.TAGS:
            print(f'{ExifTags.TAGS[key]}:{val}')
            # ExifVersion:b'0230'
            # ...
            # FocalLength:(2300, 100)
            # ColorSpace:1
            # ...
            # Model:'X-T2'
            # Make:'FUJIFILM'
            # LensSpecification:(18.0, 55.0, 2.8, 4.0)
            # ...
            # DateTime:'2019:12:01 21:30:07'
            # ...