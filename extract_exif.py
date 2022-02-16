import PIL.Image
img = PIL.Image.open('gps0.jpg')
exif_data = img._getexif()
print(exif_data)




import exifread
# Open image file for reading (binary mode)
f = open('gps0.jpg', 'rb')

# Return Exif tags
tags = exifread.process_file(f)