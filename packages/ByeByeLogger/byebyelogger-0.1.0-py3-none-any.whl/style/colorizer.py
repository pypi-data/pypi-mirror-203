import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

class Color:
    def __init__(self, color: str):
        self.color = color.upper()
        
        if self.color in Fore.__dict__:
            self.wrappercolor = Fore.__dict__[self.color]
        else:
            raise ValueError(f"Invalid color '{color}'. Choose a valid color from colorama.Fore.")
    
    def __call__(self, string: str) -> str:
        return f"{self.wrappercolor}{Style.BRIGHT}{string}{Fore.RESET}"



BLACK = Color("BLACK")
RED = Color("RED")
GREEN = Color("GREEN")
YELLOW = Color("YELLOW")
BLUE = Color("BLUE")
MAGENTA = Color("MAGENTA")
CYAN = Color("CYAN")
WHITE = Color("WHITE")
RESET = Color("RESET")
LIGHTBLACK_EX = Color("LIGHTBLACK_EX")
LIGHTRED_EX = Color("LIGHTRED_EX")
LIGHTGREEN_EX = Color("LIGHTGREEN_EX")
LIGHTYELLOW_EX = Color("LIGHTYELLOW_EX")
LIGHTBLUE_EX = Color("LIGHTBLUE_EX")
LIGHTMAGENTA_EX = Color("LIGHTMAGENTA_EX")
LIGHTCYAN_EX = Color("LIGHTCYAN_EX")
LIGHTWHITE_EX = Color("LIGHTWHITE_EX")
