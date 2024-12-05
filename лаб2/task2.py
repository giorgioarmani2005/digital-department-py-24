BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_, name, pages):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'


# TODO написать класс Library
class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.list_book = books

    def get_next_book_id(self) -> int:
        if not self.list_book:
            return 1
        next_index = self.list_book[-1].id_ + 1
        return next_index

    def get_index_by_book_id(self, id_: int):
        return_index = [index for index, item in enumerate(self.list_book) if item.id_ == id_]
        if not return_index:
            raise ValueError('Книги с запрашиваемым id не существует')
        return return_index[0] #просто хотелось лист компрехеншн, знаю, что не прям элегантно


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
