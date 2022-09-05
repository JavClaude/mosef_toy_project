import time

from tqdm import tqdm

from src.cars.car import Car


class CarUnlocker:
    @staticmethod
    def _change_year_of_construction(car: Car, new_year_of_construction: int) -> None:
        car.year_of_construction = new_year_of_construction

    @staticmethod
    def _change_car_power(car: Car, new_power: int) -> None:
        car.power = new_power

    def tampered_car(
        self, car: Car, new_year_of_construction: int, new_power: int
    ) -> None:
        self._change_year_of_construction(car, new_year_of_construction)
        self._change_car_power(car, new_power)

        for _ in tqdm(range(0, 10), desc="Unlocking car"):
            time.sleep(0.5)
