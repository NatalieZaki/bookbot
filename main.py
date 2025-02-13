def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    character_counts = count_letters(file_contents)
    for char, count in sorted(character_counts.items()):
        print(f"'{char}': {count}")
def count_words(text):
   words = text.split()
def count_letters(text):
    counts = {}
    for character in text:
        lower_character = character.lower()
        if lower_character in counts:
            counts[lower_character] += 1
        else:
            counts[lower_character] = 1
    return counts
if __name__ == "__main__":
  main()