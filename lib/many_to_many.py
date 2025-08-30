class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string.")
        self._title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title

    def contracts(self):
        """Return all contracts for this book"""
        return [c for c in Contract.all if c.book == self]

    def authors(self):
        """Return all authors who have signed contracts for this book"""
        return [c.author for c in self.contracts()]


class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    def contracts(self):
        """Return all contracts for this author"""
        return [c for c in Contract.all if c.author == self]

    def books(self):
        """Return all books written by this author through contracts"""
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Sign a contract with a book"""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Sum royalties from all contracts"""
        return sum(c.royalties for c in self.contracts())


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an Author instance.")
        if not isinstance(book, Book):
            raise Exception("Book must be a Book instance.")
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")

        self._author = author
        self._book = book
        self._date = date
        self._royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @property
    def book(self):
        return self._book

    @property
    def date(self):
        return self._date

    @property
    def royalties(self):
        return self._royalties

    @classmethod
    def contracts_by_date(cls, date):
        return [c for c in cls.all if c.date == date]
