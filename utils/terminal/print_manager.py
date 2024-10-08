import pytz 
from colorama import Fore, Style
from datetime import datetime, timedelta

utc_timezone = pytz.timezone("UTC")

def print_colored_text(identifier, text, color_name="RED"):
    color_map = {
        "BLACK": Fore.BLACK,
        "RED": Fore.RED,
        "GREEN": Fore.GREEN,
        "YELLOW": Fore.YELLOW,
        "BLUE": Fore.BLUE,
        "MAGENTA": Fore.MAGENTA,
        "CYAN": Fore.CYAN,
        "WHITE": Fore.WHITE,
        "RESET": Style.RESET_ALL,
    }

    current_time = datetime.now().strftime("[%d/%b/%Y %H:%M:%S]")
    color = color_map.get(
        color_name.upper(), Fore.RED
    )  # Default to RED if color is not found
    log_entry = f'{color}{current_time} - [ {identifier} ] - {text}{Style.RESET_ALL}'
    print(log_entry)
