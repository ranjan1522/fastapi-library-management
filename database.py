from models import Book, Member

books_db = [
    Book(id=1, title="Atomic Habits", author="James Clear", available=True),
    Book(id=2, title="Clean Code", author="Robert C. Martin", available=True),
    Book(id=3, title="The Alchemist", author="Paulo Coelho", available=True),
    Book(id=4, title="Sapiens", author="Yuval Noah Harari", available=True),
]

members_db = [
    Member(id=1, name="Aarav Sharma"),
    Member(id=2, name="Mira Patel"),
    Member(id=3, name="Ravi Kapoor"),
]

borrowed_books = {}