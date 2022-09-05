from src.cars.car import Car


class SportUtilityVehicle(Car):
    def __init__(self, brand: str, year_of_construction: int, power: int) -> None:
        super(SportUtilityVehicle, self).__init__(brand, year_of_construction, power)

    def start(self) -> None:
        print("Starting SUV")
        # Custom implementation for SUV object
