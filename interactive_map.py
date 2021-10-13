import pandas as pd
import geopandas as gpd
import folium

if __name__ == '__main__':
    # Read in a world map from the default GeoPandas data store
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Read the URL containing tables of data
    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_forest_area'
    tables = pd.read_html(url)

    # Grab the 2nd table from the page, which contains our data
    table = tables[1]

    # Merge the world DataFrame into our data table
    table = world.merge(table, how="left", left_on=['name'], right_on=['Country'])

    # Remove any rows that contain no data
    table = table.dropna(subset=['2020'])

    # Create an interactive Folium map
    forest_map = folium.Map()

    # Add our data to the map
    folium.Choropleth(
        geo_data=table,
        name='choropleth',
        data=table,
        columns=['Country', '2020'],
        key_on='feature.properties.name',
        fill_color='YlGn',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Forest area in units of 1,000 hectares',
        bins=9
    ).add_to(forest_map)

    # Save the map as an HTML file
    forest_map.save('forest.html')
