# Dagli open data di fabriano a LATLON

ogr2ogr wgs84 farmacie_sed.shp -s_srs EPSG:3004 -t_srs EPSG:4326
