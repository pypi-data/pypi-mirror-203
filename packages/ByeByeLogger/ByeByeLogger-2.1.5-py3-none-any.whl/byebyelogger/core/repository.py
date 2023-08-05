from typing import Protocol, List, Dict, Tuple, Callable, Union
from dataclasses import dataclass, field


@dataclass
class CustomLogger:
    attributes: Dict[str, Tuple[Union[str, Callable], str]] = field(default_factory=dict)
    order: List[str] = field(default_factory=list)
    separator: str = " - "
    default_style: str = ""

    def __post_init__(self):
        if self.default_style:
            self.set_style(self.default_style)

    def add(self, name: str, value: Union[str, Callable], style: str = None):
        if style is None:
            style = self.default_style
        self.attributes[name] = (value, style)

    def set_order(self, order: List[str]):
        self.order = order

    def set_style(self, style: str):
        self.default_style = style

    def apply_style(self, style: str, text: str):
        return style.format(text)

    def copy(self):
        copied_logger = CustomLogger(attributes=self.attributes.copy(),
                                     order=self.order.copy(),
                                     separator=self.separator,
                                     default_style=self.default_style)
        return copied_logger
    
    def log(self):
        formatted_attributes = []
        for attr in self.order:
            value, style = self.attributes[attr]
            if callable(value):
                value = value()
            formatted_value = self.apply_style(style, value)
            formatted_attributes.append(formatted_value)

        log_entry = self.separator.join(formatted_attributes)
        print(log_entry, end=" ")

class Loggable(Protocol):
    def log(self):
        pass

class LogRepository:

    def __init__(self, logging: Loggable):
        self.logging = logging

    def log(self, msg: str):
        self.logging.log()
        print(msg)
        