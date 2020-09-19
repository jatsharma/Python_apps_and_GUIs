# define Library Class
class Library:
    def __init__(self, list, name):
        self.book_list = list
        self.name = name
        self.lendDict = {}

    def display_book(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.book_list:
            print(book)

    def lend_book(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print("Lender-Book database has been updated, you can take the book now")
        else:
            print(f"Book is already issued to {self.lendDict[book]}")

    def add_book(self, book):
        self.book_list.append(book)
        print("Book has been added to database")

    def return_book(self, book):
        self.lendDict.pop(book)


if __name__ == '__main__':
    jatin = Library(['Python', 'Django', 'Flask', 'C++'], "Lib_1")

    while True:
        print(f"welcome to the {jatin.name} library. Enter your choice to continue")
        print("1. Display available books")
        print("2. Lend a book")
        print("3. Donate a book")
        print("4. Return a book")
        user_choice = input()

        if user_choice not in ["1", "2", "3", "4"]:
            print("Please enter a valid choice")

        else:
            user_choice = int(user_choice)

            if user_choice == 1:
                jatin.display_book()

            elif user_choice == 2:
                book = input("Enter the name of the book you want to lend")
                user = input("Enter your name")
                jatin.lend_book(user, book)

            elif user_choice == 3:
                book = input("Enter the book name you want to donate")
                jatin.add_book(book)

            elif user_choice == 4:
                book = input("Enter the book name you want to return")
                jatin.return_book(book)

            else:
                print("Not a valid option")

            print("Press q to quit and c to continue")
            user_choice2 = ""
            while user_choice2 !="c" and user_choice2 !="q":
                user_choice2 = input()
                if user_choice2 == "q":
                    exit()
                elif user_choice2 == "c":
                    continue

