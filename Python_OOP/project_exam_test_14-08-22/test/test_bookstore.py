from project_shopping_cart_unittest.bookstore import Bookstore
from unittest import TestCase, main


class BookStoreTest(TestCase):

    def setUp(self) -> None:
        self.store = Bookstore(20)
        self.books = {
            "asd": 3,
            "dsa": 4
        }

    def test_correct_initializing(self):
        self.assertEqual(20, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store.total_sold_books)

    def test_wrong_books_limit_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = 0

        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test_correct_len_method(self):
        self.store.availability_in_store_by_book_titles = self.books

        self.assertEqual(7, len(self.store))

    def test_receive_book_with_exceeded_amount_raises_exception(self):
        self.store.availability_in_store_by_book_titles = self.books

        with self.assertRaises(Exception) as ex:
            self.store.receive_book("test", 15)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_with_new_book(self):
        result = self.store.receive_book("test", 5)

        self.assertEqual({"test": 5}, self.store.availability_in_store_by_book_titles)
        self.assertEqual("5 copies of test are available in the bookstore.", result)

        second_result = self.store.receive_book("test", 3)
        self.assertEqual("8 copies of test are available in the bookstore.", second_result)
        self.assertEqual(8, len(self.store))

    def test_receive_book_with_existing_book(self):
        self.store.availability_in_store_by_book_titles = self.books
        result = self.store.receive_book("asd", 3)

        self.assertEqual("6 copies of asd are available in the bookstore.", result)
        self.assertEqual(10, len(self.store))

        second_result = self.store.receive_book("asd", 1)

        self.assertEqual("7 copies of asd are available in the bookstore.", second_result)
        self.assertEqual(11, len(self.store))


    def test_sell_book_with_non_existent_book_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("test", 1)

        self.assertEqual("Book test doesn't exist!", str(ex.exception))

    def test_sell_book_with_existing_amount_raises_exception(self):
        self.store.availability_in_store_by_book_titles = self.books

        with self.assertRaises(Exception) as ex:
            self.store.sell_book("asd", 5)

        self.assertEqual("asd has not enough copies to sell. Left: 3", str(ex.exception))

    def test_sell_book_successfully(self):
        self.store.availability_in_store_by_book_titles = self.books
        result = self.store.sell_book("asd", 2)

        self.assertEqual(2, self.store.total_sold_books)
        self.assertEqual("Sold 2 copies of asd", result)
        self.assertEqual({
            "asd": 1,
            "dsa": 4
        }, self.store.availability_in_store_by_book_titles)

    def test_str_method(self):
        self.store.availability_in_store_by_book_titles = self.books

        self.assertEqual("Total sold books: 0\n"
                         "Current availability: 7\n"
                         " - asd: 3 copies\n"
                         " - dsa: 4 copies", str(self.store))


if __name__ == "__main__":
    main()



