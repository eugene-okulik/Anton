class Books:
    material = 'бумага'
    text = ''
    isbn = ''
    reserved_book = False

    def __init__(self, name_book, autor, pages_count):
        self.name_book = name_book
        self.autor = autor
        self.pages_count = pages_count

    def reserved(self):
        self.reserved_book = True

    def print_text(self):
        status = ', зарезервирована' if self.reserved_book else ''
        text_print = (
            f'Название: {self.name_book}, '
            f'Автор: {self.autor}, '
            f'страниц: {self.pages_count}, '
            f'материал: {self.material}{status}'
        )
        print(text_print)


class SchoolBooks(Books):
    available_task = True

    def __init__(self, name_book, autor, pages_count, subject, classes):
        super().__init__(name_book, autor, pages_count)
        self.subject = subject
        self.classes = classes

    def print_text_sb(self):
        status = ', зарезервирована' if self.reserved_book else ''
        text_print = (
            f'Название: {self.name_book}, '
            f'Автор: {self.autor}, '
            f'страниц: {self.pages_count}, '
            f'предмет: {self.subject}, '
            f'класс: {self.classes}{status}'
        )
        print(text_print)


book = Books('Идиот', 'Достоевский', '500')
book.reserved()
book.print_text()

book_1 = Books('Идиот1', 'Достоевский', '500')
book_1.print_text()

book_2 = Books('Идиот2', 'Достоевский', '500')
book_2.reserved()
book_2.print_text()

book_3 = Books('Идиот3', 'Достоевский', '500')
book_3.print_text()

book_4 = Books('Идиот4', 'Достоевский', '500')
book_4.print_text()

shool_book = SchoolBooks('Математика 2 класс', 'Сафронов', '133', 'Математика', '2')
shool_book.reserved()
shool_book.print_text_sb()

shool_book_1 = SchoolBooks('История 11 класс', 'Смиронов', '322', 'История', '11')
shool_book_1.print_text_sb()
