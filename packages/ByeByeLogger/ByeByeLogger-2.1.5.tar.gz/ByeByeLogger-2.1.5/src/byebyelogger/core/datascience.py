import inspect
from byebyelogger.core.repository import CustomLogger, LogRepository

from byebyelogger.style.colorizer import LIGHTCYAN_EX, LIGHTGREEN_EX, LIGHTRED_EX
from byebyelogger.style.constants import SQUARE_BRACKETS

def get_class_name_from_stack():
    stack = inspect.stack()
    for frame_info in reversed(stack):
        frame = frame_info.frame
        if 'self' in frame.f_locals:
            name = frame.f_locals['self'].__class__.__name__
            return LIGHTGREEN_EX(name.upper())
        elif 'cls' in frame.f_locals:
            name = frame.f_locals['cls'].__name__
            return LIGHTGREEN_EX(name.upper())
    return None

def get_method_name_from_stack():
    stack = inspect.stack()
    for frame_info in reversed(stack):
        frame = frame_info.frame
        method_name = frame.f_code.co_name
        if 'self' in frame.f_locals or 'cls' in frame.f_locals:
            if method_name not in ['<module>', 'get_class_name_from_stack', 'get_method_name_from_stack']:
                return LIGHTGREEN_EX(method_name.upper())
    return None


custom = CustomLogger(order=["class_name", "method_name", "level"], default_style=SQUARE_BRACKETS)
custom.add(name="class_name", value=lambda: get_class_name_from_stack())
custom.add(name="method_name", value=lambda: get_method_name_from_stack())
custom.add(name="level", value="INFO")


PRESET_INFO = custom.copy()
PRESET_INFO.attributes["level"] = (LIGHTCYAN_EX("INFO"), SQUARE_BRACKETS)

INFO = LogRepository(PRESET_INFO)

PRESET_ERROR = custom.copy()
PRESET_ERROR.attributes["level"] = (LIGHTRED_EX("ERROR"), SQUARE_BRACKETS)

ERROR = LogRepository(PRESET_ERROR)

