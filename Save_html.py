import folium
from fitparse import FitFile, StandardUnitsDataProcessor
import os


def get_points(filename):
    fit_file = FitFile(filename, data_processor=StandardUnitsDataProcessor())
    msgs = fit_file.messages
    points = []
    for m in msgs:
        if m.name == 'record':
            points.append(tuple([m.get_value('position_lat'), m.get_value('position_long')]))
    return points


def save_map(filename, path):
    points = get_points(filename)
    ave_lat = sum(p[0] for p in points) / len(points)
    ave_lon = sum(p[1] for p in points) / len(points)
    my_map = folium.Map(location=(ave_lat, ave_lon), tiles='OpenStreetMap', zoom_start=16)
    folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(my_map)
    folium.Marker(points[0], popup='start').add_to(my_map)
    folium.Marker(points[-1], popup='finish').add_to(my_map)
    my_map.save(path + os.path.basename(filename)[:-4] + '_map.html')


if __name__ == '__main__':
    save_map(r'C:\Users\vovan\PycharmProjects\fit_to_readable\A9R90207.FIT', 'D:/Training Results/')
