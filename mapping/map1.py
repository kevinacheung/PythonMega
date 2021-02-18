#import folium
#dir(folium)
#help(folium.map)
map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles = "Stamen Terrain")
map.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi Marker", icon=folium.Icon(color='green')))
map.save("mapping/map1.html")