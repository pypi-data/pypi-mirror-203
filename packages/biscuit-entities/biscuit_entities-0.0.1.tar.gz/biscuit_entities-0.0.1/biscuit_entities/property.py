from datetime import datetime
from uuid import UUID

class Property:
    literals = set([ int, str, bool, float, UUID, datetime ])

    def __init__(self, prop_name, prop_type, prop_subtype=None, required_prop=True):
        self.name = prop_name
        self.type = prop_type
        self.subtype = prop_subtype
        self.required = required_prop

    def cast_as_literal(literal_type, value):
        if type(value) == literal_type:
            return value
        elif literal_type == datetime and type(value) == str:
            return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
        else: 
            return literal_type(value)