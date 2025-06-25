def get_book_text(file):
    with open(file) as f:
        book_contents = f.read()
    return book_contents

def main():
    b = get_book_text("./books/frankenstein.txt")
    text_to_count = b
    return text_to_count

def count(text_to_count):
    c = text_to_count.split()
    d = len(c)
    print(f"{d} words found in the document")

text = main()
count(text)