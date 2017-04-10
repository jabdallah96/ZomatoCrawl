from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Identity, Join
import unicodedata
import re

class Restaurant(Item):

    r_name = Field()
    r_id = Field()
    r_type = Field()
    r_address = Field()
    city = Field()
    link = Field()
    cost = Field()
    area = Field()
    rating = Field()
    rating_votes = Field()
    cuisines = Field()
    collections = Field()
    r_latitude = Field()
    r_longitude = Field()
    r_image = Field()
    r_tel = Field()
    r_timing = Field()

def unicode_convert(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')

def int_convert(x):
    try:
        return int(x)
    except ValueError:
        return None

def float_convert(x):
    try:
        return float(x)
    except ValueError:
        return None



class RestItemLoader(ItemLoader):
    default_input_processor = MapCompose(unicode_convert)
    default_output_processor = TakeFirst()

    r_id_in = MapCompose(int_convert)

    link_in = Identity()

    city_in = MapCompose(str.capitalize)

    cost_in = MapCompose(str.strip)

    rating_in = MapCompose(str.strip)
    
    r_name_in = MapCompose(str.strip)
    
    area_in = MapCompose(str.strip)
        
    r_type_in = MapCompose(str.strip)

    cuisines_in = MapCompose(str.strip)

    collections_in = MapCompose(str.strip)

    rating_votes_in = MapCompose(int_convert)

    cuisines_out = Identity()
    
    collections_out = Identity()

    r_address_in = MapCompose(str.strip)
    
    r_latitude_in = MapCompose(float_convert)
    
    r_longitude_in = MapCompose(float_convert)

    r_image_in = MapCompose(str.strip)

    r_tel_in = MapCompose(str.strip)

    r_timing_in = MapCompose(str.strip)








