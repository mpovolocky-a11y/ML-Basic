from homework_05.car import Car
from homework_05.engine import Engine
from homework_05.plane import Plane
from homework_05.exceptions import LowFuelError, CargoOverload

print("--- Проверка МАШИНЫ ---")
my_car = Car(weight=1500, fuel=10, fuel_consumption=2)
try:
    my_car.start()
    print("Машина успешно заведена!")
    my_engine = Engine(volume=2.0, pistons=4)
    my_car.set_engine(my_engine)
    print(f"Двигатель установлен: {my_car.engine}")
except LowFuelError as e:
    print(f"Ошибка при старте: {e}")

print("\n--- Проверка САМОЛЕТА ---")
my_plane = Plane(weight=5000, fuel=100, fuel_consumption=5, max_cargo=500)
try:
    my_plane.load_cargo(400)
    print(f"Груз 400 кг загружен. Текущий груз: {my_plane.cargo}")
    my_plane.load_cargo(200) # Это должно вызвать ошибку
except CargoOverload as e:
    print(f"Ожидаемая ошибка перегрузки: {e}")

print(f"Выгружаем всё. Было выгружено: {my_plane.remove_all_cargo()} кг")