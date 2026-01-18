"""
Создайте класс `Car`, наследник `Vehicle`
"""
from homework_05.base import Vehicle

class Car(Vehicle):
    engine = None

    def set_engine(self, engine_instance):
        self.engine = engine_instance