def main():
    file = "books/frankenstein.txt"

    frankenstein_contents = open_file(file)
    print(frankenstein_contents)

    frankenstein_wc = count_words(frankenstein_contents)
    print(frankenstein_wc)

    frankenstein_cc = count_characters(frankenstein_contents)
    print(frankenstein_cc)

    report(file, frankenstein_wc, frankenstein_cc)

def open_file(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents

def count_words(text_from_book):
    words = text_from_book.split()
    count = 0
    for word in words:
        count += 1
    return count

def count_characters(text_from_book):
    lowered_text = text_from_book.lower()
    print(lowered_text)
    chars_list = list("abcdefghijklmnopqrstuvwxyz")
    dict_text = {count: 0 for count in chars_list}
    for char in lowered_text:
        if char in chars_list:
            dict_text[char] += 1
    return dict_text 
   
def report(file, wc, count_dict):
    print(f"--- Begin report of {file} ---")
    print(f"{wc} words found in the document\n")

    for key,value in count_dict.items():
        print(f"'{key}' character was found {value} times")

    print("--- End report ---")


    





main()
