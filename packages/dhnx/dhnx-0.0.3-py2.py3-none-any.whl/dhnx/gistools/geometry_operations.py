# -*- coding: utf-8 -*-

"""
This modules holds functions for geometry operations, that are needed for
the geometry processing module `connect_points.py`.

This file is part of project dhnx (). It's copyrighted
by the contributors recorded in the version control history of the file,
available from its original location: https://github.com/oemof/DHNx

This module is not fully tested yet, so use it with care.

SPDX-License-Identifier: MIT
"""

try:
    import geopandas as gpd

except ImportError:
    print("Need to install geopandas to process geometry data.")

try:
    from shapely import wkt
    from shapely.geometry import LineString
    from shapely.geometry import MultiLineString
    from shapely.geometry import Point
    from shapely.geometry import mapping
    from shapely.ops import linemerge
    from shapely.ops import nearest_points
    from shapely.ops import unary_union
except ImportError:
    print("Need to install shapely to process geometry.")

import logging

import matplotlib.pyplot as plt
import pandas as pd


def create_forks(lines):
    """
    Creates a forks(nodes) GeoDataFrame from a "line"-GeoDataFrame
    based on the end-points of each LineString.

    Also, an index for every fork is given, and the columns 'full-id' (="forks-" + index"),
    'lat' and 'lon', which results from the geometry, are added to the GeoDataFrame.

    Parameters
    ----------
    lines : geopandas.GeoDataFrame

    Returns
    -------
    geopandas.GeoDataFrame : GeoDataFrame with Points as geometry.

    """
    nodes = gpd.GeoDataFrame(geometry=[], crs=lines.crs)

    for _, j in lines.iterrows():
        geom = j['geometry']
        p_0 = Point(geom.boundary.geoms[0])
        p_1 = Point(geom.boundary.geoms[-1])
        nodes = pd.concat(
            [nodes, gpd.GeoDataFrame(geometry=[p_0, p_1], crs=lines.crs)],
            ignore_index=True)

    # transform geometry into wkt
    nodes["geometry_wkt"] = nodes["geometry"].apply(lambda geom: geom.wkt)

    # drop duplicates of geometry column
    nodes = nodes.drop_duplicates(["geometry_wkt"])

    # create shapely geometry again
    nodes["geometry"] = nodes["geometry_wkt"].apply(
        lambda geom: wkt.loads(geom))  # pylint: disable=unnecessary-lambda

    # set index for forks
    nodes = nodes.reset_index(drop=True)
    nodes['id'] = nodes.index
    nodes['id_full'] = 'forks-' + nodes['id'].apply(str)
    nodes['lat'] = nodes['geometry'].apply(lambda x: x.y)
    nodes['lon'] = nodes['geometry'].apply(lambda x: x.x)
    nodes.set_index('id', drop=True, inplace=True)

    return nodes


def insert_node_ids(lines, nodes):
    """
    Creates the columns `from_node`, `to_node` and inserts
    the node ids (eg. forks-3, consumers-5).
    The updated "line"-GeoDataFrame is returned.

    Parameters
    ----------
    lines : geopandas.GeoDataFrame
    nodes : geopandas.GeoDataFrame

    Returns
    -------
    geopandas.GeoDataFrame
    """

    # add id to gdf_lines for starting and ending node
    # point as wkt
    lines['b0_wkt'] = lines["geometry"].apply(lambda geom: geom.boundary.geoms[0].wkt)
    lines['b1_wkt'] = lines["geometry"].apply(lambda geom: geom.boundary.geoms[-1].wkt)

    lines['from_node'] = lines['b0_wkt'].apply(lambda x: nodes.at[x, 'id_full'])
    lines['to_node'] = lines['b1_wkt'].apply(lambda x: nodes.at[x, 'id_full'])

    lines.drop(axis=1, inplace=True, labels=['b0_wkt', 'b1_wkt'])

    return lines


