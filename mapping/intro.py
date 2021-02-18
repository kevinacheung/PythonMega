import folium
#dir(folium)
#help(folium.map)
map = folium.Map(location=[38.58,-99.09], zoom_start=6)
map.save("map1.html")