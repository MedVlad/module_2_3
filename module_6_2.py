class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, _model, _color, _engine_power):
        self.owner = owner
        self._model = _model
        self._engine_power = _engine_power
        if str(_color).upper() in ' '.join(Vehicle.__COLOR_VARIANTS).upper():
            self._Vehicle_color = _color
        else:
            print(f"Нельзя сменить цвет на {_color}")

    def get_model(self):
        return f'Модель: {self._model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {str(self._engine_power)}'

    def get_color(self):
        return f'Цвет: {self._Vehicle_color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')


class Sedan(Vehicle):
    _PASSENGERS_LIMIT = 5

    def set_color(self, color):
        if str(color).upper() in ' '.join(self._Vehicle__COLOR_VARIANTS).upper():
            self._Vehicle_color = color
        else:
            print(f"Нельзя сменить цвет на {color}")
        Vehicle._color = color


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()
