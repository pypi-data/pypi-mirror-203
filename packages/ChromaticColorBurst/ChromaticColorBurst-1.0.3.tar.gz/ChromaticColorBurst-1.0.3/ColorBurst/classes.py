from dataclasses import dataclass
from typing import TypedDict
__all__ = ['Colors', 'Decorations', 'TextProperty', 'ColorCodes', 'BackgroundCodes', 'DecorationCodes', 'TextPropertyDict']

@dataclass(frozen=True, slots=True)
class Colors:
    BLACK = 'BLACK'
    RED = 'RED'
    GREEN = 'GREEN'
    YELLOW = 'YELLOW'
    BLUE = 'BLUE'
    MAGENTA = 'MAGENTA'
    CYAN = 'CYAN'
    WHITE = 'WHITE'

@dataclass(frozen=True, slots=True)
class Decorations:
    NORMAL = 'NORMAL'
    BOLD = 'BOLD'
    DIM = 'DIM'
    ITALIC = 'ITALIC'
    UNDERLINE = 'UNDERLINE'
    DOUBLE_UNDERLINE = 'DOUBLE_UNDERLINE'
    SLOW_BLINK = 'SLOW_BLINK'
    RAPID_BLINK = 'RAPID_BLINK'
    REVERSED = 'REVERSED'
    TRANSPARENT = 'TRANSPARENT'
    STRIKE = 'STRIKE'
    NORMAL_INTENSITY = 'NORMAL_INTENSITY'
    
@dataclass(slots=True)
class TextProperty:
    color: Colors = None
    background: Colors = None
    decoration: Decorations = None
    def asdict(self):
        return {
            'color': self.color,
            'background': self.background,
            'decoration': self.decoration
        }

@dataclass(frozen=True, slots=True)
class ColorCodes:
    BLACK = '30'
    RED = '31'
    GREEN = '32'
    YELLOW = '33'
    BLUE = '34'
    MAGENTA = '35'
    CYAN = '36'
    WHITE = '37'
    
@dataclass(frozen=True, slots=True)
class BackgroundCodes:
    BLACK = '40'
    RED = '41'
    GREEN = '42'
    YELLOW = '43'
    BLUE = '44'
    MAGENTA = '45'
    CYAN = '46'
    WHITE = '47'
    
@dataclass(frozen=True, slots=True)
class DecorationCodes:
    NORMAL = '0'
    BOLD = '1'
    DIM = '2'
    ITALIC = '3'
    UNDERLINE = '4'
    DOUBLE_UNDERLINE = '21'
    SLOW_BLINK = '5'
    RAPID_BLINK = '6'
    REVERSED = '7'
    TRANSPARENT = '8'
    STRIKE = '9'
    NORMAL_INTENSITY = '22'
    
class TextPropertyDict(TypedDict):
    color: str | Colors
    background: str | Colors
    decoration: str | Decorations