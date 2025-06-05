from stats import get_num_words
from stats import get_num_chars
from stats import get_sorted_char_count
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    
def get_book_text(filepath):
    """
    Reads the contents of a file and returns it as a string.

    Args:
        filepath (str): The path to the file.
    Returns:
        str: The contents of the file as a single string.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        print(f"Error: The file at '{filepath}' was not found.")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

def main():
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    char_counts = get_num_chars(book_text)
    char_list = get_sorted_char_count(char_counts)

    if book_text:
        num_words = get_num_words(book_text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in char_list:
            char=item["char"]
            num=item["num"]
            if char.isalpha():
                print(f"{char}: {num}")
        print("============= END ===============")
        


if __name__ == "__main__":
    main()
