from dataclasses import dataclass
from enum import Enum

class Color(str, Enum):
    Red = "\x1b[31m"
    Green = "\x1b[32m"
    Purple = "\x1b[34m"
    Blink = "\x1b[6m"
    Offset = "\x1b[0m"

    def __str__(self) -> str:
        return "%s" % self.value

@dataclass(frozen=True)
class Colorize:
    def colorrize(self, tx: str, color: Color = Color.Offset) -> str:
        if color in list(Color):
            return f"{color}{tx}{Color.Offset}"
        raise Exception("No Color Found")


if __name__ == "__main__":
    print("please run main.py")
