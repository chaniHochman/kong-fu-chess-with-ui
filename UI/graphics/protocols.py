from typing import Protocol
from view.img import Img

#חוזה לכל מחלקה שאחראית על ציור למסך
class Renderer(Protocol):

    def render(self, canvas:Img, snapshot) -> None:
        pass

#  חוזה לכל מחלקה שטוענת משאבים.
class Loader(Protocol):

    def load(self) -> None:
        pass