class Car:
    def __init__(self, model, vin_number, numbers):
        self.model = model
        if self.__is_valid_vin(vin_number):
            _vin = vin_number
        if self.__is_valid_numbers(numbers):
            _numbers = numbers

    @staticmethod
    def __is_valid_vin(vin_number):
        if isinstance(vin_number, int):
            if 1000000 <= vin_number <= 9999999:
                return True
            else:
                raise IncorrectVinNumber(vin_number, 'Неверный диапазон для vin номера')
        else:
            raise IncorrectVinNumber(vin_number, 'Некорректный тип vin номер')

    @staticmethod
    def __is_valid_numbers(numbers):
        if isinstance(numbers, str):
            if len(numbers) == 6:
                return True
            else:
                raise IncorrectCarNumbers(numbers, 'Неверная длина номера')
        else:
            raise IncorrectCarNumbers(numbers, 'Некорректный тип данных для номеров')


class IncorrectVinNumber(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

    def __str__(self):
        return self.message


class IncorrectCarNumbers(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

    def __str__(self):
        return self.message


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
