import PIL.Image
import PIL.ExifTags

# Resmi açma
img = PIL.Image.open("foto.jpg")

# EXIF verilerini alma
exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in PIL.ExifTags.TAGS
}

# GPS verilerini kontrol etme
if 'GPSInfo' in exif:
    gps_info = exif['GPSInfo']
    
    # Kuzey ve doğu koordinatlarını alma
    north = gps_info[2]
    east = gps_info[4]
    
    # Koordinatları yazdırma
    print("North:", north)
    print("East:", east)

    # Derece, dakika ve saniyeyi dereceye çevirme
    def convert_to_degrees(value):
        d = value[0] + (value[1] / 60.0) + (value[2] / 3600.0)
        return d

    lat = convert_to_degrees(north)
    long = convert_to_degrees(east)

    print("Latitude:", lat)
    print("Longitude:", long)

    # Harita oluşturma
    from gmplot import gmplot

    # Not: gmplot için bir API anahtarına ihtiyacınız olabilir. 
    # Eğer öyleyse, gmap = gmplot.GoogleMapPlotter(lat, long, 12, apikey='YOUR_API_KEY')
    gmap = gmplot.GoogleMapPlotter(lat, long, 12)
    gmap.marker(lat, long, "cornflowerblue")
    gmap.draw("harita.html")
else:
    print("Resimde GPS bilgisi bulunamadı.")
