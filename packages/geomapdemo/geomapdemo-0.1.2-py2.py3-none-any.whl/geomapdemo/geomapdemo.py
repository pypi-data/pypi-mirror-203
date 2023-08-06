"""Main module."""

import random
import string
import ipyleaflet



class Map(ipyleaflet.Map):

    def __init__(self, center = [40, -100], zoom = 4, **kwargs) -> None:
        """Initializes the map
        Args:
            center (tuple): The center of the map. e.g [lat, lon]. Defaults to [40, -100].
            zoom (int): The zoom level of the map. Defaults to 4.
            **kwargs: Keyword arguments to be passed to the map.
        """
        if "scroll_wheel_zoom" not in kwargs:
            """Enables scroll wheel zoom by default"""
            kwargs["scroll_wheel_zoom"] = True

        if "layers_control" not in kwargs:
            """Adds a layers control by default"""
            kwargs["layers_control"] = True

        if kwargs["layers_control"]:
            """Adds a layers control to the map"""
            self.add_layers_control()
        super().__init__(center=center , zoom=zoom, **kwargs)
        
        if "fullscreen_control" not in kwargs:
            """Adds a fullscreen control by default"""
            kwargs["fullscreen_control"] = True
        
        if kwargs["fullscreen_control"]:
            """Adds a fullscreen control to the map"""
            self.add_fullscreen_control()

        if "search_control" not in kwargs:
            """Adds a search control by default"""
            kwargs["search_control"] = True
        
        if kwargs["search_control"]:
            """Adds a search control to the map"""
            self.add_search_control()


    def add_basemap(self, basemap, **kwargs):
        """Adds a basemap to the map
        Args:
            basemap(str): The name of basemap.
            **kwargs: Keyword arguments to be passed to the basemap.
        """

        import xyzservices.providers as xyz

        if basemap.lower() =='roadmap':
            url = 'http://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}'
            self.add_tile_layer(url, basemap, **kwargs)

        elif basemap.lower() =='satellite':
            url = 'http://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}'
            self.add_tile_layer(url, basemap, **kwargs)
        
        elif basemap.lower() =='esri':
            url = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'
            self.add_tile_layer(url, basemap, **kwargs)
        
        else:
            try:
                basemap =eval(f"xyz.{basemap}")
                url=basemap.build_url()
                attribution=basemap.attribution
                self.add_tile_layer(url, name=basemap.name, attribution= attribution, **kwargs)
            except:
                raise ValueError(f"{basemap} is not a valid basemap")




        
    
    def add_tile_layer(self, url, name, attribution="", **kwargs):
        """Adds a tile layer to the map
        Args:
            url (str): The url of the tile layer.
            name (str): The name of the tile layer.
            attribution (str, optional): The attribution of the tile layer. Defaults to "".
            **kwargs: Keyword arguments to be passed to the tile layer.
        """        
        tile_layer = ipyleaflet.TileLayer(url=url, name=name, attribution=attribution, **kwargs)
        self.add_layer(tile_layer)
    

    def add_layers_control(self, position ="topright", **kwargs):
        """Adds a layers control to the map
        Args:
            position (str, optional): The position of the layers control. Defaults to "topright".
            **kwargs: Keyword arguments to be passed to the layers control.
        """        
        layers_control = ipyleaflet.LayersControl(position=position, **kwargs)
        self.add_control(layers_control)
    
    def add_fullscreen_control(self, position ="topright", **kwargs):
        """Adds a fullscreen control to the map
        Args:
            position (str, optional): The position of the fullscreen control. Defaults to "topright".
            **kwargs: Keyword arguments to be passed to the fullscreen control.
        """        
        fullscreen_control = ipyleaflet.FullScreenControl(position=position, **kwargs)
        self.add_control(fullscreen_control)
    
    def add_search_control(self, position ="topleft", **kwargs):
        """Adds a search control to the map
        Args:
            position (str, optional): The position of the search control. Defaults to "topleft".
            **kwargs: Keyword arguments to be passed to the search control.
        """  
        if "url" not in kwargs:
             """Sets the default url for the search control"""
             kwargs["url"] = "https://nominatim.openstreetmap.org/search?format=json&q={s}"    
        search_control = ipyleaflet.SearchControl(position=position, **kwargs)
        self.add_control(search_control)

    def add_draw_control(self, **kwargs):
        """Adds a draw control to the map
        Args:
            **kwargs: Keyword arguments to be passed to the draw control.
        """  
        draw_control = ipyleaflet.DrawControl(**kwargs)

        draw_control.polyline =  {
            "shapeOptions": {
                "color": "#6bc2e5",
                "weight": 8,
                "opacity": 1.0
                }   
            }
        draw_control.polygon = {
                "shapeOptions": {
                    "fillColor": "#6be5c3",
                    "color": "#6be5c3",
                    "fillOpacity": 1.0
                },
                "drawError": {
                    "color": "#dd253b",
                    "message": "Oups!"
                },
                "allowIntersection": False
            }
        draw_control.circle = {
                "shapeOptions": {
                    "fillColor": "#efed69",
                    "color": "#efed69",
                    "fillOpacity": 1.0
                }
            }
        draw_control.rectangle = {
                "shapeOptions": {
                    "fillColor": "#fca45d",
                    "color": "#fca45d",
                    "fillOpacity": 1.0
                }
            }
        self.add_control(draw_control)
    
    def add_geojson(self, data, name ='GeoJson', **kwargs):
        """Adds a geojson to the map
        Args:
            data (dict): The geojson data.
            name (str, optional): The name of the geojson. Defaults to 'GeoJson'.
            **kwargs: Keyword arguments to be passed to the geojson.
        """
        if isinstance(data, str):
            """If the data is a string, it is assumed to be a path to a geojson file"""
            import json
            with open(data, "r") as f:
                data = json.load(f)
          
        geojson = ipyleaflet.GeoJSON(data=data, name=name, **kwargs)
        self.add_layer(geojson)
    
    def add_shp(self, path, name ='Shapefile', **kwargs):
        """Adds a shapefile to the map
        Args:
            path (str): The path to the shapefile.
            name (str, optional): The name of the shapefile. Defaults to 'Shapefile'.
            **kwargs: Keyword arguments to be passed to the shapefile.
        """        
        import geopandas as gpd
        gdf = gpd.read_file(path)
        geojson = gdf.__geo_interface__
        self.add_geojson(geojson, name=name, **kwargs)





def generate_random_string(length=10, upper=False, punctuations=False, digits=False):
    """Generates a random string of fixed length

    Args:
        length (int, optional): The length of the string. Defaults to 10.
        upper (bool, optional): Whether to include uppercase letters. Defaults to False.
        punctuations (bool, optional):Whether to include punctuations. Defaults to False.
        digits (bool, optional): Whether to include digits. Defaults to False.

    Returns:
        str: The generated string.
    """    
    letters = string.ascii_lowercase
    if upper:
        letters += string.ascii_uppercase
    if digits:
        letters += string.digits
    if punctuations:
        letters += string.punctuation
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def generate_lucky_number(length=1):
    """Generates a random number of fixed length

    Args:
        length (int, optional): the length of the number. Defaults to 1.

    Returns:
        int: The generated number.
    """    
    result_str = ''.join(random.choice(string.digits) for i in range(length))
    return int(result_str)