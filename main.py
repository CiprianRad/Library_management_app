# We will make a UI app for a library, handling it's books and clients
# We will uses classes and a menu for options, handling all the possible errors that could occur
# We will need to know the number of books rented for each client
# We will need to know if a client has a rented book or not
# TODO: We will need to know 20% of our most active clients by books rented 
# We want our clients to be able to return or rent a book


class Book:  # We define a class that will create our book objects which will then turn into book instances with all their atributes
    def __init__(self, book_id, title, author, description, available=True):  # We define the atributes of our instances, we used the wording book_id as not to be confused with the client's id, basically each parameter in this function is used for the atributes of a book instance, most of them have a data type of any, instead of availability which is set to Boolean to track if the book is avaliable or not
        self.book_id = book_id  # We use the self parameter to let the function know how to acces the data stored in each attribute of the book object. We created a variable book.id that will have the value of the book's id
        self.title = title  # Analogus to the variable for id, but this time we stock the value in the title variable that get the value from the parameter title
        self.author = author  # Analogus
        self.description = description  # Analogus
        self.available = available  # Analogus
        self.rental_count = 0  # Track how many times this book has been rented

    def __str__(self):  # We made a __str__ method, we could have just as finely used a __repr__ method, however we made a custom __str__ method, to be able to represent the class objects as a string
        availability = "Available" if self.available else "Not Available"  # To be able to represent the Book object as a whole, we also need to represent if it is available or not, so we make a local variable of string type that will print a message or the other based on the condition given
        return f"[{self.book_id}] {self.title} by {self.author} - {availability} (Rented {self.rental_count} times)"  # This is the string that will represent our class objects. It will output all the memembers of the class

class Client:  # Likewise we made a Client class to create client objects
    def __init__(self, client_id, name, cnp): 
        self.client_id = client_id
        self.name = name
        self.cnp = cnp
        self.rented_books = []  # Track the list of rented book IDs. We setted the list empty so we can stack the number of rented books

    def __str__(self):  # Likewise, we made a custom __str__ method to represent all members of the class with a string
        return f"[{self.client_id}] {self.name}, CNP: {self.cnp} (Books rented: {len(self.rented_books)})"

