def verify_query(raw_query):
    checked_query = raw_query.strip().lower()
    return len(checked_query) > 1 and any(ch.isalpha() for ch in checked_query)


class BookReader:

    def __init__(self, *args):
        self.open_book(args)

    def open_book(self, book_names):
        if not book_names:
            print("Please, enter at least one book filename in a function call")
            return None

        for book_name in book_names:
            try:
                with open(book_name, encoding="utf-8") as file_object:
                    file_object.read()
            except FileNotFoundError:
                print("No books in the app directory or query error")
                return
            else:
                print(f"Current book: {book_name}")
                print("Would you like to launch word counter app? Y/N: ")
                answer = input()
                if answer.strip().lower() == "y":
                    self.count_words_in_book(book_name)

    def count_words_in_book(self, book_name):
        while True:
            print("(Enter 'exit' to close the book or quit the app entirely)")
            target_word = input(f"Which word would you like to count in the book {book_name}? ")
            if target_word.strip().lower() == 'exit':
                print("Good luck!")
                break
            if not verify_query(target_word):
                print("Invalid query. Please, try again")
                continue

            try:
                print(f"Opening content of {book_name} book...")
                with open(book_name, encoding="utf-8") as book_file_obj:
                    all_words = book_file_obj.read().split()
                    res = all_words.count(target_word)
            except FileNotFoundError:
                continue
            else:
                print(f"{book_name} has {res} words '{target_word}'")


# test task 10.10
book_r = BookReader("book1.txt", "book2.txt", "book3.txt")
