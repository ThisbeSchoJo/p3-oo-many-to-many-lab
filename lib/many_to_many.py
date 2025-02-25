class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author is self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])

class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book is self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

class Contract:
    
    all =[]

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
        pass

    @property
    def get_author(self):
        return self._author
    
    @get_author.setter
    def author(self, author_value):
        if isinstance(author_value, Author):
            self._author = author_value
        else:
            raise Exception

    @property
    def get_book(self):
        return self._book
    
    @get_book.setter
    def book(self, book_value):
        if isinstance(book_value, Book):
            self._book = book_value
        else:
            raise Exception
    
    @property
    def get_date(self):
        return self._date
    
    @get_date.setter
    def date(self, date_value):
        if (type(date_value) == str):
            self._date = date_value
        else:
            raise Exception

    @property
    def get_royalties(self):
        return self._royalties
    
    @get_royalties.setter
    def royalties(self, royalties_value):
        if (type(royalties_value) == int):
            self._royalties = royalties_value
        else:
            raise Exception
    
    @classmethod
    def contracts_by_date(self, date):
        return [contract for contract in Contract.all if contract.date == date]
    
