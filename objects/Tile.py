from ast import List
from dataclasses import dataclass
from objects.Object import Object


@dataclass
class Tile(Object):

   __contains: List[Object] = None

   @property
   def contains(self) -> List[Object]:
       return self.__contains
