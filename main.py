from stats import word_count

def get_book_text(file_path):
    with open (file_path, encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents

def main():
    word_count(get_book_text("books/frankenstein.txt"))

main()