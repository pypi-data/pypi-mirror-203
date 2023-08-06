from math import radians, cos, sin, asin, sqrt
import rasterio
from matplotlib import pyplot
from rasterio.plot import show
from rasterio.plot import show_hist

def plot(file):
    src = rasterio.open(file)
    show(src)

def plot_contour(file):
    src = rasterio.open(file)
    fig, ax = pyplot.subplots(1, figsize=(12, 12))
    show((src, 1), cmap='Greys_r', interpolation='none', ax=ax)
    show((src, 1), contour=True, ax=ax)
    pyplot.show()

def plot_hist(file, bin=50, title="Histogram"):
    src = rasterio.open(file)
    show_hist(
    src, bins=bin, lw=0.0, stacked=False, alpha=0.3,
    histtype='stepfilled', title=title)

    
def haversine(lon1: float, lat1: float, lon2: float, lat2: float) -> float:

    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers
    return c * r


