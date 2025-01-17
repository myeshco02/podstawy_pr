from ebook import EBook


def main():
    myBook = EBook("Thinking fast and slow", "Daniel Kahneman", 480)

    print("Initial Book Status:")
    myBook.Status()
    print()

    print("Book Status After Opening:")
    myBook.openBook()
    myBook.Status()
    print()

    [myBook.nextPage() for _ in range(15)]
    myBook.Status()
    print()

    myBook.closeBook()
    print()

    myBook.nextPage()
    myBook.previousPage()


# Run the main program
if __name__ == "__main__":
    main()
