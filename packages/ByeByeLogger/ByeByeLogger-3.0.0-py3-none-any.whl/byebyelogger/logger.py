from typing import List, Tuple, Callable, Union

from byebyelogger.core.configuration import Logger, LoggerConfiguration


def single_logger(color: str, level: str, format: str = None) -> Logger:
    """
    Creates a new logger instance with the specified level color, level name, and optional format.

    Args:
        color (str): The color to be applied to the level name. To import colors, for example, use:
                     "from byebyelogger.style.color import RED".
        level (str): The name of the logging level (e.g., "INFO", "WARNING").
        format (str, optional): The format to be applied to the level name. Defaults to None, which means
                                the LoggerConfiguration's default_style will be used. To import formats, for
                                example, use: "from byebyelogger.style.format import SQUARE_BRACKETS".

    Returns:
        Logger: A new logger instance with the specified configuration.

    Example:
        color = RED
        level = "INFO"
        format = SQUARE_BRACKETS

        The resulting logger output will look like:

        -> [INFO] Example message
    """
    configuration = LoggerConfiguration()
    configuration.add(color(level), format)
    return Logger(configuration)

def nested_logger(components: List[Tuple[Union[str, Callable], str]]) -> Logger:
    """
    Creates a custom logger instance with a tailored format based on the input components.

    This function allows you to configure a logger with a unique format by providing a list of components,
    including colors, level, callables, and optional styles. The output's appearance depends on the 
    order and composition of the components.

    Args:
        components (List[Tuple[Union[str, Callable], str]]): A list of tuples, where each tuple contains
            a component and an optional style. Components can include colors, level, and callables.

    Returns:
        Logger: A logger instance configured with the specified components.

    Example:
        components = [
            (timestamp_func(), SQUARE_BRACKETS),
            ("SQLITE", SQUARE_BRACKETS),
            (LIGHTCYAN_EX("INFO"), None),
        ]

        The resulting logger output will look like:

        -> [2000-01-11 11:11:11] [SQLITE] INFO Example

    """

    configuration = LoggerConfiguration()
    
    for component in components:
        configuration.add(component)
    
    return Logger(configuration)


__all__ =  ["single_logger", "nested_logger"]



