def count(text_to_count):
    c = text_to_count.split()
    d = len(c)
    print(f"Found {d} total words")

def incidence(text_to_count):
    wordcount = {}
    f = text_to_count.lower()
    g = list(f)
    for i in g:
        if i in wordcount:
            wordcount[i] += 1
        else: 
            wordcount[i] = 1
    return wordcount

def sort_on(wordcount):
    return wordcount["num"]

def sort_list(wordcount):
    char_count = []
    for i in wordcount.items():
        if i[0].isalpha():
            char_count.append({
                "char": i[0],
                "num": i[1]})        
    char_count.sort(reverse=True, key=sort_on)
    return char_count