import PIL.Image
img = PIL.Image.open('gps0.jpg')
exif_data = img._getexif()
print(exif_data)




import PIL.ExifTags
exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in PIL.ExifTags.TAGS
}