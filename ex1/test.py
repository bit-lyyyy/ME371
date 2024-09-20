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

def main():
    input_file = '/Users/adiv/git/ME371/ex1/books.csv'
    output_file = '/Users/adiv/git/ME371/ex1/book_analysis_report.txt'
    
    try:
        # Load data
        books = load_book_data(input_file)
        
        print(f"Analysis complete. Report generated: {output_file}")

        print(books)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
