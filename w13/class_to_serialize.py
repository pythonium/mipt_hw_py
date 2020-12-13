class MyClass:
    def __init__(self, name, surname, is_hired):
        self.name = name
        self.surname = surname
        self.is_hired = is_hired


def obj_to_json(my_class_instance):
    return json.dumps(my_class_instance.__dict__)


def json_to_obj(my_class_instance):

    obj_dict = json.loads(my_class_instance)
    obj = MyClass(**obj_dict)
    return obj
