def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print(count_words(text))
    create_report(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words =text.split()
    return len(words)

def count_char(text):
    text = text.lower()
    chars = {}
    for char in text:

        if char in chars and char.isalpha():
            chars[char] += 1
        elif char.isalpha():
            chars[char] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def create_report(text):
    char_dict = count_char(text)
    char_list = []
    for key,value in char_dict.items():
        char_list.append({"char": key, "num": value})
    
    char_list.sort(reverse=True, key=sort_on)    
    for item in char_list:
        print(f"The {item["char"]}  character was found {item["num"]} times")


main()