from src.cars.car import Car


class SportCar(Car):
    def __init__(self, brand: str, year_of_construction: int, power: int) -> None:
        super(SportCar, self).__init__(brand, year_of_construction, power)

    def start(self) -> None:
        print("Starting sport car")
        # Custom implementation for SportCar
