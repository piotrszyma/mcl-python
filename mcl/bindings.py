import ctypes
import inspect

from . import hook, utils

MCL_NAME = "__mcl_name__"


def is_mcl_method(obj):
    return inspect.ismethod(obj) and hasattr(obj, MCL_NAME)


def method_binding(method_name=None):
    def decorator(method_obj):
        setattr(method_obj, MCL_NAME, method_name or method_obj.__name__)
        return method_obj

    return decorator


def _build_mcl_ctypes_binding(method_obj, mcl_method_name, klass_instance):
    wrapper = utils.wrap_function(
        hook.mclbls12_384,
        mcl_method_name,
        [
            ctypes.POINTER(klass_instance),
            ctypes.c_char_p,
            ctypes.c_size_t,
            ctypes.c_int64,
        ],
    )
    return wrapper


def class_binding():
    def decorator(klass_instance):
        method_name_obj_pairs = inspect.getmembers(
            klass_instance, predicate=is_mcl_method
        )

        for method_name, method_obj in method_name_obj_pairs:
            mcl_method_name = getattr(method_obj, MCL_NAME)
            setattr(
                klass_instance,
                method_name,
                _build_mcl_ctypes_binding(method_obj, mcl_method_name, klass_instance),
            )

        return klass_instance

    return decorator