def check_double_points(gdf, radius=0.001, id_column=None):
    """Check for points, which are close to each other.

    In case, two points are close, the index of the points are printed.

    Parameters
    ----------
    gdf : geopandas.GeoDataFrame
        GeoDataFrame with Points as geometry.
    radius : float
        Maximum distance.
    id_column : str or None
        Column name which should be printed in case of near points.
        If None, the index is printed.

    Returns
    -------
    list : Indices of "near" points.
    """

    l_ids = []
    count = 0

    for r, c in gdf.iterrows():

        point = c['geometry']
        gdf_other = gdf.drop([r])
        other_points = unary_union(gdf_other['geometry'])

        # x1 = nearest_points(point, other_points)[0]
        x2 = nearest_points(point, other_points)[1]

        if point.distance(x2) <= radius:
            l_ids.append(r)

            if id_column is None:
                print_name = r
            else:
                print_name = c[id_column]

            logging.info(
                'Node {} has a near neighbour! '
                'Distance {}'.format(print_name, point.distance(x2))
            )

            count += 1

    if count > 0:
        logging.info('Number of duplicated points: ', count)
    else:
        logging.info(
            'Check passed: No points with a distance closer than {}'.format(radius))

    return l_ids


def gdf_to_df(gdf):
    """Converts a GeoDataFrame to a pandas.DataFrame by deleting the geometry column."""

    df = pd.DataFrame(
        gdf[[col for col in gdf.columns if col != 'geometry']])

    return df


def split_multilinestr_to_linestr(gdf_input):
    """Simplifies GeoDataFrames with LineStrings as geometry.

    The LineStrings (whether LineStrings, or MulitLineStings) are split into
    LineStrings with only two coordinates, one starting and one ending point.

    The other values of the GeoDataFrame are copied to the new rows
    for each row, who's geometry is split.

    Parameters
    ----------
    gdf_lines : geopandas.GeoDataFrame

    Returns
    -------
    geopandas.GeoDataFrame
    """
    gdf_lines = gdf_input.copy()

    new_lines = gpd.GeoDataFrame()

    # first: split MultiLineString into LineStrings
    for i, b in gdf_lines.iterrows():

        geom = b['geometry']

        if geom.geom_type == 'MultiLineString':

            multilinestrings = []

            for line in mapping(geom)["coordinates"]:
                multilinestrings.append(LineString(line))

            for multiline in multilinestrings:
                new_row = b.copy()
                new_row['geometry'] = multiline
                new_lines = pd.concat([new_lines, new_row.to_frame().T],
                                      ignore_index=True, sort=False)

            gdf_lines.drop(index=i, inplace=True)

    gdf_lines = pd.concat([gdf_lines, new_lines], ignore_index=True,
                          sort=False)

    gdf_lines['geometry'].crs = gdf_input.crs

    # second: split LineStrings into single Linestrings
    new_lines = gpd.GeoDataFrame()
    for i, b in gdf_lines.iterrows():

        geom = b['geometry']

        if len(geom.coords) > 2:

            num_new_lines = len(geom.coords) - 1

            for num in range(num_new_lines):
                new_row = b.copy()
                new_row['geometry'] = \
                    LineString([geom.coords[num], geom.coords[num + 1]])
                new_lines = pd.concat([new_lines, new_row.to_frame().T],
                                      ignore_index=True, sort=False)

            gdf_lines.drop(index=i, inplace=True)

    gdf_lines = pd.concat([gdf_lines, new_lines], ignore_index=True,
                          sort=False)

    gdf_lines['geometry'].crs = gdf_input.crs

    return gdf_lines


def weld_segments(gdf_line_net, gdf_line_gen, gdf_line_houses,
                  debug_plotting=False):
    """Weld continuous line segments together and cut loose ends.

    This is a public function that recursively calls the internal function
    weld_line_segments_(), until the problem cannot be simplified further.

    Find all lines that only connect to one other line and connect those
    to a single MultiLine object. Points that connect to Generators and
    Houses are not simplified. Loose ends are shortened where possible.

    Parameters
    ----------
    gdf_line_net : GeoDataFrame
        Potential pipe network.
    gdf_line_gen : GeoDataFrame
        Generators that need to be connected.
    gdf_line_houses : GeoDataFrame
        Houses that need to be connected.
    debug_plotting : bool, optional
        Plot the selection process.

    Returns
    -------
    gdf_line_net_new : GeoDataFrame
        Simplified potential pipe network.

    """
    gdf_line_net_last = gdf_line_net
    gdf_line_net_new = _weld_segments(gdf_line_net, gdf_line_gen,
                                      gdf_line_houses, debug_plotting)
    # Now do all of this recursively
    while len(gdf_line_net_new) < len(gdf_line_net_last):
        logging.info('Welding lines... reduced from {} to {} lines'.format(
            len(gdf_line_net_last), len(gdf_line_net_new)))
        gdf_line_net_last = gdf_line_net_new
        gdf_line_net_new = _weld_segments(gdf_line_net_new, gdf_line_gen,
                                          gdf_line_houses, debug_plotting)
    return gdf_line_net_new


