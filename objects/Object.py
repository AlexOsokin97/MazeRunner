from dataclasses import dataclass


@dataclass
class Object:

    __x: int
    __y: int
    __width: int
    __height: int


    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y
    
    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height