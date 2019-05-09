import folium
import pandas

# polygons_file = pandas.read_csv("Volcanoes_USA.txt")
# map = folium.Map(location=[polygons_file['LAT'].mean(), polygons_file['LON'].mean()], zoom_start=6, tiles='Base Map')
#
# #
# def color(elev):
#     minimum=int(min(points_file['ELEV']))
#     step=int((max(points_file['ELEV'])-min(points_file['ELEV']))/3)
#     if elev in range(minimum,minimum+step):
#         col='green'
#     elif elev in range(minimum+step,minimum+step*2):
#         col='orange'
#     else:
#         col='red'
#     return col

# map.save(outfile='testmap.html')

m = folium.Map(location=[42.3601, -71.0589], zoom_start=12)
m.save('map.html')
