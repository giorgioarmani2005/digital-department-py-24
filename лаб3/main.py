class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):#метод с общими атрибутами, лучше унаследовать
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):#данный метод лучше везде перегрузить
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, pages: int, name: str, author: str):
        super().__init__(name, author)
        self._pages = None
        self.set_pages(pages)

    @property
    def pages(self):
        return self._pages

    #если метод set_pages вынести в свойство, и в конструкторе
    #просто присваивать pages, то при инициализации не будет проверки.
    def set_pages(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Incorrect type for pages!")
        if value <= 0:
            raise ValueError("Incorrect value for pages!")
        self._pages = value

    @pages.setter
    def pages(self, value):
        self.set_pages(value)

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, duration: float, name: str, author: str):
        super().__init__(name, author)
        self._duration = None
        self.duration_set(duration)

    @property
    def duration(self):
        return self._duration

    def duration_set(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("Incorrect type for duration!")
        if value <= 0:
            raise ValueError("Incorrect value for duration!")
        self._duration = float(value)

    @duration.setter
    def duration(self, value):
        self.duration_set(value)
        
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
