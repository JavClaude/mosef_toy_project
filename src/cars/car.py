from abc import abstractmethod


STR_SPECIAL_MESSAGE = "Brand: {}\nYear of construction: {}\nPower: {}"


class Car:
    def __init__(self, brand: str, year_of_construction: int, power: int) -> None:
        self.brand = brand
        self.__year_of_construction = year_of_construction
        self.__power = power
        self.__has_been_tampered = False

    @abstractmethod
    def start(self) -> None:
        raise NotImplementedError()

    @property
    def year_of_construction(self) -> int:
        return self.__year_of_construction

    @year_of_construction.setter
    def year_of_construction(self, value: int) -> None:
        self.__year_of_construction = value
        self.__has_been_tampered = True

    @property
    def power(self) -> int:
        return self.__year_of_construction

    @power.setter
    def power(self, value: int) -> None:
        self.__power = value
        self.__has_been_tampered = True

    @property
    def has_been_tampered(self) -> int:
        return self.__has_been_tampered

    def __str__(self) -> str:
        return STR_SPECIAL_MESSAGE.format(
            self.brand, self.__year_of_construction, self.__power
        )
