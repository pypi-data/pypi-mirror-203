import os

def get_ome_schema_path():
    schema_path = os.path.join(os.path.dirname(__file__), "schemas", "2016-06", "ome.xsd")
    return schema_path
