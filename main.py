def main():
    book_name = "frankenstein"
    book_path = "books/{}.txt".format(book_name)
    text = get_book_text(book_path)
    num_words = count_words(text)
    print(f"--- Begin report of book {book_name.capitalize()} ---")
    print(f"{book_name.capitalize()} has {num_words} words in it!")
    print("")
    count_characters(text)
    print("--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def update_char_array(arr, character):
    for obj in arr:
        if obj['character'] == character:
            obj['count'] += 1
            return
    arr.append({'character':character, 'count':1})


def count_characters(text):
    characters = []
    for c in text.lower():
        if c.isalpha() == False:
            continue
        update_char_array(characters, c)      

    characters.sort(reverse=True, key=lambda x: x['count'])
    for c in characters:
        print(f"The '{c['character']}' character was found {c['count']} times")

main()