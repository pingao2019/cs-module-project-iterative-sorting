

class Book:

    def __init__(self, title, author, genre):

        self.title = title

        self.author = author

        self.genre = genre

    def __str__(self):
        return f"{self.title}"
    def insertion_sort_by_book_title(arr_of_books):# performs insertion sort to sort an array of books 
        # iterate through the entire array 

         # we can skip the first array element since there's nothing to compare it to 

        # do we want to iterate over the books themselves or indices 

        # we do need to have access to the book before the current book 

        # we need access to each index in order to facilitate this 

        for i in range(1, len(arr_of_books)):
            curr_book = arr_of_books[i]

            # book_index will start at i 

        #But we'll update it as we swap 
            book_index = i

        # compare curr_book with the previous book 

        # what do we compare by? 

        # swap until current book > previous book or current book ends up at the 

        # front of the array 

            while book_index > 0 and curr_book.title < arr_of_books[book_index - 1].title:
                # swap them 

                arr_of_books[book_index], arr_of_books[book_index - 1] = arr_of_books[book_index - 1], arr_of_books[book_index] 

            # we need to keep track of our current book's changing index 

                book_index -= 1
        return arr_of_books

    arr_of_books = [
        
        Book("Harry Potter and the Sorcerer's Stone", "JK Rowling", "Children's Fantasy"),

        Book("A Game of Thrones", "George RR Martin", "Adult Fantasy"),

        Book("Show Your Work", "Austin Kleon", "Self Help"),

        Book("The Lord of the Rings: The Fellowship of the Ring", "JRR Tolkien", "High Fantasy"),

        Book("Clean Code", "Robert J Martin", "Progrmming"),

        Book("The Rust Programming Language", "Steve Klabnik and Carol Nichols", "Programming"),

        Book("The Way of Kings", "Brandon Sanderson", "High Fantasy")]

​    insertion_sort_by_book_title(arr_of_books)

    for book in arr_of_books:

        print(book)

