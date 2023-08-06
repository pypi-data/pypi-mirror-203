import inspect
from byebyelogger.style.color import LIGHTGREEN_EX


def get_class_name_from_stack():
    """Retrieve the class name from the current call stack.

    Returns:
        str: The class name from the current call stack.
    """
    stack = inspect.stack()
    for frame_info in reversed(stack):
        frame = frame_info.frame
        if "self" in frame.f_locals:
            name = frame.f_locals["self"].__class__.__name__
            return LIGHTGREEN_EX(name.upper())
        elif "cls" in frame.f_locals:
            name = frame.f_locals["cls"].__name__
            return LIGHTGREEN_EX(name.upper())
    return None


def get_method_name_from_stack():
    """Retrieve the method name from the current call stack.

    Returns:
        str: The method name from the current call stack.
    """
    stack = inspect.stack()
    for frame_info in reversed(stack):
        frame = frame_info.frame
        method_name = frame.f_code.co_name
        if "self" in frame.f_locals or "cls" in frame.f_locals:
            if method_name not in [
                "<module>",
                "get_class_name_from_stack",
                "get_method_name_from_stack",
            ]:
                return LIGHTGREEN_EX(method_name.upper())
    return None
