"""
Создайте класс `Plane`, наследник `Vehicle`
"""
from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload

class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        # Вызываем родительский метод для общих полей
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, weight):
        if self.cargo + weight <= self.max_cargo:
            self.cargo += weight
        else:
            raise CargoOverload("Перегрузка! Слишком тяжелый груз")

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo