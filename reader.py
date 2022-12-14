# GEO1000 - Assignment 3
# Authors:
# Studentnumbers:

from geometry import Point, Rectangle, Circle
from strips import StripStructure


def read(file_nm, no_strips):
    """Reads a file with on the first uncommented line a bbox 
    (4 numbers separated by a space) and subsequently 0 or more lines with 
    points (2 numbers separated by a space) into a Strip Structure.
    
    If no valid box is found in the input file, it returns None.
    Otherwise a StripStructure with 0 or more points is returned.
    
    Returns - None or a StripStructure instance
    """
    objects = []

    with open(file_nm) as f:
        for line in f:
            if line[0] != "#":
                string_list = line.split()
                float_list = []
                for item in string_list:
                    float_list.append(float(item))
                objects.append(float_list)

    extent = [objects[0][0], objects[0][1], objects[0][2], objects[0][3]]
    if extent[0] < extent[2] and extent[1] < extent[3]:
        structure = StripStructure(extent, no_strips)
        for i in range(1, len(objects)):
            point = Point(objects[i][0], objects[i][1])
            structure.append_point(point)
        # breakpoint()
        return structure
    else:
        return None


def dump(structure, strip_file_nm="strips.wkt", point_file_nm="points.wkt"):
    """Dump the contents of a strip structure to 2 files that can be opened
    with QGIS.
    
    Returns - None
    """
    with open(strip_file_nm, "w") as fh:
        fh.write(structure.dump_strips())
    with open(point_file_nm, "w") as fh:
        fh.write(structure.dump_points())

