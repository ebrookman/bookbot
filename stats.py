# Function to count the number of words in a document
def get_num_words(string):
    word_count = len(string.split())
    return word_count 


def get_num_characters(string):
    characters = {}
    char_set = set()
    for character in string:
        if character.lower() in char_set:
            characters[character.lower()] += 1
        else:
            char_set.add(character.lower())
            characters[character.lower()] = 1
    return characters


def get_report(dict):
    new_list = []
    for item in dict.items():
        new_dict = {item[0]: item[1]}
        new_list.append(new_dict)
    new_list.sort(reverse=True, key=sort_on)
    return new_list

def sort_on(dict):
    return list(dict.values())[0]
