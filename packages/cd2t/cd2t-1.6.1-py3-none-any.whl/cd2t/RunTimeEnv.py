from cd2t.types.datatype import DataType
from cd2t.References import References
from cd2t.schema import SchemaError


class RunTimeEnv():
    def __init__(self) -> None:
        self.namespace = ''
        self.references = References()
        self.data_types = dict()
        self.allow_shortcuts = False

    @staticmethod
    def _check_given_namespace(namespace :str, allow_empty=False) -> None:
        if not isinstance(namespace, str):
            raise ValueError('namespace has to be a string')
        if not allow_empty and len(namespace) == 0:
            raise ValueError('namespace has to be a non empty string')
        
    def change_namespace(self, namespace :str, allow_empty=False) -> None:
        self._check_given_namespace(namespace, allow_empty)
        self.references.change_namespace(namespace)
        self.namespace = namespace

    def load_data_type(self, type_name :str, type_class :any) -> None:
        if type_name in self.data_types.keys():
            raise ValueError("Data type '%s' already loaded" % type_name)
        if not issubclass(type_class, DataType):
            raise ValueError("Loading %s failed - not %s" % (type_class, DataType))
        self.data_types[type_name] = type_class

    def load_data_types(self, data_types :dict) -> None:
        if not isinstance(data_types, dict) :
            raise ValueError("'data_types' must be a dictionary")
        for type_name, type_class in data_types.items():
            self.load_data_type(type_name, type_class)
    
    def get_data_type_class(self, data_type_name: str) -> DataType:
        if data_type_name not in self.data_types:
            raise SchemaError("Data type '%s' not found" % str(data_type_name))
        return self.data_types[data_type_name]
