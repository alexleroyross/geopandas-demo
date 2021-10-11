import geopandas as gpd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    districts = gpd.read_file("./Shapefiles/districts.shp")
    # districts.plot(cmap='jet', edgecolor='black', column='district')

    area_of_interest = gpd.read_file("./Shapefiles/area_of_interest.shp")
    # area_of_interest.plot()

    atms = gpd.read_file("./Shapefiles/atms.shp")

    # fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 8))
    # districts.plot(ax=ax1)
    # area_of_interest.plot(ax=ax2, color='green')

    # Plot multiple layers
    # fig, ax = plt.subplots(figsize=(10, 8))
    # districts.plot(ax=ax, cmap='hsv', edgecolor='black')
    # area_of_interest.plot(ax=ax, color='none', edgecolor='black')
    # atms.plot(ax=ax, color='black', markersize=14)

    # Reprojecting DataFrames
    # fig, ax = plt.subplots(figsize=(10, 8))
    # districts = districts.to_crs(epsg=32629)
    # districts.plot(ax=ax, figsize=(10, 8), cmap='hsv', edgecolor='black', column='district')
    # area_of_interest = area_of_interest.to_crs(epsg=32629)
    # area_of_interest.plot(ax=ax, figsize=(10, 8), color='none', edgecolor='black')

    # Intersecting layers
    # districts_in_aoi = gpd.overlay(districts, area_of_interest, how='intersection')
    # districts_in_aoi.plot()

    # Calculate area of intersected layer
    # Add a new column and make it the area (in km)
    # districts_in_aoi['area'] = districts_in_aoi.area/1000000

    # Exporting
    # districts_in_aoi.to_file('districts_within_aoi.shp', driver='ESRI Shapefile')

    fig, ax = plt.subplots()
    districts.plot(ax=ax, cmap='hsv', edgecolor='black', column='district')
    area_of_interest.plot(ax=ax, color='none', edgecolor='black')
    atms.plot(ax=ax, color='black', markersize=14)

    plt.show()
