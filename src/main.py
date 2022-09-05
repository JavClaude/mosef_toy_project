import argparse

from src.car_garage.car_unlocking.car_unlocker import CarUnlocker
from src.cars.sport_utility_vehicle.car import SportUtilityVehicle
from src.car_garage.car_controls.technical_control import TechnicalCarControl


def cli_wrapper() -> None:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--car_brand", type=str, required=True)
    argument_parser.add_argument("--year_of_construction", type=int, required=True)
    argument_parser.add_argument("--car_power", type=int, required=True)

    arguments = argument_parser.parse_args()

    main(arguments.car_brand, arguments.year_of_construction, arguments.car_power)


def main(car_brand: str, year_of_construction: int, car_power: int) -> None:
    technical_car_controller = TechnicalCarControl()
    car_unlocker = CarUnlocker()

    suv = SportUtilityVehicle(car_brand, year_of_construction, car_power)
    technical_car_controller.start_and_control_car(suv)

    tampered_suv = SportUtilityVehicle("Toyota", 2020, 200)
    car_unlocker.tampered_car(tampered_suv, 2022, 500)
    technical_car_controller.start_and_control_car(tampered_suv)
