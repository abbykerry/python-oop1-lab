# lib/book.py

class Book:
    """
    A class to represent a Book.

    Attributes:
    -----------
    title : str
        The title of the book.
    page_count : int
        The number of pages in the book.
    """

    def __init__(self, title, page_count):
        """
        Initialize a new Book instance.

        Parameters:
        -----------
        title : str
            The title of the book.
        page_count : int
            The number of pages in the book.
        """
        self.title = title
        # Use the setter to enforce type check on page_count
        self.page_count = page_count

    # Getter for page_count
    @property
    def page_count(self):
        return self._page_count

    # Setter for page_count with type validation
    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            # Print an error message if page_count is not an integer
            print("page_count must be an integer")

    # Method to simulate flipping a page
    def turn_page(self):
        """
        Simulates turning a page in the book.
        Prints a fun message whenever a page is turned.
        """
        print("Flipping the page...wow, you read fast!")
