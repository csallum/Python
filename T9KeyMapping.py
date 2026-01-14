dictionary = {"put", "out", "sun", "run", "smart", "truck"}
finalWords = []
mappings = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}

def mappingfun(keypadMapping):
    # Loop through every word in the dictionary
    for x in dictionary:
        # Assume the word matches until proven otherwise
        match = True

        # Compare each letter of the word with the allowed letters for that digit from keypadMapping
        for digit, letter in zip(keypadMapping, x):
            # If the letter is not allowed for this digit, it's not a match
            if letter not in mappings[digit]:
                match = False
                break

        # If all letters matched the keypad mapping, add the word to results
        if match:
            finalWords.append(x)

    return finalWords

print(mappingfun("786"))