def _weld_segments(gdf_line_net, gdf_line_gen, gdf_line_houses,
                   debug_plotting=False):
    """Weld continuous line segments together and cut loose ends.

    Find all lines that only connect to one other line and connect those
    to a single MultiLine object. Points that connect to Generators and
    Houses are not simplified. Loose ends are shortened where possible.

    Parameters
    ----------
    gdf_line_net : GeoDataFrame
        Potential pipe network.
    gdf_line_gen : GeoDataFrame
        Generators that need to be connected.
    gdf_line_houses : GeoDataFrame
        Houses that need to be connected.
    debug_plotting : bool, optional
        Plot the selection process.

    Returns
    -------
    gdf_line_net_new : GeoDataFrame
        Simplified potential pipe network.

    """
    crs = gdf_line_net.crs
    gdf_line_net_new = gpd.GeoDataFrame(geometry=[], crs=crs)
    gdf_merged_all = gpd.GeoDataFrame(geometry=[], crs=crs)
    gdf_deleted = gpd.GeoDataFrame(geometry=[], crs=crs)
    # Merge generator and houses line DataFrames to 'external' lines
    gdf_line_ext = pd.concat([gdf_line_gen, gdf_line_houses])

    for _, b in gdf_line_net.iterrows():
        def debug_plot(neighbours, color='red'):
            """Plot base map, current segment (with color) and neighbours."""
            if debug_plotting:
                _, ax = plt.subplots(1, 1, dpi=300)
                gdf_line_net.plot(ax=ax, color='blue')
                gdf_line_ext.plot(ax=ax, color='green')
                if len(neighbours) > 0:  # Prevent empty plot warning
                    neighbours.plot(ax=ax, color='orange')
                gpd.GeoDataFrame(geometry=[geom]).plot(ax=ax, color=color)

        geom = b.geometry  # The current line segment
        gdf_b = gpd.GeoDataFrame(b.to_frame().T, crs=crs)

        if any_check(geom, gdf_merged_all, how='within'):
            # Drop this object, because it is contained within a merged object
            continue  # Continue with the next line segment

        # Find all neighbours of the current segment
        mask_neighbours = [geom.touches(g) for g in gdf_line_net.geometry]
        neighbours = gdf_line_net[mask_neighbours]
        # If all of the neighbours intersect with each other, it is the
        # last segement before an intersection, which can be removed
        for neighbour in neighbours.geometry:
            if all([neighbour.intersects(g) for g in neighbours.geometry]):
                # Treat as if there was only one neighbour (like end segment)
                neighbours = gpd.GeoDataFrame(geometry=[neighbour], crs=crs)
                break

        if len(neighbours) <= 1:
            # This is a potentially unused end segment
            unused = True

            # Test if one end touches an 'external' line, while the other
            # end touches a network line segment
            p1 = geom.boundary.geoms[0]
            p2 = geom.boundary.geoms[-1]
            p1_neighbours = [p1.intersects(g) for g in neighbours.geometry]
            p2_neighbours = [p2.intersects(g) for g in neighbours.geometry]
            if (any_check(p1, gdf_line_ext, how='touches')
               and p2_neighbours.count(True) > 0):
                unused = False
            elif (any_check(p2, gdf_line_ext, how='touches')
                  and p1_neighbours.count(True) > 0):
                unused = False

            if unused:
                # If truly unused, we can discard it to simplify the network
                debug_plot(neighbours, color='white')
                gdf_deleted = pd.concat([gdf_deleted, gdf_b],
                                        ignore_index=True)
            else:
                # Keep it, if it touches a generator or a house
                debug_plot(neighbours, color='black')
                gdf_line_net_new = pd.concat([gdf_line_net_new, gdf_b],
                                             ignore_index=True)
            continue  # Continue with the next line segment

        if len(neighbours) > 2:
            # This segment has more than two neighbours. This means it is
            # part of an intersection, which we do not simplify futher.
            # However, we can check if either endpoint of the current segment
            # only has one neighbour. Then that one can still be merged.
            p1 = geom.boundary.geoms[0]
            p2 = geom.boundary.geoms[-1]
            p1_neighbours = [p1.intersects(g) for g in neighbours.geometry]
            p2_neighbours = [p2.intersects(g) for g in neighbours.geometry]
            if p1_neighbours.count(True) == 1:  # Only one neighbour allowed
                neighbours = neighbours[p1_neighbours]  # Neighbour to merge
            elif p2_neighbours.count(True) == 1:  # Only one neighbour allowed
                neighbours = neighbours[p2_neighbours]  # Neighbour to merge
            else:  # Keep this segment. Multiple lines meet at an intersection
                gdf_line_net_new = pd.concat([gdf_line_net_new, gdf_b],
                                             ignore_index=True)
                debug_plot(neighbours, color='green')
                continue  # Continue with the next line segment

        if len(neighbours) == 2:
            # There are excactly two separate neighbours that can be merged
            pass  # Run the rest of the loop

        # Before merging, we need to futher clean up the list of neighbours
        neighbours_list = []
        for neighbour in neighbours.geometry:
            if any_check(neighbour, gdf_deleted, how='equals'):
                continue  # Do not use neighbour that has already been deleted
            if any_check(neighbour, gdf_line_net_new, how='within'):
                continue  # Prevent creating dublicates
            if any_check(neighbour, gdf_line_ext, how='intersects'):
                mask = [neighbour.intersects(g) for g in gdf_line_ext.geometry]
                houses = gdf_line_ext[mask]
                # Neighbour intersects with external, but geom does not
                if all([geom.disjoint(g) for g in houses.geometry]):
                    neighbours_list.append(neighbour)
                else:  # No not merge neighbour intersecting with external
                    continue
            elif any_check(neighbour, neighbours, how='touches'):
                neighbours_list = []  # The two neighbours touch
                break  # This is a intersection that cannot be simplified
            else:  # Choose neighbour for merging
                neighbours_list.append(neighbour)
        neighbours = gpd.GeoDataFrame(geometry=neighbours_list, crs=crs)

        if len(neighbours) == 0:
            # If no neighbours are left now, continue with next line segment
            gdf_line_net_new = pd.concat([gdf_line_net_new, gdf_b],
                                         ignore_index=True)
            continue

        # Create list of all elements that should be merged
        lines = [geom] + list(neighbours.geometry)
        try:  # Works when all elements are LineStrings
            # Combine lines into a multi-linestring
            multi_line = MultiLineString(lines)
        except NotImplementedError:  # Fails if there is a MultiLineString
            lines_ = []  # Create a new list of lines, without MultiLineStrings
            for line in lines:
                if line.type == 'MultiLineString':
                    lines_ += list(line)  # Split the MultiLineString
                else:  # Linestring
                    lines_.append(line)
            # Now combine all of those into MultiLineString
            multi_line = MultiLineString(lines_)

        # Merge the MultiLineString into a single object
        merged_line = linemerge(multi_line)
        gdf_merged = gpd.GeoDataFrame(geometry=[merged_line], crs=crs)
        debug_plot(neighbours)  # Plot the segments before the merge
        debug_plot(gdf_merged, color='orange')  # ...and after the merge
        gdf_line_net_new = pd.concat([gdf_line_net_new, gdf_merged],
                                     ignore_index=True)
        gdf_merged_all = pd.concat([gdf_merged_all, gdf_merged],
                                   ignore_index=True)

    return gdf_line_net_new


