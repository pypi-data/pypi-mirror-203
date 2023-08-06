import datetime
import os

import lxml.etree as ET
import numpy as np
import shapely.ops
import shapely.wkt
from shapely.geometry import LinearRing, Polygon

# For IW mode, one burst has a duration of ~2.75 seconds and a burst
# overlap of approximately ~0.4 seconds.
# https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-1
# Additional precision calculated from averaging the differences between
# burst sensing starts in prototyping test data
BURST_INTERVAL = 2.758277
ESA_TRACK_BURST_ID_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data/sentinel1_track_burst_id.txt"

def get_info(annotation_path):
    track_burst_num = get_track_burst_num()
    _, tail = os.path.split(annotation_path)
    platform_id, swath_name, _, pol = [x.upper() for x in tail.split("-")[:4]]
    with open(annotation_path, "r") as f:
        tree = ET.parse(f)

    image_info_element = tree.find("imageAnnotation/imageInformation")
    ascending_node_time = as_datetime(image_info_element.find("ascendingNodeTime").text)

    orbit_number = int(tree.find("adsHeader/absoluteOrbitNumber").text)
    orbit_number_offset = 73 if platform_id == "S1A" else 202
    track_number = (orbit_number - orbit_number_offset) % 175 + 1

    boundary_pts = get_boundaries(tree)
    burst_list_elements = tree.find("swathTiming/burstList")

    burst_ids = []
    for i, burst_list_element in enumerate(burst_list_elements):
        # get burst timing
        sensing_time = as_datetime(burst_list_element.find("sensingTime").text)
        dt = sensing_time - ascending_node_time
        # local burst_num within one track, starting from 0
        burst_num = int((dt.seconds + dt.microseconds / 1e6) // BURST_INTERVAL)

        # convert the local burst_num to the global burst_num, starting from 1
        burst_num += track_burst_num[track_number][0]

        burst_id = f"t{track_number:03d}_{burst_num:06d}_{swath_name.lower()}"
        burst_ids.append(burst_id)
    return burst_ids, boundary_pts


def as_datetime(t_str):
    """Parse given time string to datetime.datetime object.

    Parameters:
    ----------
    t_str : string
        Time string to be parsed. (e.g., "2021-12-10T12:00:0.0")
    fmt : string
        Format of string provided. Defaults to az time format found in annotation XML.
        (e.g., "%Y-%m-%dT%H:%M:%S.%f").

    Returns:
    ------
    _ : datetime.datetime
        datetime.datetime object parsed from given time string.
    """
    return datetime.datetime.fromisoformat(t_str)


def get_boundaries(tree):
    """Parse grid points list and calculate burst center lat and lon

    Parameters:
    -----------
    tree : Element
        Element containing geolocation grid points.

    Returns:
    --------
    center_pts : list
        List of burst centroids ass shapely Points
    boundary_pts : list
        List of burst boundaries as shapely Polygons
    """
    # find element tree
    grid_pt_list = tree.find("geolocationGrid/geolocationGridPointList")

    # read in all points
    n_grid_pts = int(grid_pt_list.attrib["count"])
    lines = np.empty(n_grid_pts)
    pixels = np.empty(n_grid_pts)
    lats = np.empty(n_grid_pts)
    lons = np.empty(n_grid_pts)
    for i, grid_pt in enumerate(grid_pt_list):
        lines[i] = int(grid_pt[2].text)
        pixels[i] = int(grid_pt[3].text)
        lats[i] = float(grid_pt[4].text)
        lons[i] = float(grid_pt[5].text)

    unique_line_indices = np.unique(lines)
    n_bursts = len(unique_line_indices) - 1
    boundary_pts = [[]] * n_bursts

    # zip lines numbers of bursts together and iterate
    for i, (ln0, ln1) in enumerate(
        zip(unique_line_indices[:-1], unique_line_indices[1:])
    ):
        # create masks for lines in current burst
        mask0 = lines == ln0
        mask1 = lines == ln1

        # reverse order of 2nd set of points so plots of boundaries
        # are not connected by a diagonal line
        burst_lons = np.concatenate((lons[mask0], lons[mask1][::-1]))
        burst_lats = np.concatenate((lats[mask0], lats[mask1][::-1]))

        poly = Polygon(zip(burst_lons, burst_lats))
        boundary_pts[i] = check_dateline(poly)[0]

    return boundary_pts


def check_dateline(poly):
    """Split `poly` if it crosses the dateline.
    Parameters
    ----------
    poly : shapely.geometry.Polygon
        Input polygon.
    Returns
    -------
    polys : list of shapely.geometry.Polygon
         A list containing: the input polygon if it didn't cross
        the dateline, or two polygons otherwise (one on either
        side of the dateline).
    """

    xmin, _, xmax, _ = poly.bounds
    # Check dateline crossing
    if (xmax - xmin) > 180.0:
        dateline = shapely.wkt.loads("LINESTRING( 180.0 -90.0, 180.0 90.0)")

        # build new polygon with all longitudes between 0 and 360
        x, y = poly.exterior.coords.xy
        new_x = (k + (k <= 0.0) * 360 for k in x)
        new_ring = LinearRing(zip(new_x, y))

        # Split input polygon
        # (https://gis.stackexchange.com/questions/232771/splitting-polygon-by-linestring-in-geodjango_)
        merged_lines = shapely.ops.linemerge([dateline, new_ring])
        border_lines = shapely.ops.unary_union(merged_lines)
        decomp = shapely.ops.polygonize(border_lines)

        polys = list(decomp)
        assert len(polys) == 2
    else:
        # If dateline is not crossed, treat input poly as list
        polys = [poly]

    return polys


def get_track_burst_num(track_burst_num_file: str = ESA_TRACK_BURST_ID_FILE):
    """Read the start / stop burst number info of each track from ESA.

    Parameters:
    -----------
    track_burst_num_file : str
        Path to the track burst number files.

    Returns:
    --------
    track_burst_num : dict
        Dictionary where each key is the track number, and each value is a list
        of two integers for the start and stop burst number
    """

    # read the text file to list
    track_burst_info = np.loadtxt(track_burst_num_file, dtype=int)

    # convert lists into dict
    track_burst_num = dict()
    for track_num, burst_num0, burst_num1 in track_burst_info:
        track_burst_num[track_num] = [burst_num0, burst_num1]

    return track_burst_num
