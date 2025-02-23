import sys
from stats import word_count, sort_list, char_count # type: ignore
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    num_word = word_count(sys.argv[1])
    char_dict = char_count(sys.argv[1])
    sorted_dict = sort_list(char_dict)
    print("============ BOOKBOT ============" + "\n" +
          "Analyzing book found at books/frankenstein.txt..." + "\n" +
          "----------- Word Count ----------" + "\n" + 
          "Found " + str(num_word) + " total words \n" +
          "--------- Character Count -------")
    for char in sorted_dict:
        character = list(char.keys())[0]
        count = list(char.values())[0]
        if character.isalpha():
            print(character + ": " + str(count))
main()