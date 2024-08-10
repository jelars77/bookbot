def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        word_count = count_words(file_contents)
        character_counts = count_characters(file_contents)
        print(f"{word_count} words found in the document")

        for char, count in sorted(character_counts.items(), key=lambda item: item[1], reverse=True):
            print(f"The '{char}' character was found {count} times")

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    text = text.lower()

    for char in text:
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

if __name__ == "__main__":
    main()
