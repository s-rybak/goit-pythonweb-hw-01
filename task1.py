from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.INFO,
)


class Vehicle(ABC):
    """Vehicle interface"""

    @abstractmethod
    def start_engine(self):
        pass


class VehicleFactory:
    """Vehicle factory interface"""

    @abstractmethod
    def create_car(self) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self) -> Vehicle:
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Мотор заведено")


class USVehicleFactory(VehicleFactory):
    def create_car(self) -> Vehicle:
        return Car("Ford", "Mustang (US Spec)")

    def create_motorcycle(self) -> Vehicle:
        return Motorcycle("Harley-Davidson", "Sportster (US Spec)")


class EUVehicleFactory(VehicleFactory):
    def create_car(self) -> Vehicle:
        return Car("Ford", "Mustang (EU Spec)")

    def create_motorcycle(self) -> Vehicle:
        return Motorcycle("Harley-Davidson", "Sportster (EU Spec)")


# Використання
carUS = USVehicleFactory().create_car()
carUS.start_engine()

motorcycleUS = USVehicleFactory().create_motorcycle()
motorcycleUS.start_engine()

carEU = EUVehicleFactory().create_car()
carEU.start_engine()

motorcycleEU = EUVehicleFactory().create_motorcycle()
motorcycleEU.start_engine()
