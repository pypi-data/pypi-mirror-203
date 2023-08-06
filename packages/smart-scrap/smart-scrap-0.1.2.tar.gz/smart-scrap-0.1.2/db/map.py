import geopandas as gpd
from shapely.geometry import Point, Polygon, MultiPolygon, shape
from shapely import wkt
import folium
import pandas as pd


def create_marker_icon(color):
    # Define a function to create a custom marker icon
    return folium.Icon(
        color=color,
        icon="circle",
        prefix="fa"
    )


def marker(location, color='red', popup=None, tooltip=None):
    return folium.Marker(location=location, icon=create_marker_icon(color), popup=popup, tooltip=tooltip)


def read_csv(file, latitude='latitude', longitude='longitude', feature=None, geometry='geometry', format='', **kwargs):
    return Dataset(pd.read_csv(file, **kwargs), latitude=latitude, longitude=longitude, feature=feature, geometry=geometry, format=format, **kwargs)


class Dataset(pd.DataFrame):
    latitude_col: str = 'latitude'
    longitude_col: str = 'longitude'
    geometry_col: str = 'geometry'
    kwargs = {}
    _gdf: gpd.GeoDataFrame = None
    feature_col: str = 'geom'
    geometry_format: str = ''

    def __init__(self, data, latitude='latitude', longitude='longitude', feature=None, geometry='geometry', format='', **kwargs) -> None:
        super().__init__(data, **kwargs)
        self.kwargs = kwargs
        self.latitude_col = latitude
        self.longitude_col = longitude
        self.feature_col = feature
        self.geometry_col = geometry
        self.geometry_format = format

    @property
    def gdf(self):
        if self._gdf is None:
            self._gdf = self._create_gdf()

        return self._gdf

    def _create_gdf(self):
        if len(self) == 0:
            raise Exception('No data in Dataset to create geometry')

        if self.geometry_col in self:
            fn = shape if self.geometry_format == 'geojson' else wkt.loads if self.geometry_format == 'wkt' else None
            if fn is not None:
                self['geometry'] = self[self.geometry_col].apply(fn)
            else:
                self['geometry'] = self[self.geometry_col]
        elif self.feature_col is not None and self.feature_col in self:
            self['geometry'] = self[self.feature_col].apply(shape)
        elif self.longitude_col in self and self.latitude_col in self:
            self[self.longitude_col] = self[self.longitude_col].apply(
                lambda x: '0.0' if x == '' or x is None else x)
            self[self.latitude_col] = self[self.latitude_col].apply(
                lambda x: '0.0' if x == '' or x is None else x)
            geometry = [Point(xy) for xy in zip(
                self[self.longitude_col], self[self.latitude_col])]
            self['geometry'] = geometry

        # Create a GeoDataFrame from the DataFrame
        gdf = gpd.GeoDataFrame(self, crs='EPSG:4326')
        return gdf

    # def map_it(self, tooltip='name', geometry='geometry', color='blue', map=None, zoom_level=5):
    #     map_center = [20.5937, 78.9629]
    #     _map = map if map is not None else folium.Map(location=map_center, zoom_start=zoom_level)
    #     errs = []
    #     # Add the points to the map
    #     for idx, row in self.gdf.iterrows():
    #         if not row[geometry].is_empty:
    #             tooltip = row[name] if name in row else "{},{}".format(
    #                 row[geometry].x, row[geometry].y)
    #             marker(location=[row[geometry].y, row[geometry].x],
    #                           tooltip=tooltip, color=color).add_to(_map)
    #         else:
    #             errs.append(idx)

    #     return _map

    def map_it(self, tooltip='name', geometry='geometry', map=None, color='green', zoom_level=5, center=[20.5937, 78.9629]):
        _map = map if map is not None else folium.Map(
            location=center, zoom_start=zoom_level)
        errs = []
        # Add the points to the map
        for idx, row in self.gdf.iterrows():
            if not row[geometry].is_empty:

                geom = row[geometry]
                if isinstance(geom, Point):
                    if tooltip in row:
                        _tooltip = row[tooltip]
                    elif '{' in tooltip:
                        _tooltip = tooltip.format(**row.to_dict())
                    else:
                        _tooltip = "{},{}".format(
                            row[geometry].x, row[geometry].y)
                    marker(location=[row[geometry].y, row[geometry].x],
                           tooltip=_tooltip, color=color).add_to(_map)
                if isinstance(geom, Polygon) or isinstance(geom, MultiPolygon):
                    folium.GeoJson(data=gpd.GeoSeries(
                        geom).to_json()).add_to(_map)
            else:
                errs.append(idx)

        return _map

    @property
    def loc(self):
        """
        Purely integer-location based indexing for selection by position.

        Parameters:
            row (int): row index
            col (int or str): column index or name

        Returns:
            (scalar) : value of the scalar for the given location
        """
        return DatasetIndex(self, super().iloc)


class DatasetIndex():
    ds: Dataset

    def __init__(self, ds, df) -> None:
        self.ds = ds
        self.df = df

    def __getitem__(self, key):
        return Dataset(self.df[key], latitude=self.ds.latitude_col, longitude=self.ds.longitude_col, **self.ds.kwargs)
