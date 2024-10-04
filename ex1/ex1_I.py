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
        book['discounted_price'] = round(discounted_price,2)
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
    pass

def filter_books_by_year(books, start_year, end_year):
    """
    Filter books based on publication year range.
    Args:
        books (list of dict): List of book dictionaries
        start_year (int): Start year of the range
        end_year (int): End year of the range
    Returns:
        list of dict: Filtered list of book dictionaries
    """
    filtered_books_year = []
    for book in books:
        if 'year' in book and start_year <= int(book['year']) <= end_year:
            filtered_books_year.append(book)
    return filtered_books_year
            
    

def sort_books(books, sort_by, reverse=False):
    """
    Sort books based on a specified property.
    Args:
        books (list of dict): List of book dictionaries
        sort_by (str): Property to sort by
        reverse (bool): Sort in descending order if True
    Returns:
        list of dict: Sorted list of book dictionaries
    """
    sorted_books = sorted(books, key=lambda book: book.get(sort_by), reverse=reverse)
    return sorted_books

def find_most_prolific_author(books):
    """
    Find the author with the most books in the dataset.
    Args:
        books (list of dict): List of book dictionaries
    Returns:
        str: Name of the most prolific author
    """
    for book in books:
        author = book.get('author', None) 
        if author:
            author_tally[author] = author_tally.get(author, 0) + 1
    if author_tally:
        most_prolific_author = max(author_tally, key=author_tally.get)
        return most_prolific_author
    else:
        return None

def calculate_average_price_by_genre(books):
    """
    Calculate average book price for each genre.
    Args:
        books (list of dict): List of book dictionaries
    Returns:
        dict: Dictionary of average prices by genre
    """
    genre_totals = {}
    for book in books:
        genre = book.get('genre')
        try:
            price = float(book.get('price', 0))
            if genre:
                if genre not in genre_totals:
                    genre_totals[genre] = {'total_price': 0, 'count': 0}
                genre_totals[genre]['total_price'] += price
                genre_totals[genre]['count'] += 1
        except ValueError:
            print(f"Skipping book with invalid price: {book.get('title', 'Unknown Title')} - Price: {book.get('price')}")
    average_price_by_genre = {}
    for genre, values in genre_totals.items():
        if values['count'] > 0:
            average_price_by_genre[genre] = round(values['total_price']/ values['count'], 2)
    return average_price_by_genre
        

def generate_book_report(books, output_filename):
    """
    Generate a formatted report of books and their properties.
    Args:
        books (list of dict): List of book dictionaries
        output_filename (str): Name of the output text file
    """
    try:
        with open(output_filename, 'w') as file:
            file.write("Book Report\n")
            file.write("-----------------------------\n")
            for index, book in enumerate(books, start=1):
                file.write(f"Book {index}:\n")
                file.write(f"  Title: {book.get('title', 'N/A')}\n")
                file.write(f"  Author: {book.get('author', 'N/A')}\n")
                file.write(f"  Genre: {book.get('genre', 'N/A')}\n")
                file.write(f"  Year: {book.get('year', 'N/A')}\n")
                file.write(f"  Price: ${book.get('price', 'N/A')}\n")
            file.write("End of Report\n")
        print(f"Report successfully generated: {output_filename}")
    except Exception as e:
        print(f"An error occurred while generating the report: {e}")


def update_book_properties(books, updates):
    """
    Update book properties based on provided updates.
    Args:
        books (list of dict): List of book dictionaries
        updates (dict): Dictionary of updates for books
    Returns:
        list of dict: Updated list of book dictionaries
    """
    for book in books:
        title = book.get('title')
        
        if title in updates:
            book_updates = updates[title]

            for key, value in book_updates.items():
                if key in book:
                    book[key] = value
                else:
                    print(f"Warning: Property '{key}' not found in book '{title}'. Skipping this update.")
    return books

def convert_currency(books, exchange_rate):
    """
    Convert book prices to a different currency.
    Args:
        books (list of dict): List of book dictionaries
        exchange_rate (float): Exchange rate to apply
    Returns:
        list of dict: Updated list of book dictionaries with converted prices
    """
    # TODO: Implement currency conversion with error handling
    pass

def main():
    input_file = "books.csv"
    output_file = "book_analysis_report.txt"
    
    try:
        # Load data
        books = load_book_data(input_file)
        
        # Process data
        books = calculate_discount_price(books, 0.1)  # 10% discount
        unique_genres = find_unique_genres(books)
        
        # Perform analysis
        recent_books = filter_books_by_year(books, 2000, 2023)
        sorted_books = sort_books(books, 'price', reverse=True)
        top_author = find_most_prolific_author(books)
        
        # Generate statistics
        avg_prices = calculate_average_price_by_genre(books)
        
        # Generate report
        generate_book_report(books, output_file)
        
        # Perform updates and conversions
        updates = {'Book 1': {'year': 1960}, 'Book 2': {'price': 12.99}}
        books = update_book_properties(books, updates)
        books = convert_currency(books, 0.85)  # Convert to GBP
        
        print(f"Analysis complete. Report generated: {output_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
