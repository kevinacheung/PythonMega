import folium
import pandas
# dir(folium)
# help(folium.map)
data = pandas.read_csv("mapping/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

def color_producer(elevation):
    if elevation < 1500:
        return "green"
    elif 1500 <= elevation <= 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(iframe), 
    fill_color = color_producer(el), color = 'grey', fill_opacity=0.7))
 
map.add_child(fg)
map.save("mapping/map2.html")