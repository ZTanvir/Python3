# ÄLÄ MUUTA ALLA OLEVAA LUOKKAA Kirja
# Kirjoita ratkaisui Kirja-luokan jälkeen

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

    # STUB:# This enables easy printing of a Book object
    def __repr__(self):
        return f"{self.name} ({self.author}), {self.year} - genre: {self.genre}"


# -----------------------------
# tee ratkaisu tänne

def books_of_genre(books: list, genre: str):
    # Create a empty list with name selected_genre_books
    selecred_genre_books = []
    # From the list of books get a single book
    for book in books:
        # Check the single book genre is same as the genre parameter
        if book.genre == genre:
            # If they are same keep the book in selecred_genre_books list
            selecred_genre_books.append(book)
    # Return the selecred_genre_books list
    return selecred_genre_books
