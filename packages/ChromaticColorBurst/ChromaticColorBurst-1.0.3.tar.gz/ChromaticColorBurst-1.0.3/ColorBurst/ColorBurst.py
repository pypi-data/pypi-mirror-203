from typing import Any, Callable, Dict, TypedDict
from .classes import *

__all__ = ['ColorBurst', 'Colors', 'Decorations', 'TextProperty']

class ColorBurst:
    def __init__(self, default_property: TextProperty | None = TextProperty(), autoreset: bool = False) -> None:
        self.__prefix = '\u001b['
        self.__reset_code = self.__prefix + '0m'
        self.__reset = autoreset
        self.__properties: TextProperty | None = None
        self.update(default_property, autoreset)
    def update(self, property_: TextProperty = TextProperty(), autoreset: bool = False) -> None:
        if not property_ is None and isinstance(property_, TextProperty):
            color, background, decoration = '', '', '0'
            if property_.color:
                color = ';' + getattr(ColorCodes, property_.color)
            if property_.background:
                background = ';' + getattr(BackgroundCodes, property_.background)
            if property_.decoration:
                decoration = getattr(DecorationCodes, property_.decoration)
            self.__properties = TextProperty(color, background, decoration)
        self.__reset = autoreset
    @property
    def RESET(self):
        print(self.__reset_code, end='')
    def input_burst(self, prompt: str = '', prompt_property: TextPropertyDict | TextProperty = TextProperty(), text_property: TextPropertyDict |  TextProperty = TextProperty(), text_style: bool = False, type_: Callable = None) -> Any:
        if isinstance(prompt_property, TextProperty):
            prompt_property = prompt_property.asdict()
        prompt_color = prompt_property.get('color', None)
        prompt_back = prompt_property.get('background', None)
        prompt_decc = prompt_property.get('decoration', None)
        
        prompt_color = ';' + getattr(ColorCodes, prompt_color) if prompt_color else self.__properties.color
        prompt_back = ';' + getattr(BackgroundCodes, prompt_back) if prompt_back else self.__properties.background
        prompt_decc = getattr(DecorationCodes, prompt_decc) if prompt_decc else self.__properties.decoration
        
        if isinstance(text_property, TextProperty):
            text_property = text_property.asdict()
        text_color = text_property.get('color', None)
        text_back = text_property.get('background', None)
        text_decc = text_property.get('decoration', None)
        if any([text_color, text_back, text_decc]):
            text_color = ';' + getattr(ColorCodes, text_color) if text_color else self.__properties.color
            text_back = ';' + getattr(BackgroundCodes, text_back) if text_back else self.__properties.background
            text_decc = getattr(DecorationCodes, text_decc) if text_decc else self.__properties.decoration
            text_code = self.__reset_code + f"{self.__prefix}{text_decc}{text_color}{text_back}m"
            query = input(f"{self.__prefix}{prompt_decc}{prompt_color}{prompt_back}m{prompt}{text_code}")
            if self.__reset: self.RESET
            return type_(query) if type_ else query
    def print_burst(self, *args, properties: TextPropertyDict | TextProperty = None, separator = None, end = None) -> None:
        if properties:
            if isinstance(properties, TextProperty):
                properties = properties.asdict()
            color = properties.get('color', None)
            background = properties.get('background', None)
            decoration = properties.get('decoration', None)
            
            color = ';' + getattr(ColorCodes, color) if color else self.__properties.color
            background = ';' + getattr(BackgroundCodes, background) if background else self.__properties.background
            decoration = getattr(DecorationCodes, decoration) if decoration else self.__properties.decoration
        else:
            color, background, decoration = self.__properties.color, self.__properties.background, self.__properties.decoration
        separator = separator if separator else ' '
        if len(args) > 0:
            data = str(separator).join(args)
        else:
            data = ''
        reset = ''
        if self.__reset:
            reset = self.__reset_code
        print(f"{self.__prefix}{decoration}{color}{background}m{data}", f"{reset}", end=end)
    def get_property(self, color='', background = '', decoration = '0') -> TextProperty:
        return TextProperty(color, background, decoration)
if __name__ == '__main__':
    cb = ColorBurst(autoreset=True)
    cb.print_burst('Hello', 'World', properties=TextProperty(Colors.RED, Colors.YELLOW))
    cb.RESET
    cb.update(autoreset=True)
    cb.print_burst('Hello', 'World', properties=TextProperty(Colors.GREEN))
    cb.print_burst('Hi', properties={
        'color': "YELLOW"
    })
    cb.input_burst("What is your name? ", TextProperty(background='GREEN', color='BLUE'), TextProperty(decoration=Decorations.ITALIC, color='RED'))