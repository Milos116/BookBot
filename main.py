from stats import word_count,character_count, sort_char_count
import sys

def get_book_text(file_path):
    with open (file_path, encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents


def main():

    args = sys.argv

    if len(args) < 2:
        print ("Requiers path of the book you wish to be analyzed (as argument)")
        sys.exit(1)

    file_path = args[1]

    content = get_book_text(file_path)

    chars = character_count(content)

    sorted_chars = sort_char_count(chars)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    word_count(content)
    print("--------- Character Count -------")
    for sorted in sorted_chars:
        if sorted["char"].isalpha():
            print (f"{sorted["char"]}:{sorted["count"]}")
    print("============= END ===============")

main()