"""Small snippet to raise an IndexError."""

def get_last_letter(word):
    last_letter_index = len(word)
    last_letter = word[last_letter_index]
    return last_letter


planet = 'saturn'
print get_last_letter(planet)
