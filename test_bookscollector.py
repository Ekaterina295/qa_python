import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

# Добавить дубликат книги
    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Война и мир')
        assert list(collector.books_genre.keys()).count('Война и мир') == 1

# Установить и проверить жанр книги
    @pytest.mark.parametrize(
        'book_name, genre, expected_genre',
        [
            ('Война и мир', 'Фантастика', 'Фантастика'),
            ('Война и мир', 'Детективы', 'Детективы'),
            ('Война и мир', 'Ужасы', 'Ужасы'),
            ('Война и мир', 'Мультфильмы', 'Мультфильмы'),
            ('Война и мир', 'Комедии', 'Комедии')
        ]
    )
    def test_set_book_genre_success(self, book_name, genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre[book_name] == expected_genre

# Установить несуществующий жанр
    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Несуществующий жанр')
        assert collector.books_genre['Война и мир'] == ''


# Успешный вывод списка книг с определенным жанром

    def test_get_books_with_specific_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Детективы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Война и мир']

# Успешное добавление книги в Избранное
    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        collector.add_book_in_favorites('Война и мир')
        assert 'Война и мир' in collector.favorites

# Успешная проверка, что книги нет в Избранном
    def test_add_book_in_favorites_not_in_books_genre(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Книга которой нет')
        assert 'Книга которой нет' not in collector.favorites

# Отсутствие дублирования книги при добавлении в Избранное
    def test_add_book_in_favorites_already_added(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        collector.add_book_in_favorites('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        assert collector.favorites.count('Война и мир') == 1

# Успешное удаление книги из Избранного
    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        collector.add_book_in_favorites('Война и мир')
        collector.delete_book_from_favorites('Война и мир')
        assert 'Война и мир' not in collector.favorites

# Успешное получение списка Избранных книг
    def test_get_list_of_favorites_books_success(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Детективы')
        collector.add_book_in_favorites('Война и мир')
        collector.add_book_in_favorites('Преступление и наказание')
        assert collector.get_list_of_favorites_books() == ['Война и мир', 'Преступление и наказание']

# Успешная проверка вывода списка книг, подходящих для детей
    def test_get_books_for_children_success(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Детективы')
        collector.add_new_book('Три богатыря')
        collector.set_book_genre('Три богатыря', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Война и мир', 'Три богатыря']

