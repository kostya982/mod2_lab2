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


class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"

    def __str__(self):
        return f'Книга "{self.name}"'


class Library:
    def __init__(self, books=None):
        self.books = books or []

    def get_next_book_id(self):
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':

# Создаем экземпляры класса Book
 list_books = [Book(book_dict["id"], book_dict["name"], book_dict["pages"]) for book_dict in BOOKS_DATABASE]

# Инициализируем библиотеку с книгами
library_with_books = Library(books=list_books)

# Проверяем следующий id для пустой библиотеки
print(Library().get_next_book_id())

# Проверяем следующий id для непустой библиотеки
print(library_with_books.get_next_book_id())

# Проверяем индекс книги с id = 1
print(library_with_books.get_index_by_book_id(1))
