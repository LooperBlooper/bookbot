import sys
from stats import count_words
from stats import count_chars
from stats import dict_list
# Check if the user provided a book path
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Get the book path from the command line argument
book_path = sys.argv[1]


def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    num_words = count_words(get_book_text(book_path))
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    the_list = dict_list(count_chars(get_book_text(book_path)))
    for item in the_list:
        print(f"{item['char']}: {item['num']}")

    
main()