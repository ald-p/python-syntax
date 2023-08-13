words = ["hello", "Hey", "goodbye", "Yo", "yes"];

def print_upper_words(words, starting_letters):
    """
    Given list of words and set of starting letters,
    print only words starting with letters provided in starting letters and print each word capitalized
    """

    for word in words:
        word = word.lower();
        for letter in starting_letters:
            if word.startswith(letter):
              capitalized = word.capitalize();
              print(capitalized);

print_upper_words(words, {"h", "y"})