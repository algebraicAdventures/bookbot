def word_count(string):
    return len(string.split())

def char_count(string):
    count = {}
    for char in string.lower():
        if char.isalpha():
            if not char in count:
                count[char] = 0
            count[char] += 1
    return count

def sort_on_count(dict):
    return dict["count"]

def dict_to_list(dict):
    list = []
    for char in dict:
        list.append({"char" : char, "count" : dict[char]})
    return list

def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        total_words = word_count(file_contents)
        char_counts = dict_to_list(char_count(file_contents))
        char_counts.sort(key=sort_on_count,reverse=True)
        print(f"--- Begin report of {path} ---")
        print(f"{word_count(file_contents)} words found in the document\n")
        for char in char_counts:
            print(f"The '{char["char"]}' character was found {char["count"]} times")
        print("--- End Report ---")

main()