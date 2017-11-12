import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation <= 1500:
        return "pink"
    if 1500 < elevation <= 3000:
        return "purple"
    else:
        return "blue"

map = folium.Map(location=[38.01, -99.09], zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

# for lt, ln, el in zip(lat, lon, elev):
#     fg.add_child(folium.Marker(location=[lt, ln], popup=str(el) + " m", icon=folium.Icon(color=color_producer(el))))

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=el/300, popup=str(el) + " m", fill = True,
                                     fill_color=color_producer(el), color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(open(file='world.json').read()))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")