class LibraryManager:  #  We made a class to manage our Library. In this class we will define all the methods for the 2 previously defined classes Book and Client. It will be the equivelant of a module with operations.
    def __init__(self):  # Surely, we will need to be able to keep trakc of our Clients and Books, so we will define to empty lists for each one, since lists are iterable, ordered and indexed, they will come in handy to operate the instances of each class
        self.books = []
        self.clients = []

    # Book Methods
    def add_book(self, book):  # A simple function, that takes parameter which we will later make it an object from the book class, when we call the function
        self.books.append(book)  # It simply appends a book to the book list
        print("Book added successfully!")  # We print a message if the operation was succesful

    def remove_book(self, book_id):  # We want to be able to delete book only be referring to their id, since we might have books with the same title, or books from the same author
        for book in self.books:  # We want to iterate through the whole list until we find the id given by the user
            if book.book_id == book_id:  # A conditional statement in case the id was found
                self.books.remove(book)  # We use the remove() method to remove values from the book list
                print("Book removed successfully!")  # We print a message in case the operation was succesful
                return  # We do not want anything to be returned, in this case, we left the return empty because we are not expecting anything to be returned from this method. With this empty return we make sure the function stop executing after the return call.
        print("Book not found!")  # Since we had an if condition for the case the id is in the book list, if it wasn't found, we will print a message accordingly

    def list_books(self):
        if not self.books:  # The "if not [list]" syntax can be translated to: "If the list is empty"
            print("No books available.")
        else:
            for book in self.books:  # In case there are values in the list, we want to print all of them
                print(book)

    def update_book(self, book_id, title=None, author=None, description=None, available=None):  # We setted the parameters to None for multiple reasons, one of which is that we want to be able to update only certain atributes of each instance, and eacht time the user wants to update a book, he doesn't have to give values for every attribute
        for book in self.books:  # We iterate through the list
            if book.book_id == book_id:  # In case an id was found statement
                if title: book.title = title  # What this conditional statements do is they check which parameter was given a new value and which ones were left to None value, therefore, based on the second previous comment, because we passed them as None, the user can leave other field empty
                if author: book.author = author # Analogus, we check if the author has been changed
                if description: book.description = description  # Analogus we check if the book description has been changed
                if available is not None: book.available = available  # This is a special case, cause the availability of the book is meant to be a Boolean value. However, False, is considered a "falsy" value in Python, and doing the analogus here will not work, since in the case availability was False it would be treated just the same as if availabilty was None. Hence, by checking if availabilty is not None, the interpretor will now know to distinguish between the 3 casea: True, False or None.
                print("Book updated successfully!")
                return  # This is a function for updating, so we don't want to return anything
        print("Book not found!")  # In case no book with the id was found.

    def search_books(self, title=None, author=None):  # Once again, we want the user to be able to search a book by name or author, depending on his preferance.
        results = []  # We declare an empty list that will get all the books with the title, or the books written by the author
        for book in self.books:  # We iterate the book list. As a note, since we declared the value in the list to "book", the word "book" will be taking the place of "self". Note: the self parameter will make sure we can acces the class attributes such as self.books, and self.clients. Moreover, it tells the method we defined to refer to the instances in this class
            if (title and title.lower() in book.title.lower()) or (author and author.lower() in book.author.lower()):  # To translate the conditions in the syntax: " If a title has been provided, then, turn the title to lowercase, and make sure it is found in the set of data with the title atribute of each instance of the class Book, which will be turned to lowercase to make sure the search is case insensitive"
                results.append(book)  # We add the found items to our results list
        
        if results:  # The "if [list]" syntax can be translate to "If the list is not empty"
            print("\nSearch Results for Books:")
            for book in results:  # We iterate the results list and print our its elements
                print(book)
        else:
            print("No matching books found.")

    def rent_book(self, book_id, client_id):
        book = next((b for b in self.books if b.book_id == book_id), None)  # We defined a variable book and used the iteration method next() to go thorough the list of self.books until we find the given id, and if it wasn't found, the variable book, will get the value None
        client = next((c for c in self.clients if c.client_id == client_id), None)  # Analogus like the book variable method
        if not book:  #  The "if not (value)" syntax can be translated to: "If the value of book is None"
            print("Book not found!")
            return  # If the book was not found we stop the function call
        if not client:
            print("Client not found!")  
            return  # If the client was not found we stop the function call
        if not book.available:  # The "If not (Bool)" syntax can be trnslated to: "If (Bool == False)"
            print(f"The book '{book.title}' is currently not available.")
            return  # If the book is not available we want to stop the call of the function. 
        book.available = False # We exhausted the possible "wrong" cases, that means the book was rented. Remember we set the variable book to the book with the id given, and now we set it's availability to False
        book.rental_count += 1  # We increment the variable defined in the Book class with 1, in that the book was rented
        client.rented_books.append(book.book_id)  # To the client with the specified id we place in it's list of rented books, the book with the specified id
        print(f"The book '{book.title}' has been rented to {client.name}.")

    def return_book(self, book_id, client_id):  # This is the "undo" function for the rent_book() function, so it only makes sense they are similar in syntax
        book = next((b for b in self.books if b.book_id == book_id), None)  # Analogus from this line till the second return
        client = next((c for c in self.clients if c.client_id == client_id), None)
        if not book:
            print("Book not found!")
            return
        if not client:
            print("Client not found!")
            return
        if book.book_id not in client.rented_books:  # In this case, we need to check if the client has the book rented or not, iow, we need to check if the book id is found in the clien's list of rented books
            print(f"{client.name} does not have '{book.title}' rented.")
            return  # If the book was not found in his rented book list, we want the function to stop running
        book.available = True  # At this stage we already went through all the wrong possibilities, that means the book will be returned, therefore we set its availability to True
        client.rented_books.remove(book.book_id)  # We want to remove the book from the client's rented books list.
        print(f"The book '{book.title}' has been returned by {client.name}.")

    def show_most_rented_books(self):
        most_rented_books = sorted(self.books, key=lambda b: -b.rental_count)  # We make a new list with the most rented books. We use the sorted() method whcih can take up to 3 parameters. We gave it an iterator, that being the booklist, and they key to which to sort by is the rental count of each book sorted descendingly, hence this is why we used a lambda function which will return the negative value of the rental count. Just as well, we could have return b and then give another parameter to the function: reverse = True

        if not most_rented_books:  # If the list is empty, then it means no books are rented
            print("No books have been rented yet.")
        else:
            print("\nMost rented books:")
            for book in most_rented_books:  # We print all the books in the list
                print(book)

    # Client Methods
    def add_client(self, client):
        self.clients.append(client)
        print("Client added successfully!")

    def remove_client(self, client_id):
        for client in self.clients:
            if client.client_id == client_id:
                self.clients.remove(client)
                print("Client removed successfully!")
                return
        print("Client not found!")

    def list_clients(self):
        if not self.clients:
            print("No clients available.")
        else:
            for client in self.clients:
                print(client)

    def update_client(self, client_id, name=None, cnp=None):
        for client in self.clients:
            if client.client_id == client_id:
                if name: client.name = name
                if cnp: client.cnp = cnp
                print("Client updated successfully!")
                return
        print("Client not found!")

    def search_clients(self, name=None, cnp=None):
        results = []
        for client in self.clients:
            if (name and name.lower() in client.name.lower()) or (cnp == client.cnp):
                results.append(client)
        
        if results:
            print("\nSearch Results for Clients:")
            for client in results:
                print(client)
        else:
            print("No matching clients found.")

    def show_clients_with_rentals(self):
        clients_with_rentals = [client for client in self.clients if client.rented_books]
        sorted_clients = sorted(clients_with_rentals, key=lambda c: (c.name.lower(), -len(c.rented_books)))

        if not sorted_clients:
            print("No clients with rented books.")
        else:
            print("\nClients with rented books:")
            for client in sorted_clients:
                print(client)