def any_check(geom_test, gdf, how):
    """Improve speed for an 'any()' test on a list comprehension.

    Replace a statement like...

    .. code::

        if any([geom_test.touches(g) for g in gdf.geometry]):

    ... with the following:

    .. code::

        if any_check(geom_test, gdf, how='touches'):

    Instead of iterating through all of 'g in gdf.geometry', return
    'True' after the first match.

    Parameters
    ----------
    geom_test : Shapely object
        Object which's function 'how' is called.
    gdf : GeoDataFrame
        All geometries in gdf are passed to 'how'.
    how : str
        Shapely object function like equals, almost_equals,
        contains, crosses, disjoint, intersects, touches, within.

    Returns
    -------
    bool
        True if any call of function 'how' is True.

    """
    for g in gdf.geometry:
        method_to_call = getattr(geom_test, how)
        result = method_to_call(g)
        if result:  # Return once the first result is True
            return True
    return False


def check_crs(gdf, crs=4647):
    """Convert CRS to EPSG:4647 - ETRS89 / UTM zone 32N (zE-N).

    This is the (only?) Coordinate Reference System that gives the correct
    results for distance calculations.


    """
    if gdf.crs.to_epsg() != crs:
        gdf.to_crs(epsg=crs, inplace=True)
        logging.info('CRS of GeoDataFrame converted to EPSG:{0}'.format(crs))

    return gdf
