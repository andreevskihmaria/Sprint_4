from main import BooksCollector
import pytest

class TestBooksCollector:


    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    
    @pytest.mark.parametrize('name', ['', 'Невероятно длинное название книги для нашего теста'])
    def test_add_new_book_with_invalid_name_does_not_add_book(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 0
    

    def test_set_book_genre_an_existing_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер и Кубок огня')
        collector.set_book_genre('Гарри Поттер и Кубок огня', 'Фантастика')

        assert collector.get_book_genre('Гарри Поттер и Кубок огня') == 'Фантастика'


    def test_set_book_genre_does_not_exist_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Удивительная история')
        collector.set_book_genre('Удивительная история', 'Приключение')

        assert collector.get_book_genre('Удивительная история') == ''


    def test_get_book_genre_book_exists(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'
    

    def test_get_books_with_specific_genre_returns_books_with_needed_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Кладбище домашних животных')

        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.set_book_genre('Кладбище домашних животных', 'Ужасы')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер', 'Властелин колец']


    def test_get_books_genre_returns_current_books_dictionary(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')

        assert collector.get_books_genre() == {'Гарри Поттер': ''}


    def test_get_books_for_children_returns_children_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('101 далматинец')
        collector.add_new_book('Один дома')

        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('101 далматинец', 'Мультфильмы')
        collector.set_book_genre('Один дома', 'Комедии')

        assert collector.get_books_for_children() == ['Гарри Поттер', '101 далматинец', 'Один дома']


    @pytest.mark.parametrize('name, genre', [['Кладбище домашних животных', 'Ужасы'], ['Таинственная история Билли Миллигана', 'Детективы']])
    def test_get_books_for_children_does_not_include_age_rating_books(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_books_for_children() == []


    def test_add_book_in_favorites_book_exists(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']


    def test_add_book_in_favorites_book_doesnt_exist(self):
        collector = BooksCollector()

        collector.add_book_in_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == []


    def test_add_book_in_favorites_add_double_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']


    def test_delete_book_from_favorites_book_exists(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Властелин колец')

        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Властелин колец')

        assert collector.get_list_of_favorites_books() == ['Гарри Поттер', 'Властелин колец']
        