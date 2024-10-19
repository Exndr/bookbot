#imports

import string


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print(text)
    print(f"This text has: {word_count} words")
    print(f"--- Begin report of {book_path}! ---")
    count_chars_report(text)
    print("End of book report!")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = len(text.split())
    return words


#Return a dictionary of the character counts
def count_chars_report(text):
    #lower the text
    lowered_text = text.lower()
    #initialize your dictionary
    char_dict = {letter: 0 for letter in string.ascii_lowercase}
    #Iterate through the lowered_text
    for char in lowered_text:
        if char in char_dict:
            char_dict[char] += 1
    #return char_dict

    #Let's make our report with some cleaner code
        #1. Convert dictionary into a list of dictionaries - List comprehension
    list_of_dicts = [{'letter': key, 'count': value} for key, value in char_dict.items()]

    #Print said report
    for item in list_of_dicts:
        print(f"The '{item['letter']} character was found {item['count']}' times.")


    


main()



