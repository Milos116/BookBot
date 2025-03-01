def word_count(content):
    word_list= content.split()
    num_word = len(word_list)
    print(f"Found {num_word} total words")



def character_count(content):
    char_dict = {}
    for char in content:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1
    return char_dict

def sort_char_count(char_dict):

    chars_list = []

    for char, count in char_dict.items():
        char_dict = {"char": char, "count": count}
        chars_list.append(char_dict)

    def sort_on(dict):
        return dict["count"]
    
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list