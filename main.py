def main():
    print("--- Begin Report of Frankenstein ---")
    with open("books/Frank.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        print(f"{word_count} words found in the document.\n")
        count_characters(file_contents)

def count_characters(book_text):
    lower_string = book_text.lower()
    char_count = {}
    for char in lower_string:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    list = convert_to_list(char_count)
    
    list.sort(reverse=True, key=sort_on)
    for item in list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
def convert_to_list(dict):
    list = []
    for key in dict:
        list.append({"char": key, "num": dict[key]})
    return list

def sort_on(dict):
    return dict["num"]

main()