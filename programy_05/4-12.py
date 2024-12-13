import csv

# Define a dictionary to map genres to filenames
genre_to_filename = {
    'Fantasy': 'books_fantasy.txt',
    'Historical': 'books_historical.txt',
    'Romance': 'books_romance.txt',
    'Classic': 'books_classic.txt'
}

def read_books(filename):
    """Read books from a CSV file and return a list of books."""
    books = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
    return books

def categorize_books_by_genre(books):
    """Organize books by genre into a dictionary."""
    categorized_books = {genre: [] for genre in genre_to_filename.keys()}
    for book in books:
        genre = book['Genre']
        if genre in categorized_books:
            categorized_books[genre].append(book)
    return categorized_books

def write_books_by_genre(books_by_genre):
    """Write categorized books to separate files based on genre."""
    for genre, books in books_by_genre.items():
        filename = genre_to_filename.get(genre)
        if filename:
            with open(filename, 'w', encoding='utf-8') as file:
                for book in books:
                    file.write(f"{book['Title']},{book['Author']},{book['Genre']},{book['Year']}\n")

def main():
    books = read_books('books.csv')
    books_by_genre = categorize_books_by_genre(books)
    write_books_by_genre(books_by_genre)
    print("Books have been categorized and written to their respective files.")

if __name__ == "__main__":
    main()
