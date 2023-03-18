from constants import *


class Key:
    def __init__(self, value) -> None:
        if isinstance(value, int):
            self.code = value
            self.name = CODE_2_NAME[self.code]
            self.char = NAME_2_CHAR[self.name]
        if isinstance(value, str):
            self.char = NAME_2_CHAR.get(value, value)
            self.name = CHAR_2_NAME.get(value, value)
            self.code = NAME_2_CODE[self.name]
        print(self.char, end="")

    def __str__(self) -> str:
        return self.char
