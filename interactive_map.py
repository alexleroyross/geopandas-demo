import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import certifi

if __name__ == '__main__':
    # nybb = gpd.read_file(gpd.datasets.get_path('nybb'))
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    # cities = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)_per_capita'
    tables = pd.read_html(url)
    table = tables[1]
    table['Country/Territory'] = table['Country/Territory'].apply(str).str.split('\\')[0]
    table = world.merge(table, how="left", left_on=['name'], right_on=['Country/Territory'])

    pass

    # nybb.explore()

    # plt.show()
