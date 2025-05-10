from stats import count_string, character_instance_data, sort_dictionary_of_characters

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()

    return contents

def main():
    frankenstein_txt = get_book_text('./books/frankenstein.txt')
    frankenstein_word_count = count_string(frankenstein_txt)
    frankenstein_character_list_alpha = character_instance_data(frankenstein_txt)
    frankenstein_sorted_count = sort_dictionary_of_characters(frankenstein_character_list_alpha)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {frankenstein_word_count} total words")
    print("--------- Character Count -------")

    for dict in frankenstein_sorted_count:
        if dict['char'].isalpha():
            print(f"{dict['char']}: {dict['num']}")

    print("============= END ===============")



main()
