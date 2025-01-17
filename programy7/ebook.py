class EBook:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.totalPages = pages
        self.currentPage = 0 
        self.isOpen = False

    def openBook(self):
        self.isOpen = True
        self.currentPage = 1
        print(f"Book '{self.title}' is now open.")

    def closeBook(self):
        self.is_open = False
        self.currentPage = 0
        print(f"Book '{self.title}' is now closed.")

    def nextPage(self):
        if not self.isOpen:
            print("Cannot turn page. Book is closed.")
            return

        if self.currentPage < self.totalPages:
            self.currentPage += 1
            print(f"Turned to page {self.currentPage}")
        else:
            print("You've reached the last page of the book.")

    def previousPage(self):
        if not self.isOpen:
            print("Cannot turn page. Book is closed.")
            return

        if self.currentPage > 1:
            self.currentPage -= 1
            print(f"Turned to page {self.currentPage}")
        else:
            print("You're on the first page.")

    def Status(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Total Pages: {self.totalPages}")

        if self.isOpen:
            print(f"Current Page: {self.currentPage}")
            print("Book is Open")
        else:
            print("Book is Closed")