import matplotlib.pyplot as plt

from dhnx.plotting import InteractiveMap
from dhnx.plotting import StaticMap
from dhnx.network import ThermalNetwork

# initialize a thermal network
thermal_network = ThermalNetwork()

# load data from csv
thermal_network.from_csv_folder('data_csv_input')

# save thermal network to csv
thermal_network.to_csv_folder('data_csv_output')

# get graph of thermal network
graph = thermal_network.to_nx_graph()

# plot static map
static_map = StaticMap(thermal_network)

static_map.draw(background_map=False)
plt.savefig('static_map_wo_background.png')

static_map.draw(background_map=True)
plt.savefig('static_map_w_background.png')

# plot interactive map
interactive_map = InteractiveMap(thermal_network)
map = interactive_map.draw()
map.save('interactive_map.html')
