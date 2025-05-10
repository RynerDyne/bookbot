
def count_string(text):
    words = text.split()
    word_count = len(words)

    return word_count

def character_instance_data_alpha(text):
    character_data = {}
    lowercase_text = text.lower()
    for i in range(0, len(lowercase_text)):
        if lowercase_text[i] not in character_data:
            character_data[lowercase_text[i]] = 1
        else:
            character_data[lowercase_text[i]] += 1
    return character_data

def sort_dictionary_of_characters(dictionary_of_characters):
    list_of_dict = []
    for character in dictionary_of_characters:
        list_of_dict.append({"char": character, "num": dictionary_of_characters[character]})
    
    def sort_on_char(dict):
        return dict["char"]
    list_of_dict.sort(key=sort_on_char)

    return list_of_dict



