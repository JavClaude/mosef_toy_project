import time

from tqdm import tqdm

from src.cars.car import Car


class TechnicalCarControl:
    @staticmethod
    def _print_car_information(car: Car) -> None:
        print(f"Running technical control for:\n{car}")

    @staticmethod
    def _start_the_car(car: Car) -> None:
        car.start()

    @staticmethod
    def _control_car(car: Car) -> True:
        if car.has_been_tampered:
            print("Car has been tampered, technical control is KO: ❌ \n")
            return False
        print("Technical control is OK: ✅ \n")
        return True

    def start_and_control_car(self, car: Car) -> bool:
        self._print_car_information(car)
        for _ in tqdm(range(0, 10), desc="Controlling car..."):
            time.sleep(0.5)
        self._start_the_car(car)
        technical_control_status = self._control_car(car)
        return technical_control_status
