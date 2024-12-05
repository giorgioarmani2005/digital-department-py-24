# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union


class Car:
    def __init__(self, make: str, model: Union[str, int], year: int):
        """
        Creating and preparing the "Car" object for work

        :param make: brand this car
        :param model: name model`s
        :param year: year of issue

        Examples:
        >>> car = Car("Lada", "Priora", 1999) # initializing the class instance
        """
        if year < 1886:
            raise ValueError("Year must be greater than or equal to 1886 (the year the first car was invented).")
        if not isinstance(make, str):
            raise TypeError("Brand can only be a string!")
        if not isinstance(model, (str, int)):
            raise TypeError("Make can only be a string or integer!")
        if not isinstance(year, int):
            raise TypeError("Year can only be a integer!")
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self) -> str:
        """Starts the car's engine.

        Returns:
            str: Confirmation that the engine has started.

        Example:
            >>> car = Car("BMV", "x5", 2020)
            >>> car.start_engine()
            'Engine started.'
        """
        pass

    def stop_engine(self) -> str:
        """Stops the car's engine.

        Returns:
            str: Confirmation that the engine has stopped.

        Example:
            >>> car = Car("Toyota", "Camry", 2020)
            >>> car.stop_engine()
            'Engine stopped.'
        """
        pass


class SuperHero:
    def __init__(self, name: str, powers: Union[list, str], year_active: int):
        """
        Creating and preparing the "SuperHero" object for work

        :param name: name this hero
        :param powers: unusual superpower
        :param year_active: when did he become famous

        Examples:
        >>> hero = SuperHero("Iron man", "No", 2000) # initializing the class instance
        """
        if year_active < 1900:
            raise ValueError("Year active must be greater than or equal to 1900.")
        if not isinstance(name, str):
            raise TypeError("Name can only be a string!")
        if not isinstance(powers, (list, str)):
            raise TypeError("Powers can only be a string or list!")
        if not isinstance(year_active, int):
            raise TypeError("Year active can be only a integer!")
        self.name = name
        self.powers = powers
        self.year_active = year_active

    def fight_crime(self) -> str:
        """Fights crime in the city.

        Returns:
            str: Confirmation that the superhero is fighting crime.

        Example:
            >>> boring_hero = SuperHero("Superman", ["flight", "super strength"], 1938)
            >>> boring_hero.fight_crime()
            'Superman is fighting crime!'
        """
        pass

    def save_people(self) -> str:
        """Saves people in danger.

        Returns:
            str: Confirmation that the superhero has saved someone.

        Example:
            >>> favorite_hero = SuperHero("Spider-man", ["super agility", "super strength"], 1938)
            >>> favorite_hero.save_people()
        """
        pass


class Refrigerator:
    def __init__(self, brand: str, capacity: Union[float, int], temperature: Union[float, int]):
        """
        Creating and preparing the "Refrigerator" object for work

        :param brand: brand refrigerator
        :param capacity: capacity refrigerator
        :param temperature: temerature inside

        Examples:
        >>> glass = Refrigerator("LG", 10, 3.5) # initializing the class instance
        """
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        if temperature < -30 or temperature > 10:
            raise ValueError("Temperature must be between -30 and 10 degrees Celsius.")
        if not isinstance(capacity, (float, int)):
            raise TypeError("Incorrect type capacity")
        if not isinstance(temperature, (float, int)):
            raise TypeError("Incorrect type temperature")
        self.brand = brand
        self.capacity = capacity  # in liters
        self.temperature = temperature  # in degrees Celsius

    def cool(self) -> str:
        """Activates the cooling function of the refrigerator.

        Returns:
            str: Confirmation that the refrigerator is cooling.

        Example:
            >>> fridge = Refrigerator("LG", 300, 4)
            >>> fridge.cool()
        """
        pass

    def open_door(self) -> str:
        """Opens the refrigerator door.

        Returns:
            str: Confirmation that the door is open.

        Example:
            >>> new_fridge = Refrigerator("Samsung", 60, 5)
            >>> new_fridge.open_door()
        """
        pass


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