def main():
    manager = LibraryManager()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Update Book")
        print("5. Add Client")
        print("6. Remove Client")
        print("7. List Clients")
        print("8. Update Client")
        print("9. Search Books")
        print("10. Search Clients")
        print("11. Rent Book")
        print("12. Return Book")
        print("13. Show Clients with Rentals")
        print("14. Show Most Rented Books")
        print("15. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            description = input("Enter book description: ")
            available = input("Is the book available? (yes/no): ").strip().lower() == 'yes'
            manager.add_book(Book(book_id, title, author, description, available))

        elif choice == '2':
            book_id = input("Enter book ID to remove: ")
            manager.remove_book(book_id)

        elif choice == '3':
            manager.list_books()

        elif choice == '4':
            book_id = input("Enter book ID to update: ")
            title = input("Enter new title (leave blank to skip): ")
            author = input("Enter new author (leave blank to skip): ")
            description = input("Enter new description (leave blank to skip): ")
            available_input = input("Is the book available? (yes/no/leave blank to skip): ").strip().lower()
            available = True if available_input == 'yes' else False if available_input == 'no' else None
            manager.update_book(book_id, title, author, description, available)

        elif choice == '5':
            client_id = input("Enter client ID: ")
            name = input("Enter client name: ")
            cnp = input("Enter client CNP: ")
            manager.add_client(Client(client_id, name, cnp))

        elif choice == '6':
            client_id = input("Enter client ID to remove: ")
            manager.remove_client(client_id)

        elif choice == '7':
            manager.list_clients()

        elif choice == '8':
            client_id = input("Enter client ID to update: ")
            name = input("Enter new name (leave blank to skip): ")
            cnp = input("Enter new CNP (leave blank to skip): ")
            manager.update_client(client_id, name, cnp)

        elif choice == '9':
            title = input("Enter book title to search (leave blank to skip): ")
            author = input("Enter book author to search (leave blank to skip): ")
            manager.search_books(title, author)

        elif choice == '10':
            name = input("Enter client name to search (leave blank to skip): ")
            cnp = input("Enter client CNP to search (leave blank to skip): ")
            manager.search_clients(name, cnp)

        elif choice == '11':
            book_id = input("Enter book ID to rent: ")
            manager.rent_book(book_id)

        elif choice == '12':
            book_id = input("Enter book ID to return: ")
            manager.return_book(book_id)

        elif choice == '13':
            manager.show_clients_with_rentals()

        elif choice == '14':
            manager.show_most_rented_books()

        elif choice == '15':
            print("Exiting the system.")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()