class Car:
    """
    Базовый класс для автомобилей.
    """

    def __init__(self, brand: str, model: str, year: int, mileage: float) -> None:
        """
        Конструктор класса Car.

        :param brand: Бренд автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска.
        :param mileage: Пробег автомобиля в километрах.
        """
        self.brand = brand
        self.model = model
        self.year = year
        self._mileage = mileage  # Доступ к пробегу осуществляется через методы, что обеспечивает контроль за его изменением.

    def drive(self, distance: float) -> None:
        """
        Метод для увеличения пробега автомобиля на заданное расстояние.

        :param distance: Расстояние в километрах, на которое будет увеличен пробег.

        Do not repeat yourself. Чтобы каждый раз не проверять передаваемое значение инкапсулировали
        """
        if distance < 0:
            raise ValueError("Distance cannot be negative.")
        self._mileage += distance

    def get_mileage(self) -> float:
        """
        Метод для получения пробега автомобиля.

        Его стоит унаследовать, поскольку никаких ограничений на получение пробега нет

        :return: Пробег автомобиля.
        """
        return self._mileage

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Car.

        :return: Строка с информацией об автомобиле.

        Данные атрибуты присущи всем авто, поэтому стоит унаследовать в дочерних классах.
        """
        return f"Автомобиль: {self.brand} {self.model}, {self.year} года выпуска, пробег: {self._mileage}"

    def __repr__(self) -> str:
        """
        Возвращает "официальное" строковое представление объекта Car.

        :return: Строка с информацией о классе и атрибутах.

        """
        return f"{self.__class__.__name__}(brand='{self.brand!r}', model='{self.model!r}', year={self.year!r}, mileage={self._mileage!r})"


class ElectricCar(Car):
    """
    Дочерний класс для электрических автомобилей.
    """

    def __init__(self, brand: str, model: str, year: int, mileage: float, battery_capacity: float) -> None:
        """
        Конструктор класса ElectricCar, расширяющий Car.

        :param brand: Бренд электрического автомобиля.
        :param model: Модель электрического автомобиля.
        :param year: Год выпуска.
        :param mileage: Пробег электрического автомобиля в километрах.
        :param battery_capacity: Вместимость аккумулятор.
        """
        super().__init__(brand, model, year, mileage)
        self._battery_capacity = battery_capacity

    def drive(self, distance: float) -> None:
        """
        Перегруженный метод drive для электрических автомобилей.

        Этот метод учитывает, что электрические автомобили могут иметь ограничения на пробег,
        зависящие от ёмкости аккумулятора. Например, можно ограничить пробег по отношению к
        ёмкости аккумулятора (1 кВтч = 5 км пробега).

        :param distance: Расстояние в километрах.
        """
        max_distance = self._battery_capacity * 5
        if distance > max_distance:
            raise ValueError(f"Cannot drive more than {max_distance} km on a full charge.")
        self._mileage += distance

    def __repr__(self) -> str:
        """
        Возвращает "официальное" строковое представление объекта ElectricCar.

        Перегруженный метод, так как имеются собственные атрибуты.

        :return: Строка с информацией о классе и атрибутах.
        """
        return f"{self.__class__.__name__}(brand='{self.brand}', model='{self.model}', year={self.year}, mileage={self._mileage}, battery_capacity={self._battery_capacity})"


if __name__ == "__main__":
    # пример использования классов
    my_car = Car("Toyota", "Rav 4", 2020, 15000)
    print(my_car)
    my_car.drive(100)
    print(my_car.get_mileage())

    my_electric_car = ElectricCar("Tesla", "Model 3", 2021, 8000, 75)
    print(my_electric_car)
    my_electric_car.drive(444)  # здесь выйдет ошибка
    print(my_electric_car.get_mileage())
