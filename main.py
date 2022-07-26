import PIL.Image

img = PIL.Image.open("foto.jpg")

import PIL.ExifTags

exif={
    PIL.ExifTags.TAGS[k]: v
    for k,v in img._getexif().items()
    if k in PIL.ExifTags.TAGS
}
exif['GPSInfo']

north = exif['GPSInfo'][2]
east = exif['GPSInfo'][4]

print(north)
print(east)

lat = ((((north[0] * 60) + north[1]) * 60) + north[2])/60/60
long = ((((east[0] * 60) + east[1]) * 60) + east[2])/60/60

lat, long =float(lat),float(long)

print(lat)
print(long)

from gmplot import gmplot
gmap=gmplot.GoogleMapPlotter(lat,long,12)
gmap.marker(lat,long,"cornflowerblue")
gmap.draw("harita.html")

