class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")

class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.set_number_of_pages(number_of_pages)

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, number_of_pages):
        if number_of_pages > 0:
            self.__number_of_pages = number_of_pages
        else:
            print("Number of pages must be positive.")

    def display_info(self):
        super().display_info()
        print(f"Number of pages: {self.__number_of_pages}")

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("Issue number must be positive.")

    def display_info(self):
        super().display_info()
        print(f"Issue number: {self.__issue_number}")


# Testing the Classes 
if __name__ == "__main__":
    # Creating objects
    pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
    book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
    mag1 = Magazine("National Geographic", "Various Authors", 202)

    # Printing the information
    print("Publication Information:")
    pub1.display_info()

    print("\nBook Information:")
    book1.set_number_of_pages(-310)  # setting invalid value on attribute
    book1.display_info()
    print(book1.get_number_of_pages())

    print("\nMagazine Information:")
    mag1.display_info()
    print(mag1.get_issue_number())