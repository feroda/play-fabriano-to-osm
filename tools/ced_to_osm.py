#!/usr/bin/env python

import sys
import shapefile

fmt_changeset = """
<osm>
<changeset>
    <tag k="created_by" v="fero with python" />
    <tag k="comment" v="from city open data to osm" />
    {nodes_string}
</changeset>
</osm>
"""

fmt_node = """
<node lat="{lat}" lon="{lon}">
    <tag k="amenity" v="{kind}" />
    <tag k="name" v="{name}" />
    {tags_string}
</node>
"""


def main(argv):

    if len(argv) < 2:
        print("Usage {0} <shapefile basename>".format(*argv))
        sys.exit(100)

    basename = argv[1]
    sf = shapefile.Reader(basename)


if __name__ == "__main__":
    main(sys.argv)
