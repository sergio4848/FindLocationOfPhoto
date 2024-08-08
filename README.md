Sure, here's an explanation of the project in English:

### Project Overview

This project involves reading an image, extracting its GPS metadata, converting the GPS coordinates to a readable format, and then plotting these coordinates on a Google map using the `gmplot` library. The final output is an HTML file that displays the location on the map.

### Steps and Code Explanation

1. **Importing Required Libraries:**
   ```python
   import PIL.Image
   import PIL.ExifTags
   from gmplot import gmplot
   ```
   We import the necessary libraries. `PIL` (Python Imaging Library) is used for image processing, and `gmplot` is used for plotting the coordinates on Google Maps.

2. **Opening the Image:**
   ```python
   img = PIL.Image.open("foto.jpg")
   ```
   This line opens the image file named "foto.jpg".

3. **Extracting EXIF Data:**
   ```python
   exif = {
       PIL.ExifTags.TAGS[k]: v
       for k, v in img._getexif().items()
       if k in PIL.ExifTags.TAGS
   }
   ```
   We extract the EXIF (Exchangeable Image File Format) metadata from the image. EXIF data contains information about the image, such as the camera settings and, importantly for this project, the GPS information.

4. **Checking for GPS Information:**
   ```python
   if 'GPSInfo' in exif:
       gps_info = exif['GPSInfo']
       
       north = gps_info[2]
       east = gps_info[4]
       
       print("North:", north)
       print("East:", east)
   ```
   We check if the EXIF data contains GPS information. If it does, we extract the north (latitude) and east (longitude) coordinates.

5. **Converting GPS Coordinates to Degrees:**
   ```python
   def convert_to_degrees(value):
       d = value[0] + (value[1] / 60.0) + (value[2] / 3600.0)
       return d

   lat = convert_to_degrees(north)
   long = convert_to_degrees(east)

   print("Latitude:", lat)
   print("Longitude:", long)
   ```
   GPS coordinates are often stored as degrees, minutes, and seconds. We convert these values to a single degree value for both latitude and longitude.

6. **Plotting the Coordinates on a Google Map:**
   ```python
   gmap = gmplot.GoogleMapPlotter(lat, long, 12)
   gmap.marker(lat, long, "cornflowerblue")
   gmap.draw("harita.html")
   ```
   We use `gmplot` to create a Google Map centered at the extracted coordinates. A marker is placed at these coordinates, and the map is saved as an HTML file named "harita.html".

### Error Handling

If the image does not contain GPS information, the program prints a message indicating that no GPS data was found:
```python
else:
    print("Resimde GPS bilgisi bulunamadı.")
```

### Requirements

Ensure that the required libraries are installed:
```sh
pip install pillow gmplot
```

**Note:** For `gmplot`, you may need a Google Maps API key. If you do not have one, you can obtain it from the Google Cloud Platform.

### Summary

This project demonstrates how to work with image metadata to extract GPS coordinates and plot them on a map using Python. It covers opening an image, reading EXIF data, converting GPS coordinates to a readable format, and visualizing the location on a Google Map.
