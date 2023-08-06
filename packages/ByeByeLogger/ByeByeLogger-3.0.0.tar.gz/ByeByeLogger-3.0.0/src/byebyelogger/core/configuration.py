from dataclasses import dataclass, field
from typing import Callable, Dict, List, Protocol, Tuple, Union


from byebyelogger.style.format import SQUARE_BRACKETS


@dataclass
class LoggerConfiguration:
    """
    A dataclass representing the configuration of a logger.

    Attributes:
        attributes (Dict[str, Tuple[Union[str, Callable], str]]): A dictionary that maps attribute names to
            tuples containing their values and styles.
        order (List[str]): A list that defines the order in which attributes appear in the log output.
        separator (str): The string used to separate attributes in the log output.
        default_style (str): The default style to be applied to attributes that don't have a specific style.
    """
    attributes: Dict[str, Tuple[Union[str, Callable], str]] = field(
        default_factory=dict
    )
    order: List[str] = field(default_factory=list)
    separator: str = " - "
    default_style: str = ""

    def __post_init__(self):
        if self.default_style:
            self.set_style(self.default_style)

    def add(self, value: Union[str, Callable], style: str = None):
        name = str(value)
        if style is None:
            style = SQUARE_BRACKETS  # sets  on default style
        self.attributes[name] = (value, style)
        self.order.append(name)

    def set_order(self, order: List[str]):
        self.order = order

    def set_style(self, style: str):
        self.default_style = style

    def apply_style(self, style: str, text: str):
        return style.format(text)

    def log(self):
        formatted_attributes = []
        for attr in self.order:
            value, style = self.attributes[attr]
            if callable(value):
                value = value()
            formatted_value = self.apply_style(
                style, str(value)
            )  # konvertiert Wert zu String
            formatted_attributes.append(formatted_value)

        log_entry = self.separator.join(formatted_attributes)
        print(log_entry, end=" ")

class Preset(Protocol):
    """
    A protocol defining the log method to be implemented by logger presets.
    """
    def log(self):
        pass

class Logger:
    """
    A class that creates a logger instance with a specified preset.

    Args:
        logging (Preset): An instance of a logging preset that implements the `Preset` protocol.

    Methods:
        log(msg: str): Logs a message using the specified preset.
    """
    
    def __init__(self, logging: Preset):
        self.logging = logging

    def log(self, msg: str):
        self.logging.log()
        print(msg)
