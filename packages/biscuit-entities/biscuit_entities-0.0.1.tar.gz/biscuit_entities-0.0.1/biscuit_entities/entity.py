from .property import Property

class Entity:
    properties = []
    queries = []

    def __str__(self):
        serialized = self.serialize()
        serialized_string = str(serialized)

        return serialized_string

    @classmethod
    def build(cls, dict):
        # create a new instance of the class
        instance = cls()

        try:
            # for each value in the dictionary, assign the corresponding value
            # within the object
            for property in cls.properties:
                if property.name not in dict or dict[property.name] is None:
                    if property.required:
                        raise Exception(f"Property '{property.name}' was required, but not found in input.")

                    setattr(instance, property.name, None)
                else:
                    if property.type in Property.literals:
                        setattr(instance, property.name, Property.cast_as_literal(property.type, dict[property.name]))
                    elif property.type == list:
                        property_list = []

                        if dict[property.name] != "{}":
                            for element in dict[property.name]:
                                if property.subtype in Property.literals:
                                    property_list.append(Property.cast_as_literal(property.subtype, element))
                                elif getattr(property.subtype, "build", None):
                                    property_list.append(property.subtype.build(element))

                        setattr(instance, property.name, property_list)

            # return new instance
            return instance
        except Exception as e:
            err_msg = f"Failed to build {cls.__name__} instance. {e}"
            raise Exception(err_msg)
        
    @classmethod
    def build_many(cls, dict):
        insts = []

        for element in dict:
            inst = cls.build(element)
            insts.append(inst)

        return insts

    def serialize(self):
        try:
            dict = {}

            for property in self.__dict__:
                if type(self.__dict__[property]) == list:
                    property_list = []

                    for element in self.__dict__[property]:
                        if getattr(element, "serialize", None):
                            property_list.append(element.serialize())
                        else:
                            property_list.append(element)

                    dict[property] = property_list
                elif getattr(self.__dict__[property], "build", None):
                    dict[property] = self.__dict__[property].serialize()
                else:
                    dict[property] = self.__dict__[property]

            return dict
        except Exception as e:
            err_msg = f"Failed to serialize {self.__class__.__name__} instance. {e}"
            raise Exception(err_msg)