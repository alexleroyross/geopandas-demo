import geopandas as gpd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

if __name__ == '__main__':
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    cities = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

    world = world[(world.pop_est > 0) & (world.name != "Antarctica")]
    world['gdp_per_cap'] = world.gdp_md_est / world.pop_est

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_aspect('equal')
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="3%", pad=0.1)
    world.plot(
        ax=ax,
        cax=cax,
        column='gdp_per_cap',
        cmap='OrRd',
        legend=True,
        legend_kwds={
            'label': "GDP Per Capita",
            'orientation': "vertical"
        },
        missing_kwds={
            'color': 'lightgrey',
            'edgecolor': 'red',
            'hatch': '///',
            'label': 'Missing values',
        }
    )
    cities = cities.to_crs(world.crs)
    cities.plot(ax=ax, color='black', markersize=6)

    plt.show()
