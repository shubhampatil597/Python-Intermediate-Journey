class Library:

    college = "D Y Patil College"

    def __init__(self, library_name, book_count):

        self.library_name = library_name
        self.book_count = book_count

    def display(self):

        print("\nLibrary Information")
        print("---------------------")
        print("Library Name:", self.library_name)
        print("Book Count:", self.book_count)
        print("College:", Library.college)

    @staticmethod
    def validate_books(book_count):

        if book_count > 0:
            return True

        return False

library1 = Library(
    "Central Library",
    5000
)

library1.display()

print(
    "Valid Book Count:",
    Library.validate_books(5000)
)