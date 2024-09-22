import csv
import json

def load_book_data(filename):
    """
    Read book data from a CSV file.
    Args:
        filename (str): Name of the CSV file
    Returns:
        list of dict: List of dictionaries containing book properties
    """
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
        dict_list = [row for row in csv_reader]
    return dict_list
    

def calculate_discount_price(books, discount_rate):
    """
    Calculate and add discounted price for each book.
    Args:
        books (list of dict): List of book dictionaries
        discount_rate (float): Discount rate to apply
    Returns:
        list of dict: Updated list of book dictionaries with discounted price
    """
    for book in books:
        original_price = float(book['price'])
        discounted_price = original_price * (1-discount_rate)
        book['price'] = round(discounted_price,2)
    return books
    

def find_unique_genres(books):
    """
    Find unique genres from the data.
    Args:
        books (list of dict): List of book dictionaries
    Returns:
        set: Set of unique genres
    """
    genres = set()
    for book in books:
        if 'genre' in book:
            genres.add(book['genre'])
    return genres
    
def main():
    input_file = '/Users/adiv/git/ME371/ex1/books.csv'
    output_file = '/Users/adiv/git/ME371/ex1/book_analysis_report.txt'
    
    try:
        # Load data
        books = load_book_data(input_file)
        
        #print(f"Analysis complete. Report generated: {output_file}")

        #print(books)

        books_updated = calculate_discount_price(books, .1)

        #print(books_updated)

        genres = find_unique_genres(books)
        print(genres)


    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
