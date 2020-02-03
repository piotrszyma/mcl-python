import inspect

MCL_NAME = "__mcl_name__"

def is_mcl_method(obj):
    return inspect.ismethod(obj) and hasattr(fn, MCL_NAME)


def method_binding(method_name = None):
    def decorator(fn):
        setattr(fn, MCL_NAME, method_name or fn.__name__)
        return fn

    return method_binding


def class_binding():
    def decorator(cls):
        methods = inspect.getmembers(cls, predicate=is_mcl_method)

        return cls

    return class_binding
