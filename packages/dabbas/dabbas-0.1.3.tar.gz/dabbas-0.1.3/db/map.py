import geopandas as gpd
from shapely.geometry import Point, Polygon, MultiPolygon, shape
from shapely import wkt, wkb
import folium
from pandas import *
import pandas as pd
from pandas_flavor import register_dataframe_method, register_dataframe_accessor
from .connection import connection_url


def create_marker_icon(color):
    # Define a function to create a custom marker icon
    return folium.Icon(
        color=color,
        icon="circle",
        prefix="fa"
    )


def force_dataset(self, df):
    print(df)
    if isinstance(df, DataFrame):
        return Dataset(df, latitude=self.latitude_col, longitude=self.longitude_col, feature=self.feature_col, geometry=self.geometry_col, format=self.geometry_format, **self.kwargs)

    return df


def force_dataset_fn(fun):
    """Turn from Dataframe- to Dataset-instance-returning function."""

    def wrapper(self, *args, **kwargs):
        print('running wrapped', fun, args, kwargs)
        result = fun(self, *args, **kwargs)
        print('running wrapped', fun, result, args, kwargs)
        return force_dataset(self, result)
    return wrapper


class DatasetFromDataFrame(type):
    def __new__(cls, name, bases, dct):
        child = super().__new__(cls, name, bases, dct)
        for base in bases:
            for field_name, field in base.__dict__.items():
                if callable(field):
                    if field_name not in dct:
                        print(field_name)
                        setattr(child, field_name, force_dataset_fn(field))
        return child


def marker(location, color='red', popup=None, tooltip=None):
    return folium.Marker(location=location, icon=create_marker_icon(color), popup=popup, tooltip=tooltip)


def read_csv(file, latitude='latitude', longitude='longitude', geometry='geometry', format='wkt', **kwargs):
    csv = pd.read_csv(file, **kwargs)
    try:
        return csv.geo(latitude=latitude, longitude=longitude, geometry=geometry, format=format, **kwargs)
    except Exception as e:
        print(e)
        return csv


def read_sql(sql, con=connection_url(), latitude='latitude', longitude='longitude', geometry='geom', format='wkb', **kwargs):
    sql = pd.read_sql(sql, con, **kwargs)
    try:
        return sql.geo(latitude=latitude, longitude=longitude, geometry=geometry, format=format, **kwargs)
    except Exception as e:
        print(e)
        return sql


@register_dataframe_accessor("geo")
class GeoDataFrameAccessor():
    def __init__(self, df):
        self._df = df

    def __call__(self, *args, **kwargs):
        self._df = create_geometry_column(self._df, *args, **kwargs)
        return gpd.GeoDataFrame(self._df, crs='EPSG:4326')


format_map = {
    'geojson': shape,
    'wkt': wkt.loads,
    'wkb': wkb.loads,
    '': lambda x: x
}


def create_geometry_column(df: pd.DataFrame, format='', geometry='geometry', latitude='latitude', longitude='longitude'):
    df = df.copy()
    if len(df) == 0:
        raise Exception('No data in Dataset to create geometry')

    if geometry in df:
        if format in format_map:
            df.loc[:, 'geometry'] = df.loc[:,
                                           geometry].apply(format_map[format])
        else:
            df.loc[:, 'geometry'] = df.loc[:, geometry]
    elif longitude in df and latitude in df:
        df.loc[:, longitude] = df[longitude].apply(
            lambda x: '0.0' if x == '' or x is None else x)
        df.loc[:, latitude] = df[latitude].apply(
            lambda x: '0.0' if x == '' or x is None else x)
        geom = [Point(xy) for xy in zip(
            df[longitude], df[latitude])]
        df.loc[:, 'geometry'] = geom

    return df

    # # Create a GeoDataFrame from the DataFrame
    # gdf = gpd.GeoDataFrame(df, crs='EPSG:4326')
    # return gdf


@register_dataframe_method
def map_it(df: pd.DataFrame, format='', tooltip='name', geometry='geometry', map=None, color='green', zoom_level=5, center=[20.5937, 78.9629]):
    if isinstance(df, gpd.GeoDataFrame):
        gdf = df
    else:
        gdf = df.geo(format)

    _map = map if map is not None else folium.Map(
        location=center, zoom_start=zoom_level)
    errs = []
    # Add the points to the map
    for idx, row in gdf.iterrows():
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

# class GeoDataFrameAccessor:
#     def __init__(self, df):
#         self._df = df

#     def is_old_lady(self):
#         df = self._df
#         is_lady = df["Sex"] == "female"
#         is_old = df["Age"] > 70
#         return df[is_old & is_lady]


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

    # def __getitem__(self, key):
    #     if isinstance(key, slice):
    #         return self.loc[key]
    #     df = super().__getitem__(key)
    #     if isinstance(df, pd.DataFrame):
    #         return Dataset(df, latitude=self.latitude_col, longitude=self.longitude_col, feature=self.feature_col, geometry=self.geometry_col, format=self.geometry_format, **self.kwargs)
    #     else:
    #         return df

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
        return Dataset(self.df[key], latitude=self.ds.latitude_col, longitude=self.ds.longitude_col,
                       feature=self.ds.feature_col, geometry=self.ds.geometry_col, format=self.ds.geometry_format,
                       **self.ds.kwargs)
