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
    def __init__(self, id_: int, name: str, pages: int):
        """
        Конструктор класса Book.

        Args:
            id_ (int): Идентификатор книги.
            name (str): Название книги.
            pages (int): Количество страниц в книге.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Метод для форматированного вывода информации о книге.

        Returns:
            str: Строка с информацией о книге.
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Метод для представления объекта в виде строки, которая может быть использована для инициализации объекта.

        Returns:
            str: Валидная строка Python для инициализации объекта.
        """
        return f'Book(id_={self.id}, name=\'{self.name}\', pages={self.pages})'


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
