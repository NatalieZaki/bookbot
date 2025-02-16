def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(f"--- Begin report of books/frankenstein.txt ---")
    word_count = count_words(file_contents)
    character_counts = count_letters(file_contents)
    print(f"{word_count} words found in the document")
    chars_list = []
    for char, count in character_counts.items():
        chars_list.append({"char": char, "count": count})
    chars_list.sort(reverse=True, key=sort_on)
    for char_dict in chars_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
    print("--- End report ---")
def count_words(text):
   words = text.split()
   return len(words)
def sort_on(dict):
    return dict["count"]
def count_letters(text):
    counts = {}
    for character in text:
        lower_character = character.lower()
        if lower_character.isalpha():
            if lower_character in counts:
                counts[lower_character] += 1
            else:
                counts[lower_character] = 1
    return counts
if __name__ == "__main__":
  main()