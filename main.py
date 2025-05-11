from stats import count_string, character_instance_data_alpha, sort_dictionary_of_characters
import sys


# Graceful program exit if too many, or not enought arguments
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()

    return contents

def main():
    book_txt = get_book_text(book_path)
    book_word_count = count_string(book_txt)
    book_character_list_alpha = character_instance_data_alpha(book_txt)
    book_sorted_count = sort_dictionary_of_characters(book_character_list_alpha)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")

    for dict in book_sorted_count:
        if dict['char'].isalpha():
            print(f"{dict['char']}: {dict['num']}")

    print("============= END ===============")



main()
