from stats import *
import sys 

if len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    link = sys.argv[1]

def get_book_text(file):
    with open(file) as f:
        book_contents = f.read()
    return book_contents

def main():
    b = get_book_text(link)
    text_to_count = b
    return text_to_count



text = main()
print("============ BOOKBOT ============")
print(f"Analyzing book found at {link}...")
print("----------- Word Count ----------")
count(text)
print("--------- Character Count -------")

char_counts = incidence(text)
sorted_chars = sort_list(char_counts)

for dic_item in sorted_chars:
    print(f"{dic_item['char']}: {dic_item['num']}")

print("============= END ===============")
